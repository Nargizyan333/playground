import os
import cv2
import numpy as np

import detector

class Recognizer:
    def __init__(self):
        self.__detector = detector.Detector()
        self.__recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.__people = []
        if os.path.exists('trained.yml'):
            self.__recognizer.read('trained.yml')
            with open('people.txt', 'r') as f:
                for line in f.readlines():
                    self.__people.append(line.strip())
        else:
            if len(os.listdir("faces")) == 0:
                print("No faces found.")
            else:
                features = []
                labels = []
                for label, folder in enumerate(os.listdir("./faces")):
                    self.__people.append(folder)
                    folder_path = os.path.join("./faces", folder)
                    for filename in os.listdir(folder_path):
                        file_path = os.path.join(folder_path, filename)
                        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                        faces = self.__detector.detect(img)
                        for face in faces:
                            roi = self.__detector.get_roi(img, face)
                            features.append(roi)
                            labels.append(label)
                self.__recognizer.train(features, np.array(labels))
                self.__recognizer.save('trained.yml')
                with open("people.txt", "x") as f:
                    for index, person in enumerate(self.__people):
                        if index != len(self.__people) - 1:
                            f.write(person + "\n")
                        else:
                            f.write(person)

    def recognize(self, img):
        return self.__recognizer.predict(img)

    def get_people(self):
        return self.__people

    def get_name(self, label):
        return self.__people[label]

    def add_person(self, person):
        if person not in self.__people:
            folder_path = os.path.join("./faces", person)
            if os.path.exists(folder_path):
                with open('people.txt', 'a') as f:
                    f.write('\n' + person)
                features = []
                labels = []
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                    faces = self.__detector.detect(img)
                    for face in faces:
                        roi = self.__detector.get_roi(img, face)
                        features.append(roi)
                        labels.append(len(self.__people))
                self.__recognizer.update(features, np.array(labels))
                if os.path.exists('trained.yml'):
                    os.remove("./trained.yml")
                self.__recognizer.write('trained.yml')
                self.__people.append(person)