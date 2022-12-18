from conexaoDB import *
from Funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, _nome, _endereco, _telefone, _cpf, _salario, __titulacao, __area_formacao):
        super().__init__(_nome, _endereco, _telefone, _cpf, _salario)
        self.__titulacao = __titulacao
        self.__area_formacao = __area_formacao

    def _cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into professor (nome, endereco, telefone, cpf, salario, titulacao, area_formacao) values ('{self._nome}','{self._endereco}', '{self._telefone}', '{self._cpf}', '{self._salario}', '{self.__titulacao}', '{self.__area_formacao}')"
        c.executarDML(comando)

    def _alterar(self, _nome, _cpf):
        c = ConexaoDB()
        comando = f"update professor set nome ='{_nome}' where cpf='{_cpf}'"
        c.executarDML(comando)
    

    def _excluir(self, _cpf):
        c = ConexaoDB()
        comando = f"delete from professor where cpf='{_cpf}'"
        c.executarDML(comando)


    def _consultar(self, _cpf):
        c = ConexaoDB()
        comando = f"select * from professor where cpf='{_cpf}'"
        resultado = c.executarDQL(comando)
        return resultado

    