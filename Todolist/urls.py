from django.urls import path
from . import views

urlpatterns = [
    path('getall/',views.getTodo),
    path('getbyid/<int:tid>/',views.getByIdTodo),
    path('add/',views.addTodo),
    path('update/<int:tid>/',views.updateTodo),
    path('delete/<int:tid>/',views.deleteTodo),
]