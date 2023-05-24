class Position:
    def __init__(self, x: float, y: float):
        self.X = x
        self.Y = y
    
    @property
    def X(self) -> float:
        return self.__X

    @X.setter
    def X(self, value) -> float:
        self.__X = value

    @property
    def Y(self) -> float:
        return self.__Y

    @X.setter
    def Y(self, value) -> float:
        self.__Y = value