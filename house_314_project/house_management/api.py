__author__ = 'VladIulian'
from django.views.decorators.csrf import csrf_exempt

# Sets the light bulb intensity.
# Should contain:
# INTENSITY - Integer between 0 and 100,
# BULB_ID - Light bulb id.
@csrf_exempt
def set_light_bulb_intensity(request):
    intensity = request.META['HTTP_INTENSITY']
    bulb_id = request.META['HTTP_BULB_ID']
    # TODO
    return None

# Should contain:
# BULB_ID - Light bulb id.
# Will return an integer value containing the intensity.
def get_light_bulb_intensity(request):
    bulb_id = request.META['HTTP_BULB_ID']
    # TODO
    return None

# Gets the temperature as a float value.
def get_temperature(request):
    # TODO
    return None