import cv2
import pickle
from util import process_image
import cvzone

cap = cv2.VideoCapture('parking_video.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)
width, height = 70, 30


def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        

        if process_image(imgCrop) ==0:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 5

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, f'Free Spots: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0,200,0))

                       
while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    checkParkingSpace(img)

  
    cv2.imshow("Image", img)
   
    cv2.waitKey(10)