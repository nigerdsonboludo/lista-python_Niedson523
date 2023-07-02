#Lista de Exercício 4 - Questão 2
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

def ler_vetor_reverso():
    try:
        vetor = []
        for i in range(10):
            num = float(input(f"Digite o número {i+1}: "))
            vetor.append(num)

        vetor_reverso = vetor[::-1]  # Inverte a ordem do vetor

        print("Números na ordem inversa:")
        for num in vetor_reverso:
            print(num)

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números reais.")

ler_vetor_reverso()
