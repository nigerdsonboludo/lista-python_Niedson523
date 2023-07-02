#Lista de Exercício 7 - Questão 14
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def aumentar_salario(self, porcentual_de_aumento):
        aumento = self.salario * (porcentual_de_aumento / 100)
        self.salario += aumento


# Exemplo de uso da classe Funcionario
harry = Funcionario("Harry", 25000)
print("Salário atual:", harry.get_salario())

harry.aumentar_salario(10)
print("Salário após aumento:", harry.get_salario())
