from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, viewsets

from .models import Planet, Category, User
from .serializers import *
from .forn import *

from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist

class PlanetsView(APIView):
    def get(self, request):
        planets = Planet.objects.all()
        serializer = PlanetSerializer(planets, many=True, read_only=True)
        return Response({'planets' : serializer.data})
    def post(self, request):
            form = UserForm(request.POST)
        if form.is_valid():
        post = form.save()
        return JsonResponse({'msg': 'Пост сохранен','id': post.id})

        return Response({'error': None, 'result': 'Планета успешно добавлена'})

class PlanetView(APIView):
    def get(self, request, planet_name):
        try:
            planet = Planet.objects.get(name=planet_name)
            serializer = PlanetSerializer(planet, many=False, read_only=True)
            return Response({'planets' : serializer.data})
        except ObjectDoesNotExist:
            return Response({'error': 'NotFound'})

    def post(self, request):
        form = PlanetForm(request.POST)
        if form.is_valid():
            # post = form.save()
            return JsonResponse({'msg': 'Планета успешно добавлена'})

        return Response({'error': "not valid"})


class CategoryesView(APIView):
    def get(self, request):
        categoryes = Category.objects.all()
        serializer = CategorySerializer(categoryes, many=True)

        return Response({'categoryes' : serializer.data})
    def post(self, request):
        return Response({'error': None, 'result': 'Категория успешно добавлена'})

class UserView(APIView):
    def get(self, request, user_name):
        try:
            user = User.objects.get(username=user_name)
            return Response({'username' : user.username})
        except ObjectDoesNotExist:
            return Response({'error': 'NotFound'})

    def post(self, request):
        return Response({'error': None, 'result': 'Пользователь успешно добавлен'})


class MyPlanetsView(APIView):
    def get(self, request, user_name):
        try:
            user = User.objects.get(username=user_name)
            planets = Planet.objects.filter(author=user.id)
            serializer = PlanetSerializer(planets, many=True, read_only=True)

            return Response({'username' : serializer.data})
        except ObjectDoesNotExist:
            return Response({'error': 'User not found'})


class NotesView(APIView):
    def get(self, request, user_name):
        try:
            user = User.objects.get(username=user_name)

            serializer = PlanetSerializer(user.notes, many=True, read_only=True)

            return Response({'planets' : serializer.data})
        except ObjectDoesNotExist:
            return Response({'error': 'User not found'})


    # def Post(self, request):
    #     return Response({'error': None, 'result': 'Пользователь успешно добавлен'})


@require_GET
def space_view(request, pk):
    # return HttpResponse(f"<html> <h1> Space #{pk} </h1>  </html>")
    return render(request, 'base.html', {'guest': pk})

# @require_GET
# def user(request, user_name):
#     return JsonResponse({"login": user_name})

# @require_POST
# def create_user(request, user_name):
#     form = UserForm(request.POST)
#     if form.is_valid():
#         post = form.save()
#         return JsonResponse({'msg': 'Пост сохранен','id': post.id})
#     return JsonResponse({'errors': form.errors}, status=400)
#     # return JsonResponse({"login": user_name})


# @require_GET
# def planetsList(request):
#     return JsonResponse({"planet_list": ["Марс", "Земля", "Венера"]})

# @require_GET
# def categoryes(request):
#     return JsonResponse({"categoryes": ["Карлик", "Газовый гигант", "Экзопланета"]})

# @require_GET
# def planetsList(request):
#     return JsonResponse({"planet_list": ["Марс", "Земля", "Венера"]})

# @require_GET
# def planet(request, planet_name):
#     return JsonResponse({"planet_name": planet_name, "author": "user1234"})

# @require_POST
# def create_planet(request):
#     return JsonResponse({"planet_name": 'Сатурн'})


# @require_GET
# def user_planets(request, user_name):
#     return JsonResponse({"planet_list": [{'id': 1}, {'id': 2}]})
# Create your views here.
