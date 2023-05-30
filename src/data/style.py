from enum import Enum

class Rendering(str, Enum):
    D = "D"
    F = "F"
    DF = "DF"
    FD = "FD"

class BaseStyle:
    def __init__(self, rendering: Rendering):
        self.rendering = rendering

    @property
    def rendering(self) -> Rendering:
        return self.__rendering

    @rendering.setter
    def rendering(self, value) -> Rendering:
        self.__rendering = value

class RectangleStyle(BaseStyle()):
    def __init__(self, rendering: Rendering, corner: bool=False, radius: int=0):
        self.rendering = rendering
        self.corner = corner
        self.radius = radius
    
    @property
    def corner(self) -> bool:
        return self.__corner

    @corner.setter
    def corner(self, value) -> bool:
        self.__corner = value

    @property
    def radius(self) -> int:
        return self.__radius

    @radius.setter
    def radius(self, value) -> int:
        self.__radius = value


