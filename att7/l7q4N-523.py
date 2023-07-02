#Lista de Exercício 7 - Questão 4
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


# Exemplo de uso da classe Pessoa
pessoa = Pessoa("João", 18, 70, 170)

print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Peso:", pessoa.peso)
print("Altura:", pessoa.altura)

pessoa.envelhecer()
print("Nova idade:", pessoa.idade)
print("Nova altura:", pessoa.altura)

pessoa.engordar(5)
print("Novo peso:", pessoa.peso)

pessoa.emagrecer(2)
print("Novo peso:", pessoa.peso)
