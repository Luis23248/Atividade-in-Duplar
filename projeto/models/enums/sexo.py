from enum import Enum

class Sexo(Enum):
    MASCULINO = ("Masculino", 'M')
    FEMININO = ("Feminio", 'F')

    def __init__(self, nome: str, caractere: str) -> None:
        self.nome = nome 
        self.caractere = caractere