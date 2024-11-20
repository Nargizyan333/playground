import cv2

import detector
import recognizer

class FrameProcessing:
    def __init__(self):
        self.recognizer = recognizer.Recognizer()
        self.__detector = detector.Detector()
        self.__confidence_threshold = 30
        self.__is_grayscale_on = False
        self.__is_blurred = False
        self.__is_HSV_on = False
        self.__is_Lab_on = False
        self.__is_median_filtering_on = False
        self.__MAX_CONFIDENCE = 255

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.__detector.detect(gray)
        for face in faces:
            roi = self.__detector.get_roi(gray, face)
            roi = cv2.resize(roi, (200, 200))
            label, confidence = self.recognizer.recognize(roi)
            print(label, confidence)
            if confidence < self.__confidence_threshold:
                name = "Unknown"
            else:
                name = self.recognizer.get_name(label)
            conf = 100 - (confidence / self.__MAX_CONFIDENCE) * 100
            self.annotate_frame(frame, face, name, conf)
        if self.__is_grayscale_on:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self.__is_blurred:
            frame = cv2.GaussianBlur(frame, (7, 7), 0)
        if self.__is_HSV_on:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        if self.__is_Lab_on:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        if self.__is_median_filtering_on:
            frame = cv2.medianBlur(frame, 9)
        return frame

    def add_person(self, name):
        self.recognizer.add_person(name)

    def annotate_frame(self, frame, face, name, confidence):
        x, y, w, h = face

        color = (0, 255, 0)
        thickness = 2
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)

        label = f"{name} ({confidence:.2f})"

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        font_thickness = 1
        text_size, _ = cv2.getTextSize(label, font, font_scale, font_thickness)
        text_w, text_h = text_size

        cv2.rectangle(frame, (x, y - text_h - 10), (x + text_w, y), (0, 255, 0), cv2.FILLED)

        text_color = (0, 0, 0)
        cv2.putText(frame, label, (x, y - 5), font, font_scale, text_color, font_thickness)

    def grayscale(self):
        if self.__is_grayscale_on:
            self.__is_grayscale_on = False
        else:
            self.__is_grayscale_on = True
            self.__is_HSV_on = False
            self.__is_Lab_on = False

    def blur(self):
        if self.__is_blurred:
            self.__is_blurred = False
        else:
            self.__is_blurred = True
            self.__is_median_filtering_on = False

    def hsv(self):
        if self.__is_HSV_on:
            self.__is_HSV_on = False
        else:
            self.__is_HSV_on = True
            self.__is_Lab_on = False
            self.__is_grayscale_on = False

    def lab(self):
        if self.__is_Lab_on:
            self.__is_Lab_on = False
        else:
            self.__is_Lab_on = True
            self.__is_HSV_on = False
            self.__is_grayscale_on = False

    def median_filtering(self):
        if self.__is_median_filtering_on:
            self.__is_median_filtering_on = False
        else:
            self.__is_median_filtering_on = True
            self.__is_blurred = False