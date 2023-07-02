#Lista de Exercício 7 - Questão 13
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


# Exemplo de uso da classe Funcionario
funcionario1 = Funcionario("João", 2500.0)
funcionario2 = Funcionario("Maria", 3500.0)

print("Dados do funcionário 1:")
print("Nome:", funcionario1.get_nome())
print("Salário:", funcionario1.get_salario())

print("\nDados do funcionário 2:")
print("Nome:", funcionario2.get_nome())
print("Salário:", funcionario2.get_salario())
