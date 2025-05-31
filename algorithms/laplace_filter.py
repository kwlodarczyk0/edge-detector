import numpy as np
from scipy.signal import convolve2d
from algorithms.filter import Filter


class LaplaceFilter(Filter):
    def filter(self, img, threshold):
        img = np.array(img.convert('L'))  # konwersja do skali szarości

        # Maska Laplace’a (8-kierunkowa)
        kernel = np.array([[ -1, -1, -1],
                           [ -1,  8, -1],
                           [ -1, -1, -1]])

        laplacian = convolve2d(img, kernel, mode='same', boundary='symm')
        laplacian = np.abs(laplacian)
        laplacian = np.uint8(np.clip(laplacian, 0, 255))

        return np.uint8((laplacian > threshold) * 255)