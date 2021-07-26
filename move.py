from djitellopy import tello
from time import sleep

# first connect drone object to machine's wifi
# create drone object
drone = tello.Tello()
drone.connect()

print(drone.get_battery())

drone.takeoff()
drone.send_rc_control(0, 50, 0, 0)
sleep(2)
drone.send_rc_control(0, 0, 0, 0)
drone.land()
