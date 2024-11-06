from rest_framework.urls import path
from . import views

urlpatterns = [
    path('login/',views.login),
    path('signup/',views.signup),
    path('getall/',views.getall),
    path('getbyid/<int:id>/',views.getbyid),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
]
