#Lista de Exercício 5 - Questão 1
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

def imprimir_padrao(n):
    if n < 1:
        raise ValueError("O valor de n deve ser pelo menos 1")

    for i in range(1, n+1):
        linha = [str(i)] * i
        print("   ".join(linha))


try:
    valor_n = int(input("Digite o valor de n: "))
    imprimir_padrao(valor_n)

except ValueError:
    print("Erro: o valor informado deve ser um número inteiro positivo.")
