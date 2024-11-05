import cv2 as cv

img = cv.imread("./img/sunflowers.png", cv.IMREAD_COLOR)
img_grayscale = cv.imread("./img/sunflowers.png", cv.IMREAD_GRAYSCALE)

if cv.imwrite("./img/sunflowers_grayscale.png", img_grayscale):
    print("Success")
else:
    print("Failure")

cv.imshow("Sunflowers", img)
cv.waitKey(0)
cv.destroyAllWindows()