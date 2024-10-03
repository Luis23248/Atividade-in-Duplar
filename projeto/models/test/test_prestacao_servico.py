import pytest
from projeto.models.prestacao_servico import PrestacaoServico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def prestacao_servico_valido():
    return PrestacaoServico(1234, "LPL", "71988417575","LP@gmail.com",
            Endereco("Rua I", "3","Casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO
                     .nome),"04.254.147/3334-26","378","12/12/2024","15/08/2030")

def test_validar_id(prestacao_servico_valido):
    assert prestacao_servico_valido.id == 1234

def test_validar_nome(prestacao_servico_valido):
    assert prestacao_servico_valido.nome == "LPL"

def test_validar_telefone(prestacao_servico_valido):
    assert prestacao_servico_valido.telefone ==  "71988417575"

def test_validar_email(prestacao_servico_valido):
    assert prestacao_servico_valido.email == "LP@gmail.com"

def test_validar_cnpj(prestacao_servico_valido):
    assert prestacao_servico_valido.cnpj == "04.254.147/3334-26"

def test_validar_inscricao(prestacao_servico_valido):
    assert prestacao_servico_valido.inscricao == "378"

def test_validar_contrato_inicio(prestacao_servico_valido):
    assert prestacao_servico_valido.contrato_inicio == "12/12/2024"

def test_validar_contrato_fim(prestacao_servico_valido):
    assert prestacao_servico_valido.contrato_fim == "15/08/2030"


"""DATA DE CONTRATAÇÃO Tests"""
def test_data_contrato_inicio_vazio():
    with pytest.raises(ValueError, match="A data do contrato inicio não deve estar vazia."):
        PrestacaoServico(1234, "LPL", "71988417575","LP@gmail.com",
            Endereco("Rua I", "3","Casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO.nome),"04.254.147/3334-26","378","","15/08/2030")
        
def test_data_contrato_inicio_tipo_invalido():
    with pytest.raises(TypeError, match="A data do contrato inicio deve ser uma string."):
        PrestacaoServico(1234, "LPL", "71988417575","LP@gmail.com",
            Endereco("Rua I", "3","Casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO.nome),"104.254.147/3334-26","378",562024,"15/08/2030")
        
def test_data_contrato_fim_vazio():
    with pytest.raises(ValueError, match="A data do contrato fim não deve estar vazia."):
        PrestacaoServico(1234, "LPL", "71988417575","LP@gmail.com",
            Endereco("Rua I", "3","Casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO.nome),"104.254.147/3334-26","378","12/12/2024","")
        
def test_data_contrato_fim_tipo_invalido():
    with pytest.raises(TypeError, match="A data do contrato fim deve ser uma string."):
        PrestacaoServico(1234, "LPL", "71988417575","LP@gmail.com",
            Endereco("Rua I", "3","Casa","78541-333","São Paulo",UnidadeFederativa.SAO_PAULO.nome),"104.254.147/3334-26","378","12/12/2024",562029)
