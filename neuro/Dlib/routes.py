from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.Dlib.camera import VideoCamera, VideoCameraHog
import os
import os.path
Dlib = Blueprint('Dlib',__name__)


@Dlib.route('/dlib')
def index():
    # rendering webpage
    x =os.path.exists('neuro/static/assets/video/dlib.mp4')
    if x == False:
        return render_template('dlib.html')
    else:
        os.remove('neuro/static/assets/video/dlib.mp4')
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

@Dlib.route('/uploader_dlib', methods = ['GET', 'POST'])
def upload_file():
   success = None
   if request.method == 'POST':
      f = request.files['file']
      f.save("neuro/static/assets/video/"+f.filename)
      os.rename("neuro/static/assets/video/"+f.filename,r"neuro/static/assets/video/dlib.mp4")
      success = "File uploaded successfully"
      return render_template('dlib.html',success=success)