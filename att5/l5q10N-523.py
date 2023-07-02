#Lista de Exercício 5 - Questão 10
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

import random

class Craps:
    def __init__(self):
        self.ponto = None

    def lancarDados(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return dado1 + dado2

    def jogar(self):
        try:
            primeira_jogada = self.lancarDados()

            if primeira_jogada == 7 or primeira_jogada == 11:
                print(f"Você tirou {primeira_jogada}. Parabéns, você ganhou!")
                return
            elif primeira_jogada == 2 or primeira_jogada == 3 or primeira_jogada == 12:
                print(f"Você tirou {primeira_jogada}. Que pena, você perdeu!")
                return

            self.ponto = primeira_jogada
            print(f"Seu Ponto é {self.ponto}. Continue jogando até tirar {self.ponto} novamente ou um 7.")

            while True:
                jogada = self.lancarDados()

                if jogada == self.ponto:
                    print(f"Você tirou {jogada}. Parabéns, você ganhou!")
                    return
                elif jogada == 7:
                    print(f"Você tirou {jogada}. Que pena, você perdeu!")
                    return
        except Exception as e:
            raise ValueError(f"Erro ao jogar Craps: {str(e)}")


try:
    jogo = Craps()
    jogo.jogar()
except ValueError as e:
    print(f"Erro: {str(e)}")
