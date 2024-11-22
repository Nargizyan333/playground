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
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('g'):
            frame_processor.grayscale()
        elif key == ord('s'):
            frame_processor.hsv()
        elif key == ord('l'):
            frame_processor.lab()
        elif key == ord('b'):
            frame_processor.blur()
        elif key == ord('n'):
            frame_processor.median_filtering()
        elif key == ord('v'):
            frame_processor.vertical_flip()
        elif key == ord('h'):
            frame_processor.horizontal_flip()

    cap.release()
    cv2.destroyAllWindows()