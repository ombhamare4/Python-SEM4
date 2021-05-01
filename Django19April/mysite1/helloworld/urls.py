from django.contrib import admin
from django.urls import path
from .import views
#url.py of helloworld folder
urlpatterns = [
    path('hello/',views.hello ,name="hello"),
    path('greet/',views.greet ,name="greet"),
    path('student/',views.student ,name="student"),
]
