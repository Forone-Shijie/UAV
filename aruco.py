import numpy as np
import time
import cv2
import cv2.aruco as aruco


cap = cv2.VideoCapture(0)


font = cv2.FONT_HERSHEY_SIMPLEX #font for displaying text (below)

#num = 0
while True:
    ret, frame = cap.read()
    h1, w1 = frame.shape[:2]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
    #dst1 = cv2.undistort(frame, mtx, dist, None, newcameramtx)
    '''
    detectMarkers(...)
        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
        mgPoints]]]]) -> corners, ids, rejectedImgPoints
    '''

    #使用aruco.detectMarkers()函数可以检测到marker，返回ID和标志板的4个角点坐标
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray,aruco_dict,parameters=parameters)

#    如果找不打id
    if ids is not None:

        # flatten the ArUco IDs list
        ids = ids.flatten()
        # loop over the detected ArUCo corners
        for (markerCorner, markerID) in zip(corners, ids):
            # extract the marker corners (which are always returned in
            # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            cv2.rectangle(frame, topLeft, bottomRight, (0,255, 0), 3)

            # marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
            # draw the ArUco marker ID on the image
            cv2.putText(frame, str(markerID),
                        (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
            print("[INFO] ArUco marker ID: {}".format(markerID))


    else:
        ##### DRAW "NO IDS" #####
        cv2.putText(frame, "No Ids", (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)


    # 显示结果框架
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)

    if key == 27:         # 按esc键退出
        print('esc break...')
        cap.release()
        cv2.destroyAllWindows()
        break

    if key == ord(' '):   # 按空格键保存
#        num = num + 1
#        filename = "frames_%s.jpg" % num  # 保存一张图像
        filename = str(time.time())[:10] + ".jpg"
        cv2.imwrite(filename, frame)