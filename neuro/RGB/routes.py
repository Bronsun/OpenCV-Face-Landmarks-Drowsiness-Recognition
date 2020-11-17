from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app


RGB = Blueprint('RGB',__name__)


@RGB.route('/rgb')
def index():
    # rendering webpage
    return render_template('rgb.html')
