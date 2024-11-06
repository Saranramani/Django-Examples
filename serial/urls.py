from django.urls import path
from . import views

urlpatterns = [
    path('albums/',views.AlbumList.as_view()),
    path('tracks/',views.TracksPost.as_view()),
    path('tracklist/',views.Tracks.as_view()),
]