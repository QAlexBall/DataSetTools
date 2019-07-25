import cv2
import time
import argparse

parser = argparse.ArgumentParser(description="test for video")
parser.add_argument('-p', '--video_path', required=True)
args = parser.parse_args()
video_path = args.video_path

cap = cv2.VideoCapture(video_path)
time.sleep(2)

count = 0
while True:
    count += 1
    ret, frame = cap.read()
    print(ret, count)
    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
