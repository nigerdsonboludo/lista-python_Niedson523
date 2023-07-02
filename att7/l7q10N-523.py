#Lista de Exercício 7 - Questão 10
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}.")
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecer_por_litro(self, litros):
        valor_a_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            print(f"Valor a ser pago: R${valor_a_pagar:.2f}")
        else:
            print("Não há combustível suficiente na bomba.")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade


# Exemplo de utilização da classe BombaCombustivel
bomba = BombaCombustivel("Gasolina", 4.99, 1000)

# Abastecer por valor
bomba.abastecer_por_valor(50)  # Abastecer R$ 50
# Saída: Foram abastecidos 10.02 litros de Gasolina.

# Abastecer por litro
bomba.abastecer_por_litro(30)  # Abastecer 30 litros
# Saída: Valor a ser pago: R$ 149.70

# Alterar valor do litro
bomba.alterar_valor(5.10)  # Valor do litro de Gasolina alterado para R$ 5.10

# Alterar combustível
bomba.alterar_combustivel("Etanol")  # Tipo de combustível alterado para Etanol

# Alterar quantidade de combustível
bomba.alterar_quantidade_combustivel(800)  # Quantidade de combustível restante na bomba alterada para 800 litros
