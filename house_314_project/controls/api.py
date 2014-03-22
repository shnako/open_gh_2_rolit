__author__ = 'VladIulian'
from django.views.decorators.csrf import csrf_exempt
import urllib2, urllib
from django.http import HttpResponse
from house_314_project.settings import raspi_address


# Sets the light bulb intensity.
# Should contain:
# INTENSITY - Integer between 0 and 100,
# BULB_ID - Light bulb id.
@csrf_exempt
def set_light_bulb_intensity(request):
    post_data = [('HTTP_INTENSITY', request.POST['HTTP_INTENSITY']),('HTTP_BULB_ID', request.POST['HTTP_BULB_ID']),]
    result = urllib2.urlopen('http://' + raspi_address + '/api/set_light_bulb_intensity/', urllib.urlencode(post_data))
    return HttpResponse(status=result.getcode())

# Should contain:
# BULB_ID - Light bulb id.
# Will return an integer value containing the intensity.
@csrf_exempt
def get_light_bulb_intensity(request):
    post_data = [('HTTP_BULB_ID', request.POST['HTTP_BULB_ID']),]
    result = urllib2.urlopen('http://' + raspi_address + '/api/get_light_bulb_intensity/', urllib.urlencode(post_data))
    return HttpResponse(result.read(), status=result.getcode())

# Gets the temperature as a float value.
@csrf_exempt
def get_temperature(request):
    result = urllib2.urlopen('http://' + raspi_address + '/api/get_temperature/')
    if result.getcode() == 200:
        return HttpResponse(result.read(), status=200)
    else:
        return HttpResponse(status=result.getcode())
