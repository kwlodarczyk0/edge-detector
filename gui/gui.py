from abc import ABC, abstractmethod

class GUI(ABC):

    @abstractmethod
    def setup_ui(self):
        pass

    @abstractmethod
    def upload_image(self):
        pass

    @abstractmethod
    def apply_transformation(self):
        pass

