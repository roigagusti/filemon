from flask import Blueprint, session, redirect, url_for
#from decorators import login_required

rgine = Blueprint('rgine', __name__)

@rgine.route('/ricard')
#@login_required
def ricard():
    return "Ricard page"