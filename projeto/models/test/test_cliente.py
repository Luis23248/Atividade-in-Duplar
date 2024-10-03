import pytest
from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def cliente_valido():
    return Cliente(1234, "LPL","71988417575", "LP@gmail.com",
                    Endereco("Rua I","3","Casa", "43900-000", "São Paulo", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)


def test_validar_id(cliente_valido):
    assert cliente_valido.id == 1234

def test_validar_nome(cliente_valido):
    assert cliente_valido.nome == "LPL"

def test_validar_telefone(cliente_valido):
    assert cliente_valido.telefone ==  "71988417575"

def test_validar_email(cliente_valido):
    assert cliente_valido.email == "LP@gmail.com"


def test_validar_sexo(cliente_valido):
    assert cliente_valido.sexo == Sexo.MASCULINO.nome

def test_validar_estado_civil(cliente_valido):
    assert cliente_valido.estado_civil == EstadoCivil.SOLTEIRO.nome

def test_validar_data_nascimento(cliente_valido):
    assert cliente_valido.data_de_nascimento == "04/01/2003"

def test_validar_protocolo_de_atendimento(cliente_valido):
    assert cliente_valido.protocolo_de_atendimento == 2323


def test_validar_nome_tipo_invalido():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
         Cliente(1234, 1123, "71988417575", "LP@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)

def test_nome_vazio_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):       
        Cliente(1234, "", "71988417575", "LP@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)

def test_comprimento_telefone_invalido():
    with pytest.raises(TypeError, match="Número de telefone deve conter 11 digitos."):      
        Cliente(1234, "LPL", "719884175753", "LP@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)
        
def test_telefone_tipo_invalido():
    with pytest.raises(TypeError, match="Coloque o número em forma de texto"):       
        Cliente(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)
        

def test_telefone_com_texto():
    with pytest.raises(ValueError, match="O número de telefone deve conter apenas dígitos."):
       Cliente(1234, "LPL", "71988417575er", "LP@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)

def test_telefone_vazio():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio"):
        Cliente(1234, "LPL", "", "LP@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)            


def test_protocolo_de_atendimento_tipo_invalido():
    with pytest.raises(TypeError, match="O protocolo de atendimento deve ser número"):
        Cliente(1234, "LPL", "71988417575", "LP@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", "2323")

def test_protocolo_de_atendimento_valor_negativo_retorna_mensagem():
    with pytest.raises(ValueError, match="O protocolo de atendimento deve ser número positivo."):
        Cliente(1234, "LPL", "71988417575", "LP@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", -2323)

def test_id_numero_em_string_retorna_mensagem():
    with pytest.raises(TypeError, match="O id deve ser número."):
        Cliente("1234", "LPL", "71988417575", "LP@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)

def test_email_vazio_retorna_menagem():
    with pytest.raises(TypeError, match="O email não deve estar vazio."):
        Cliente(1234, "LPL", "71988417575", "",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)

def test_email_formato_invalido():
    with pytest.raises(ValueError, match="O email é inválido."):
        Cliente(1234, "LPL", "71988417575", "robsoncaminhoes@gmail.com",
            Endereco("Rua I","3","casa", "78541-333", "Salvador", UnidadeFederativa.SAO_PAULO.nome),Sexo.MASCULINO.nome, EstadoCivil.SOLTEIRO.nome, "04/01/2003", 2323)


