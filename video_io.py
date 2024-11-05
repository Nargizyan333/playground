import cv2 as cv

"""
vid = cv.VideoCapture("./vid/test.mp4")

if vid.isOpened() is False:
    print("Error opening video stream or file")
else:
    fps = vid.get(cv.CAP_PROP_FPS)
    print(f"Current FPS: {fps}")

    frame_count = vid.get(cv.CAP_PROP_FRAME_COUNT)
    print(f"Frame count: {frame_count}")

    while vid.isOpened():
        ret, frame = vid.read()
        if ret:
            cv.imshow("Video", frame)
            key = cv.waitKey(20)
            if key == ord('q'):
                break
        else:
            break

vid.release()
cv.destroyAllWindows()
"""

# Real-time

vid = cv.VideoCapture(0)

if vid.isOpened() is False:
    print("Error opening video stream or file")
else:
    frame_width = int(vid.get(3))
    frame_height = int(vid.get(4))
    frame_size = (frame_width, frame_height)
    fps = 20
    output = cv.VideoWriter('./vid/output.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, frame_size)
    while vid.isOpened():
        ret, frame = vid.read()
        if ret:
            output.write(frame)
        else:
            break
    output.release()

vid.release()
cv.destroyAllWindows()