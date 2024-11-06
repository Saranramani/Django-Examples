from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog


# get all api
class BlogGet(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# getbyid api
class BlogGetById(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# post api
class BlogPost(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# put api
class BlogPut(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# delete api
class BlogDelete(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# get all and post api
class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# getbyid and put and delete
class BlogRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer