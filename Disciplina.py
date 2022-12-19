from conexaoDB import ConexaoDB

class Disciplina:

    def __init__(self, codigo, nome, carga_horaria):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into disciplina (codigo, nome, carga_horaria) values ('{self.codigo}','{self.nome}', '{self.carga_horaria}')"
        c.executarDML(comando)


    def alterar(codigo, carga_horaria):
        c = ConexaoDB()
        comando = f"update disciplina set carga_horaria = '{carga_horaria}' where codigo='{codigo}'"
        c.executarDML(comando)
    

    def excluir(nome):
        c = ConexaoDB()
        comando = f"delete from disciplina where nome='{nome}'"
        c.executarDML(comando)


    def consultar(nome):
        c = ConexaoDB()
        comando = f"select * from disciplina where nome='{nome}'"
        resultado = c.executarDQL(comando)
        return resultado

    