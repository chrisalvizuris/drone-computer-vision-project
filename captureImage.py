from djitellopy import tello
import cv2

# create drone object
drone = tello.Tello()
drone.connect()

# get_battery will return the battery percentage in an integer range between 0-100
print(drone.get_battery())

# stream will give us all the frames 1 by 1 and we can process them
drone.streamon()

# There are a continuous number of frames, so we'll use a while loop
while True:
    image = drone.get_frame_read().frame  # give us individual frame from drone
    image = cv2.resize(image, (360, 240))  # resize the size of the frame to be smaller so that it is faster
    cv2.imshow('Image', image)  # create a window called 'Image' so that we can display our image result
    cv2.waitKey(1)  # give the result a delay so that it doesn't crash

