from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app


Drowsiness = Blueprint('Drowsiness',__name__)


@Drowsiness.route('/drowsiness')
def index():
    # rendering webpage
    return render_template('drowsiness.html')




