#Lista de Exercício 4 - Questão 1
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Vetor:
    def ler_vetor(self):
        vetor = []
        for i in range(5):
            try:
                numero = int(input("Digite um número inteiro: "))
                vetor.append(numero)
            except ValueError:
                print("Valor inválido. Digite um número inteiro válido.")
                return
        return vetor

    def mostrar_vetor(self, vetor):
        for numero in vetor:
            print(numero)

vetor_objeto = Vetor()
vetor_numeros = vetor_objeto.ler_vetor()
vetor_objeto.mostrar_vetor(vetor_numeros)
