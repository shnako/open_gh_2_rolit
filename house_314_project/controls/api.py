__author__ = 'VladIulian'
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse
from house_314_project.settings import raspi_address


# Sets the light bulb intensity.
# Should contain:
# INTENSITY - Integer between 0 and 100,
# BULB_ID - Light bulb id.
@csrf_exempt
def set_light_bulb_intensity(request):
    intensity = request.META['HTTP_INTENSITY']
    bulb_id = request.META['HTTP_BULB_ID']
    result = requests.get('http://' + raspi_address + '/api/set_light_bulb_intensity/', intensity=intensity, bulb_id=bulb_id)
    return HttpResponse(status=result.status_code)

# Should contain:
# BULB_ID - Light bulb id.
# Will return an integer value containing the intensity.
@csrf_exempt
def get_light_bulb_intensity(request):
    bulb_id = request.META['HTTP_BULB_ID']
    result = requests.get('http://' + raspi_address + '/api/get_light_bulb_intensity/', bulb_id=bulb_id)
    if result.status_code == 200:
        return HttpResponse(result.text, status=200)
    else:
        return HttpResponse(status=result.status_code)

# Gets the temperature as a float value.
@csrf_exempt
def get_temperature(request):
    result = requests.get('http://' + raspi_address + '/api/get_temperature/')
    if result.status_code == 200:
        return HttpResponse(result.text, status=200)
    else:
        return HttpResponse(status=result.status_code)
