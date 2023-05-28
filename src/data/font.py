class Font:
    def __init__(self, family: str, size: int):
        self.family = family
        self.size = size
    
    @property
    def family(self) -> str:
        return self.__family

    @family.setter
    def family(self, value) -> str:
        self.__family = value

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, value) -> int:
        self.__size = value