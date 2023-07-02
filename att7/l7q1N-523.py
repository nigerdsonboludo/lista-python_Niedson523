#Lista de Exercício 7 - Questão 1
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor


# Exemplo de uso da classe Bola
minha_bola = Bola("Azul", 10, "Plástico")
print("Cor da bola:", minha_bola.mostraCor())

minha_bola.trocaCor("Verde")
print("Cor da bola após troca:", minha_bola.mostraCor())
