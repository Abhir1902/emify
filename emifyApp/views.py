from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

from emifyApp.camera import LaptopVideoCamera 
import time

def index(request):
    return render(request,'emifyApp/home.html')

def gen(camera):
    while True:
        end = time.time() + 5 
        # m = []
        frame = camera.get_frame() 
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        # while time.time() < end: 
        #     m.append(camera.get_result())
        # max = 0
        # for i in m:
        #     if m.count(i) > max:
        #         max = m.count(i)
        # for i in m:
        #     if m.count(i)==max:
        #         print(i)
        #         break 
        
        
def video_feed(request):
    return StreamingHttpResponse(gen(LaptopVideoCamera()),content_type = 'multipart/x-mixed-replace; boundary=frame')

def getR(request): 
    return 