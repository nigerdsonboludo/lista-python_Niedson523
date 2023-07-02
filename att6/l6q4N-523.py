#Lista de Exercício 6 - Questão 4
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class StaircaseNamePrinter:
    def __init__(self, name):
        self.name = name

    def print_staircase_name(self):
        try:
            for i in range(1, len(self.name) + 1):
                substring = self.name[:i].upper()
                print(substring)
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    name = input('Digite o seu nome: ')

    printer = StaircaseNamePrinter(name)
    printer.print_staircase_name()


if __name__ == '__main__':
    main()
