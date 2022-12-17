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


#bota aq
def cad(nome, matricula, cpf, curso):

def cad(nome, curso, matricula)
print(nome, curso, matricula) 
cad('digite o nome', 'digite curso', 'digite matricula')




    menu == 1:
            # CADASTRO
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite sua matricula: ")
            cpf = input("Digite o seu cpf: ")
            curso = input("Digite o seu curso: ")
            aluno = Aluno(nome, matricula, cpf, curso)
            aluno.cadastrar()

def alt():

def exc():

def con():


# todo o codígo de CRUD 
# create
##aluno/funcionario
#read
##
#update
##atualizar cadeira/salario/matricula 
#delete
##deletar uma cadeira/aluno/funcionario

##nome = input("Digite o nome do(a) aluno(a):")
##matricula = input("Digite a matrícula do(a) aluno(a)")
##cpf = input("Digite o seu CPF:")
##curso = input("Digite o curso que está matriculado:")

/* def __init__(self):
        pass 
    
    def read(self):
        print("Escolha uma das opções para visualizar\n")
        print("\n 1 - Funcionários\n 2 - Aluno\n 3 - Curso\n 4 - Disciplina")
        escolha2 = int(input("\nEscolha: "))*/