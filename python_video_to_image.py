import cv2
import os
# import threading

vidcap = cv2.VideoCapture('./video_data/vehicles.mp4')

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        directory = "generated_data"
        if not os.path.exists(directory):
            os.makedirs(directory)
        cv2.imwrite(f"{directory}/image{str(count)}.jpg", image)
        cv2.imshow("Frame", image)
    return hasFrames

sec = 0
frameRate = 0.5
count = 1

while success := getFrame(sec):
    count = count + 1
    sec += frameRate
    sec = round(sec, 2)

    if cv2.waitKey(1) == ord('q'):
        break


vidcap.release()
cv2.destroyAllWindows()
