from django.urls import path
from . import views
from . import views1

urlpatterns = [
    path('login/',views.Login.as_view()),
    path('signup/',views.Signup.as_view()),
    path('getall/',views.TodoApiGet.as_view()),
    path('getbyid/<int:pk>/',views.TodoApiGetById.as_view()),
    path('add/',views.TodoApiPost.as_view()),
    path('update/<int:pk>/',views.TodoApiPut.as_view()),
    path('delete/<int:pk>/',views.TodoApiDelete.as_view()),
    # path('todoapi/',views1.TodoApiGet.as_view()),
    # path('todoapi/<int:pk>',views1.TodoApiGet.as_view()),
]
