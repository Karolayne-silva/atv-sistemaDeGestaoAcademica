from conexaoDB import *
from Aluno import *
from Curso import *
from Disciplina import *
from Funcionario import *
from Professor import *
from TecnAdministrativo import *

########################################################################################

def menu():
  opcao = 0
  while opcao != 5:
    print("o que você deseja fazer? \n digite o número correspondente:")
    opcao = int(input("1-Cadastrar \n 2-Alterar \n 3-Excluir \n 4-Consultar \n 5-Sair"))

    if opcao == 1:
      #cadastrar: aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_cadastro = int(input("Cadastrar: \n 1-Aluno \n 2-Professor \n 3-Curso \n 4-Disciplina \n 5-Técnico administrativo"))
      if opcao_cadastro == 1:
        # cadastrar aluno
        nome = input("Informe o nome do aluno: ")
        matricula = input("Informe a matrícula do aluno: ")
        cpf = input("Informe o CPF do aluno: ")
        curso = input("Informe o curso do aluno: ")
        aluno = Aluno
        aluno.cadastrar(nome, matricula, cpf, curso)
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
        professor = Professor
        professor._cadastrar(nome, endereco, telefone, cpf, salario, titulacao, area_formacao)
        print("Professor cadastrado com sucesso!")


      elif opcao_cadastro == 3:
        # cadastrar curso
        codigo = input("Informe o código do curso: ")
        nome = input("Informe o nome do curso: ")
        duracao = input("Informe a duração do curso: ")
        curso = Curso
        curso.cadastrar(codigo, nome, duracao)
        print("Curso cadastrado com sucesso!")


      elif opcao_cadastro == 4:
        # cadastrar disciplina
        codigo = input("Informe o código da disciplina: ")
        nome = input("Informe o nome da disciplina: ")
        carga_horaria = input("Informe a carga horária da disciplina: ")
        disciplina = Disciplina
        disciplina.cadastrar(codigo, nome, carga_horaria)
        print("Disciplina cadstrada com sucesso!")


      elif opcao_cadastro ==5:
        # cadastrar técnico administrativo
        nome = input("Informe o nome do técnico: ")
        endereco = input("Informe o endereco do técnico: ")
        telefone = input("Informe o telefone do técnico: ")
        cpf = input("Informe o CPF do técnico: ")
        salario = input("Informe o salário do técnico: ")
        tecadmin = TecnAdministrativo
        tecadmin._cadastrar(nome, endereco, telefone, cpf, salario)
        print("Técnico cadastrado com sucesso!")
      

    elif opcao == 2:
      #alterar:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_alteracao = int(input("Alterar: \n 1-Aluno \n 2-Professor \n 3-Curso \n 4-Disciplina \n 5-Técnico administrativo"))
      if opcao_alteracao == 1:
        # alterar aluno
        nome = input("Informe o novo nome do aluno: ")
        cpf = input("Informe o CPF do aluno a ser alterado: ")
        aluno = Aluno
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
        # alterar técnico administrativo
        nome = input("Informe o novo nome do nome do técnico administrativo: ")
        cpf =  input("Informe o novo CPF do técnico administrativo: ")
        tecadmin = TecnAdministrativo
        tecadmin._alterar(nome, cpf)
        print("Técnico Administrativo alterado com sucesso!")



    elif opcao == 3:
      #excluir:  aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_exclusao = int(input("Excluir: \n 1-Aluno \n 2-Professor \n 3-Curso \n 4-Disciplina \n 5-Técnico administrativo"))
      if opcao_exclusao == 1:
        # excluir aluno
        nome = input("Informe o nome do aluno a ser excluido: ")
        aluno = Aluno
        aluno.excluir(nome)
        print("Aluno Excluido com sucesso!")


      elif opcao_exclusao == 2:
        # excluir professor
        cpf = input("Informe o CPF do professor que você deseja excluir: ")
        professor = Professor
        professor._excluir(cpf)
        print("Professor excluido com sucesso!")

      elif opcao_exclusao == 3:
        # excluir curso
        nome = input("Informe o nome do curso a ser excluido: ")
        curso = Curso
        curso.excluir(nome)
        print("Curso excluido com sucesso!")


      elif opcao_exclusao == 4:
        # excluir disciplina
        nome = input("Informe o nome da disciplina a ser excluida: ")
        disciplina = Disciplina
        disciplina.excluir(nome)
        print("Disciplina excluida com sucesso!")


      elif opcao_exclusao == 5:
        # excluir técnico administrativo
        cpf = input("Infomre o CPF do técnico a ser excluido: ")
        tecadmin = TecnAdministrativo
        tecadmin._alterar(cpf)
        print("Técnico administrativo excluído com sucesso!")


    elif opcao == 4:
        #consultar: aluno, curso, Disciplina, Funcionario, professor, tecAdmin
      opcao_consultar = int(input("Consultar: \n 1-Aluno \n 2-Professor \n 3-Curso \n 4-Disciplina \n 5-Técnico administrativo"))
      if opcao_consultar ==1:
        # consultar aluno
        nome = input("Informe o nome do aluno a ser consultado: ")
        aluno = Aluno
        aluno.consultar(nome)


      elif opcao_consultar == 2:
        # consultar professor
        cpf = input("Informe o CPF do professor a ser consultado: ")
        professor._consultar(cpf)


      elif opcao_consultar == 3:
        # consultar curso
        nome = input("Informe o nome do curso a ser consultada: ")
        curso = Curso
        curso.consultar(nome)


      elif opcao_consultar == 4:
        # consultar disciplina
        nome = input("Informe o nome da disciplina a ser consultada: ")
        disciplina = Disciplina
        disciplina.consultar(nome)
        

      elif opcao_consultar == 5:
        # consultar técnico administrativo
        cpf = input("Informe o CPF do técnico administrativo: ")
        tecadmin = TecnAdministrativo
        tecadmin._alterar(cpf)






########################################################################################
