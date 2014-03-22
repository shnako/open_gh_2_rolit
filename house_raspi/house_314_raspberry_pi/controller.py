__author__ = 'Mircea  Iordache'

from house_raspi.settings import servo, ser
import RPi.GPIO as GPIO
import math

# Uses
bulbs = [-1, 0, 0, 0]
bulbs_ids = [-1, 23, 24, 25]

# Sets the light bulb intensity.
# Should contain:
# INTENSITY - Integer between 0 and 100,
# BULB_ID - Light bulb id.
def set_light_bulb_intensity(intensity, bulb_id):
    # TODO
    bulbs[bulb_id] = intensity

    if (intensity < 1): 
       intensity = 1
    if (intensity == 100):
       intensity = 99
    servo.set_servo(bulbs_ids[bulb_id], intensity*200) 

# Should contain:
# BULB_ID - Light bulb id.
# Will return an integer value containing the intensity.
def get_light_bulb_intensity(bulb_id):
    return bulbs[bulb_id]

# Gets the temperature as a float value.
def get_temperature():
    # TODO
   val = ser.readline()
   new_val = val.split("\n")
   volts = float(new_val[0])
   ohms = (909/volts)- 1000

   lnohm = math.log1p(ohms)

   a = 0.002197222470870
   b = 0.000161097632222
   c = 0.000000125008328

   t1 = (b*lnohm)
   c2 = c*lnohm
   t2 = math.pow(c2,3)
   temp = 1/(a+t1+t2)
   tempc = temp - 273.15 - 4
   
   #print ohms
   return tempc

#Gets the current consumption as a float
def get_current_consumption():
    Va = 12*bulbs[1]/100
    Vb = 12*bulbs[2]/100
    Vc = 12*bulbs[3]/100
    power = 1.6*(Va+Vb+Vc)
    return power
