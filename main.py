import cv2
import cv2.aruco as aruco
import numpy
import CirclesDetect
import ArUcoDetect

if __name__ == '__main__':
    capture = cv2.VideoCapture('../UAV_video/aaa.avi')
    if capture.isOpened() is True:
        while (True):

            ret, frame = capture.read()
            CirclesDetect.HoughCircles(frame)
            marker_result = ArUcoDetect.marker_detect(frame)

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        capture.release()
        cv2.waitKey(0)  # 无穷大等待时间
        cv2.destroyAllWindows()
    else:
        print("Capture is not opened !")