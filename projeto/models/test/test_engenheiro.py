import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def engenheiro_valido():
    return Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com",
                      Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", "032.457.995-23", 
                      "17375890", "1337", Setor.ENGENHARIA.nome, 5800, "crea")


def test_validar_id(engenheiro_valido):
    assert engenheiro_valido.id == 1234

def test_validar_nome(engenheiro_valido):
    assert engenheiro_valido.nome == "LPL"

def test_validar_telefone(engenheiro_valido):
    assert engenheiro_valido.telefone == "71912345678"

def test_validar_email(engenheiro_valido):
    assert engenheiro_valido.email == "LP@gmail.com"

def test_validar_cpf(engenheiro_valido):
    assert engenheiro_valido.cpf == "032.457.995-23"

def test_validar_rg(engenheiro_valido):
    assert engenheiro_valido.rg == "17375890"

def test_validar_matricula(engenheiro_valido):
    assert engenheiro_valido.matricula == "1337"

def test_validar_setor(engenheiro_valido):
    assert engenheiro_valido.setor == Setor.ENGENHARIA.nome

def test_validar_salario(engenheiro_valido):
    assert engenheiro_valido.salario == 5800


def test_validar_endereco(engenheiro_valido):
    assert engenheiro_valido.endereco.logadouro == "Rua I"
    assert engenheiro_valido.endereco.numero == "3"
    assert engenheiro_valido.endereco.complemento == "Casa"
    assert engenheiro_valido.endereco.cidade == "São Paulo"
    assert engenheiro_valido.endereco.cep == "78541-333"
    assert engenheiro_valido.endereco.uf == UnidadeFederativa.SAO_PAULO.nome == "São Paulo"

""" CPF TESTS"""
def test_cpf_vazio():
    with pytest.raises(ValueError, match="O CPF não deve estar vazio."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "", 
                    "17375890", "1337", Setor.ENGENHARIA.nome, 5800, "crea")

def test_cpf_tipo_invalido():
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", 032.45799523, 
                    "17375890", "1337", Setor.ENGENHARIA.nome, 5800, "crea")

def test_cpf_formato_invalido():
    with pytest.raises(ValueError, match="O CPF deve conter 11 dígitos numéricos."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", "1337", Setor.ENGENHARIA.nome, 5800, "crea")

"""RG Tests"""
def test_rg_vazio():
    with pytest.raises(ValueError, match="O RG não deve estar vazio."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "", "4556", Setor.ENGENHARIA.nome, 5800, "crea")


def test_rg_tipo_invalido():
    with pytest.raises(TypeError, match="O RG deve ser um texto."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    17375890, "1337", Setor.ENGENHARIA.nome, 5800, "crea")
        

"""MATRÍCULA Tests"""
def test_matricula_vazio():
    with pytest.raises(ValueError, match="A matrícula não deve estar vazia."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", "", Setor.ENGENHARIA.nome, 5800, "crea")            

def test_matricula_tipo_invalido():
    with pytest.raises(TypeError, match="A matrícula deve ser um texto."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")
        
"""SALÁRIO Tests"""
def test_salario_tipo_invalido():
    with pytest.raises(TypeError, match="O salário deve ser um número."):       
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", "1337", Setor.ENGENHARIA.nome, "Cinco mil e oitocentos", "crea")

def test_salario_negativo():
    with pytest.raises(ValueError, match="O salário não pode ser negativo."):   
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, -5800, "crea")


"""ENDEREÇO Tests"""
def test_logradouro_vazio():
    with pytest.raises(TypeError, match="O logradouro não deve estar vazio."):     
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")


        
def test_logadouro_tipo_invalido():
     with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco(448, "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")

          
def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", 3, "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")

      
def test_numero_vazio():
    with pytest.raises(TypeError, match="O número não deve estar vazio."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")
              
      
def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", 78541333, "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")

        

def test_cep_formato_invalido():
    with pytest.raises(ValueError, match="O formato do CEP é inválido."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-3x*33", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")

       
def test_cep_vazio():
    with pytest.raises(TypeError, match="O CEP não deve estar vazio."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")
      
      
def test_cidade_vazia():
    with pytest.raises(TypeError, match="A cidade não deve estar vazia."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", "", UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")


def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
        Engenheiro(1234, "LPL", "71912345678", "LP@gmail.com", 
                    Endereco("Rua I", "3", "Casa", "78541-333", 1248, UnidadeFederativa.SAO_PAULO.nome), 
                    Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "032.457.995-203", 
                    "17375890", 1337, Setor.ENGENHARIA.nome, 5800, "crea")

         
def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
        Engenheiro(123, "Wagner", "71982345670", "wagner@gmail.com",
                      Endereco("Drena", "93", 123, "43900-000", "Sâo Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                      Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "05/06/2005", "12345678900", 
                      "12435533", "4556", Setor.ENGENHARIA.nome, 2600, "crea")
        


def test_validar_endereco(endereco_valido):
    assert endereco_valido.logadouro == "Rua I"
    assert endereco_valido.numero == "3"
    assert endereco_valido.complemento == "Casa"
    assert endereco_valido.cep == "78541-333"
    assert endereco_valido.cidade == "São Paulo"
    assert endereco_valido.uf == UnidadeFederativa.SAO_PAULO.nome



def test_logradouro_vazio():
    with pytest.raises(TypeError, match="O logradouro não deve estar vazio."):
        Endereco("","3","Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome)

        
def test_logadouro_tipo_invalido():
     with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
            Endereco(123,"3","Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome)

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
        Endereco("Rua I",123,"Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome)


def test_numero_vazio():
    with pytest.raises(TypeError, match="O número não deve estar vazio."):
        Endereco("Rua I","","Casa", "78541-333", "São paulo", UnidadeFederativa.SAO_PAULO.nome)

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
        Endereco("Rua I","3","Casa", 78541333, "São Paulo", UnidadeFederativa.SAO_PAULO.nome)


def test_cep_formato_invalido():
    with pytest.raises(ValueError, match="O formato do CEP é inválido."):
        Endereco("Rua I","3","Casa", "-=x78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome)

def test_cep_vazio():
    with pytest.raises(TypeError, match="O CEP não deve estar vazio."):
         Endereco("Rua I","3","Casa", "", "São Paulo", UnidadeFederativa.SAO_PAULO.nome)

def test_cidade_vazia():
    with pytest.raises(TypeError, match="A cidade não deve estar vazia."):
          Endereco("Rua I","3","Casa", "78541-333", "", UnidadeFederativa.SAO_PAULO.nome)


def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
            Endereco("Rua I","3","Casa", "78541-333", 9090, UnidadeFederativa.SAO_PAULO.nome)

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
         Endereco("Rua I","3",1234, "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome)    