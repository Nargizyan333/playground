import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./img/sunflowers.png")
height, width = img.shape[:2]
aspect_ratio = width/height
print(f"height: {height}, width: {width}")
print(f"aspect_ratio: {aspect_ratio}")

down_points = (1000, 800)
resized_down = cv.resize(img, down_points, interpolation=cv.INTER_LINEAR)
# plt.imshow(resized_down[:,:,::-1])

up_points = (3000, 2400)
resized_up = cv.resize(img, up_points, interpolation=cv.INTER_LINEAR)
# plt.imshow(resized_up[:,:,::-1])

scale_up_x = 1.2
scale_up_y = 1.2
scaled_up = cv.resize(img, None, fx=scale_up_x, fy=scale_up_y, interpolation=cv.INTER_LINEAR)
new_height, new_width = scaled_up.shape[:2]
print(f"new_height: {new_height}, new_width: {new_width}")
# plt.imshow(scaled_up[:,:,::-1])

down_factor = 0.6
ret_inter_lin = cv.resize(img, None, fx=down_factor, fy=down_factor, interpolation=cv.INTER_LINEAR)
ret_inter_area = cv.resize(img, None, fx=down_factor, fy=down_factor, interpolation=cv.INTER_AREA)
ret_inter_near = cv.resize(img, None, fx=down_factor, fy=down_factor, interpolation=cv.INTER_LINEAR)
# cv.imshow("Linear :: Area :: Near", np.concatenate([ret_inter_lin, ret_inter_area, ret_inter_near], axis=1))
# cv.waitKey(0)
# cv.destroyAllWindows()