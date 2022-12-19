from conexaoDB import ConexaoDB
from Funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, nome, endereco, telefone, cpf, salario, titulacao, area_formacao):
        super().__init__(nome, endereco, telefone, cpf, salario)
        self.titulacao = titulacao
        self.area_formacao = area_formacao

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into professor (nome, endereco, telefone, cpf, salario, titulacao, area_formacao) values ('{self.nome}','{self.endereco}', '{self.telefone}', '{self.cpf}', '{self.salario}', '{self.titulacao}', '{self.area_formacao}')"
        c.executarDML(comando)

    def alterar( nome, cpf):
        c = ConexaoDB()
        comando = f"update professor set nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(comando)
    

    def excluir(cpf):
        c = ConexaoDB()
        comando = f"delete from professor where cpf='{cpf}'"
        c.executarDML(comando)


    def consultar(cpf):
        c = ConexaoDB()
        comando = f"select * from professor where cpf='{cpf}'"
        resultado = c.executarDQL(comando)
        return resultado

