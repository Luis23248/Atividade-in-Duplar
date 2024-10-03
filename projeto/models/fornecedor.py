from projeto.models.abstratos.juridica import Juridica
from projeto.models.endereco import Endereco

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao)
        self.produto = self._verificar_produto(produto)


    def _verificar_produto(self, valor):

        self._verificar_produto_tipo_invalido(valor)
        self._verificar_produto_vazio(valor)

        self.produto = valor
        return self.produto

    def _verificar_produto_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O produto deve ser um texto.")

    def _verificar_produto_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O produto não deve estar vazio.")
