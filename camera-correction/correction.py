import cv2
import pickle
import numpy as np

if __name__ == '__main__':
    # 获取矫正参数

    mtx=np.array([[671.645539,0.000000,654.483761],[0.000000,676.466858,397.811229],[0.000000,0.000000,1.000000]])
    dist=np.array([-0.005329,-0.006301,0.015264,0.000201,0.000000])

    #capture = cv2.VideoCapture(0)

    # 获取图像尺寸
    #img = capture.read()
    h, w = 720, 1280
    new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    x, y, w, h = roi      # roi 提取的不准确，可能需要手动调整
    vid = cv2.VideoCapture(0)
    while True:
        state, src = vid.read()
        cv2.imshow('src', src)
        dst = cv2.undistort(src, mtx, dist, None, new_camera_mtx)
        cv2.imshow('img1', dst)
        dst = dst[y:y + h, x:x + w]
        cv2.imshow('img2', dst)
        cv2.waitKey(1)