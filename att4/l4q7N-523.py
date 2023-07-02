#Lista de Exercício 4 - Questão 7
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo 

def realizar_operacoes_vetor():
    try:
        vetor = []
        for i in range(5):
            num = int(input(f"Digite o número {i+1}: "))
            vetor.append(num)

        soma = sum(vetor)
        multiplicacao = 1
        for num in vetor:
            multiplicacao *= num

        print("Números digitados:")
        for num in vetor:
            print(num)
        print("Soma:", soma)
        print("Multiplicação:", multiplicacao)

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números inteiros.")

realizar_operacoes_vetor()
