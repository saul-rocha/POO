from src.alunos import Alunos

class Turma:
    def __init__(self):
        self._turma = {}

    @property
    def turma(self):
        return self._turma

    ##adiciona um aluno na turma(dicionario)
    def add_aluno(self, matricula, nome, n1, n2, n3):
        a = Alunos(matricula, nome, n1, n2, n3)
        self._turma[matricula] = a
    ##encerra a turma
    def encerramento_turma(self, lista_res):

        for key, a in self._turma.items():
            lista_res.append(a.nome)
            lista_res.append(a.media())

        return 1 ## retorna 1 para confirmar a execução da função

    def listagem_alunos(self, lista_alunos, verifica):
        if(verifica):##verifica se ja foi chamada a função encerramento
            for i in range(1,len(lista_alunos),2): # laço for que incia do segundo indice e pula duas posição por loop
                print("Nome:", lista_alunos[i-1])
                print("Nota Final: ", lista_alunos[i])
            res = 1 ## res recebe um se foi encerrada antes
        else:
            res = 0 ## res recebe 0 se a turma não tiver sido encerrada

        return res ## retorna 1 se a função foi executada e 0 caso contrario

    ##retorna a nota necessária para passar na final
    def aluno_de_final(self, matricula):
        return self._turma[matricula].final()