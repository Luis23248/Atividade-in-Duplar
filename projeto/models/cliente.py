from projeto.models.abstratos.fisica import Fisica
from abc import ABC

from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo

class Cliente(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_de_nascimento: str, protocolo_de_atendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_de_nascimento)
        self.protocolo_de_atendimento = self._verificar_protocolo_de_atendimento(protocolo_de_atendimento)

    def _verificar_protocolo_de_atendimento(self, valor):

        if not isinstance(valor, int):
            raise TypeError("O protocolo de atendimento deve ser número.")
        
        if valor <= 0:
            raise ValueError("O protocolo de atendimento deve ser número positivo.")
        
        self.protocolo_de_atendimento = valor
        return self.protocolo_de_atendimento
    
