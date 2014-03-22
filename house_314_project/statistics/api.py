__author__ = 'VladIulian'
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse
from house_314_project.settings import raspi_address


# Gets the current global consumption from the pi.
@csrf_exempt
def get_current_consumption(request):
    result = requests.get('http://' + raspi_address + '/api/get_curret_consumption/')
    if result.status_code == 200:
        return HttpResponse(result.text, status=200)
    else:
        return HttpResponse(status=result.status_code)

# Gets the average consumption for the specified.
# Have START_DATE and END_DATE in the request.
@csrf_exempt
def get_average_consumption(request):
    start_date = request.META['HTTP_START_DATE']
    end_date = request.META['HTTP_END_DATE']
    return None

# Gets the average consumption for the specified area. HARD CODE for demo.
# Have START_DATE and END_DATE in the request.
@csrf_exempt
def get_area_average_consumption(request):
    start_date = request.META['HTTP_START_DATE']
    end_date = request.META['HTTP_END_DATE']
    return None

# Gets the average consumption for the specified.
# Have START_DATE and END_DATE in the request.
@csrf_exempt
def get_city_average_consumption(request):
    start_date = request.META['HTTP_START_DATE']
    end_date = request.META['HTTP_END_DATE']
    return None
