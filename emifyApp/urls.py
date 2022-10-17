from django.urls import path
from emifyApp import views, camera
urlpatterns = [
    path('',views.index, name = 'index'),
    path('video_feed',views.video_feed, name = 'video_feed'),
    path('emotion',views.getR, name = "emotion")
]
