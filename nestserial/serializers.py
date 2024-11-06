from rest_framework import serializers
from .models import Collage,Dept


class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = ['id','CollageCode','CollageName','CollageDistrict','collage',]
        extra_kwagr = {'collage':{'write_only':True}}

class CollageSerializer(serializers.ModelSerializer):
    collage = DeptSerializer(many=True,read_only=True)
    class Meta:
        model = Collage
        fields = ['CType','collage']
