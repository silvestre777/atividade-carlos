from enum import Enum

class Unidade_Federativa(Enum):
    BAHIA = ("Bahia" ,"BA")
    SAO_PAULO = ("São Paulo" ,"SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")

    def __init__(self, estado:str, sigla: str) -> None:
        self.estado = estado
        self.sigla = sigla