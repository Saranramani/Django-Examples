from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def register(request):
    content = {
        "Details":"Permitted"
    }
    return Response(content)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        token = Token.objects.get(user=user)
        res = {
            "token":token.key,
            "Details":"User was authenticated and Login successfully!"
        }
        return Response(res,status=200)
    else: 
        return Response({"Details":"Login Failed"},status=400)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)
        res = {
            "token":token.key,
            "user":serializer.data
        }
        return Response(res,status=201)
    return Response(serializer.errors,status=400)
