from re import T
import cv2
from random import randrange

# load some pre-trained data on face frontals from opencv
haar_cascade_face = cv2.CascadeClassifier(
    "C:\\Users\\kanch\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

# choose an image to detect faces
img = cv2.imread('JIN_Instagram.jpg')
#img = cv2.imread('img for pjct5.webp')
# to capture video from webcam
#webcam = cv2.VideoCapture(0)

# iterate forever over frames
while True:

    # read the current frame
    successful_frame_read, frame = webcam.read()
    # must convert to grayscale
    greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    face_coordinates = haar_cascade_face.detectMultiScale(greyscaled_img)

    # draw rectangles around the faces

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(128, 256),
                                                  randrange(128, 256), randrange(128, 256)), 2)

    cv2.imshow('project4 face detect', frame)
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key == 113:
        break

# release the videocapture object
webcam.release()


'''
# detect faces
face_coordinates = haar_cascade_face.detectMultiScale(greyscaled_img)
# print(face_coordinates)

# draw rectangles around the faces

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 256),
                  randrange(128, 256), randrange(128, 256)), 2)

# display the image with the faces
cv2.imshow('project4 face detect', img)
cv2.waitKey()


print("code complete")

'''
