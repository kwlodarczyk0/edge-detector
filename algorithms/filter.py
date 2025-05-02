from abc import ABC, abstractmethod

class Filter(ABC):
    # Abstract method: Subclasses must implement this method
    @abstractmethod
    def filter(self,img,threshold):
        pass