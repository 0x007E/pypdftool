from data.element import ElementSize

class Link (ElementSize):
    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, value) -> str:
        self.__link = value
    
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, value) -> str:
        self.__text = value