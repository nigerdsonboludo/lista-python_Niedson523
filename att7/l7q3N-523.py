#Lista de Exercício 7 - Questão 3
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornarLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)


# Exemplo de uso da classe Retangulo
ladoA = float(input("Informe o valor do lado A: "))
ladoB = float(input("Informe o valor do lado B: "))

meu_retangulo = Retangulo(ladoA, ladoB)

area = meu_retangulo.calcularArea()
perimetro = meu_retangulo.calcularPerimetro()

print("Área do retângulo:", area)
print("Perímetro do retângulo:", perimetro)

# Considerando um piso retangular de dimensões 0.5m x 0.5m
quantidade_pisos = area / (0.5 * 0.5)
quantidade_rodapes = 2 * (ladoA + ladoB)

print("Quantidade de pisos necessários:", quantidade_pisos)
print("Quantidade de rodapés necessários:", quantidade_rodapes)
