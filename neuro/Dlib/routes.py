from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.Dlib.camera import VideoCamera, VideoCameraHog

Dlib = Blueprint('Dlib',__name__)


@Dlib.route('/dlib')
def index():
    # rendering webpage
    return render_template('dlib.html')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    


@Dlib.route('/video_feed_demo_dlib')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@Dlib.route('/video_feed_demo_dlib_2')
def video_feed_2():
    return Response(gen(VideoCameraHog()), mimetype='multipart/x-mixed-replace; boundary=frame')

