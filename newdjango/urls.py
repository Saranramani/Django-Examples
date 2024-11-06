from django.urls import path,include
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Home page</h1>")


urlpatterns = [
    path('',home),
    path('api/',include('apiapp.urls')),
    path('cls/',include('classapp.urls')),
    path('gen/', include('testgen.urls')),
    path('test/',include('testingapp.urls')),
    path('mix/', include('testmix.urls')),
    path('todo/',include('Todolist.urls')),
    path('token/',include('tokenapp.urls')),
    path('filter/',include('filter.urls')),
    path('serial/',include('serial.urls')),
    path('nest/',include('nestserial.urls')),
]
