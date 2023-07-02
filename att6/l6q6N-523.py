#Lista de Exercício 6 - Questão 6
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

import datetime
import calendar

class DateConverter:
    def __init__(self, date):
        self.date = date

    def convert_date(self):
        try:
            # Converte a data fornecida em uma data datetime
            date_obj = datetime.datetime.strptime(self.date, '%d/%m/%Y')

            # Obtém o nome do mês por extenso
            month = calendar.month_name[date_obj.month]

            # Imprime a data com o nome do mês por extenso
            print(f"Você nasceu em {date_obj.day} de {month} de {date_obj.year}.")
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    date = input('Digite a data de nascimento (dd/mm/aaaa): ')

    converter = DateConverter(date)
    converter.convert_date()


if __name__ == '__main__':
    main()
