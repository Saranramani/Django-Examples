from django.urls import path
from . import views

urlpatterns = [
    path('getall/',views.CollageList.as_view()),
    path('addcollage/',views.CreateCollage.as_view()),
    path('adddept/',views.CreateDept.as_view()),
    path('getbyid/<int:pk>',views.GetByIdList.as_view()),
    path('update/',views.UpdateList.as_view()),
    path('delete/',views.DeleteList.as_view()),
]
