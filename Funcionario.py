from conexaoDB import *

class Funcionario:
    def __init__(self, nome, endereco, telefone, cpf, salario):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf
        self.salario = salario
    
    def cadastrar(self):
        c = ConexaoDB()
        comando = "editar"
        c.executarDML(comando)

    def alterar(self):
        c = ConexaoDB
        comando = "editar"
        c.executarDML(comando)

    def excluir(self):
        c = ConexaoDB()
        comando = "editar"
        c.executarDML(comando)

    def consultar(self):
        c = ConexaoDB()
        comando = "editar"
        resultado = c.executarDQL(comando)
        return resultado