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
detector = dlib.get_frontal_face_detector() #For detecting faces
landmark_path="neuro/static/assets/RGBModels/predictor.dat" #Path of the file - if stored in the same directory. Else, give the relative path
predictor = dlib.shape_predictor(landmark_path) #For identifying landmarks
yawn_status = False 
yawn_count = 0

def yawning(image):
       
        facial_landmarks = get_facial_landmarks(image)
        if type(facial_landmarks) == str:
            return image, 0
       
        landmarks_image = landmarks_annotation(image, facial_landmarks)
        
        upperlip_centroid = upperlip(facial_landmarks)
        lower_lip_centroid = lowerlip(facial_landmarks)
       
        lips_dist = abs(upperlip_centroid - lower_lip_centroid)
        return landmarks_image, lips_dist   

def get_facial_landmarks(image):
        face = detector(image, 1)
        
        if len(face) > 1:
            return "Multiple faces detected in the frame!!"
        if len(face) == 0:
            return "No face detected in the frame!!"
        
        return np.matrix([[pred.x, pred.y] for pred in predictor(image, face[0]).parts()])

def get_facial_landmarks(image):
        face = detector(image, 1)
      
        if len(face) > 1:
            return "Multiple faces detected in the frame!!"
        if len(face) == 0:
            return "No face detected in the frame!!"
        
        return np.matrix([[pred.x, pred.y] for pred in predictor(image, face[0]).parts()])

   
def landmarks_annotation(image, facial_landmarks):
     
        image = image.copy()
        for coord, p in enumerate(facial_landmarks):
           
            position = (p[0, 0], p[0, 1])
          
            cv2.putText(image, str(coord), position, cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 255, 255))
        return image

    
def upperlip(facial_landmarks):
        ulip = []
      
        for i in range(50,53):
            
            ulip.append(facial_landmarks[i])
        for i in range(61,64):
            
            ulip.append(facial_landmarks[i])
       
        ulip_mean = np.mean(ulip, axis=0)
        return int(ulip_mean[:,1])#

     
def lowerlip(facial_landmarks):
        llip = []
        
        for i in range(65,68):
            
            llip.append(facial_landmarks[i])
        for i in range(56,59):
           
            llip.append(facial_landmarks[i])
        
        llip_mean = np.mean(llip, axis=0)
        return int(llip_mean[:,1])


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
        yawn_status = False 
        yawn_count = 0
        _, image_frame = self.video.read()
        landmarks_image, lips_dist = yawning(image_frame)
        previous_status = yawn_status  
        image_frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
        interpolation=cv2.INTER_AREA)   

    
        if lips_dist > 47:
            yawn_status = True
            output_text = " Number of Yawns: " + str(yawn_count + 1)
            cv2.putText(landmarks_image, "You are yawning", (50,450), cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,0))
            cv2.putText(landmarks_image, output_text, (50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255))
            
        else:
            yawn_status = False 
            
        if previous_status == True and yawn_status == False:
            yawn_count += 1
        
            
        ret, jpeg = cv2.imencode('.jpg', landmarks_image)
        return jpeg.tobytes()



