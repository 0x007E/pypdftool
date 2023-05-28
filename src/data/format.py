from enum import Enum

class PageType(str, Enum):
    A3 = "A3"
    A4 = "A4"
    A5 = "A5"
    LETTER = "LETTER"
    LEGAL = "LEGAL"

class Orientation(str, Enum):
    PORTRAIT = "P"
    LANDSCAPE = "L"

class Format:
    def __init__(self, pagetype: PageType=PageType.A4, orientation: Orientation=Orientation.LANDSCAPE):
        self.pagetype = pagetype
        self.orientation = orientation
    
    @property
    def pagetype(self) -> PageType:
        return self.__pagetype

    @pagetype.setter
    def pagetype(self, value) -> PageType:
        self.__pagetype = value

    @property
    def orientation(self) -> Orientation:
        return self.__orientation

    @orientation.setter
    def orientation(self, value) -> Orientation:
        self.__orientation = value