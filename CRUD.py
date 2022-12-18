from conexaoDB import ConexaoDB
from Aluno import Aluno
from Curso import Curso
from Disciplina import Disciplina
from Funcionario import Funcionario
from Professor import Professor
from TecnAdministrativo import TecnAdministrativo

def menu():
    print("o que você deseja fazer?" /n "digite o número correspondente:")
    print("01 Cadastrar")
    print("02 Alterar dados")
    print("03 Excluir dados")
    print("04 Apagar dados")

if menu == 0:

    elif menu == 1:
        #cadastrar: aluno, curso, Disciplina, Funcionario, professor, tecAdmin
        opcao = int (
             input(
                "Cadastrar: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
            )
        )


    elif menu == 2:
        #alterar:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
        opcao = int (
             input(
                "Alterar: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
            )
        )

    elif menu == 3:
        #excluir:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
        opcao = int (
             input(
                "Excluir: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina? "
            )
        )

    elif menu == 4:
        #consultar:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
        opcao = int (
             input(
                "Consultar: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
            )
        )
        
#cadastro
class faculdade:
    def __init__(self):
        pass
    
    if menu == 1
    def cadastro(self):
        print("\n Para realizar o cadastro, informe os dados abaixo:")
    
        self.nome = input("Digite o seu nome:")
        self.cpf = input('Digite o seu CPF:')
        self.matricula = input('Digite a sua matrícula:')
        self.curso = input('Digite o seu curso:')

        print("\n Cadastro realizado com sucesso!")
        
        ##colocar o try/except caso necessário
    
#consultar
    if menu == 4:
     def consultar(self):
        print("Qual informação gostaria de verificar?")
        print("\n 1. Funcionário\n 2. Aluno\n 3.Curso\n 4. Disciplina")
        opcao_consult = int(input("\nOpção: "))
        
        if opcao_consult == 1:
        self.nome = input("Informe o nome do funcionário:")
        ##try:
                ##c = ConexaoDB() # faz a conexão com o banco 
                ##sql = f"select * from funcionarios where CPF='{self.CPF}'" # define o que será feito na tabela funcionário
                ##c.executarDQL(sql)
                ##print("essas são as informações dos funcionários")
                ##c.desconectar()
            ##except Error as ex:
                ##print('Erro de conexão:', ex)
        print("As informações disponíveis desse funcionário, são:")
        print("Deseja consultar mais alguma informação?")
        opcao_consult = int(input("\n 1. Funcionário\n 2. Aluno\n 3.Curso\n 4. Disciplina\n 5. Voltar ao menu"))
        if opcao_consult == 1
        self.consultar()
        elif opcao_consult == 5
        self.menu()
#deletar
if menu == 3: 
    def deletar(self):
        print("O que deseja deletar?")
        print("\n 1. Funcionário\n 2. Aluno\n 3.Curso\n 4. Disciplina")
        opcao_delete = int(input("\nOpção:"))
        if opcao_delete == 4:
            print("Qual disciplina deseja deletar?")
            print("Insira o código da disciplina:")
            self.codigo = input("Código:")
#atualizar
if menu == 2:
    def atualizar(self):
        print("O que deseja atualizar?")
        print("\n 1. Funcionário\n 2. Aluno\n 3.Curso\n 4. Disciplina")
        opcao_att = int(input("Opção:"))

        if opcao_att = 1:
            self.nome = input("Digite o novo nome:")
            self.cpf = input("Informe o CPF:")




