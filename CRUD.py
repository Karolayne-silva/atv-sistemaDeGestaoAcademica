from conexaoDB import *
from Aluno import Aluno
from Curso import Curso
from Disciplina import Disciplina
from Funcionario import *
from Professor import Professor
from TecnAdministrativo import TecnAdministrativo

########################################################################################

def menu():
  opcao = 0
  while opcao != 5:
    print("O que você deseja fazer? \n1-Cadastrar \n2-Alterar \n3-Excluir \n4-Consultar \n5-Sair\n")
    opcao = int(input("Digite o número correspondente: "))

    if opcao == 1:
      #cadastrar: aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      print("Cadastro de: \n1-Aluno \n2-Professor \n3-Curso \n4-Disciplina \n5-Técnico administrativo\n")
      opcao_cadastro = int(input("Digite o número correspondente: "))
      # Opções:
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
        codigo = input("Informe o código do curso: ")
        nome = input("Informe o nome do curso: ")
        duracao = input("Informe a duração do curso: ")
        curso = Curso(codigo, nome, duracao)
        curso.cadastrar()
        print("Curso cadastrado com sucesso!")


      elif opcao_cadastro == 4:
        # cadastrar disciplina
        codigo = input("Informe o código da disciplina: ")
        nome = input("Informe o nome da disciplina: ")
        carga_horaria = input("Informe a carga horária da disciplina: ")
        disciplina = Disciplina(codigo, nome, carga_horaria)
        disciplina.cadastrar()
        print("Disciplina cadstrada com sucesso!")


      elif opcao_cadastro ==5:
        # cadastrar técnico administrativo
        nome = input("Informe o nome do técnico: ")
        endereco = input("Informe o endereco do técnico: ")
        telefone = input("Informe o telefone do técnico: ")
        cpf = input("Informe o CPF do técnico: ")
        salario = input("Informe o salário do técnico: ")
        tecadmin = TecnAdministrativo(nome, endereco, telefone, cpf, salario)
        tecadmin._cadastrar()
        print("Técnico cadastrado com sucesso!")
      

    elif opcao == 2:
      #alterar:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_alteracao = int(input("Alterar: \n1-Aluno \n2-Professor \n3-Curso \n4-Disciplina \n5-Técnico administrativo"))
      if opcao_alteracao == 1:
        # alterar aluno
        nome = input("Informe o novo nome do aluno: ")
        cpf = input("Informe o CPF do aluno a ser alterado: ")
        aluno = Aluno(nome, cpf)
        aluno.alterar()
        print("Aluno alterado com sucesso!")


      elif opcao_alteracao == 2:
        # alterar professor
        nome = input("Informe o novo nome do professor: ")
        cpf = input("Informe o CPF do professor a ser alterado: ")
        professor = Professor(nome, cpf)
        professor._alterar()
        print("Professor alterado com sucesso!")


      elif opcao_alteracao == 3:
        # alterar curso
        nome = ("Informe o novo nome do professor: ")
        codigo = ("Informe o novo código do curso: ")
        curso = Curso(nome, codigo)
        curso.alterar()
        print("Curso alterado com sucesso!")
      

      elif opcao_alteracao == 4:
        # alterar disciplina
        codigo = ("Informe o novo código da disciplina: ")
        nome = ("Informe o novo nome da disciplina: ")
        carga_horaria = ("Informe a nova carga horária da disciplina: ")
        disciplina = Disciplina(codigo, nome, duracao)
        disciplina.alterar()
        print("Disciplina alterada com sucesso!")


      elif opcao_alteracao ==5:
        # alterar técnico administrativo
        nome = input("Informe o novo nome do nome do técnico administrativo: ")
        cpf =  input("Informe o novo CPF do técnico administrativo: ")
        tecadmin = TecnAdministrativo(nome, cpf)
        tecadmin._alterar()
        print("Técnico Administrativo alterado com sucesso!")



    elif opcao == 3:
      #excluir:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_exclusao = int(input("Excluir: \n1-Aluno \n2-Professor \n3-Curso \n4-Disciplina \n5-Técnico administrativo"))
      if opcao_exclusao == 1:
        # excluir aluno
        nome = input("Informe o nome do aluno a ser excluido: ")
        aluno = Aluno(nome)
        aluno.excluir()
        print("Aluno Excluido com sucesso!")


      elif opcao_exclusao == 2:
        # excluir professor
        cpf = input("Informe o CPF do professor que você deseja excluir: ")
        professor = Professor(cpf)
        professor._excluir()
        print("Professor excluido com sucesso!")

      elif opcao_exclusao == 3:
        # excluir curso
        nome = input("Informe o nome do curso a ser excluido: ")
        curso = Curso(nome)
        curso.excluir()
        print("Curso excluido com sucesso!")


      elif opcao_exclusao == 4:
        # excluir disciplina
        nome = input("Informe o nome da disciplina a ser excluida: ")
        disciplina = Disciplina(nome)
        disciplina.excluir()
        print("Disciplina excluida com sucesso!")


      elif opcao_exclusao == 5:
        # excluir técnico administrativo
        cpf = input("Infomre o CPF do técnico a ser excluido: ")
        tecadmin = TecnAdministrativo(cpf)
        tecadmin._alterar()
        print("Técnico administrativo excluído com sucesso!")


    elif opcao == 4:
        #consultar: aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_consultar = int(input("Consultar: \n 1-Aluno \n 2-Professor \n 3-Curso \n 4-Disciplina \n 5-Técnico administrativo"))
      if opcao_consultar ==1:
        # consultar aluno
        nome = input("Informe o nome do aluno a ser consultado: ")
        aluno = Aluno(nome)
        aluno.consultar()


      elif opcao_consultar == 2:
        # consultar professor
        cpf = input("Informe o CPF do professor a ser consultado: ")
        professor = Professor(cpf)
        professor._consultar()


      elif opcao_consultar == 3:
        # consultar curso
        nome = input("Informe o nome do curso a ser consultada: ")
        curso = Curso(nome)
        curso.consultar()


      elif opcao_consultar == 4:
        # consultar disciplina
        nome = input("Informe o nome da disciplina a ser consultada: ")
        disciplina = Disciplina(nome)
        disciplina.consultar()
        

      elif opcao_consultar == 5:
        # consultar técnico administrativo
        cpf = input("Informe o CPF do técnico administrativo: ")
        tecadmin = TecnAdministrativo(cpf)
        tecadmin._alterar()


menu()



########################################################################################
