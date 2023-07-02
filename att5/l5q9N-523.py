#Lista de Exercício 5 - Questão 9
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class NumeroInteiro:
    def __init__(self, numero):
        self.numero = numero

    def obterReverso(self):
        try:
            if not isinstance(self.numero, int):
                raise ValueError("O valor informado não é um número inteiro.")
            
            reverso = int(str(abs(self.numero))[::-1])  # Converte para string, inverte e converte de volta para inteiro
            
            if self.numero < 0:
                reverso *= -1  # Mantém o sinal negativo do número original
            
            return reverso
        except Exception as e:
            raise ValueError(f"Erro ao obter o reverso: {str(e)}")


try:
    numero = int(input("Informe um número inteiro: "))
    numero_objeto = NumeroInteiro(numero)
    reverso = numero_objeto.obterReverso()
    print(f"O reverso do número {numero} é: {reverso}")
except ValueError as e:
    print(f"Erro: {str(e)}")
