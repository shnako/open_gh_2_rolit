__author__ = 'Lord Ache'
from django.views.decorators.csrf import csrf_exempt

# Uses
bulbs = [-1, 100, 0, 100]
bulbs_ids = [-1, 23, 24, 25]

# Sets the light bulb intensity.
# Should contain:
# INTENSITY - Integer between 0 and 100,
# BULB_ID - Light bulb id.
def set_light_bulb_intensity(intensity, bulb_id):
    # TODO
    bulbs[bulb_id] = intensity

# Should contain:
# BULB_ID - Light bulb id.
# Will return an integer value containing the intensity.
def get_light_bulb_intensity(bulb_id):
    return bulbs[bulb_id]

# Gets the temperature as a float value.
def get_temperature():
    # TODO
    return -1