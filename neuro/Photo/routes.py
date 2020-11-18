from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.Photo.camera import VideoCameraThermalHaar,VideoCameraThermalHog,VideoCameraRGB
import os
import os.path
Photo = Blueprint('Photo',__name__)


@Photo.route('/photo')
def index():
    # rendering webpage
    x =os.path.exists('neuro/static/assets/Photos/demo.png')
    if x == False:
        return render_template('photo.html')
    else:
        os.remove('neuro/static/assets/Photos/demo.png')
    return render_template('photo.html')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    


@Photo.route('/video_feed_demo_photo_haar')
def video_feed():
    return Response(gen(VideoCameraThermalHog()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@Photo.route('/video_feed_demo_photo_hog')
def video_feed_2():
    return Response(gen(VideoCameraThermalHaar()), mimetype='multipart/x-mixed-replace; boundary=frame')


@Photo.route('/video_feed_demo_photo_rgb')
def video_feed_3():
    return Response(gen(VideoCameraRGB()), mimetype='multipart/x-mixed-replace; boundary=frame')    

@Photo.route('/uploader_photo', methods = ['GET', 'POST'])
def upload_file():
   success = None
   if request.method == 'POST':
      f = request.files['file']
      f.save("neuro/static/assets/Photos/"+f.filename)
      os.rename("neuro/static/assets/Photos/"+f.filename,r"neuro/static/assets/Photos/demo.png")
      success = "File uploaded successfully"
      return render_template('photo.html',success=success)