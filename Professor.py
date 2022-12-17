from conexaoDB import *
from Funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, nome, endereco, telefone, cpf, salario, titulacao, areaFormacao, funcionario_cpf):
        super().__init__(nome, endereco, telefone, cpf, salario)
        self.titulacao = titulacao
        self.areaFormacao = areaFormacao
        self.funcionario_cpf = funcionario_cpf 
    

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into professor (nome, endereco, telefone, cpf, salario, titulacao, areaFormacao) values ('{self.nome}','{self.endereco}', '{self.telefone}', '{self.cpf}', '{self.salario}', '{self.titulacao}', '{self.areaFormacao}','{self.funcionario_cpf}')"
        c.executarDML(comando)


    def alterar(self, nome, cpf):
        c = ConexaoDB()
        comando = f"update professor set nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(comando)
    

    def excluir(self, cpf):
        c = ConexaoDB()
        comando = f"delete from professor where cpf='{cpf}'"
        c.executarDML(comando)


    def consultar(self, cpf):
        c = ConexaoDB()
        comando = f"select * from professor where cpf='{cpf}'"
        resultado = c.executarDQL(comando)
        return resultado

    