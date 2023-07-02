#Lista de Exercício 6 - Questão 12
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class PhoneNumberValidator:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def validate_and_fix(self):
        try:
            # Remover traços e espaços em branco
            phone_number = self.phone_number.replace('-', '').replace(' ', '')

            if len(phone_number) == 7:
                phone_number = '3' + phone_number

            formatted_number = f'{phone_number[:4]}-{phone_number[4:]}'

            print(f'Telefone corrigido sem formatação: {phone_number}')
            print(f'Telefone corrigido com formatação: {formatted_number}')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    try:
        phone_number = input('Telefone: ')

        validator = PhoneNumberValidator(phone_number)
        validator.validate_and_fix()
    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')


if __name__ == '__main__':
    main()
