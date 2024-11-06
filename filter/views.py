from .models import Filter
from .serializers import FilterSerializer
from rest_framework import generics
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import pagination


# class LargeResultsSetPagination(pagination.PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

# class StandardResultsSetPagination(pagination.PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

class BlogGet(generics.ListAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


class BlogPost(generics.CreateAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer

class PurchaseList(generics.ListAPIView):
    serializer_class = FilterSerializer

    
    def get_queryset(self):
        queryset = Filter.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset1 = queryset.filter(first_name=username)
            return queryset1
        return Response({"Passed params was not in table!"})


