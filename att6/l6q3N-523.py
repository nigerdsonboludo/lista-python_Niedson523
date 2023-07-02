#Lista de Exercício 6 - Questão 3
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class VerticalNamePrinter:
    def __init__(self, name):
        self.name = name

    def print_vertical_name(self):
        try:
            for letter in self.name:
                print(letter.upper())
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    name = input('Digite o seu nome: ')

    printer = VerticalNamePrinter(name)
    printer.print_vertical_name()


if __name__ == '__main__':
    main()
