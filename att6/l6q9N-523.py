#Lista de Exercício 6 - Questão 9
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class CPFValidator:
    def __init__(self, cpf):
        self.cpf = cpf

    def is_valid_cpf(self):
        try:
            # Remove caracteres de formatação do CPF
            cpf_cleaned = ''.join(e for e in self.cpf if e.isdigit())

            # Verifica se o CPF possui 11 dígitos
            if len(cpf_cleaned) != 11:
                return False

            # Verifica se todos os dígitos são iguais
            if cpf_cleaned == cpf_cleaned[0] * 11:
                return False

            # Verifica o primeiro dígito verificador
            sum_ = sum(int(cpf_cleaned[i]) * (10 - i) for i in range(9))
            digit_1 = (sum_ * 10) % 11
            if digit_1 == 10:
                digit_1 = 0
            if str(digit_1) != cpf_cleaned[9]:
                return False

            # Verifica o segundo dígito verificador
            sum_ = sum(int(cpf_cleaned[i]) * (11 - i) for i in range(10))
            digit_2 = (sum_ * 10) % 11
            if digit_2 == 10:
                digit_2 = 0
            if str(digit_2) != cpf_cleaned[10]:
                return False

            return True

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')
            return False


def main():
    cpf = input('Digite o número do CPF (formato xxx.xxx.xxx-xx): ')

    validator = CPFValidator(cpf)
    if validator.is_valid_cpf():
        print('CPF válido.')
    else:
        print('CPF inválido.')


if __name__ == '__main__':
    main()
