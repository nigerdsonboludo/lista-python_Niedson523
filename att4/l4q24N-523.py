#Lista de Exercício 4 - Questão 24
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

import random

class Dado:
    def __init__(self, lados):
        if lados < 2:
            raise ValueError("O dado deve ter pelo menos 2 lados")
        self.lados = lados

    def lancar(self):
        return random.randint(1, self.lados)


def simular_lancamento_dados(dado, num_lancamentos):
    resultados = [0] * dado.lados

    for _ in range(num_lancamentos):
        resultado = dado.lancar()
        resultados[resultado - 1] += 1

    return resultados


def exibir_resultados(resultados):
    for i, contagem in enumerate(resultados, 1):
        print(f"Valor {i} foi obtido {contagem} vezes")


try:
    dado = Dado(6)  # Cria um dado de 6 lados
    num_lancamentos = 100

    resultados = simular_lancamento_dados(dado, num_lancamentos)

    exibir_resultados(resultados)

except ValueError as e:
    print(f"Erro: {e}")
