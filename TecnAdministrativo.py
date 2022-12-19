from conexaoDB import ConexaoDB
from Funcionario import Funcionario

class TecnAdministrativo(Funcionario):
    def __init__(self, nome, endereco, telefone, cpf, _salario):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf
        self._salario = _salario

    def cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into tecnico_administrativo (nome, endereco, telefone, cpf, salario) values ('{self.nome}','{self.endereco}', '{self.telefone}', '{self.cpf}', '{self._salario}')"
        c.executarDML(comando)


    def alterar(nome, cpf):
        c = ConexaoDB()
        comando = f"update tecnico_administrativoset nome ='{nome}' where cpf='{cpf}'"
        c.executarDML(comando)
    

    def excluir(cpf):
        c = ConexaoDB()
        comando = f"delete from tecnico_administrativo where cpf='{cpf}'"
        c.executarDML(comando)


    def consultar(cpf):
        c = ConexaoDB()
        comando = f"select * from tecnico_administrativo where cpf='{cpf}'"
        resultado = c.executarDQL(comando)
        return resultado
    
