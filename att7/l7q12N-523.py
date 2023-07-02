#Lista de Exercício 7 - Questão 12
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicione_juros(self):
        juros = self.saldo * self.taxa_juros / 100
        self.saldo += juros

    def get_saldo(self):
        return self.saldo


# Exemplo de uso da classe ContaInvestimento
poupanca = ContaInvestimento(1000.0, 10.0)  # Saldo inicial de R$1000,00 e taxa de juros de 10%

for _ in range(5):
    poupanca.adicione_juros()

saldo_final = poupanca.get_saldo()
print(f"Saldo final: R${saldo_final:.2f}")
