__author__ = 'VladIulian'
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Sets the light bulb intensity.
# Should contain:
# INTENSITY - Integer between 0 and 100,
# BULB_ID - Light bulb id.
@csrf_exempt
def set_light_bulb_intensity(request):
    intensity = request.META['HTTP_INTENSITY']
    bulb_id = request.META['HTTP_BULB_ID']
    try:
        set_light_bulb_intensity(intensity=intensity, bulb_id=bulb_id)
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=418)

# Should contain:
# BULB_ID - Light bulb id.
# Will return an integer value containing the intensity.
@csrf_exempt
def get_light_bulb_intensity(request):
    bulb_id = request.META['HTTP_BULB_ID']
    try:
        intensity = get_light_bulb_intensity(bulb_id)
        return HttpResponse(intensity, status=200)
    except:
        return HttpResponse(status=418)

# Gets the temperature as a float value.
@csrf_exempt
def get_temperature(request):
    try:
        temperature = get_temperature()
        return HttpResponse(temperature, status=200)
    except:
        return HttpResponse(status=418)