#Lista de Exercício 6 - Questão 11
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

import random

class HangmanGame:
    def __init__(self, words_file):
        self.words = self.read_words(words_file)
        self.word = self.choose_word()
        self.guessed_letters = []
        self.remaining_attempts = 6

    def read_words(self, file):
        try:
            with open(file, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except Exception as e:
            print(f'Erro ao ler o arquivo: {str(e)}')
            return []

    def choose_word(self):
        return random.choice(self.words)

    def play(self):
        print('Jogo da Forca!')
        print('Adivinhe a palavra antes de ser enforcado.')

        while not self.is_game_over():
            print('\n' + '-' * 30)
            self.print_hangman(self.remaining_attempts)
            self.print_word(self.guessed_letters)
            letter = self.take_guess()
            self.check_guess(letter)

        if '_' not in self.print_word(self.guessed_letters):
            print(f'\nParabéns! Você adivinhou a palavra "{self.word}" e venceu!')
        else:
            print(f'\nVocê foi enforcado! A palavra era "{self.word}".')

    def print_hangman(self, attempts):
        hangman = [
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
              ===''',
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     /
              ===''',
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |
              ===''',
            '''
               --------
               |      |
               |      O
               |     \\|
               |      |
               |
              ===''',
            '''
               --------
               |      |
               |      O
               |      |
               |      |
               |
              ===''',
            '''
               --------
               |      |
               |      O
               |    
               |      
               |
              ===''',
            '''
               --------
               |      |
               |      
               |    
               |      
               |
              ==='''
        ]
        print(hangman[6 - attempts])

    def print_word(self, guessed_letters):
        result = ''
        for letter in self.word:
            if letter in guessed_letters:
                result += letter + ' '
            else:
                result += '_ '
        print('\nA palavra é:', result.strip())
        return result

    def take_guess(self):
        while True:
            try:
                letter = input('\nDigite uma letra: ').upper()
                if len(letter) != 1 or not letter.isalpha():
                    raise ValueError
                return letter
            except ValueError:
                print('Digite apenas uma letra.')

    def check_guess(self, letter):
        if letter in self.word:
            print(f'\nA letra "{letter}" está na palavra!')
            self.guessed_letters.append(letter)
        else:
            print(f'\nA letra "{letter}" não está na palavra.')
            self.remaining_attempts -= 1
            print(f'Você errou pela {7 - self.remaining_attempts}ª vez.')

    def is_game_over(self):
        if self.remaining_attempts == 0 or '_' not in self.print_word(self.guessed_letters):
            return True
        return False


def main():
    words_file = 'palavras.txt'  # Nome do arquivo com as palavras
    game = HangmanGame(words_file)
    game.play()


if __name__ == '__main__':
    main()
