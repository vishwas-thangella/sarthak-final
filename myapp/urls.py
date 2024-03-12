from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("services",views.Services,name="services"),
    path("contact",views.contact,name="contact"),
    path("achivements",views.achivements,name="achivements")
]
