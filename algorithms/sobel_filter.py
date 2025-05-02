from algorithms.filter import Filter
import cv2 as cv
import numpy as np

class SobelFilter(Filter):
    def filter(self,img,threshold):
        img = np.array(img.convert('L'))
        sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
        sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
        sobel = cv.magnitude(sobelX, sobelY)
        sobel = np.uint8(np.clip(sobel, 0, 255))
        return np.uint8((sobel > threshold) * 255)