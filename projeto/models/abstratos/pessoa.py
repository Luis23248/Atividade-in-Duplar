from projeto.models.endereco import Endereco
from abc import ABC
import re

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verficar_email(email)
        self.endereco = endereco


    """Método para verificação de nome"""
    def _verificar_nome(self, valor):
        self._verificar_nome_tipo_invalido(valor)
        self._verificar_nome_vazio(valor)
        
        self.nome = valor
        return self.nome
    
    def _verificar_nome_tipo_invalido(self, valor):
         if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")
         
    def _verificar_nome_vazio(self, valor):
            if not valor.strip():
                raise TypeError("O nome não deve estar vazio.")

    """Método para verificação de telefone"""
    def _verificar_telefone(self, valor):
        self._verificar_telefone_tipo_invalido(valor)
        self._verificar_telefone_vazio(valor)
        self._verificar_telefone_com_texto(valor)
        self._verificar_comprimento_do_telefone(valor)
        
        self.telefone = valor
        return self.telefone
    
    def _verificar_telefone_tipo_invalido(self,valor):
         if not isinstance(valor, str):
            raise TypeError("Coloque o número em forma de texto")

    def _verificar_telefone_vazio(self, valor: str):
         if not valor.strip():
             raise TypeError("O telefone não deve estar vazio")

             
    def _verificar_telefone_com_texto(self, valor: str):
        if not valor.isdigit():
            raise ValueError("O número de telefone deve conter apenas dígitos.")
        
         
    def _verificar_comprimento_do_telefone(self, valor):
        if len(valor) != 11:
            raise TypeError("Número de telefone deve conter 11 digitos.")
         

        

    def _verificar_id(self, valor):
        self._verificar_id_tipo_invalido(valor)
        
        self.id = valor
        return self.id

    def _verificar_id_tipo_invalido(self, valor):
        if not isinstance(valor, int):
            raise TypeError("O id deve ser número.")


    def _verficar_email(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O email é inválido.") 
        if not valor.strip():
            raise ValueError("O email não deve estar vazio.") 
        self.email = valor
        return self.email
    
