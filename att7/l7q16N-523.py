#Lista de Exercício 7 - Questão 16
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida * 0.5

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira * 1.5

    def humor(self):
        if self.fome < 30 and self.tedio < 30:
            return "Feliz"
        elif self.fome >= 70 and self.tedio >= 70:
            return "Triste"
        else:
            return "Normal"

    def __str__(self):
        return f"Bichinho: {self.nome}\nFome: {self.fome}\nTédio: {self.tedio}"


# Exemplo de uso da classe BichinhoVirtual
nome_bichinho = input("Digite o nome do seu bichinho virtual: ")
bichinho = BichinhoVirtual(nome_bichinho)

print("Humor:", bichinho.humor())

quantidade_comida = int(input("Digite a quantidade de comida fornecida: "))
bichinho.alimentar(quantidade_comida)

tempo_brincadeira = int(input("Digite o tempo de brincadeira em minutos: "))
bichinho.brincar(tempo_brincadeira)

print("Humor após alimentar e brincar:", bichinho.humor())

opcao_secreta = input("Digite a opção secreta para mostrar os valores exatos do bichinho (digite 'sair' para sair): ")

if opcao_secreta == "mostrar":
    print(bichinho)
elif opcao_secreta == "sair":
    print("Saindo...")
else:
    print("Opção inválida!")
