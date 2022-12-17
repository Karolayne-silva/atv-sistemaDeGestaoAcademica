from conexaoDB import *
from Funcionario import Funcionario

class TecnAdministrativo(Funcionario):
    def __init__(self, nome, endereco, telefone,cpf, salario, funcionario_cpf):
        super().__init__(self, nome, endereco, telefone, cpf, salario)
        self.funcionario_cpf = funcionario_cpf

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into tecnAdministrativo (nome, endereco, telefone, cpf, salario) values ('{self.nome}','{self.endereco}', '{self.telefone}', '{self.cpf}', '{self.salario}', '{self.funcionario_cpf}')"
        c.executarDML(comando)


    def alterar(self, nome, cpf):
        c = ConexaoDB()
        comando = f"update tecnAdministrativo set nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(comando)
    

    def excluir(self, cpf):
        c = ConexaoDB()
        comando = f"delete from tecnAdministrativo where cpf='{cpf}'"
        c.executarDML(comando)


    def consultar(self, cpf):
        c = ConexaoDB()
        comando = f"select * from tcnAdministrativo where cpf='{self.cpf}'"
        resultado = c.executarDQL(comando)
        return resultado
    
