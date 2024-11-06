from .serializers import CollageSerializer,DeptSerializer
from .models import Collage,Dept
from rest_framework import generics
from rest_framework.response import Response


class CreateCollage(generics.CreateAPIView):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer

class CreateDept(generics.CreateAPIView):
    queryset = Dept.objects.all()
    serializer_class = DeptSerializer

class CollageList(generics.ListAPIView):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer

class GetByIdList(generics.RetrieveAPIView):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer

class UpdateList(generics.UpdateAPIView):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer

class DeleteList(generics.DestroyAPIView):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializer

