from conexaoDB import *

class Curso:
    def __init__(self, codigo, nome, duracao, professor_funcionario_cpf, curso_codigo):
        self.codigo = codigo
        self.nome = nome
        self.duracao = duracao
     
    

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into curso (codigo, nome, duracao) values ('{self.codigo}','{self.nome}', '{self.duracao}')"
        c.executarDML(comando)


    def alterar(self, nome, codigo):
        c = ConexaoDB()
        comando = f"update curso set nome ='{nome}' where codigo='{codigo}'"
        c.executarDML(comando)
    

    def excluir(self, nome):
        c = ConexaoDB()
        comando = f"delete from curso where nome='{nome}'"
        c.executarDML(comando)


    def consultar(self, nome):
        c = ConexaoDB()
        comando = f"select * from curso where nome='{nome}'"
        resultado = c.executarDQL(comando)
        return resultado

        