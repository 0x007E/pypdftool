from data.position import Position
from data.size import Size

class Element:
    @property
    def position(self) -> Position:
        return self.__position
    
    @position.setter
    def position(self, value) -> Position:
        self.__position = value

class ElementSize(Element):
    @property
    def size(self) -> Size:
        return self.__size
    
    @size.setter
    def size(self, value) -> Size:
        self.__size = value