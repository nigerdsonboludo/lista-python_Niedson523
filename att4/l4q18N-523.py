#Lista de Exercício 4 - Questão 18
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Enquete:
    def __init__(self):
        self.votos = [0] * 23

    def registrar_voto(self, jogador):
        if jogador >= 1 and jogador <= 23:
            self.votos[jogador-1] += 1
        else:
            print("Número de jogador inválido. Tente novamente.")

    def calcular_percentual(self, votos_jogador, total_votos):
        return (votos_jogador / total_votos) * 100

    def exibir_resultados(self):
        total_votos = sum(self.votos)

        print(f"Foram computados {total_votos} votos.")
        print()
        print("Jogador   Votos   %")
        print("--------------------")
        
        for jogador, votos_jogador in enumerate(self.votos):
            if votos_jogador > 0:
                percentual = self.calcular_percentual(votos_jogador, total_votos)
                print(f"{jogador+1:<9}{votos_jogador:<8}{percentual:.1f}%")

        melhor_jogador = self.votos.index(max(self.votos)) + 1
        votos_melhor_jogador = self.votos[melhor_jogador-1]
        percentual_melhor_jogador = self.calcular_percentual(votos_melhor_jogador, total_votos)

        print()
        print(f"O melhor jogador foi o número {melhor_jogador}, com {votos_melhor_jogador} votos, correspondendo a {percentual_melhor_jogador:.1f}% do total de votos.")


enquete = Enquete()

print("Enquete: Quem foi o melhor jogador?")
print("Número do jogador (0=fim): ")
jogador = int(input())

while jogador != 0:
    enquete.registrar_voto(jogador)
    print("Número do jogador (0=fim): ")
    jogador = int(input())

enquete.exibir_resultados()
