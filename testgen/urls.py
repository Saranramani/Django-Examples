from django.urls import path
from . import views 

urlpatterns = [
    path('getall/', views.BlogGet.as_view()),
    path('getbyid/<int:pk>/', views.BlogGetById.as_view()),
    path('add/', views.BlogPost.as_view()),
    path('update/<int:pk>/', views.BlogPut.as_view()),
    path('delete/<int:pk>/', views.BlogDelete.as_view()),
    path('todos/', views.BlogListCreate.as_view()),
    path('todos/<int:pk>/', views.BlogRetriveUpdateDestroy.as_view()),
]