import cv2

class Detector:
    def __init__(self):
        self.__XML_FILE_PATH = "./haarcascade_frontalface_alt2.xml"
        self.__detector = cv2.CascadeClassifier(self.__XML_FILE_PATH)
        self.__minSize = (150, 150)

    def detect(self, img):
        return self.__detector.detectMultiScale(img, minSize=self.__minSize)

    def get_roi(self, img, region):
        x, y, w, h = region
        return img[y:y+h, x:x+w]
