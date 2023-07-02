#Lista de Exercício 5 - Questão 12
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

import random

class Embaralhador:
    def __init__(self, palavra):
        self.palavra = palavra.lower()

    def embaralhar(self):
        try:
            caracteres = list(self.palavra)
            random.shuffle(caracteres)
            palavra_embaralhada = ''.join(caracteres)
            return palavra_embaralhada.upper()
        except Exception as e:
            raise ValueError(f"Erro ao embaralhar a palavra: {str(e)}")


try:
    palavra = input("Digite uma palavra: ")
    embaralhador = Embaralhador(palavra)
    palavra_embaralhada = embaralhador.embaralhar()
    print(f"Palavra embaralhada: {palavra_embaralhada}")
except ValueError as e:
    print(f"Erro: {str(e)}")
