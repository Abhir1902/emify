from django.urls import path
from emifyApp import views 
urlpatterns = [
    path('video_feed/',views.video_feed),
    path('index/',views.index)
]
