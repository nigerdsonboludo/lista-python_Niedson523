#Lista de Exercício 4 - Questão 9
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Vetor:
    def __init__(self):
        self.elementos = []

    def adicionar_elemento(self, elemento):
        self.elementos.append(elemento)

    def calcular_soma_quadrados(self):
        soma = 0
        for elemento in self.elementos:
            soma += elemento ** 2
        return soma

def calcular_soma_quadrados_vetor():
    try:
        vetor = Vetor()

        for i in range(10):
            num = int(input(f"Digite o número {i+1}: "))
            vetor.adicionar_elemento(num)

        soma_quadrados = vetor.calcular_soma_quadrados()

        print("Soma dos quadrados dos elementos do vetor:", soma_quadrados)

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números inteiros.")

calcular_soma_quadrados_vetor()
