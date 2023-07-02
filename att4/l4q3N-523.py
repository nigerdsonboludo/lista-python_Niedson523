#Lista de Exercício 4 - Questão 3
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

def calcular_media_notas():
    try:
        notas = []
        for i in range(4):
            nota = float(input(f"Digite a nota {i+1}: "))
            notas.append(nota)

        soma = sum(notas)
        media = soma / len(notas)

        print("Notas digitadas:")
        for nota in notas:
            print(nota)
        print("Média:", media)

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números reais.")

calcular_media_notas()
