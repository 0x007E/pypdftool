from data.element import Element
from data.style import BaseStyle

class Circle (Element):
    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, value) -> float:
        self.__radius = value

    @property
    def style(self) -> BaseStyle:
        return self.__style

    @style.setter
    def style(self, value) -> BaseStyle:
        self.__style = value