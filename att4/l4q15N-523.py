#Lista de Exercício 4 - Questão 15
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Notas:
    def __init__(self):
        self.valores = []

    def adicionar_valor(self, valor):
        self.valores.append(valor)

    def quantidade_valores_lidos(self):
        return len(self.valores)

    def mostrar_valores(self):
        for valor in self.valores:
            print(valor, end=" ")
        print()

    def mostrar_valores_inverso(self):
        for valor in reversed(self.valores):
            print(valor)

    def calcular_soma(self):
        return sum(self.valores)

    def calcular_media(self):
        return sum(self.valores) / len(self.valores)

    def quantidade_valores_acima_media(self):
        media = self.calcular_media()
        return sum(valor > media for valor in self.valores)

    def quantidade_valores_abaixo_sete(self):
        return sum(valor < 7 for valor in self.valores)


def realizar_operacoes_notas():
    try:
        notas = Notas()

        while True:
            valor = float(input("Digite um valor de nota (ou -1 para encerrar): "))
            if valor == -1:
                break
            notas.adicionar_valor(valor)

        print("Quantidade de valores lidos:", notas.quantidade_valores_lidos())
        print("Valores informados:", end=" ")
        notas.mostrar_valores()
        print("Valores em ordem inversa:")
        notas.mostrar_valores_inverso()
        print("Soma dos valores:", notas.calcular_soma())
        print("Média dos valores:", notas.calcular_media())
        print("Quantidade de valores acima da média:", notas.quantidade_valores_acima_media())
        print("Quantidade de valores abaixo de sete:", notas.quantidade_valores_abaixo_sete())
        print("Programa encerrado.")

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números.")

realizar_operacoes_notas()
