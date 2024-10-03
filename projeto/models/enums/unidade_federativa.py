from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")
    SAO_PAULO = ("São Paulo", "SP")

    def __init__(self, nome: str, sigla: str) -> None:
        self.nome = nome
        self.sigla = sigla