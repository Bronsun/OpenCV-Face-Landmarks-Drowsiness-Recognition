from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app


Contact = Blueprint('Contact',__name__)


@Contact.route('/contact')
def contact():
    # rendering webpage
    return render_template('contact.html')




