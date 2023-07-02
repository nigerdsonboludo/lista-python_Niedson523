#Lista de Exercício 4 - Questão 17
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []

    def adicionar_salto(self, distancia):
        self.saltos.append(distancia)

    def calcular_media_saltos(self):
        if len(self.saltos) == 0:
            return 0

        return sum(self.saltos) / len(self.saltos)


def ler_distancias(atleta):
    print(f"Atleta: {atleta.nome}")

    for i in range(1, 6):
        try:
            distancia = float(input(f"{i}º Salto: "))
            atleta.adicionar_salto(distancia)
        except ValueError:
            print("Valor inválido. Digite apenas números.")

    print("\nResultado final:")
    print(f"Atleta: {atleta.nome}")
    print(f"Saltos: {' - '.join(str(salto) for salto in atleta.saltos)}")
    print(f"Média dos saltos: {atleta.calcular_media_saltos()} m.")


def main():
    while True:
        nome = input("Digite o nome do atleta (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break

        atleta = Atleta(nome)
        ler_distancias(atleta)


main()
