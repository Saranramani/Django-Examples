from  rest_framework import serializers
from django.contrib.auth.models import User
from .models import TodoClass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
    
    def create(self, valid_data):
        user = User.objects.create_user(**valid_data)
        return user

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoClass
        fields = ['id','todo']
    