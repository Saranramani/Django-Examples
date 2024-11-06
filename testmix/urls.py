from rest_framework.urls import path
from . import views

urlpatterns = [
    path('getall/',views.BlogGetPost.as_view()),
    path('getbyid/<int:pk>',views.BlogGetId.as_view()),
    path('update/<int:pk>',views.BlogPut.as_view()),
    path('delete/<int:pk>',views.BlogDelete.as_view()),
]
