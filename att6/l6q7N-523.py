#Lista de Exercício 6 - Questão 7
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class StringAnalyzer:
    def __init__(self, phrase):
        self.phrase = phrase

    def count_spaces(self):
        try:
            space_count = self.phrase.count(' ')
            print(f'Quantidade de espaços em branco: {space_count}')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

    def count_vowels(self):
        try:
            vowels = ['a', 'e', 'i', 'o', 'u']
            vowel_count = 0
            for char in self.phrase.lower():
                if char in vowels:
                    vowel_count += 1
            print(f'Quantidade de vogais (a, e, i, o, u): {vowel_count}')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    phrase = input('Digite uma frase: ')

    analyzer = StringAnalyzer(phrase)
    analyzer.count_spaces()
    analyzer.count_vowels()


if __name__ == '__main__':
    main()
