import cv2
import numpy as np

def show_detection(image, faces):
    """Draws a rectangle over each detected face"""
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)
    return image

img = cv2.imread("./img/musk.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cas_alt2 = cv2.CascadeClassifier("./xml/haarcascade_frontalface_alt2.xml")
cas_default = cv2.CascadeClassifier("./xml/haarcascade_frontalface_default.xml")

faces_alt2 = cas_alt2.detectMultiScale(gray)
faces_default = cas_default.detectMultiScale(gray)

img_faces_default = show_detection(img.copy(), faces_default)
img_faces_alt2 = show_detection(img.copy(), faces_alt2)

cv2.imshow("Face Detection", img_faces_alt2)
cv2.waitKey(0)

cv2.imshow("Face Detection", img_faces_default)
cv2.waitKey(0)

cv2.destroyAllWindows()

retval, faces_haar_alt2 = cv2.face.getFacesHAAR(img, "./xml/haarcascade_frontalface_alt2.xml")
retval, faces_haar_default = cv2.face.getFacesHAAR(img, "./xml/haarcascade_frontalface_default.xml")

faces_haar_alt2 = np.squeeze(faces_haar_alt2)
faces_haar_default = np.squeeze(faces_haar_default)


img_faces_alt2 = show_detection(img.copy(), [faces_haar_alt2])
img_faces_default = show_detection(img.copy(), [faces_haar_default])

cv2.imshow("Face Detection", img_faces_alt2)
cv2.waitKey(0)

cv2.imshow("Face Detection", img_faces_default)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Pre-trained

net1 = cv2.dnn.readNetFromCaffe("deploy.prototxt",
                                "res10_300x300_ssd_iter_140000_fp16.caffemodel")

blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), [104., 117., 123.],
                     False, False)

net1.setInput(blob)
detections = net1.forward()

h, w = img.shape[:2]

detected_faces = 0
for i in range(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.7:
        detected_faces += 1
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        text = "{:.3f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(img, (startX, startY), (endX, endY), (255, 0, 0), 3)
        cv2.putText(img, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX,
           0.9, (0, 0, 255), 2)

cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()