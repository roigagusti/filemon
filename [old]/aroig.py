from flask import Blueprint, session, redirect, url_for
#from decorators import login_required

aroig = Blueprint('aroig', __name__)



### APP ###
#-- PROVES --#


#-- PRODUCCIÓ --#
@aroig.route('/agus')
#@login_required
def agusti():
    return "Agustí page en blueprint"