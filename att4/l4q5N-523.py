#Lista de Exercício 4 - Questão 5
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Numeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def ler_numeros(self):
        try:
            for i in range(20):
                num = int(input(f"Digite o número {i+1}: "))
                if num % 2 == 0:
                    self.pares.append(num)
                else:
                    self.impares.append(num)

        except ValueError:
            print("Valor inválido. Certifique-se de digitar apenas números inteiros.")

    def imprimir_vetores(self):
        print("Números digitados:")
        for num in self.numeros:
            print(num)

        print("Números pares:")
        for par in self.pares:
            print(par)

        print("Números ímpares:")
        for impar in self.impares:
            print(impar)

numeros = Numeros()
numeros.ler_numeros()
numeros.imprimir_vetores()
