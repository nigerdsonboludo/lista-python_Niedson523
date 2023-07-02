#Lista de Exercício 6 - Questão 10
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class NumberConverter:
    def __init__(self, number):
        self.number = number

    def convert_to_words(self):
        try:
            words = {
                0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro',
                5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove',
                10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze',
                15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove',
                20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta',
                60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa'
            }

            if self.number < 0 or self.number > 99:
                print('Digite um número entre 0 e 99.')
                return

            if self.number in words:
                print(words[self.number])
                return

            tens = self.number // 10 * 10
            units = self.number % 10

            result = words[tens]
            if units > 0:
                result += f' e {words[units]}'

            print(result)
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    try:
        number = int(input('Digite um número entre 0 e 99: '))

        converter = NumberConverter(number)
        converter.convert_to_words()
    except ValueError:
        print('Digite um número válido.')


if __name__ == '__main__':
    main()
