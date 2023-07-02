#Lista de Exercício 7 - Questão 11
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print(f"O carro percorreu {distancia} quilômetros.")
        else:
            print("Não há combustível suficiente para percorrer essa distância.")

    def obter_gasolina(self):
        return self.combustivel

    def adicionar_gasolina(self, quantidade):
        self.combustivel += quantidade


# Exemplo de uso da classe Carro
meuFusca = Carro(15)  # Consumo de 15 km/l

meuFusca.adicionar_gasolina(20)  # Abastecer com 20 litros de combustível

meuFusca.andar(100)  # Andar 100 km
# Saída: O carro percorreu 100 quilômetros.

gasolina_restante = meuFusca.obter_gasolina()
print(f"Combustível restante: {gasolina_restante} litros")
# Saída: Combustível restante: 13.333333333333334 litros
