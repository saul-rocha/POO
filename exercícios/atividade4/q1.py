from src.turma import Turma

turma = Turma()

lista_alunos = []
res = 0

def menu():
    print("1 - Adicionar Aluno\n2 - Encerrar Turma\n3 - Listar Alunos\n4 - Nota Necessária na Final\n0 - Sair")
    esc = int(input("Digite uma opção: "))

    return esc

while True:

    op = menu()
    ## adiciona um aluno na turma
    if op == 1:
        mat = int(input("Matricula: "))
        nome = (input("Nome: "))
        n1 = float(input("Nota1: "))
        n2 = float(input("Nota2: "))
        n3 = float(input("Nota3: "))
        turma.add_aluno(mat, nome, n1, n2, n3)
        """
        testes
        turma.add_aluno(1, "saul", 10, 10, 10)
        turma.add_aluno(2, "pedro", 6, 6, 6)
        turma.add_aluno(3, "sjovi", 0, 0, 0)"""

    elif op == 2:
       res = turma.encerramento_turma(lista_alunos) ## encerra a turma e atribui 1 para res
       print("Ok!")

    elif op == 3:
        if (not res): ## se res for 0, então significa que a função de encerrar turma NÃO foi executada e entao executa ela aqui
            print("turma nao encerrada!\nEncerrando...")
            res = turma.encerramento_turma(lista_alunos)
            res = turma.listagem_alunos(lista_alunos, res)
            print("Ok!")
        else: ## caso ja tenha sido executada a função de encerramento, então executa apenas a listagem
            print("listando...")
            res = turma.listagem_alunos(lista_alunos, res)
            print("Ok!")

    elif op == 4:
        matric = int(input("matricula: "))

        nota = turma.aluno_de_final(matric)
        med = turma.turma[matric].media()
        if nota != 0:
            print("Media:", med)
            print("Nota necessária:", nota)
        else:
            if med >= 7:
                print("Media:", med)
                print("Passou")
            else:
                print("Media:", med)
                print("Reprovado")
    elif op == 0:
        break




