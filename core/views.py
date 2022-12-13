from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.

def hello(request):
    return JsonResponse({'Yoga': 'Yoga Class APP', 'name': "Mayank Saini"})