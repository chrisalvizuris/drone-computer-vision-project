# tested tello controls with this python file

from djitellopy import tello
from time import sleep

# first connect drone object to machine's wifi
# create drone object
# drone = tello.Tello()
# drone.connect()

# get_battery will return the battery percentage in an integer range between 0-100
# print(drone.get_battery())

# takeoff, move forward 50 centimeters in 2 seconds, move right 30 centimeters in 2 seconds, and then land
# drone.takeoff()
# drone.send_rc_control(0, 50, 0, 0)
# sleep(2)
# drone.send_rc_control(30, 0, 0, 0)
# sleep(2)
# drone.send_rc_control(0, 0, 0, 0)
# drone.land()
