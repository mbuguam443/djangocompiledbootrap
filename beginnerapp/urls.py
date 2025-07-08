from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfunctionCall, name="index"),
    path('about', views.myFunctionAbout, name="about"),
    path('add/<int:a>/<int:b>', views.myFunctionAdd, name="add"),
    path('json/<str:name>/<int:age>', views.myFunctionJson, name="json"),
    path('myfirstpage', views.myFirstPage, name="myfirstpage"),
    path('mysecondpage', views.mySecondPage, name="mysecondpage"),
]
