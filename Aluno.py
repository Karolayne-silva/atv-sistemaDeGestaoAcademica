from conexaoDB import *

class Aluno:

    def __init__(self, __nome, __matricula, __cpf, __curso):
        self.__nome = __nome
        self.__matricula = __matricula
        self.__cpf = __cpf
        self.__curso = __curso


    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into aluno (nome, matricula, cpf, curso) values ('{self.__nome}','{self.__matricula}', '{self.__cpf}', '{self.__curso}')"
        c.executarDML(comando)


    def alterar(self, __nome, __cpf):
        c = ConexaoDB()
        comando = f"update aluno set nome ='{__nome}' where cpf='{__cpf}'"
        c.executarDML(comando)
    

    def excluir(self, __nome):
        c = ConexaoDB()
        comando = f"delete from aluno where nome='{__nome}'"
        c.executarDML(comando)


    def consultar(self, __nome):
        c = ConexaoDB()
        comando = f"select * from pessoa where nome='{__nome}'"
        resultado = c.executarDQL(comando)
        return resultado
    