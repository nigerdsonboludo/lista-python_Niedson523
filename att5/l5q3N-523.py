#Lista de Exercício 5 - Questão 3
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Soma:
    def calcular_soma(self, num1, num2, num3):
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)) or not isinstance(num3, (int, float)):
            raise ValueError("Os argumentos devem ser números")
        
        return num1 + num2 + num3


def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        
        soma = Soma()
        resultado = soma.calcular_soma(num1, num2, num3)
        print(f"A soma dos números é: {resultado}")
    except ValueError as e:
        print(f"Erro: {str(e)}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")


if __name__ == "__main__":
    main()
