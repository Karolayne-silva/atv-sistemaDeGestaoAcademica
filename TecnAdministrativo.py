from conexaoDB import *
from Funcionario import Funcionario

class TecnAdministrativo(Funcionario):
    def __init__(self, _nome, _endereco, _telefone, _cpf, _salario):
        self._nome = _nome
        self._endereco = _endereco
        self._telefone = _telefone
        self._cpf = _cpf
        self._salario = _salario

    def _cadastrar(self):
        c = ConexaoDB()
        comando = f"insert into tecnico_administrativo (nome, endereco, telefone, cpf, salario) values ('{self._nome}','{self._endereco}', '{self._telefone}', '{self._cpf}', '{self._salario}')"
        c.executarDML(comando)


    def _alterar(self, _nome, _cpf):
        c = ConexaoDB()
        comando = f"update tecnico_administrativoset nome ='{_nome}' where cpf='{_cpf}'"
        c.executarDML(comando)
    

    def _excluir(self, _cpf):
        c = ConexaoDB()
        comando = f"delete from tecnico_administrativo where cpf='{_cpf}'"
        c.executarDML(comando)


    def _consultar(self, _cpf):
        c = ConexaoDB()
        comando = f"select * from tecnico_administrativo where cpf='{self._cpf}'"
        resultado = c.executarDQL(comando)
        return resultado
    
