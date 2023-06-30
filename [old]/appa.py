from flask import Flask, render_template, session, request, redirect, url_for

# Importacions per LoginWithMicrosoft
import requests
from flask_session import Session
import app_config
from classes.functionsMicrosoft import _load_cache, _save_cache, _build_msal_app, _build_auth_code_flow, _get_token_from_cache

# BLueprints
from aroig import aroig
from mrubio import mrubio
from xcastany import xcastany
from rgine import rgine


app = Flask(__name__)
app.config.from_object(app_config)
app.register_blueprint(aroig)
app.register_blueprint(mrubio)
app.register_blueprint(xcastany)
app.register_blueprint(rgine)
Session(app)


# Necessari per quan es treballa en localhost
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)



### APP ###
#-- PROVES --#


#-- PRODUCCIÓ --#
@app.route("/")
def index():
    if not session.get("user"):
        return redirect(url_for("login"))
    username = session["user"].get("name")
    text = 'Welcome to Filemon, ' + username
    return render_template('home.html',user=username,text=text)



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
            return render_template("auth_error.html", result=result)
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
    return render_template('display.html', result=graph_data)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        app_config.AUTHORITY + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))


app.jinja_env.globals.update(_build_auth_code_flow=_build_auth_code_flow)  # Used in template


if __name__ == "__main__":
    app.run()