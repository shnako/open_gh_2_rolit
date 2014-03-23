__author__ = 'VladIulian'
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse
from house_314_project.settings import raspi_address
import urllib2

# Gets the current global consumption from the pi.
@csrf_exempt
def get_current_consumption(request):
    result =  urllib2.urlopen('http://' + raspi_address + '/api/get_current_consumption/')
    if result.getcode() == 200:
        return HttpResponse(result.read(), status=200)
    else:
        return HttpResponse(status=result.getcode())