from algorithms.filter import Filter
import cv2 as cv
import numpy as np


class CannyFilter(Filter):
    def filter(self,img,threshold):
        img = np.array(img.convert('L'))
        # edges = cv.Canny(img, threshold1=100, threshold2=200)
        lower = int(max(0, threshold * 0.5))
        upper = int(min(255, threshold))
        return cv.Canny(img, lower, upper)
        # return edges