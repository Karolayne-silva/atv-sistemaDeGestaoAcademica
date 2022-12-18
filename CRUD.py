from conexaoDB import ConexaoDB
from Aluno import Aluno
from Curso import Curso
from Disciplina import Disciplina
from Funcionario import Funcionario
from Professor import Professor
from TecnAdministrativo import TecnAdministrativo


def menu():

    print("o que você deseja fazer? /n digite o número correspondente:")
    input("1-Cadastrar /n 2-Alterar /n 3-Excluir /n 4-Consultar")



    if menu == 0:
        #cadastrar: aluno, curso, Disciplina, Funcionario, professor, tecAdmin
        opcao = int (
             input(
                "Cadastrar: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
            )
        )


    if menu == 1:
        #alterar:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
        opcao = int (
             input(
                "Alterar: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
            )
        )

    if menu == 2:
        #excluir:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
        opcao = int (
             input(
                "Excluir: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina? "
            )
        )

    if menu == 3:
        #consultar:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
        opcao = int (
             input(
                "Consultar: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
            )
        )
        
#cadastro
#class faculdade:
#    def __init__(self):
#        pass
    a = Aluno()
########################################################################################

def menu():
  opcao = 0
  while opcao != 5:
    print("o que você deseja fazer? /n digite o número correspondente:")
    print("1-Cadastrar /n 2-Alterar /n 3-Excluir /n 4-Consultar /n 5-Sair")
    opcao = int(input())

    if opcao == 1:
      #cadastrar: aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_cadastro = int (
        input(
          "Cadastrar: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
        )
      )
      if opcao_cadastro == 1:
        # cadastrar aluno
        nome = input("Informe o nome do aluno: ")
        matricula = input("Informe a matrícula do aluno: ")
        cpf = input("Informe o CPF do aluno: ")
        curso = input("Informe o curso do aluno: ")
        aluno = Aluno(nome, matricula, cpf, curso)
        aluno.cadastrar()
        print("Aluno cadastrado com sucesso!")



      elif opcao_cadastro == 2:
        # cadastrar professor
        nome = input("Informe o nome do professor: ")
        endereco = input("Informe o endereco do  professor: ")
        telefone = input("Informe o telefone do professor: ")
        cpf = input("Informe o CPF do professor: ")
        salario = input("Informe o salário do professor: ")
        titulacao = input("Informe a titulação do professor: ")
        area_formacao = input("Informe a área de formação do professor: ")
        professor = Professor(nome, endereco, telefone, cpf, salario, titulacao, area_formacao)
        professor._cadastrar()
        print("Professor cadastrado com sucesso!")

      elif opcao_cadastro == 3:
        # cadastrar curso
        codigo =
        nome =
        duracao =
        curso = Curso(codigo, nome, duracao)
        curso.cadastrar()
        print("Curso cadastrado com sucesso!")


      elif opcao_cadastro == 4:
        # cadastrar disciplina
        codigo =
        nome =
        carga_horaria = 
        disciplina = Disciplina
        disciplina.cadastrar(codigo, nome, duracao)
        print("Disciplina cadstrada com sucesso!")


      elif opcao_cadastro ==5:
        # cadastrar funcionario



      

    elif opcao == 2:
      #alterar:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_alteracao = int (
        input(
          "Alterar: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
        )
      )
      if opcao_alteracao == 1:
        # alterar aluno
        cpf = input("Informe o CPF do aluno a ser alterado: ")
        nome = input("Informe o novo nome do aluno: ")
        aluno = Aluno(nome, "", cpf, "")
        aluno.alterar(nome, cpf)
        print("Aluno alterado com sucesso!")


      elif opcao_alteracao == 2:
        # alterar professor
        nome = input("Informe o novo nome do professor: ")
        cpf = input("Informe o CPF do professor a ser alterado: ")
        professor = Professor
        professor._alterar(nome, cpf)
        print("Professor alterado com sucesso!")


      elif opcao_alteracao == 3:
        # alterar curso
        nome = ("Informe o novo nome do professor: ")
        codigo = ("Informe o novo código do curso: ")
        curso = Curso
        curso.alterar(nome, codigo)
        print("Curso alterado com sucesso!")
      



      elif opcao_alteracao == 4:
        # alterar disciplina
        codigo = ("Informe o novo código da disciplina: ")
        nome = ("Informe o novo nome da disciplina: ")
        carga_horaria = ("Informe a nova carga horária da disciplina: ")
        disciplina = Disciplina
        disciplina.alterar(codigo, nome, duracao)
        print("Disciplina alterada com sucesso!")


      elif opcao_alteracao ==5:
        # alterar funcionario








    elif opcao == 3:
      #excluir:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_exclusao = int (
        input(
          "Excluir: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
        )
      )
      if opcao_exclusao == 1:
        # excluir aluno
        nome = input("Informe o nome do aluno a ser excluido: ")
        aluno = Aluno(nome)
        aluno._excluir(nome)
        print("Aluno Excluido com sucesso!")


        elif opcao_exclusao == 2:
        # excluir professor
        cpf = input("Informe o CPF do professor que você deseja excluir: ")
        professor = Professor
        professor._excluir(cpf)
        print("Professor excluido com sucesso!")

        elif opcao_exclusao == 2:
        # excluir curso
        nome = input("Informe o nome do curso a ser excluido: ")
        curso = Curso
        curso.excluir(nome)
        print("Curso excluido com sucesso!")



        elif opcao_exclusao == 3:
        # excluir disciplina
        nome = 
        disciplina = Disciplina
        disciplina.excluir()
        print("Disciplina excluida com sucesso!")



        elif opcao_exclusao == 4:
        # excluir funcionário





    elif opcao == 4:
        #consultar: aluno, curso, Disciplina, Funcionario, professor, tecAdmin
        opcao_consultar = int (
            input(
                "Consultar: /n 1-Aluno /n 2-Professor /n 3-Curso /n 4-Disciplina "
            )
        )
        if opcao_consultar ==1:
        # consultar aluno
        nome = input("Informe o nome do aluno a ser consultado: ")
        aluno = Aluno(nome)
        aluno.consultar(nome)
        print("eh isto")


        elif opcao_consultar == 2:
        # consultar professor
        cpf = input("Informe o CPF do professor a ser consultado: ")
        professor._consultar(cpf)
        print("hola")





        elif opcao_consultar == 3:
        # consultar curso
        nome = input("Informe o nome do curso a ser consultada: ")
        curso = Curso
        curso.consultar(nome)
        print("rs")



        elif opcao_consultar == 4:
        # consultar disciplina
        nome = input("Informe o nome da disciplina a ser consultada: ")
        disciplina = Disciplina
        disciplina.consultar(nome)
        print("hehe")









########################################################################################






    if opcao == 1
    def cadastro(self):
        print("\n Para realizar o cadastro, informe os dados abaixo:")
    
        self.nome = input("Digite o seu nome:")
        self.cpf = input('Digite o seu CPF:')
        self.matricula = input('Digite a sua matrícula:')
        self.curso = input('Digite o seu curso:')

        print("\n Cadastro realizado com sucesso!")
        
        ##colocar o try/except caso necessário
    
#consultar
    if opcao == 2:
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
if opcaou == 3: 
    def deletar(self):
        print("O que deseja deletar?")
        print("\n 1. Funcionário\n 2. Aluno\n 3.Curso\n 4. Disciplina")
        opcao_delete = int(input("\nOpção:"))
        if opcao_delete == 4:
            print("Qual disciplina deseja deletar?")
            print("Insira o código da disciplina:")
            self.codigo = input("Código:")
#atualizar
if opcao == 2:
    def atualizar(self):
        print("O que deseja atualizar?")
        print("\n 1. Funcionário\n 2. Aluno\n 3.Curso\n 4. Disciplina")
        opcao_att = int(input("Opção:"))

        if opcao_att = 1:
            self.nome = input("Digite o novo nome:")
            self.cpf = input("Informe o CPF:")




