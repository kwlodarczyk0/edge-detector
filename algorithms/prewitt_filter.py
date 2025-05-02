import numpy as np
from scipy.signal import convolve2d

from algorithms.filter import Filter


class PrewittFilter(Filter):
    def filter(self, img, threshold):
        img = np.array(img.convert('L'))  # konwersja do skali szarości

        # Maski Prewitta
        kernelX = np.array([[-1, 0, 1],
                            [-1, 0, 1],
                            [-1, 0, 1]])

        kernelY = np.array([[1, 1, 1],
                            [0, 0, 0],
                            [-1, -1, -1]])

        prewittX = convolve2d(img, kernelX, mode='same', boundary='symm')
        prewittY = convolve2d(img, kernelY, mode='same', boundary='symm')

        magnitude = np.sqrt(prewittX ** 2 + prewittY ** 2)
        magnitude = np.uint8(np.clip(magnitude, 0, 255))

        return np.uint8((magnitude > threshold) * 255)