#Lista de Exercício 6 - Questão 8
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class PalindromeChecker:
    def __init__(self, sequence):
        self.sequence = sequence

    def is_palindrome(self):
        try:
            # Remove espaços e pontuação da sequência
            cleaned_sequence = ''.join(e.lower() for e in self.sequence if e.isalnum())

            # Verifica se a sequência é igual à sua inversão
            if cleaned_sequence == cleaned_sequence[::-1]:
                print(f'A sequência "{self.sequence}" é um palíndromo.')
            else:
                print(f'A sequência "{self.sequence}" não é um palíndromo.')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    sequence = input('Digite uma sequência de caracteres: ')

    checker = PalindromeChecker(sequence)
    checker.is_palindrome()


if __name__ == '__main__':
    main()
