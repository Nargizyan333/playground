import os
import cv2

import detector
import frame_processing

frame_processor = frame_processing.FrameProcessing()
detector = detector.Detector()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
else:
    while True:
        ret, frame = cap.read()
        to_show = frame_processor.process_frame(frame)
        cv2.imshow('frame', to_show)
        if cv2.waitKey(3) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(3) & 0xFF == ord('g'):
            frame_processor.grayscale()
        elif cv2.waitKey(3) & 0xFF == ord('s'):
            frame_processor.hsv()
        elif cv2.waitKey(3) & 0xFF == ord('l'):
            frame_processor.lab()
        elif cv2.waitKey(3) & 0xFF == ord('b'):
            frame_processor.blur()
        elif cv2.waitKey(3) & 0xFF == ord('n'):
            frame_processor.median_filtering()
    cap.release()
    cv2.destroyAllWindows()