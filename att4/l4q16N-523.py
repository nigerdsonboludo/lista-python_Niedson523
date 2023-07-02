#Lista de Exercício 4 - Questão 16
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Vendedor:
    def __init__(self, vendas_brutas):
        self.vendas_brutas = vendas_brutas

    def calcular_salario(self):
        return 200 + 0.09 * self.vendas_brutas

def contar_salarios_vendedores(vendedores):
    intervalos = [0] * 9  # Lista de contadores para os intervalos de valores

    for vendedor in vendedores:
        salario = vendedor.calcular_salario()

        if salario < 300:
            intervalos[0] += 1
        elif salario < 400:
            intervalos[1] += 1
        elif salario < 500:
            intervalos[2] += 1
        elif salario < 600:
            intervalos[3] += 1
        elif salario < 700:
            intervalos[4] += 1
        elif salario < 800:
            intervalos[5] += 1
        elif salario < 900:
            intervalos[6] += 1
        elif salario < 1000:
            intervalos[7] += 1
        else:
            intervalos[8] += 1

    return intervalos

def main():
    vendedores = []  # Lista para armazenar os vendedores

    while True:
        try:
            venda_bruta = float(input("Digite a venda bruta do vendedor (-1 para encerrar): "))
            if venda_bruta == -1:
                break

            vendedor = Vendedor(venda_bruta)
            vendedores.append(vendedor)
        except ValueError:
            print("Valor inválido. Digite apenas números.")

    intervalos = contar_salarios_vendedores(vendedores)

    print("Quantidade de vendedores nos intervalos de salários:")
    print("$200 - $299:", intervalos[0])
    print("$300 - $399:", intervalos[1])
    print("$400 - $499:", intervalos[2])
    print("$500 - $599:", intervalos[3])
    print("$600 - $699:", intervalos[4])
    print("$700 - $799:", intervalos[5])
    print("$800 - $899:", intervalos[6])
    print("$900 - $999:", intervalos[7])
    print("$1000 em diante:", intervalos[8])

main()
