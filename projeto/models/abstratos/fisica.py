from abc import ABC
from projeto.models.abstratos.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

class Fisica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_de_nascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)

        self.sexo = sexo
        self.estado_civil = estado_civil
        self.data_de_nascimento = self._verificar_data_nascimento(data_de_nascimento)

    

    def _verificar_data_nascimento(self, valor):
        self._verificar_data_nascimento_vazio(valor)

        self.data_de_nascimento = valor
        return self.data_de_nascimento
    
    def _verificar_data_nascimento_vazio(self, valor):
        if not valor.strip():
            raise ValueError("A data de nascimento não pode estar vazia")