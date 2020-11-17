from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
import cv2

Thermal = Blueprint('Thermal',__name__)


@Thermal.route('/thermal')
def index():
    return render_template('thermal.html')

