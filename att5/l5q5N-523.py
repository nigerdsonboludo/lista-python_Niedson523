#Lista de Exercício 5 - Questão 5
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class CalculadoraImposto:
    def somaImposto(self, taxaImposto, custo):
        if not isinstance(taxaImposto, (int, float)):
            raise ValueError("A taxa de imposto deve ser um número")
        if not isinstance(custo, (int, float)):
            raise ValueError("O custo deve ser um número")

        imposto = custo * (taxaImposto / 100)
        custo_total = custo + imposto
        return custo_total


def main():
    try:
        taxaImposto = float(input("Digite a taxa de imposto (em porcentagem): "))
        custo = float(input("Digite o custo do item: "))
        
        calculadora = CalculadoraImposto()
        custo_final = calculadora.somaImposto(taxaImposto, custo)
        print(f"O custo final com imposto é: R${custo_final:.2f}")
    except ValueError as e:
        print(f"Erro: {str(e)}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")


if __name__ == "__main__":
    main()
