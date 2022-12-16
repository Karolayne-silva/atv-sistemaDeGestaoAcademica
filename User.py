from conexaoDB import *


class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into pessoa (nome, idade, sexo) values ('{self.nome}','{self.idade}', '{self.sexo}')"
        c.executarDML(comando)


    def alterar(self, nome, sexo):
        c = ConexaoDB()
        comando = f"update pessoa set nome ='{nome}' where sexo='{sexo}'"
        c.executarDML(comando)
    

    def excluir(self, nome):
        c = ConexaoDB()
        comando = f"delete from pessoa where nome='{nome}'"
        c.executarDML(comando)


    def consultar(self, nome):
        c = ConexaoDB()
        comando = f"select * from pessoa where nome='{self.nome}'"
        resultado = c.executarDQL(comando)
        return resultado
        

    