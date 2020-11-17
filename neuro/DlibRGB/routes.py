from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.DlibRGB.camera import VideoCamera

DlibRGB = Blueprint('DlibRGB',__name__)


@DlibRGB.route('/dlibRGB')
def index():
    # rendering webpage
    return render_template('dlibRGB.html')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    


@DlibRGB.route('/video_feed_demo_dlibRGB')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


