import os
from data.element import ElementSize

class Image (ElementSize):
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, value) -> str:
        if(not os.path.exists(value)):
            raise FileNotFoundError(value)
        self.__path = value
    
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, value) -> str:
        self.__text = value