import cv2 as cv
import numpy as np

# LAB
# The respective values of Green, Orange and Red ( which are the extremes of the A Component ) has not changed in the B Component
# The respective values of Blue and Yellow ( which are the extremes of the B Component ) has not changed in the A component.

indoor_img = cv.imread("./img/indoor.png")
indoor_img_lab = cv.cvtColor(indoor_img, cv.COLOR_BGR2LAB)
a_indoor = indoor_img_lab[:,:,1]
b_indoor = indoor_img_lab[:,:,2]
outdoor_img = cv.imread("./img/outdoor.png")
outdoor_img_lab = cv.cvtColor(outdoor_img, cv.COLOR_BGR2LAB)
a_outdoor = outdoor_img_lab[:,:,1]
b_outdoor = outdoor_img_lab[:,:,2]

indoor = np.concatenate((a_indoor, b_indoor), axis=1)
outdoor = np.concatenate((a_outdoor, b_outdoor), axis=1)

cv.imshow("indoor", indoor)
cv.imshow("outdoor", outdoor)

cv.waitKey(0)
cv.destroyAllWindows()

# YCrCb

indoor_img_yCrCb = cv.cvtColor(indoor_img, cv.COLOR_BGR2YCrCb)
outdoor_img_yCrCb = cv.cvtColor(outdoor_img, cv.COLOR_BGR2YCrCb)

y_indoor = indoor_img_yCrCb[:,:,0]
Cr_indoor = indoor_img_yCrCb[:,:,1]
Cb_indoor = indoor_img_yCrCb[:,:,2]

y_outdoor = outdoor_img_yCrCb[:,:,0]
Cr_outdoor = outdoor_img_yCrCb[:,:,1]
Cb_outdoor = outdoor_img_yCrCb[:,:,2]

indoor = np.concatenate((y_indoor, Cr_indoor, Cb_indoor), axis=1)
outdoor = np.concatenate((y_outdoor, Cr_outdoor, Cb_outdoor), axis=1)

cv.imshow("Indoor", indoor)
cv.imshow("Outdoor", outdoor)

cv.waitKey(0)
cv.destroyAllWindows()

# HSV

indoor_img_hsv = cv.cvtColor(indoor_img, cv.COLOR_BGR2HSV)
outdoor_img_hsv = cv.cvtColor(outdoor_img, cv.COLOR_BGR2HSV)

h_indoor = indoor_img_hsv[:,:,0]
s_indoor = indoor_img_hsv[:,:,1]
v_indoor = indoor_img_hsv[:,:,2]

h_outdoor = outdoor_img_hsv[:,:,0]
s_outdoor = outdoor_img_hsv[:,:,1]
v_outdoor = outdoor_img_hsv[:,:,2]

indoor = np.concatenate((h_indoor, s_indoor, v_indoor), axis=1)
outdoor = np.concatenate((h_outdoor, s_outdoor, v_outdoor), axis=1)

cv.imshow("Indoor", indoor)
cv.imshow("Outdoor", outdoor)

cv.waitKey(0)
cv.destroyAllWindows()