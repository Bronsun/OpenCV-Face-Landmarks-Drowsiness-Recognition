from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.Haar.camera import VideoCamera

Haar = Blueprint('Haar',__name__)


@Haar.route('/haar')
def index():
    # rendering webpage
    return render_template('haar.html')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    


@Haar.route('/video_feed_haar')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

