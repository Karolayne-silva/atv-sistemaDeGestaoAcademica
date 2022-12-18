from conexaoDB import *

class Disciplina:

    def __init__(self, __codigo, __nome, __carga_horaria):
        self.__codigo = __codigo
        self.__nome = __nome
        self.__carga_horaria = __carga_horaria

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into disciplina (codigo, nome, carga_horaria) values ('{self.__codigo}','{self.__nome}', '{self.__carga_horaria}')"
        c.executarDML(comando)


    def alterar(self, __cargaHoraria, __nome):
        c = ConexaoDB()
        comando = f"update disciplina set cargaHoraria ='{__cargaHoraria}' where nome='{__nome}'"
        c.executarDML(comando)
    

    def excluir(self, __nome):
        c = ConexaoDB()
        comando = f"delete from disciplina where nome='{__nome}'"
        c.executarDML(comando)


    def consultar(self, __nome):
        c = ConexaoDB()
        comando = f"select * from disciplina where nome='{__nome}'"
        resultado = c.executarDQL(comando)
        return resultado

    