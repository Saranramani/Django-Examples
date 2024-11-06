from rest_framework import serializers
from .models import Album,Track


class TracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id','title','track','duration','album',]
        extra_kwagr = {'album':{'write_only':True}}

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TracksSerializer(many=True, read_only=True)
    
    class Meta:
        model = Album
        fields = ['id','artist','tracks']