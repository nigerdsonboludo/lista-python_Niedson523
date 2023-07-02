#Lista de Exercício 5 - Questão 13
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Moldura:
    def __init__(self, linhas=1, colunas=1):
        self.linhas = self.validarValor(linhas, 1, 20)
        self.colunas = self.validarValor(colunas, 1, 20)

    def validarValor(self, valor, valor_min, valor_max):
        try:
            valor = int(valor)
            if valor < valor_min:
                return valor_min
            elif valor > valor_max:
                return valor_max
            return valor
        except:
            return valor_min

    def desenharMoldura(self):
        try:
            linha_horizontal = '+' + '-' * self.colunas + '+'
            linha_vertical = '|' + ' ' * self.colunas + '|'

            print(linha_horizontal)
            for _ in range(self.linhas):
                print(linha_vertical)
            print(linha_horizontal)
        except Exception as e:
            raise ValueError(f"Erro ao desenhar a moldura: {str(e)}")


try:
    linhas = input("Informe a quantidade de linhas (1-20): ")
    colunas = input("Informe a quantidade de colunas (1-20): ")

    moldura = Moldura(linhas, colunas)
    moldura.desenharMoldura()
except ValueError as e:
    print(f"Erro: {str(e)}")
