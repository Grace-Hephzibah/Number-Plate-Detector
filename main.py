import cv2

nPlateCascade = cv2.CascadeClassifier("resources/haarcascade_russian_plate_number.xml")
minArea = 500
color1 = (255, 0, 255)
color2 = (0, 255, 0)

name = "test1"

img = cv2.imread("resources/" + name + ".jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
numberPlate = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in numberPlate:
    area = w*h
    if area > minArea:
        cv2.rectangle(img, (x,y), (x+w, y+h), color1, 2)
        cv2.putText(img, "Number Plate", (x,y-5),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color1, 2)
        imgNumberPlate= img[y:y+h, x:x+w]
        cv2.imshow("Number Plate", imgNumberPlate)

cv2.imshow("Test Screen", img)

cv2.waitKey(0)