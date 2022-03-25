from django.urls import path, re_path
from django.http import HttpResponse
from spaceapp.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path('(?P<pk>\d+)/', space_view),

    path('user/<str:user_name>', user, name="user"),

    path('user/<str:user_name>/my_planets/', user_planets, name="user_planets"),

    path('create_planet/', create_planet, name="create_planet"),

    path('create_user/<str:user_name>', create_user),
    path('planetsList/', planetsList),
    path('categories/', categories),

    path('planet/<str:planet>', planet),

    # path,
]
