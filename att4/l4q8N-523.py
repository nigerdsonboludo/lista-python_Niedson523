#Lista de Exercício 4 - Questão 8
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

def armazenar_informacoes_pessoas():
    try:
        idades = []
        alturas = []

        for i in range(5):
            idade = int(input(f"Digite a idade da pessoa {i+1}: "))
            altura = float(input(f"Digite a altura da pessoa {i+1}: "))

            idades.append(idade)
            alturas.append(altura)

        print("Idades na ordem inversa:")
        for idade in reversed(idades):
            print(idade)

        print("Alturas na ordem inversa:")
        for altura in reversed(alturas):
            print(altura)

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números inteiros para idade e números reais para altura.")

armazenar_informacoes_pessoas()
