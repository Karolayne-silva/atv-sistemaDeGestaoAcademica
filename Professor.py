from conexaoDB import *
from Funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, nome, endereco, telefone, cpf, salario, titulacao, areaFormacao):
        super().__init__(nome, endereco, telefone, cpf, salario)
        self.titulacao = titulacao
        self.areaFormacao = areaFormacao
    
    