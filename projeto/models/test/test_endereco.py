from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
import pytest

@pytest.fixture
def endereco_valido():
    return Endereco("Rua I", "3","Casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO.nome)


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