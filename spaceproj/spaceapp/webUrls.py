from django.contrib import admin
from django.urls import path, include
from spaceapp.webViews import *

urlpatterns = [
    path('info/', space_info),
]
