#Lista de Exercício 6 - Questão 1
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class StringComparator:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def compare_strings(self):
        try:
            len1 = len(self.string1)
            len2 = len(self.string2)
            content_equal = self.string1 == self.string2

            print(f'String 1: {self.string1}\nTamanho de "{self.string1}": {len1} caracteres')
            print(f'String 2: {self.string2}\nTamanho de "{self.string2}": {len2} caracteres')

            if len1 == len2:
                print('As duas strings são de tamanhos iguais.')
            else:
                print('As duas strings são de tamanhos diferentes.')

            if content_equal:
                print('As duas strings possuem conteúdo igual.')
            else:
                print('As duas strings possuem conteúdo diferente.')

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    string1 = input('Digite a primeira string: ')
    string2 = input('Digite a segunda string: ')

    comparator = StringComparator(string1, string2)
    comparator.compare_strings()


if __name__ == '__main__':
    main()
