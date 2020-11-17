from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.Hog.camera import VideoCamera

Hog = Blueprint('Hog',__name__)


@Hog.route('/hog')
def index():
    # rendering webpage
    return render_template('hog.html')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    


@Hog.route('/video_feed_hog')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

