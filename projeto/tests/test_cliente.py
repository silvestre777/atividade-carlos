import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import Unidade_Federativa
from projeto.models.cliente import Cliente
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import Estado_Civil

@pytest.fixture
def criar_cliente():
    cliente = Cliente(3323, "revoada", 719879392, "revoada@gmail.com", 
                      Endereco("amaralina", "99", "Frente", "434124", "Salvador", Unidade_Federativa.BAHIA), "30/03/2000", 
                      Sexo.MASCULINO, Estado_Civil.DIVORCIADO, "12223413234")
    return cliente

def test_cliente_id_valido(criar_cliente):
     assert criar_cliente.id == 3323

def test_cliente_nome_valido(criar_cliente):
     assert criar_cliente.nome == "revoada"