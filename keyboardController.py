from djitellopy import tello
import keyboardModule as km
from time import sleep

km.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.takeoff()


def get_key_input():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if km.get_key('LEFT'): lr = -speed
    elif km.get_key('RIGHT'): lr = speed

    if km.get_key('UP'): ud = -speed
    elif km.get_key('DOWN'): ud = speed


while True:
    drone.send_rc_control(0, 0, 0, 0)
