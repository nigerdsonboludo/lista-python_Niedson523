#Lista de Exercício 4 - Questão 12
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Aluno:
    def __init__(self, idade, altura):
        self.idade = idade
        self.altura = altura

def contar_alunos_altura_inferior_media(alunos):
    if len(alunos) == 0:
        return 0

    soma_alturas = sum(aluno.altura for aluno in alunos)
    media_alturas = soma_alturas / len(alunos)

    count = 0
    for aluno in alunos:
        if aluno.idade > 13 and aluno.altura < media_alturas:
            count += 1

    return count

def calcular_alunos_altura_inferior_media():
    try:
        alunos = []

        for i in range(30):
            idade = int(input(f"Digite a idade do aluno {i+1}: "))
            altura = float(input(f"Digite a altura do aluno {i+1}: "))
            aluno = Aluno(idade, altura)
            alunos.append(aluno)

        count = contar_alunos_altura_inferior_media(alunos)
        print("Número de alunos com mais de 13 anos e altura inferior à média:", count)

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números inteiros para idade e números reais para altura.")

calcular_alunos_altura_inferior_media()
