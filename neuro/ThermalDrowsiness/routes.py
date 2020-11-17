from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.ThermalDrowsiness.camera import VideoCamera

ThermalDrowsiness = Blueprint('ThermalDrowsiness',__name__)


@ThermalDrowsiness .route('/thermalDrowsiness')
def index():
    # rendering webpage
    return render_template('thermalDrowsiness.html')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    


@ThermalDrowsiness .route('/video_feed_thermal_drowsiness')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

