from django.urls import path
from . import views

urlpatterns = [
    path('purchase/',views.PurchaseList.as_view()),
    path('getall/', views.BlogGet.as_view()),
    path('add/', views.BlogPost.as_view()), 
]

