#Lista de Exercício 5 - Questão 4
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Verificador:
    def verificar_numero(self, num):
        if not isinstance(num, (int, float)):
            raise ValueError("O argumento deve ser um número")

        if num > 0:
            return 'P'
        elif num <= 0:
            return 'N'


def main():
    try:
        num = float(input("Digite um número: "))
        
        verificador = Verificador()
        resultado = verificador.verificar_numero(num)
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Erro: {str(e)}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")


if __name__ == "__main__":
    main()
