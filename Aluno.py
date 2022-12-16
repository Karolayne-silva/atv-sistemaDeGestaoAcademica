from conexaoDB import *

class Aluno:

    def __init__(self, nome, matricula, cpf, curso):
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.curso = curso


    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into aluno (nome, matricula, cpf, curso) values ('{self.nome}','{self.matricula}', '{self.cpf}', '{self.curso}')"
        c.executarDML(comando)


    def alterar(self, nome, cpf):
        c = ConexaoDB()
        comando = f"update aluno set nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(comando)
    

    def excluir(self, nome):
        c = ConexaoDB()
        comando = f"delete from aluno where nome='{nome}'"
        c.executarDML(comando)


    def consultar(self, nome):
        c = ConexaoDB()
        comando = f"select * from pessoa where nome='{nome}'"
        resultado = c.executarDQL(comando)
        return resultado
    