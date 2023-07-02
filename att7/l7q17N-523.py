#Lista de Exercício 7 - Questão 17
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

import random


class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 100)
        self.tedio = random.randint(0, 100)

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida * 0.5

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira * 1.5

    def ouvir(self):
        print(f"{self.nome}: Estou bem!")

    def humor(self):
        if self.fome < 30 and self.tedio < 30:
            return "Feliz"
        elif self.fome >= 70 and self.tedio >= 70:
            return "Triste"
        else:
            return "Normal"


class FazendaDeBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionar_bichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentar_todos(self, quantidade_comida):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade_comida)

    def brincar_todos(self, tempo_brincadeira):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo_brincadeira)

    def ouvir_todos(self):
        for bichinho in self.bichinhos:
            bichinho.ouvir()

    def mostrar_humor_todos(self):
        for bichinho in self.bichinhos:
            print(f"{bichinho.nome}: Humor {bichinho.humor()}")


# Exemplo de uso da classe FazendaDeBichinhos

fazenda = FazendaDeBichinhos()

fazenda.adicionar_bichinho(BichinhoVirtual("Bichinho 1"))
fazenda.adicionar_bichinho(BichinhoVirtual("Bichinho 2"))
fazenda.adicionar_bichinho(BichinhoVirtual("Bichinho 3"))

fazenda.mostrar_humor_todos()

quantidade_comida = int(input("Digite a quantidade de comida fornecida para todos os bichinhos: "))
fazenda.alimentar_todos(quantidade_comida)

tempo_brincadeira = int(input("Digite o tempo de brincadeira em minutos para todos os bichinhos: "))
fazenda.brincar_todos(tempo_brincadeira)

fazenda.mostrar_humor_todos()

print("Ouvindo todos os bichinhos:")
fazenda.ouvir_todos()
