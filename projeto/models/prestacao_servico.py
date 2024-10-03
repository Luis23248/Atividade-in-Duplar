from projeto.models.abstratos.juridica import Juridica
from projeto.models.endereco import Endereco

class PrestacaoServico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao: str, contrato_inicio: str, contrato_fim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao)
        self.contrato_inicio = self._verificar_contrato_inicio(contrato_inicio)
        self.contrato_fim = self._verificar_contrato_fim(contrato_fim)


    
    def _verificar_contrato_inicio(self, valor):
        self._verificar_contrato_inicio_tipo_invalido(valor)
        self._verificar_contrato_inicio_vazio(valor)

        self.contrato_inicio = valor
        return self.contrato_inicio


    def _verificar_contrato_inicio_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A data do contrato inicio deve ser uma string.")

    def _verificar_contrato_inicio_vazio(self, valor):
        if not valor.strip():
            raise ValueError("A data do contrato inicio não deve estar vazia.")

    
    def _verificar_contrato_fim(self, valor):
         self._verificar_contrato_fim_tipo_invalido(valor)
         self._verificar_contrato_fim_vazio(valor)
         
         self.contrato_fim = valor
         return self.contrato_fim

    def _verificar_contrato_fim_tipo_invalido(self, valor):
         if not isinstance(valor, str):
             raise TypeError("A data do contrato fim deve ser uma string.")

    def _verificar_contrato_fim_vazio(self, valor):
         if not valor.strip():
             raise ValueError("A data do contrato fim não deve estar vazia.")
