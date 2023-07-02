#Lista de Exercício 6 - Questão 5
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class InvertedStaircaseNamePrinter:
    def __init__(self, name):
        self.name = name

    def print_inverted_staircase_name(self):
        try:
            for i in range(len(self.name), 0, -1):
                substring = self.name[:i].upper()
                print(substring)
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    name = input('Digite o seu nome: ')

    printer = InvertedStaircaseNamePrinter(name)
    printer.print_inverted_staircase_name()


if __name__ == '__main__':
    main()
