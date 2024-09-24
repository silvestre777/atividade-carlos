import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.fisica import Fisica
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import Estado_Civil

@pytest.fixture
def criando_pessoa_fisica():
    fisica = Fisica(333, "Joao", "7198854726", "Mateus@gmail.com", 
                                Endereco("Rua F", "11", "Em frente a Fazenda", "74858100", "Salvador", Unidade_Federativa.BAHIA), 
                                Sexo.MASCULINO, Estado_Civil.SEPARADO, "08/08/2000")
    return fisica

def test_pessoa_fisica_id_valido(criando_pessoa_fisica):
     assert criando_pessoa_fisica.id == 333

def test_pessoa_fisica_nome_valido(criando_pessoa_fisica):
     assert criando_pessoa_fisica.nome == "Joao"