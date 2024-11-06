from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer,UserSerializer 
from .models import Todos
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTodo(req):
    todo = Todos.objects.all()
    TodoData = TodoSerializer(todo,many=True)
    return Response(TodoData.data,status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getByIdTodo(req,tid):
    try:
        todo = Todos.objects.get(id=tid)
    except Todos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    TodoData = TodoSerializer(todo,many=False)
    return Response(TodoData.data,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTodo(req):
    todo = TodoSerializer(data=req.data)
    if todo.is_valid():
        todo.save()
        return Response(todo.data,status=status.HTTP_201_CREATED)
    return Response(todo.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTodo(req,tid):
    try:
        todo = Todos.objects.get(id=tid)
    except Todos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    todoData = TodoSerializer(todo,data=req.data)
    if todoData.is_valid():
        todoData.save()
        return Response(todoData.data)
    return Response(todoData.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTodo(req,tid):
    try:
        todo = Todos.objects.get(id=tid)
    except Todos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)