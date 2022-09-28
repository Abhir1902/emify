import cv2 
from django.conf import settings
from deepface import DeepFace 
class LaptopVideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        if not self.video.isOpened():
            self.video = cv2.VideoCapture(1) 
        
    def __del__(self):
        self.video.release()
    
    def get_frame(self): 
        success,frame = self.video.read() 
        result = DeepFace.analyze(frame,actions = ['emotion'],enforce_detection=False)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,result['dominant_emotion'],(50,50),font,3, (0,0,0),2,cv2.LINE_4)
        ret, jpeg = cv2.imencode('.jpg',frame)
        return jpeg.tobytes()