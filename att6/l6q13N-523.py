#Lista de Exercício 6 - Questão 13
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

import random

class WordGame:
    def __init__(self, words_file):
        self.words = self.read_words(words_file)
        self.word = self.choose_word()
        self.shuffled_word = self.shuffle_word()
        self.attempts = 6

    def read_words(self, file):
        try:
            with open(file, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except Exception as e:
            print(f'Erro ao ler o arquivo: {str(e)}')
            return []

    def choose_word(self):
        return random.choice(self.words)

    def shuffle_word(self):
        shuffled_word = list(self.word)
        random.shuffle(shuffled_word)
        return ''.join(shuffled_word)

    def play(self):
        print('Jogo da Palavra Embaralhada!')
        print(f'Adivinhe a palavra embaralhada. Você tem {self.attempts} tentativas.')

        while self.attempts > 0:
            print('\n' + '-' * 30)
            print(f'Palavra embaralhada: {self.shuffled_word}')
            guess = input('Digite sua tentativa: ').upper()
            if self.check_guess(guess):
                print('Parabéns! Você acertou a palavra!')
                return

            self.attempts -= 1
            print(f'Tentativa incorreta! Você tem {self.attempts} tentativas restantes.')

        print(f'Você perdeu! A palavra era "{self.word}".')

    def check_guess(self, guess):
        if guess == self.word:
            return True
        return False


def main():
    words_file = 'palavras.txt'  # Nome do arquivo com as palavras
    game = WordGame(words_file)
    game.play()


if __name__ == '__main__':
    main()
