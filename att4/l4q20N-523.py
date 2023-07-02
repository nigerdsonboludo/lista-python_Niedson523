#Lista de Exercício 4 - Questão 20
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Abono:
    def __init__(self):
        self.salarios = []

    def receber_salarios(self):
        print("Projeção de Gastos com Abono")
        print("============================")
        print("Digite o salário de cada funcionário (0 para encerrar):")

        while True:
            salario = float(input("Salário: "))

            if salario == 0:
                break

            self.salarios.append(salario)

    def calcular_abono(self):
        abonos = []

        for salario in self.salarios:
            abono = salario * 0.2 if salario * 0.2 >= 100 else 100
            abonos.append(abono)

        return abonos

    def exibir_resultados(self):
        abonos = self.calcular_abono()
        total_funcionarios = len(self.salarios)
        total_gasto = sum(abonos)
        valor_minimo = abonos.count(100)
        maior_valor = max(abonos)

        print("\nSalário    - Abono")
        for i in range(len(self.salarios)):
            print(f"R$ {self.salarios[i]:.2f} - R$ {abonos[i]:.2f}")

        print(f"\nForam processados {total_funcionarios} colaboradores")
        print(f"Total gasto com abonos: R$ {total_gasto:.2f}")
        print(f"Valor mínimo pago a {valor_minimo} colaboradores")
        print(f"Maior valor de abono pago: R$ {maior_valor:.2f}")


abono = Abono()
abono.receber_salarios()
abono.exibir_resultados()
