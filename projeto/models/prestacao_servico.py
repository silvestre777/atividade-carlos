from ..models.endereco import Endereco
from ..models.juridica import Juridica

class PrestacaoServico(Juridica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, contratoInicio: str,contratoFim: str) -> None:
        super().__init__(nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"Inicio do contrato: {self.contratoInicio}"
            f"Final do contrato: {self.contratoFim}"
            )