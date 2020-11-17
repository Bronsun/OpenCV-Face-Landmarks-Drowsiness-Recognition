#camera.py
# import the necessary packages
import cv2
import matplotlib.pyplot as plt
import dlib
from imutils import face_utils 
import numpy as np 
import argparse 
import imutils

# defining face detector

ds_factor=0.6

class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()
   
    def get_frame(self):
       #extracting frames
        ret, frame= self.video.read()

        frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
        interpolation=cv2.INTER_AREA)   

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face_rects=dlib.simple_object_detector('/neuro/static/assets/ThermalModels/hog_detector.svm')
        

        rects=face_rects(gray,1)
        for (i, rect) in enumerate(rects): 
    
            (x, y, w, h) = face_utils.rect_to_bb(rect) 
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2) 

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

