from rest_framework.decorators import APIView
from .serializers import ClassSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import TodoClass
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication


class Login(APIView):
    def post(self,request):
        username=request.data.get('username')
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

class Signup(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            res = {
                "Details":"New user was created",
                "token":token.key,
                "user":serializer.data
            }
            return Response(res,status=201)
        return Response(serializer.errors,status=400)


class Logout(APIView):
    # permission_classes = (IsAuthenticated)
    def post(self, request):
        username = request.user.username
        request.user.auth_token.delete()
        return Response({f"Logged Out {username}!"}, status=status.HTTP_204_NO_CONTENT)

class TodoApiGet(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        try:
            user = TodoClass.objects.all()
        except TodoClass.DoesNotExist:
            return Response({"Detail":"Nothing To Show The table Was Empty!"},status=status.HTTP_400_BAD_REQUEST)
        serializer = ClassSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class TodoApiGetById(APIView):
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self,request,pk):
        try:
            user = TodoClass.objects.get(id=pk)
            serializer = ClassSerializer(user,many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except TodoClass.DoesNotExist:
            return Response({"Detail":"Nothing In This Id"},status=status.HTTP_404_NOT_FOUND)
        

class TodoApiPost(APIView):
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TodoApiPut(APIView):
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def put(self,request,pk):
        try:
            user = TodoClass.objects.get(id=pk)
            serializer = ClassSerializer(user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({"Detail":"Nothing In This Id, Can't Update"},status=status.HTTP_400_BAD_REQUEST)
        

class TodoApiDelete(APIView):
#     authentication_classes=[TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
    def delete(self,request,pk):
        try:
            user = TodoClass.objects.get(id=pk)
        except:
            return Response({"Detail":"Nothing In This Id, Can't Delete!"},status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)