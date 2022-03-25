from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST

@require_GET
def space_view(request, pk):
    # return HttpResponse(f"<html> <h1> Space #{pk} </h1>  </html>")
    return render(request, 'base.html', {'guest': pk})

@require_GET
def user(request, user_name):
    return JsonResponse({"login": user_name})

@require_POST
def create_user(request, user_name):
    return JsonResponse({"login": user_name})

@require_GET
def planetsList(request):
    return JsonResponse({"planet_list": ["Марс", "Земля", "Венера"]})

@require_GET
def categories(request):
    return JsonResponse({"categories": ["Карлик", "Газовый гигант", "Экзопланета"]})

@require_GET
def planetsList(request):
    return JsonResponse({"planet_list": ["Марс", "Земля", "Венера"]})

@require_GET
def planet(request, planet_name):
    return JsonResponse({"planet_name": planet_name, "author": "user1234"})

@require_POST
def create_planet(request):
    return JsonResponse({"planet_name": 'Сатурн'})


@require_GET
def user_planets(request, user_name):
    return JsonResponse({"planet_list": [{'id': 1}, {'id': 2}]})
# Create your views here.
