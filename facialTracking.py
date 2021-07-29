from djitellopy import tello
import time
import cv2
import numpy as np

# create drone object
drone = tello.Tello()
drone.connect()

# stream will give us all the frames 1 by 1 and we can process them
drone.streamon()
drone.takeoff()

# instruct the drone to fly up so that it can be within a frame that is as tall as me
drone.send_rc_control(0, 0, 20, 0)
time.sleep(2)

forward_backward_range = [6200, 6800]
width, height = 360, 240

# pid controller, values as [proportional, integral, derivative]
pid = [0.4, 0.4, 0]
previous_error = 0


def detect_face(image):
    """
    Function to implement Haar Cascade model for facial detection

    :param image: Takes in drone's camera
    :return: Image's center and area values as 2 element list
    """
    face_cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    # convert to gray scale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.2, 8)

    # create a list of all of the faces, then...
    # create a list of all of the areas of the faces
    my_face_list_centered = []
    my_face_list_area = []

    for (x, y, width, height) in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 0, 255), 2)

        # centers are used to determine when the camera is rotated
        center_x = x + y // 2
        center_y = y + height // 2

        # area is used to determine when the camera moves forward and backwords
        area = width * height
        cv2.circle(image, (center_x, center_y), 5, (0, 255, 0), cv2.FILLED)
        my_face_list_centered.append([center_x, center_y])
        my_face_list_area.append(area)

    # once we get the index of the max value we can use that to get the center_x and center_y values of
    # the corresponding face
    if len(my_face_list_area) != 0:
        i = my_face_list_area.index(max(my_face_list_area))
        return image, [my_face_list_centered[i], my_face_list_area[i]]
    else:
        return image, [[0, 0], 0]


def track_face(drone, info, width, pid, previous_error):
    """
    This function takes in the drone and then continually tracks the face's location and readjusts
    drone's position accordingly.

    :param drone: Drone that is being called.
    :param info: Two-element list of image's center and area values, which are returned from detect_face()
    :param width: Width of the image
    :param pid: Pid controller. Only use proportional and integral values.
    :param Previous_error: error that was returned from track_face(). Deviation from center.
    :return: Error, which is the deviation from center. Will be used as previous_error in future use.
    """

    area = info[1]
    x, y = info[0]

    # find the deviation from the center
    error = x - width // 2

    # speed will be the drone's yaw velocity
    speed = pid[0] * error + pid[1] * (error - previous_error)
    # we need to keep the speed between -100 and 100 with np.clip()
    speed = int(np.clip(speed, -100, 100))

    # keep the drone stationary if nothing is going on
    if forward_backward_range[0] < area < forward_backward_range[1]:
        forward_backward = 0

    # if the drone gets too close, move backwards 20 centimeters
    elif area > forward_backward_range[1]:
        forward_backward = -20

    # if the drone is too far, move forward 20 centimeters
    elif area < forward_backward_range[0] and area != 0:
        forward_backward = 20

    if x == 0:
        speed = 0
        error = 0

    drone.send_rc_control(0, forward_backward, 0, speed)

    # we return the error because it will be used as previous_error when called again
    return error

# created a capture variable to test on external webcam
# capture = cv2.VideoCapture(1)


while True:
    # _, img = capture.read()
    image = drone.get_frame_read().frame
    img = cv2.resize(img, (width, height))
    img, info = detect_face(img)
    previous_error = track_face(drone, info, width, pid, previous_error)
    print("Area", info[1], "Center", info[0])
    cv2.imshow("Output", img)

    # apply the mask of 0xff and then return the unicode point of 'q'
    # this lets me terminate the drone with the keyboard
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break
