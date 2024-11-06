from serial.models import Album,Track
from rest_framework.response import Response
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help='Retriveing datas from Album and Track'
    
    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='Get artist name')
        parser.add_argument('title', type=str, help='Get name of the track')
    
    def handle(self, *args, **kwargs):
        album_id = kwargs['id']
        track_title = kwargs['title']
        
        album = Album.objects.get(id=album_id)
        tracks = Track.objects.get(title=track_title)
        
        return (album.artist)