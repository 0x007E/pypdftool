from drawing.position import Position
from drawing.size import Size

class Content:
    @property
    def position(self) -> Position:
        return self.__position
    
    @position.setter
    def position(self, value) -> Position:
        self.__position = value

class ContentSize(Content):
    @property
    def size(self) -> Size:
        return self.__size
    
    @size.setter
    def size(self, value) -> Size:
        self.__size = value