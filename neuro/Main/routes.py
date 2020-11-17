from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.Main.camera import VideoCamera

Main = Blueprint('Main',__name__)


@Main.route('/')
def index():
    # rendering webpage
    return render_template('main.html')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

