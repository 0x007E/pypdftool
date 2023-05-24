from data.content import ContentSize
from drawing.font import Font
from drawing.position import Position
from data.style import RectangleStyle

class Rectangle (ContentSize):
    @property
    def style(self) -> RectangleStyle:
        return self.__style

    @style.setter
    def style(self, value) -> RectangleStyle:
        self.__style = value