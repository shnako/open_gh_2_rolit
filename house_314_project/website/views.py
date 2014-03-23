__author__ = 'VladIulian'
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

@csrf_exempt
def dashboard(request):
    return render_to_response('index.html')

@csrf_exempt
def house(request):
    return render_to_response('house.html')
