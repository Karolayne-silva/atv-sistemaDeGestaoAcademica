from conexaoDB import ConexaoDB

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


    def alterar(nome, cpf):
        c = ConexaoDB()
        comando = f"update aluno set nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(comando)
    

    def excluir(nome):
        c = ConexaoDB()
        comando = f"delete from aluno where nome='{nome}'"
        c.executarDML(comando)


    def consultar(nome):
        c = ConexaoDB()
        comando = f"select * from aluno where nome='{nome}'"
        resultado = c.executarDQL(comando)
        return resultado
    