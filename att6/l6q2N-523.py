#Lista de Exercício 6 - Questão 2
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class NameReverser:
    def __init__(self, name):
        self.name = name

    def reverse_name(self):
        try:
            reversed_name = self.name[::-1].upper()
            print(f'Nome ao contrário em maiúsculas: {reversed_name}')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    name = input('Digite o seu nome: ')

    reverser = NameReverser(name)
    reverser.reverse_name()


if __name__ == '__main__':
    main()
