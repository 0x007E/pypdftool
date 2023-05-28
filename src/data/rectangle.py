from data.element import ElementSize
from data.style import RectangleStyle

class Rectangle (ElementSize):
    @property
    def style(self) -> RectangleStyle:
        return self.__style

    @style.setter
    def style(self, value) -> RectangleStyle:
        self.__style = value