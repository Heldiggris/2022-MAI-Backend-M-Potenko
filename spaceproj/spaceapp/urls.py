from django.urls import path, re_path
from django.http import HttpResponse
from spaceapp.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    # re_path('(?P<pk>\d+)/', space_view),


    path('user/<str:user_name>/my_planets/', MyPlanetsView.as_view(), name="user_planets"),
    path('user/<str:user_name>/notes/', NotesView.as_view(), name="user_planets"),

    # path('create_planet/', create_planet, name="create_planet"),
    path('user/<str:user_name>', UserView.as_view(), name="user"),
    # path('create_user/<str:user_name>', create_user, name="create_user"),
    # path('planetsList/', planetsList, name="planetsList"),

    path('planet/<str:planet_name>', PlanetView.as_view(), name="planet"),
    path('categoryes', CategoryesView.as_view(), name="categories"),
    path('planets', PlanetsView.as_view(), name="planets"),
    # path,
]
