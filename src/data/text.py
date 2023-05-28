from data.element import Element
from data.font import Font

class Text (Element):
    def __init__(self, font: Font, text: str):
        self.font = font
        self.text = text

    @property
    def font(self) -> Font:
        return self.__font

    @font.setter
    def font(self, value) -> Font:
        self.__font = value
    
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, value) -> str:
        self.__text = value