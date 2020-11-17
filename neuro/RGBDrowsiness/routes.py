from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.RGBDrowsiness.camera import VideoCamera

RGBDrowsiness = Blueprint('RGBDrowsiness',__name__)


@RGBDrowsiness .route('/rgbDrowsiness')
def index():
    # rendering webpage
    return render_template('rgbdrowsiness.html')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    


@RGBDrowsiness .route('/video_feed_thermal_rgbdrowsiness')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

