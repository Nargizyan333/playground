import os
import sys
import cv2

from frame_processing import FrameProcessing

frame_processor = FrameProcessing()

cap = cv2.VideoCapture(0)
frame_count = 1
img_count = 1

if not cap.isOpened():
    print("Cannot open camera")
else:
    dir_path = os.path.join("./faces", sys.argv[1])
    os.mkdir(dir_path)
    while True:
        frame_count += 1
        ret, frame = cap.read()
        if not ret:
            print("Cannot read camera")
            break
        cv2.imshow("frame", frame)
        if frame_count == 10:
            img_name = os.path.join(dir_path, sys.argv[1]) + str(img_count) + ".jpg"
            cv2.imwrite(img_name, frame)
            img_count += 1
            frame_count = 0
        if img_count == 9:
            break

cap.release()
cv2.destroyAllWindows()

frame_processor.recognizer.add_person(sys.argv[1])