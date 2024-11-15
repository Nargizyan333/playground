import cv2 as cv
import numpy as np

img = cv.imread("./img/blob.png", cv.IMREAD_GRAYSCALE)

params = cv.SimpleBlobDetector_Params()

# Setting threshold
params.minThreshold = 10
params.maxThreshold = 200

# Filter by area
params.filterByArea = True
params.minArea = 1500

# Filter by circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by convexity
params.filterByConvexity = True
params.minConvexity = 0.87

# Filter by inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Creating a detector with the parameters
ver = cv.__version__.split('.')
if int(ver[0]) < 3:
    detector = cv.SimpleBlobDetector(params)
else:
    detector = cv.SimpleBlobDetector_create(params)

key_points = detector.detect(img)
img_with_key_points = cv.drawKeypoints(
    img, key_points, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Display the image with keypoints
cv.imshow("Blob Detection", img_with_key_points)

cv.waitKey(0)
cv.destroyAllWindows()