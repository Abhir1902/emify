import cv2
from cv2 import CAP_DSHOW 
from django.conf import settings
from deepface import DeepFace 
class LaptopVideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0,CAP_DSHOW)
        
    def __del__(self):
        self.video.release()
    
    def get_frame(self): 
        success,frame = self.video.read() 
        result = DeepFace.analyze(frame,actions = ['emotion'],enforce_detection=False)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,result['dominant_emotion'],(50,50),font,3, (0,0,0),2,cv2.LINE_4)
        ret, jpeg = cv2.imencode('.jpeg',frame)
        return jpeg.tobytes()

        
    def get_result(self):
        success,frame = self.video.read()
        result = DeepFace.analyze(frame,actions = ['emotion'],enforce_detection=False)
        return result['dominant_emotion'] 