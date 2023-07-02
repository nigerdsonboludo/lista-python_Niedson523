#Lista de Exercício 4 - Questão 6
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) > 0:
            soma = sum(self.notas)
            media = soma / len(self.notas)
            return media
        else:
            return 0

def contar_alunos_aprovados():
    try:
        alunos = []
        num_alunos_aprovados = 0

        for i in range(10):
            nome = input(f"Digite o nome do aluno {i+1}: ")
            aluno = Aluno(nome)

            for j in range(4):
                nota = float(input(f"Digite a nota {j+1} do aluno {aluno.nome}: "))
                aluno.adicionar_nota(nota)

            media = aluno.calcular_media()
            if media >= 7.0:
                num_alunos_aprovados += 1

            alunos.append(aluno)

        print("Número de alunos com média maior ou igual a 7.0:", num_alunos_aprovados)

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números reais.")

contar_alunos_aprovados()
