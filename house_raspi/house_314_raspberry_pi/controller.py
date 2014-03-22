__author__ = 'Mircea  Iordache'

from house_raspi.settings import servo
import RPi.GPIO as GPIO

# Uses
bulbs = [-1, 100, 0, 100]
bulbs_ids = [-1, 23, 24, 25]

# Sets the light bulb intensity.
# Should contain:
# INTENSITY - Integer between 0 and 100,
# BULB_ID - Light bulb id.
def set_light_bulb_intensity(intensity, bulb_id):
    # TODO
    if (intensity < 1): 
       intensity = 1
    if (intensity == 100):
       intensity = 99
    bulbs[bulb_id] = intensity
    servo.set_servo(bulbs_ids[bulb_id], intensity*200) 

# Should contain:
# BULB_ID - Light bulb id.
# Will return an integer value containing the intensity.
def get_light_bulb_intensity(bulb_id):
    return bulbs[bulb_id]

# Gets the temperature as a float value.
def get_temperature():
    # TODO
    return GPIO.input(12)
