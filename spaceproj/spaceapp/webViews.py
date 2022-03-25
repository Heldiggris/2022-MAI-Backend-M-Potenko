from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def space_info(request):
    return HttpResponse("<html> <h1> Space Info </h1>  </html>")
