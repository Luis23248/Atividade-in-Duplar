import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa



@pytest.fixture
def fornecedor_valido():
    return Fornecedor(1234, "LPL", "71988417575","LP@gmail.com",
            Endereco("Rua I", "3","Casa","78541-333","Sâo Paulo",UnidadeFederativa.SAO_PAULO.nome),"04.254.147/3334-26","378","PS4")



def test_validar_id(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.id == 1234

def test_validar_nome(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.nome == "LPL"

def test_validar_telefone(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.telefone ==  "71988417575"

def test_validar_email(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.email == "LP@gmail.com"

def test_validar_cnpj(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.cnpj == "04.254.147/3334-26"

def test_validar_inscricao(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.inscricao == "378"

def test_validar_produto(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.produto == "PS4"

def test_validar_endereco(fornecedor_valido: Fornecedor):
    assert fornecedor_valido.endereco.logadouro == "Rua I"
    assert fornecedor_valido.endereco.numero == "3"
    assert fornecedor_valido.endereco.complemento == "Casa"
    assert fornecedor_valido.endereco.cep == "78541-333"
    assert fornecedor_valido.endereco.cidade == "São Paulo"
    assert fornecedor_valido.endereco.uf == UnidadeFederativa.SAO_PAULO.nome == "São Paulo"


"""NOME Tests"""
def test_validar_nome_tipo_invalido():
    with pytest.raises(TypeError, match="O nome deve ser um texto."):
        Fornecedor(1234, 123, "71988417575","LP@gmail.com",
            Endereco("Rua I", "93","casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO.nome),"14.796.606/0001-90","445","Manga")
        
def test_nome_vazio_retorna_mensagem():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
        Fornecedor(1234, "", "71988417575","LP@gmail.com",
            Endereco("Rua I", "3","Casa","78541-333","Sâo Paulo",UnidadeFederativa.SAO_PAULO.nome),"04.254.147/3334-26","378","PS4")


"""ID Tests"""
def test_id_numero_em_string_retorna_mensagem():
    with pytest.raises(TypeError, match="O id deve ser número."):
        Fornecedor("1234", "LPL", "71988417575","LP@gmail.com",
            Endereco("Rua I", "3","Casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO.nome),"04.254.147/3334-26","378","PS4")
        

"""EMAIL Tets"""
def test_email_vazio_retorna_menagem():
    with pytest.raises(TypeError, match="O email não deve estar vazio."):     
        Fornecedor("1234", "LPL", "71988417575", "",
            Endereco("Rua I", "3","Casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO.nome),"04.254.147/3334-26","378","PS4")


def test_email_formato_invalido():
    with pytest.raises(ValueError, match="O email é inválido."):
        Fornecedor("1234", "LPL", "71988417575","_LP@gmail.com",
            Endereco("Rua I", "3","Casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO.nome),"04.254.147/3334-26","378","PS4")
        

"""PRODUTO Tests"""
def test_produto_tipo_invalido():
    with pytest.raises(TypeError, match="O produto deve ser um texto."):
        Fornecedor(1234, "LPL", "71988417575", "LP@gmail.com",
                   Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", 2342)

def test_produto_vazio():
    with pytest.raises(ValueError, match="O produto não deve estar vazio."):
        Fornecedor(1234, "LPL", "71988417575", "LP@gmail.com",
                   Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "")

"""TELEFONE Tests"""
def test_comprimento_telefone_invalido():
    with pytest.raises(TypeError, match="Número de telefone deve conter 11 digitos."):
        Fornecedor(1234, "LPL", "719884175758", "LP@gmail.com",
                   Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")

        
def test_telefone_tipo_invalido():
    with pytest.raises(TypeError, match="Coloque o número em forma de texto"):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")

def test_telefone_com_texto():
    with pytest.raises(ValueError, match="O número de telefone deve conter apenas dígitos."):
        Fornecedor(1234, "LPL", "71988417575xY", "LP@gmail.com",
            Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")    

def test_telefone_vazio():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio"):
        Fornecedor(1234, "LPL", "", "LP@gmail.com",
            Endereco("Rua I", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")

"""ENDEREÇO Tests"""
def test_logradouro_vazio():
    with pytest.raises(TypeError, match="O logradouro não deve estar vazio."):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("", "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")
        
def test_logadouro_tipo_invalido():
     with pytest.raises(TypeError, match="O logradouro deve ser um texto."):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco(332, "3", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")


def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve ser um texto."):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I", 3, "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")

def test_numero_vazio():
    with pytest.raises(TypeError, match="O número não deve estar vazio."):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I", "", "Casa", "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="O CEP deve ser um texto."):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I", "3", "Casa", 78541-333, "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")


def test_cep_formato_invalido():
    with pytest.raises(ValueError, match="O formato do CEP é inválido."):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I", "3", "Casa", "78541//33", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")


def test_cep_vazio():
    with pytest.raises(TypeError, match="O CEP não deve estar vazio."):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I", "3", "Casa", "", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")


def test_cidade_vazia():
    with pytest.raises(TypeError, match="A cidade não deve estar vazia."):  
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I", "3", "Casa", "78541-333", "", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")


def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve ser um texto."):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I", "3", "Casa", "78541-333", 244, UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")   

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve ser um texto."):
        Fornecedor(1234, "LPL", 71988417575, "LP@gmail.com",
            Endereco("Rua I", "3", 337, "78541-333", "São Paulo", UnidadeFederativa.SAO_PAULO.nome), 
                   "04.254.147/3334-26", "378", "PS4")
  

