from enum import Enum

class EstadoCivil(Enum):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    SEPARADO = "Separado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"

    def __init__(self, nome: str) -> None:
        self.nome = nome