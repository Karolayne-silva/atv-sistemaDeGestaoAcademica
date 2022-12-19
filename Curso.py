from conexaoDB import ConexaoDB

class Curso:
    def __init__(self, codigo, nome, __duracao):
        self.codigo = codigo
        self.nome = nome
        self.__duracao = __duracao
     
    

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into curso (codigo, nome, duracao) values ('{self.codigo}','{self.nome}', '{self.__duracao}')"
        c.executarDML(comando)


    def alterar(nome, codigo):
        c = ConexaoDB()
        comando = f"update curso set nome ='{nome}' where codigo='{codigo}'"
        c.executarDML(comando)
    

    def excluir(nome):
        c = ConexaoDB()
        comando = f"delete from curso where nome='{nome}'"
        c.executarDML(comando)


    def consultar(nome):
        c = ConexaoDB()
        comando = f"select * from curso where nome='{nome}'"
        resultado = c.executarDQL(comando)
        return resultado

        