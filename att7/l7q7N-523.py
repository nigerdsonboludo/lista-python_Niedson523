#Lista de Exercício 7 - Questão 7
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, novo_valor):
        self.fome = novo_valor

    def alterar_saude(self, novo_valor):
        self.saude = novo_valor

    def alterar_idade(self, novo_valor):
        self.idade = novo_valor

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_humor(self):
        humor = self.fome + self.saude
        return humor


# Exemplo de uso da classe BichinhoVirtual
bichinho = BichinhoVirtual("Tama")

print("Nome:", bichinho.retornar_nome())
print("Fome:", bichinho.retornar_fome())
print("Saúde:", bichinho.retornar_saude())
print("Idade:", bichinho.retornar_idade())
print("Humor:", bichinho.retornar_humor())

bichinho.alterar_nome("Tama Jr.")
bichinho.alterar_fome(10)
bichinho.alterar_saude(90)
bichinho.alterar_idade(1)

print("Nome:", bichinho.retornar_nome())
print("Fome:", bichinho.retornar_fome())
print("Saúde:", bichinho.retornar_saude())
print("Idade:", bichinho.retornar_idade())
print("Humor:", bichinho.retornar_humor())
