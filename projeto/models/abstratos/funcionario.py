from projeto.models.abstratos.fisica import Fisica
from abc import ABC
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor

class Funcionario(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_de_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_de_nascimento)
        self.cpf = self._verificar_cpf(cpf)
        self.rg = self._verificar_rg(rg)
        self.matricula = self._verificar_matricula(matricula)
        self.setor = setor
        self.salario = self._verificar_salario(salario)


    def _verificar_cpf(self, valor):
        self._verificar_cpf_tipo_invalido(valor)
        self._verificar_cpf_vazio(valor)
        self._verificar_cpf_formato(valor)

        self.cpf = valor
        return self.cpf


    def _verificar_cpf_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O CPF deve ser um texto.")
        
        
    def _verificar_cpf_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O CPF não deve estar vazio.")
        
    def _verificar_cpf_formato(self, valor):
         if len(valor) != 11 or not valor.isdigit():
            raise ValueError("O CPF deve conter 11 dígitos numéricos.")

    def _verificar_rg(self, valor):

        self._verificar_rg_tipo_invalido(valor)
        self._verificar_rg_vazio(valor)
        
        self.rg = valor
        return self.rg

    def _verificar_rg_tipo_invalido(self, valor):
            if not isinstance(valor, str):
                raise TypeError("O RG deve ser um texto.")


    def _verificar_rg_vazio(self, valor):
        if not valor.strip():
            raise ValueError("O RG não deve estar vazio.")

    

    def _verificar_matricula(self, valor):
        self._verificar_matricula_tipo_invalido(valor)
        self._verificar_matricula_vazio(valor)

        self.matricula = valor
        return self.matricula

    def _verificar_matricula_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A matrícula deve ser um texto.")

    def _verificar_matricula_vazio(self, valor):
        if not valor.strip():
            raise ValueError("A matrícula não deve estar vazia.")


    def _verificar_salario(self, valor):
        self._verificar_salario_tipo_invalido(valor)
        self._verificar_salario_negativo(valor)

        self.salario = valor
        return self.salario

    def _verificar_salario_tipo_invalido(self, valor):
        if not isinstance(valor, (float, int)):
            raise TypeError("O salário deve ser um número.")

    def _verificar_salario_negativo(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo.")