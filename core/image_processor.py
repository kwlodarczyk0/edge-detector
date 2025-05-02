from PIL import Image

from algorithms.canny_filter import CannyFilter
from algorithms.sobel_filter import SobelFilter
from algorithms.prewitt_filter import PrewittFilter

class ImageProcessor:
    @staticmethod
    def apply_filter(pil_image: Image.Image, filter_name: str,threshold) -> Image.Image:
        if filter_name == "canny":
            return Image.fromarray(CannyFilter().filter(pil_image,threshold))
        elif filter_name == "sobel":
            return Image.fromarray(SobelFilter().filter(pil_image,threshold))
        elif filter_name == "prewitt":
            return Image.fromarray(PrewittFilter().filter(pil_image,threshold))
        else:
            raise ValueError(f"Unsupported filter: {filter_name}")