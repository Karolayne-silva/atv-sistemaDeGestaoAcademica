from conexaoDB import *

class Funcionario:
    def __init__(self, nome, endereco, telefone, cpf, salario):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf
        self.salario = salario
    
    def __cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into funcionario (nome, endereco, telefone, cpf, salario) values ('{self.nome}','{self.endereco}', '{self.telefone}', '{self.cpf}', '{self.salario}')"
        c.executarDML(comando)


    def __alterar(self, nome, cpf):
        c = ConexaoDB()
        comando = f"update funcionario nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(comando)
    

    def __excluir(self, cpf):
        c = ConexaoDB()
        comando = f"delete from funcionario where cpf='{cpf}'"
        c.executarDML(comando)


    def __consultar(self, cpf):
        c = ConexaoDB()
        comando = f"select * from funcionario where cpf='{self.cpf}'"
        resultado = c.executarDQL(comando)
        return resultado

