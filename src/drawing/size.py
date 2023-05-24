class Size:
    def __init__(self, width: float=0, height: float=0):
        self.width = width
        self.height = height
    
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value) -> float:
        self.__width = value

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, value) -> float:
        self.__height = value