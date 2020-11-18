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
face_cascade=cv2.CascadeClassifier('neuro/static/assets/ThermalModels/cascade.xml')
face_cascade_RGB=cv2.CascadeClassifier('neuro/static/assets/RGBModels/cascade.xml')
ds_factor=0.6


class VideoCameraThermalHaar(object):
  
    def __init__(self):
       #capturing video
       self.video = cv2.imread("neuro/static/assets/Photos/demo.png")
    
    

    def get_frame(self):
       #extracting frames
        ret= self.video.copy()

        ret=cv2.resize(ret,None,fx=ds_factor,fy=ds_factor,
        interpolation=cv2.INTER_AREA)   

        gray=cv2.cvtColor(ret,cv2.COLOR_BGR2GRAY)
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in face_rects:
            cv2.rectangle(ret,(x,y),(x+w,y+h),(0,255,0),2)
            break
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', ret)
        return jpeg.tobytes()

class VideoCameraThermalHog(object):
    def __init__(self):
       #capturing video
       self.video = cv2.imread('neuro/static/assets/Photos/demo.png')
    
    
    def get_frame(self):
       #extracting frames
        ret= self.video.copy()

        ret=cv2.resize(ret,None,fx=ds_factor,fy=ds_factor,
        interpolation=cv2.INTER_AREA)   

        gray=cv2.cvtColor(ret,cv2.COLOR_BGR2GRAY)
        face_rects=dlib.simple_object_detector('neuro/static/assets/ThermalModels/hog_detector.svm')
        predictor = dlib.shape_predictor('neuro/static/assets/ThermalModels/predictor.dat')

        rects=face_rects(gray,1)
        for (i, rect) in enumerate(rects): 
    # We will determine the facial landmarks for the face region, then 
            # can convert the facial landmark (x, y)-coordinates to a NumPy array 
            shape = predictor(gray, rect) 
            shape = face_utils.shape_to_np(shape) 
        
            # We then convert dlib's rectangle to a OpenCV-style bounding box 
            # [i.e., (x, y, w, h)], then can draw the face bounding box 
            (x, y, w, h) = face_utils.rect_to_bb(rect) 
            cv2.rectangle(ret, (x, y), (x + w, y + h), (255, 255, 0), 2) 
        
            # We then loop over the (x, y)-coordinates for the facial landmarks  
            # and draw them on the image 
            for (x, y) in shape: 
                cv2.circle(ret, (x, y), 2, (0, 0, 255), -2) 
        ret, jpeg = cv2.imencode('.jpg', ret)
        return jpeg.tobytes()

class VideoCameraRGB(object):
    def __init__(self):
       #capturing video
       self.video = cv2.imread("neuro/static/assets/Photos/demo.png")
    
   

    def get_frame(self):
       #extracting frames
        ret= self.video.copy()

        ret=cv2.resize(ret,None,fx=ds_factor,fy=ds_factor,
        interpolation=cv2.INTER_AREA)   

        gray=cv2.cvtColor(ret,cv2.COLOR_BGR2GRAY)
        face_rects=face_cascade_RGB.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in face_rects:
            cv2.rectangle(ret,(x,y),(x+w,y+h),(0,255,0),2)
            break
        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', ret)
        return jpeg.tobytes()