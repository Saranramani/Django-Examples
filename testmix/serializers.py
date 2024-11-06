from rest_framework import serializers
from .models import Blog1

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog1
        fields = '__all__'