from .element import ElementSize
from .style import RectangleStyle

class Rectangle (ElementSize):
    @property
    def style(self) -> RectangleStyle:
        return self.__style

    @style.setter
    def style(self, value) -> RectangleStyle:
        self.__style = value