from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)
        res = {
            "Token":token.key,
            "UserDetails": serializer.data
        }
        return Response(res,status=status.HTTP_201_CREATED)
    return Response({"A user with this username already exixst"},status=status.HTTP_409_CONFLICT)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        return Response({"Detail":"Successfully Login","username":user.username},status=200)
    else:
        return Response({"Detail":"Login Failed"},status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def getall(request):
    try:
        item = User.objects.all()
    except User.DoesNotExist:
        return Response({"Detail":"There is No Users"},status=status.HTTP_204_NO_CONTENT)
    allUsers = UserSerializer(item,many=True)
    return Response(allUsers.data,status=200)

@api_view(['GET'])
def getbyid(request,id):
    try:
        item = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"Detail":"No User Available in this Id"},status=status.HTTP_204_NO_CONTENT)
    allUsers = UserSerializer(item,many=False)
    return Response(allUsers.data,status=200)

@api_view(['PUT'])
def update(request,id):
    try:
        item = User.objects.get(id=id)
    except:
        return Response({"Detail":"There is No User, can't Update"},status=status.HTTP_403_FORBIDDEN)
    allUsers = UserSerializer(item,data=request.data)
    if allUsers.is_valid():
        allUsers.save()
        return Response(allUsers.data,status=status.HTTP_202_ACCEPTED)
    return Response(allUsers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request,id):
    try:
        item = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"Detail":"No User can't to Delete"},status=status.HTTP_404_NOT_FOUND)
    item.delete()
    return Response({"Detail":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)




# @api_view(['POST'])
# def login(req):
#     username = req.data.get('username')
#     password = req.data.get('password')
#     user = authenticate(req,username=username,password=password)
#     if user is not None:
#         return Response({"Details":"Login Successfully","username":user.username,"e-mail":user.email},status=201)
#     else:
#         return Response({"Details":"Login Failed"},status=400)


# @api_view(['POST'])
# def signup(req):
#     serializer = UserSerializer(data=req.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         token = Token.objects.create(user=user)
#         res = {
#             "token":token.key,
#             "user":serializer.data
#         }
#         return Response(res,status=201)
#     return Response(serializer.errors,status=400)
