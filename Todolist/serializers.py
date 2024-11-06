from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todos

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
    
    def create(self, valid_data):
        user = User.objects.create_user(**valid_data)
        return user

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'