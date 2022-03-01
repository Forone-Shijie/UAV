import cv2

capture = cv2.VideoCapture(0)

if capture.isOpened() is True:
    while (True):
        ret, frame = capture.read()

        cv2.imshow("frame", frame)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    capture.release()
    cv2.waitKey(0)  # 无穷大等待时间
    cv2.destroyAllWindows()

else:
    print("Camera is not opened !")