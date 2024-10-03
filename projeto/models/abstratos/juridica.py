from projeto.models.abstratos.pessoa import Pessoa
from abc import ABC

from projeto.models.endereco import Endereco

class Juridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.inscricao = self._verficar_inscricao(inscricao)


    def _verificar_cnpj(self, valor):
        self._verificar_cnpj_vazio(valor)

        self.cnpj = valor
        return self.cnpj
    
    def _verificar_cnpj_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O cnpj não deve estar vazio.")
        
    def _verficar_inscricao(self, valor):
        self._verificar_inscricao_tipo_invalido(valor)
        self._verificar_inscricao_vazio(valor)

        self.inscricao = valor
        return self.inscricao
    
    def _verificar_inscricao_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A inscrição deve ser texto.")
    
    def _verificar_inscricao_vazio(self, valor):
         if not valor.strip():
            raise ValueError("A inscrição não deve estar vazio.")