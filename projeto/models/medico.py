from projeto.models.abstratos.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estado_civil: EstadoCivil, data_de_nascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, crm: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estado_civil, data_de_nascimento, cpf, rg, matricula, setor, salario)
        self.crm = crm