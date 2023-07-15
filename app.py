from flask import Flask, render_template, request, redirect, url_for, make_response
import pandas as pd
import io
from classes.functions import *
from classes.rompeflix import putMediaRT

app = Flask(__name__)


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
# KPI
@app.route('/components')
def kpi():
    return render_template('evolution.html',components=components,cases=cases,projects=projects,headers=headers)

#SKU REQUEST
@app.route('/sku/request')
def skuRequest():
    global staff
    global supplyTeam
    global materials
    if staff == '':
        staff,supplyTeam = get011hTeam()        
        materials = materialGroup()
    response_value = request.args.get('response')
    return render_template('sku.html',staff=staff,supplyTeam=supplyTeam,materials=materials,response=response_value)

@app.route('/sku/add',methods=['POST'])
def addRequest():
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
    materials = materialsList()
    return render_template('sku-list.html',materials=materials)

@app.route('/sku/download-list')
def downloadList():
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
    return render_template('ifc.html')

# ROMPEFLIX
@app.route('/rompeflix')
def rompeflix():
    action = request.args.get('action')
    token = request.args.get('token')
    if token == '0e51e56f135585a3ab38fa0212e074b3776bc9b16376e0b55b270a82c3e91c86':
        sync = action == 'sync'
    else:
        sync = False
    actualitzat,inserit = putMediaRT()
    return render_template('rompeflix.html',sync=sync,actualitzat=actualitzat,inserit=inserit)

if __name__ == '__main__':
    app.run()