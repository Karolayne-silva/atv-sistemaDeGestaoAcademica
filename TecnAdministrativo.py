from conexaoDB import *
from Funcionario import Funcionario

class TecnAdministrativo(Funcionario):
    def __init__(self, nome, endereco, telefone,cpf, salario):
        super().__init__(self, nome, endereco, telefone, cpf, salario)

