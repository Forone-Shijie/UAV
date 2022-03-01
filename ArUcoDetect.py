import cv2
import numpy as np
import cv2.aruco as aruco

import csv


# marker位置
def marker_detect(frame):

    #图片简单处理
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 灰度化
    gray = cv2.medianBlur(gray, 3)  # 中值模糊
    # th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
    # cv2.imshow("th3", th3)
    # kernel = np.ones((5, 5), np.uint8)  # 创建全一矩阵，数值类型设置为uint8
    # erosion = cv2.erode(th3, kernel, iterations=1)  # 腐蚀处理 采用高斯的方式
    # cv2.imshow("erosion", erosion)
    # dilation = cv2.dilate(erosion, kernel, iterations=1)  # 膨胀处理
    # cv2.imshow("dilation", dilation)
    gray = cv2.equalizeHist(gray)  #提升对比度

    markers_result = dict()
    dictionary = aruco.Dictionary_create(20, 5) #这里采用的是20，5生成的aruco图形
    parameters = aruco.DetectorParameters_create()

    # parameters.adaptiveThreshWinSizeMin = 10
    # parameters.adaptiveThreshWinSizeMax = 30
    # parameters.adaptiveThreshWinSizeStep = 2
    # parameters.polygonalApproxAccuracyRate = 0.1

    (corners, ids, rejectedImgPoints) = aruco.detectMarkers(gray, dictionary, parameters=parameters)
    if ids is not None:

        aruco.drawDetectedMarkers(gray, corners, ids)
        # cv2.imshow("out", gray)

        ids = ids.flatten()
        #print(corners)
        print(ids)
        for (markerCorner, markerID) in zip (corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            topLeft = (int(topLeft[0]), int(topLeft[1]))
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))

            # draw the bounding box of the ArUCo detection
            cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

            cX = int ((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int ((topLeft[1] + bottomRight[1]) / 2.0)

            cv2.circle(frame, (cX, cY), 4, (0,0,255), -1)
            cv2.putText(frame, str(markerID), (topLeft[0], topLeft[1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, ('cX: '+ str(cX) + ' cY: ' +str(cY)), (topLeft[0], topLeft[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            #cv2.imshow("frame", frame)

            markers_result.update({str(id): (cX, cY)})
    else:
        markers_result = None
    return markers_result


if __name__ == '__main__':
    # capture = cv2.VideoCapture('../100GOPRO/GH010572.MP4')
    # capture = cv2.VideoCapture(0)
    capture = cv2.VideoCapture('/data/sjzhang/UAV/dataset/UAV_video/zzy.avi')
    num = 0
    if capture.isOpened() is True:
        while (True):

            ret, frame = capture.read()

            marker_result = marker_detect(frame)
            cv2.imwrite('/data/sjzhang/UAV/dataset/UAV_video/zzy/im' + str(num + 1000) + '.png', frame)
            num += 1
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        capture.release()
        cv2.waitKey(0)  # 无穷大等待时间
        cv2.destroyAllWindows()
    else:
        print("Capture is not opened !")






