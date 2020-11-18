from flask import render_template, url_for, flash, redirect,request,Blueprint,Response
from neuro import app
from neuro.ThermalDrowsiness.camera import VideoCamera
import os
import os.path
ThermalDrowsiness = Blueprint('ThermalDrowsiness',__name__)


@ThermalDrowsiness .route('/thermalDrowsiness')
def index():
    # rendering webpage
    x =os.path.exists('neuro/static/assets/video/thermalD.mp4')
    if x == False:
        return render_template('thermalDrowsiness.html')
    else:
        os.remove('neuro/static/assets/video/thermalD.mp4')
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

@ThermalDrowsiness.route('/uploader_thermalD', methods = ['GET', 'POST'])
def upload_file():
   success = None
   if request.method == 'POST':
      f = request.files['file']
      f.save("neuro/static/assets/video/"+f.filename)
      os.rename("neuro/static/assets/video/"+f.filename,r"neuro/static/assets/video/thermalD.mp4")
      success = "File uploaded successfully"
      return render_template('thermalDrowsiness.html',success=success)