from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.DlibRGB.camera import VideoCamera
import os
import os.path
DlibRGB = Blueprint('DlibRGB',__name__)


@DlibRGB.route('/dlibRGB')
def index():
    # rendering webpage
    x = os.path.exists('neuro/static/assets/video/RGBDetect.mp4')
    if x == False:
        return render_template('dlibRGB.html')
    else:
        os.remove('neuro/static/assets/video/RGBDetect.mp4')
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


@DlibRGB.route('/uploader_RGBDetect',methods=['GET','POST'])
def upload_file():
   success = None
   if request.method == 'POST':
      f = request.files['file']
      f.save("neuro/static/assets/video/"+f.filename)
      os.rename("neuro/static/assets/video/"+f.filename,r"neuro/static/assets/video/RGBDetect.mp4")
      success = "File uploaded successfully"
      return render_template('dlibRGB.html',success=success)