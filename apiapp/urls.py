from django.urls import path
from . import views

urlpatterns = [
    path('getall/',views.getData, name='gettodos'),
    path('getbyid/<int:id>/',views.getById, name='getalltodos'),
    path('add/',views.addData, name='addtodo'),
    path('update/<int:id>/',views.updateData, name='updatetodo'),
    path('delete/<int:id>/',views.deleteData, name='deletetodo'),
]