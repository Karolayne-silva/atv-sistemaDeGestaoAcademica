from conexaoDB import *

class Curso:
    def __init__(self, __codigo, __nome, __duracao):
        self.__codigo = __codigo
        self.__nome = __nome
        self.__duracao = __duracao
     
    

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into curso (codigo, nome, duracao) values ('{self.__codigo}','{self.__nome}', '{self.__duracao}')"
        c.executarDML(comando)


    def alterar(self, __nome, __codigo):
        c = ConexaoDB()
        comando = f"update curso set nome ='{__nome}' where codigo='{__codigo}'"
        c.executarDML(comando)
    

    def excluir(self, __nome):
        c = ConexaoDB()
        comando = f"delete from curso where nome='{__nome}'"
        c.executarDML(comando)


    def consultar(self, __nome):
        c = ConexaoDB()
        comando = f"select * from curso where nome='{__nome}'"
        resultado = c.executarDQL(comando)
        return resultado

        