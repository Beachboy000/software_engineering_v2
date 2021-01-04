from django.contrib import admin
from django.urls import path, include
from . import views
from .views import showTemplate


urlpatterns = [
    path('',views.showTemplate,name='showTemplate'),
]

