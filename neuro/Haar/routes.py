from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.Haar.camera import VideoCamera
import os
import os.path
Haar = Blueprint('Haar',__name__)


@Haar.route('/haar')
def index():
    x =os.path.exists('neuro/static/assets/video/Haar.mp4')
    if x == False:
        return render_template('haar.html')
    else:
        os.remove('neuro/static/assets/video/Haar.mp4')
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

@Haar.route('/uploader_haar', methods = ['GET', 'POST'])
def upload_file():
   success = None
   if request.method == 'POST':
      f = request.files['file']
      f.save("neuro/static/assets/video/"+f.filename)
      os.rename("neuro/static/assets/video/"+f.filename,r"neuro/static/assets/video/Haar.mp4")
      success = "File uploaded successfully"
      return render_template('haar.html',success=success)