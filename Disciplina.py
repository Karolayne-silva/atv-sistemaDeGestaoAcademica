from conexaoDB import *

class Disciplina:

    def __init__(self, codigo, nome, carga_horaria):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into disciplina (codigo, nome, carga_horaria) values ('{self.codigo}','{self.nome}', '{self.carga_horaria}')"
        c.executarDML(comando)


    def alterar(self, cargaHoraria, nome):
        c = ConexaoDB()
        comando = f"update disciplina set cargaHoraria ='{cargaHoraria}' where nome='{nome}'"
        c.executarDML(comando)
    

    def excluir(self, nome):
        c = ConexaoDB()
        comando = f"delete from disciplina where nome='{nome}'"
        c.executarDML(comando)


    def consultar(self, nome):
        c = ConexaoDB()
        comando = f"select * from disciplina where nome='{nome}'"
        resultado = c.executarDQL(comando)
        return resultado

    