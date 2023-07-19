from flask import Flask, render_template, request, redirect, url_for, make_response
import pandas as pd
import io
from classes.functions import *
from classes.rompeflix import putMediaRT
from classes.ifc import getIFCInfo, unitaryTest

# Importacions per LoginWithMicrosoft
import requests
from flask import session
from flask_session import Session
import app_config
from classes.functionsMicrosoft import _load_cache, _save_cache, _build_msal_app, _build_auth_code_flow, _get_token_from_cache

# Iniciem la APP
app = Flask(__name__)
app.config.from_object(app_config)
Session(app)

# Necessari per quan es treballa en localhost
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


# FUNCTIONS    
def componentsDict(cases_of_study, headers):
    output = {}
    for case in cases_of_study:
        output[case] = [header for header in headers if header.case == case]
    return output

# GLOBAL VARIABLES
staff = ''
supplyTeam = ''
materials = ''

# PROVES
@app.route('/prova')
def prova():
    a = 'a'
    return a


# ----- PRODUCCIÓ -----
@app.route('/index')
def index():
    return redirect(url_for('kpi'))

# KPI
@app.route('/components')
def kpi():
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template('evolution.html',components=components,cases=cases,projects=projects,headers=headers)

#SKU REQUEST
@app.route('/sku/request')
def skuRequest():
    if not session.get("user"):
        return redirect(url_for("login"))
    global staff
    global supplyTeam
    global materials
    
    name = session["user"].get("name")
    if materials == '':      
        materials = materialGroup()
    response_value = request.args.get('response')
    return render_template('sku.html',name=name,materials=materials,response=response_value)

@app.route('/sku/add',methods=['POST'])
def addRequest():
    if not session.get("user"):
        return redirect(url_for("login"))
    mperson = request.form['mperson']
    mtype = request.form['mtype']
    mproject = request.form['mproject']
    msimilar = request.form['msimilar']
    mgroup = request.form['mgroup']
    mdescription = request.form['mdescription']
    munits = request.form['munits']
    mmainmaterial = request.form['mmainmaterial']
    mbrand = request.form['mbrand']
    mmodel = request.form['mmodel']
    minfo = request.form['minfo']
    data = [mperson,mtype,mproject,msimilar,mgroup,mdescription,munits,mmainmaterial,mbrand,mmodel,minfo]
    response = insertSKUrequested(data)
    return redirect(url_for('skuRequest',response=response))

@app.route('/sku/list')
def requestedList():
    if not session.get("user"):
        return redirect(url_for("login"))
    materials = materialsList()
    return render_template('sku-list.html',materials=materials)

@app.route('/sku/download-list')
def downloadList():
    if not session.get("user"):
        return redirect(url_for("login"))
    materials = materialsList()
    json = excelMaterials(materials)
    df = pd.DataFrame(json)
    file_name = 'SKU pending list.xlsx'
    sheet_name = 'SKU' 
    excel_buffer = io.BytesIO()
    headers = ['sku','SKU_temporal','requested_by','material_type','material_project','similar_to','material_group','material_description1','material_unit','main_material','material_brand','material_model','material_information']
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer,header=headers,sheet_name=sheet_name,index=False)
    excel_buffer.seek(0)
    response = make_response(excel_buffer.getvalue())
    response.headers['Content-Disposition'] = f'attachment; filename={file_name}'
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    return response
    

#IFC files
@app.route('/ifc')
def ifc():
    if not session.get("user"):
        return redirect(url_for("login"))
    export = request.args.get('export')
    response = request.args.get('response')
    return render_template('ifc.html',export=False,response='')

@app.route('/analytics',methods=['POST'])
def ifcAnalytics():
    if not session.get("user"):
        return redirect(url_for("login"))
    ifc_file = request.files['ifcfile']
    path = 'static/ifc/ifc_file.ifc'
    ifc_file.save(path)
    
    type = request.form['analysisType']
    if type == 'inspect':
        c = int(request.form['entity_C'])
        eu = int(request.form['entity_EU']) 
        lg = int(request.form['entity_LG'])
        op = int(request.form['entity_OP'])
        mep = int(request.form['entity_MEPBox'])
        box = int(request.form['entity_Box'])
        h = int(request.form['entity_H'])
        ps = int(request.form['entity_PS'])
        entities = [c,eu,lg,op,mep,box,h,ps]
        getIFCInfo(path,entities)
        response = ''
        export = True
    else:
        response = unitaryTest(path,type)
        export = False
    return render_template('ifc.html',export=export,response=response)

# ROMPEFLIX
@app.route('/rompeflix',methods=['GET'])
def rompeflix():
    action = request.args.get('action')
    token = request.args.get('token')
    
    if token == '0e51e56f135585a3ab38fa0212e074b3776bc9b16376e0b55b270a82c3e91c86':
        sync = action == 'sync'
    else:
        sync = False
        if not session.get("user"):
            return redirect(url_for("login"))
    
    actualitzat,inserit = putMediaRT()
    return render_template('rompeflix.html',sync=sync,actualitzat=actualitzat,inserit=inserit)




# Login Stuff
@app.route("/login")
def login():
    session["flow"] = _build_auth_code_flow(scopes=app_config.SCOPE)
    return render_template("login.html", auth_url=session["flow"]["auth_uri"])

@app.route(app_config.REDIRECT_PATH)
def authorized():
    try:
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}), request.args)
        if "error" in result:
            return render_template("login-authError.html", result=result)
        session["user"] = result.get("id_token_claims")
        _save_cache(cache)
    except ValueError:
        pass
    return redirect(url_for("index"))

@app.route("/display")
def graphcall():
    token = _get_token_from_cache(app_config.SCOPE)
    if not token:
        return redirect(url_for("login"))
    graph_data = requests.get(  # Use token to call downstream service
        app_config.ENDPOINT,
        headers={'Authorization': 'Bearer ' + token['access_token']},
        ).json()
    return render_template('login-display.html', result=graph_data)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        app_config.AUTHORITY + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))


app.jinja_env.globals.update(_build_auth_code_flow=_build_auth_code_flow)  # Used in template

if __name__ == "__main__":
    app.run()