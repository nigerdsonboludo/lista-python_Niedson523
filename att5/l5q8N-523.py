#Lista de Exercício 5 - Questão 8
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class NumeroInteiro:
    def __init__(self, numero):
        self.numero = numero

    def contarDigitos(self):
        try:
            if not isinstance(self.numero, int):
                raise ValueError("O valor informado não é um número inteiro.")
            
            if self.numero < 0:
                self.numero *= -1  # Considera apenas o valor absoluto

            if self.numero == 0:
                return 1

            contador = 0
            while self.numero > 0:
                self.numero //= 10
                contador += 1
            
            return contador
        except Exception as e:
            raise ValueError(f"Erro ao contar dígitos: {str(e)}")


try:
    numero = int(input("Informe um número inteiro: "))
    numero_objeto = NumeroInteiro(numero)
    quantidade_digitos = numero_objeto.contarDigitos()
    print(f"A quantidade de dígitos do número {numero} é: {quantidade_digitos}")
except ValueError as e:
    print(f"Erro: {str(e)}")
