from djitellopy import tello
import keyboardModule as km
from time import sleep

km.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())


def get_key_input():
    """
    Function to read in a specific key from a keyboard and control the drone via the pressed key.
    Example - pressing the right arrow button on keyboard moves drone to the right

    :return: Returns the values used in send_rc_controls() individually.
    """

    left_right, forward_backward, up_down, yaw_velocity = 0, 0, 0, 0
    speed = 50

    if km.get_key('LEFT'):
        left_right = -speed
    elif km.get_key('RIGHT'):
        left_right = speed

    if km.get_key('UP'):
        forward_backward = speed
    elif km.get_key('DOWN'):
        forward_backward = -speed

    if km.get_key('w'):
        up_down = speed
    elif km.get_key('s'):
        up_down = -speed

    if km.get_key('a'):
        yaw_velocity = speed
    elif km.get_key('d'):
        yaw_velocity = -speed

    if km.get_key('q'):
        drone.land()

    if km.get_key('t'):
        drone.takeoff()

    return [left_right, forward_backward, up_down, yaw_velocity]


while True:
    vals = get_key_input()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.5)
