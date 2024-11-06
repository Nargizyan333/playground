import cv2 as cv
import numpy as np

img = cv.imread("./img/sunflowers.png")
cv.imshow("Original", img)

cropped = img[:100, :100]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
cv.destroyAllWindows()

# Patches

height, width = img.shape[:2]
M = height // 5
N = width // 5
x1 = 0
y1 = 0

for y in range(0, height, M):
    for x in range(0, width, N):
        if (height - y) < M or (width - x) < N:
            break
        x1 += N
        y1 += M
        if x1 >= width:
            x1 = width - 1
        if y1 >= height:
            y1 = height - 1
        tile = img[y:y + M, x:x + N]
        cv.imwrite('./saved_patches/' + 'tile' + str(x) + '_' + str(y) + '.jpg', tile)
        cv.rectangle(img, (x, y), (x + N, y + M), (0, 0, 255), 1)

cv.imshow("Sunflowers", img)
cv.waitKey(0)
cv.destroyAllWindows()