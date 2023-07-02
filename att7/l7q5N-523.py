#Lista de Exercício 7 - Questão 5
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

# Exemplo de uso da classe ContaCorrente
conta = ContaCorrente(1234, "João")
print("Número da conta:", conta.numero_conta)
print("Nome do correntista:", conta.nome_correntista)
print("Saldo:", conta.saldo)

conta.alterarNome("João Silva")
print("Novo nome do correntista:", conta.nome_correntista)

conta.deposito(100)
print("Saldo após depósito:", conta.saldo)

conta.saque(50)
print("Saldo após saque:", conta.saldo)

conta.saque(100)
