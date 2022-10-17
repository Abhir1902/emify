from django.shortcuts import render
from django.http import StreamingHttpResponse

from emifyApp.camera import LaptopVideoCamera 

def index(request):
    return render(request,'emifyApp/home.html')

def gen(camera):
    while True: 
        frame = camera.get_frame() 
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
def video_feed(request):
    return StreamingHttpResponse(gen(LaptopVideoCamera()),content_type = 'multipart/x-mixed-replace; boundary = frame')