from rest_framework.decorators import APIView
from .serializers import ClassSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import TodoClass

class TodoApiGet(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            try:
                user = TodoClass.objects.get(id=pk)
            except TodoClass.DoesNotExist:
                return Response({"Detail":"Id Was Not Found!"},status=status.HTTP_404_NOT_FOUND)
            serializer = ClassSerializer(user,many=False)
            return Response(serializer.data,status=status.HTTP_200_OK) 
        user = TodoClass.objects.all()
        serializer = ClassSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,pk=None):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Detail":"New Data Added Successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            user = TodoClass.objects.get(id=pk)
        except:
            return Response({"Detail":"Nothing In This Id, Can't Update"},status=status.HTTP_400_BAD_REQUEST)
        serializer = ClassSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Detail":"Item Has Been Updated Successfully!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_308_PERMANENT_REDIRECT)

    def delete(self,request,pk):
        try:
            user = TodoClass.objects.get(id=pk)
        except TodoClass.DoesNotExist:
            return Response({"Detail":"Nothing In This Id, Can't Delete!"},status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"Detail":"Item Has Been Deleted Successfully!"},status=status.HTTP_204_NO_CONTENT)