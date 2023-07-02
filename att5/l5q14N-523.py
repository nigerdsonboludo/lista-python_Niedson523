#Lista de Exercício 5 - Questão 14
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class QuadradoMagico:
    def __init__(self):
        self.solucoes = []

    def verificarQuadradoMagico(self, quadrado):
        # Verificar se a soma das linhas, colunas e diagonais é igual
        soma = sum(quadrado[0:3])
        if sum(quadrado[3:6]) != soma or sum(quadrado[6:9]) != soma:
            return False
        if sum(quadrado[0:7:3]) != soma or sum(quadrado[1:8:3]) != soma or sum(quadrado[2:9:3]) != soma:
            return False
        if quadrado[0] + quadrado[4] + quadrado[8] != soma or quadrado[2] + quadrado[4] + quadrado[6] != soma:
            return False
        return True

    def encontrarQuadradosMagicos(self):
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Gerar todas as permutações possíveis
        permutacoes = self.permutacao(numeros, 9)

        for permutacao in permutacoes:
            if self.verificarQuadradoMagico(permutacao):
                self.solucoes.append(permutacao)

    def permutacao(self, numeros, tamanho):
        if tamanho == 1:
            return [numeros]
        else:
            resultado = []
            for i in range(tamanho):
                for permutacao in self.permutacao(numeros, tamanho-1):
                    resultado.append(permutacao[:i] + [numeros[tamanho-1]] + permutacao[i:])
            return resultado


quadrado_magico = QuadradoMagico()
quadrado_magico.encontrarQuadradosMagicos()

if len(quadrado_magico.solucoes) == 0:
    print("Nenhum quadrado mágico encontrado.")
else:
    print(f"Quadrados Mágicos encontrados:")
    for solucao in quadrado_magico.solucoes:
        print(f"{solucao[0]} {solucao[1]} {solucao[2]}")
        print(f"{solucao[3]} {solucao[4]} {solucao[5]}")
        print(f"{solucao[6]} {solucao[7]} {solucao[8]}")
        print()
