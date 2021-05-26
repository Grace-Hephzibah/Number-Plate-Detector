'''
if 0xFF == ord('s'):
    cv2.imwrite("resources/Scanned Documents/NoPlate_of_"+ name + ".jpg", imgNumberPlate)
    cv2.rectangle(img, (0,200), (640, 300), color2, cv2.FILLED)
    cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_PLAIN, 2, color2, 2)

    cv2.imshow("Saved Document", img)
    cv2.waitKey(0)
'''