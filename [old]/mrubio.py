from flask import Blueprint, session, redirect, url_for
#from decorators import login_required

mrubio = Blueprint('mrubio', __name__)

@mrubio.route('/marc')
#@login_required
def marc():
    return "Marc page"