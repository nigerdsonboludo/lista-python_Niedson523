#Lista de Exercício 4 - Questão 11
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Vetor:
    def __init__(self):
        self.elementos = []

    def adicionar_elemento(self, elemento):
        self.elementos.append(elemento)

    def intercalar_vetores(self, vetor2, vetor3):
        vetor_intercalado = Vetor()
        for i in range(len(self.elementos)):
            vetor_intercalado.adicionar_elemento(self.elementos[i])
            vetor_intercalado.adicionar_elemento(vetor2.elementos[i])
            vetor_intercalado.adicionar_elemento(vetor3.elementos[i])
        return vetor_intercalado

def intercalar_tres_vetores():
    try:
        vetor1 = Vetor()
        vetor2 = Vetor()
        vetor3 = Vetor()

        for i in range(10):
            num1 = int(input(f"Digite o número {i+1} do primeiro vetor: "))
            vetor1.adicionar_elemento(num1)

        for i in range(10):
            num2 = int(input(f"Digite o número {i+1} do segundo vetor: "))
            vetor2.adicionar_elemento(num2)

        for i in range(10):
            num3 = int(input(f"Digite o número {i+1} do terceiro vetor: "))
            vetor3.adicionar_elemento(num3)

        vetor_intercalado = vetor1.intercalar_vetores(vetor2, vetor3)

        print("Vetor intercalado:")
        for elemento in vetor_intercalado.elementos:
            print(elemento)

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números inteiros.")

intercalar_tres_vetores()
