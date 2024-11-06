from .serializers import BlogSerializer
from .models import Blog1
from rest_framework import mixins
from rest_framework import generics

class BlogGetPost(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Blog1.objects.all()
    serializer_class = BlogSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class BlogGetId(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Blog1.objects.all()
    serializer_class = BlogSerializer
    
    def get(self,request,pk,*args,**kwargs):
        return self.retrieve(request,id=pk,*args,**kwargs)

class BlogPut(mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Blog1.objects.all()
    serializer_class = BlogSerializer
    
    def get(self,request,pk,*args,**kwargs):
        return self.update(request,id=pk,*args,**kwargs)

class BlogDelete(mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Blog1.objects.all()
    serializer_class = BlogSerializer
    
    def get(self,request,pk,*args,**kwargs):
        return self.destroy(request,id=pk,*args,**kwargs)