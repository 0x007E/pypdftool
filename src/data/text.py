from data.content import Content
from drawing.font import Font

class Text (Content):
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