#Lista de Exercício 4 - Questão 4
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

def contar_consoantes():
    consoantes = []
    try:
        vetor = []
        for i in range(10):
            char = input(f"Digite o caractere {i+1}: ")
            vetor.append(char)

        for char in vetor:
            if char.isalpha() and char.lower() not in 'aeiou':
                consoantes.append(char)

        print("Consoantes lidas:")
        for consoante in consoantes:
            print(consoante)

        print("Total de consoantes:", len(consoantes))

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas caracteres.")

contar_consoantes()
