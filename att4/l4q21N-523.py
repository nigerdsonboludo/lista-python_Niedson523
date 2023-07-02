#Lista de Exercício 4 - Questão 21
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Carro:
    def __init__(self, modelo, consumo):
        self.modelo = modelo
        self.consumo = consumo

    def calcular_combustivel(self, distancia):
        litros = distancia / self.consumo
        return litros

    def calcular_custo(self, litros, preco_combustivel):
        custo = litros * preco_combustivel
        return custo

    def exibir_dados(self, distancia, preco_combustivel):
        litros = self.calcular_combustivel(distancia)
        custo = self.calcular_custo(litros, preco_combustivel)

        print(f"{self.modelo} - {self.consumo:.1f} km por litro")
        print(f"{litros:.1f} litros - R$ {custo:.2f}")


def obter_dados_carros():
    carros = []

    for i in range(5):
        print(f"Veículo {i+1}")
        modelo = input("Nome: ")
        consumo = float(input("Km por litro: "))

        carro = Carro(modelo, consumo)
        carros.append(carro)

    return carros


def encontrar_menor_consumo(carros):
    menor_consumo = float("inf")
    modelo_menor_consumo = ""

    for carro in carros:
        if carro.consumo < menor_consumo:
            menor_consumo = carro.consumo
            modelo_menor_consumo = carro.modelo

    return modelo_menor_consumo


def exibir_relatorio_final(carros, distancia, preco_combustivel):
    print("\nRelatório Final")

    for i, carro in enumerate(carros):
        litros = carro.calcular_combustivel(distancia)
        custo = carro.calcular_custo(litros, preco_combustivel)

        print(f"{i+1} - {carro.modelo:<15} - {carro.consumo:>5.1f} - {litros:>8.1f} litros - R$ {custo:>7.2f}")

    modelo_menor_consumo = encontrar_menor_consumo(carros)
    print(f"\nO menor consumo é do {modelo_menor_consumo}.")


carros = obter_dados_carros()
distancia = 1000
preco_combustivel = 2.25

print("\nComparativo de Consumo de Combustível")
exibir_relatorio_final(carros, distancia, preco_combustivel)
