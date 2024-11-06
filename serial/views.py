from rest_framework import generics
from .serializers import AlbumSerializer,TracksSerializer
from .models import Album,Track

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TracksPost(generics.CreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TracksSerializer

class Tracks(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TracksSerializer
