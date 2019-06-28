#!usr/bin/python
# -*- coding: utf-8 -*-

#import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
 
def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    gray = cv2.GaussianBlur(gray, (5, 5), 0)        
    edged = cv2.Canny(gray, 35, 125)               
 
    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # 求最大面积 
    c = max(cnts, key = cv2.contourArea)
 
    # compute the bounding box of the of the paper region and return it
    # cv2.minAreaRect() c代表点集，返回rect[0]是最小外接矩形中心点坐标，
    # rect[1][0]是width，rect[1][1]是height，rect[2]是角度
    return cv2.minAreaRect(c)

def find_person(image):

    frame = imutils.resize(image, width=min(400, image.shape[1]))
    # detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
         padding=(8, 8), scale=1.05)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    #非极大抑制 消除多余的框 找到最佳人体位置
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    
    return pick
 
def distance_to_camera(knownWidth, focalLength, perWidth):  
    # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth            



# initialize the known distance from the camera to the object, which
# in this case is 24 inches
KNOWN_DISTANCE = 24.0
#KNOWN_DISTANCE = 610
# initialize the known object width, which in this case, the piece of
# paper is 11 inches wide
KNOWN_WIDTH = 11.69
KNOWN_HEIGHT = 8.27
KNOW_PERSON_HEIGHT = 70.87
#KNOWN_WIDTH = 297
#KNOWN_HEIGHT = 210

# initialize the list of images that we'll be using
IMAGE_PATHS = ["Picture1.jpg", "Picture2.jpg", "Picture3.jpg","Picture4.jpg","Picture5.jpg","Picture6.jpg","Picture7.jpg"]
 
# load the furst image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
image = cv2.imread(IMAGE_PATHS[0]) 
marker = find_marker(image)           
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH  
#focalLength = 811.82
print('focalLength = ',focalLength)

camera = cv2.VideoCapture(0)
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

ya_max = 0
yb_max = 0

while camera.isOpened():
    # get a frame
    (grabbed, frame) = camera.read()

    # 如果不能抓取到一帧，说明我们到了视频的结尾
    if not grabbed:
        break
    
    frame = imutils.resize(frame, width=min(400, frame.shape[1]))

    #marker = find_marker(frame)
    marker = find_person(frame)
    
    #inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
    for (xA, yA, xB, yB) in marker:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        ya_max = yA
        yb_max = yB

    pix_person_height = yb_max - ya_max
    if pix_person_height == 0:
        #pix_person_height = 1
	    continue
    print (pix_person_height)
    #print (pix_person_height)
    inches = distance_to_camera(KNOW_PERSON_HEIGHT, focalLength, pix_person_height)
    print("%.2fcm" % (inches *30.48/ 12))
    # draw a bounding box around the image and display it
    #box = np.int0(cv2.cv.BoxPoints(marker))
    #cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
    cv2.putText(frame, "%.2fcm" % (inches *30.48/ 12),
             (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
	     2.0, (0, 255, 0), 3)

    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows() 

