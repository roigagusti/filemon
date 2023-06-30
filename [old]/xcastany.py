from flask import Blueprint, session, redirect, url_for
#from decorators import login_required

xcastany = Blueprint('xcastany', __name__)

@xcastany.route('/xavi')
#@login_required
def index():
    return "bitch"