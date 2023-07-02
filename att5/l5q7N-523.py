#Lista de Exercício 5 - Questão 7
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Pagamento:
    def __init__(self, valor_prestacao, dias_atraso):
        self.valor_prestacao = valor_prestacao
        self.dias_atraso = dias_atraso

    def valorPagamento(self):
        if self.valor_prestacao <= 0:
            raise ValueError("O valor da prestação deve ser maior que zero.")
        
        if self.dias_atraso <= 0:
            return self.valor_prestacao
        else:
            multa = self.valor_prestacao * 0.03
            juros = self.valor_prestacao * (0.001 * self.dias_atraso)
            return self.valor_prestacao + multa + juros

def relatorio_diario(prestacoes):
    quantidade = len(prestacoes)
    valor_total = sum(prestacoes)
    print(f"Relatório do dia:\nQuantidade de prestações pagas: {quantidade}\nValor total recebido: R${valor_total:.2f}")

prestacoes_pagas = []
while True:
    try:
        valor = float(input("Informe o valor da prestação (0 para sair): "))
        if valor == 0:
            break

        dias_atraso = int(input("Informe o número de dias em atraso: "))

        pagamento = Pagamento(valor, dias_atraso)
        valor_total = pagamento.valorPagamento()
        prestacoes_pagas.append(valor_total)

        print(f"Valor a ser pago: R${valor_total:.2f}\n")
    except ValueError as e:
        print(f"Erro: {str(e)}\n")

relatorio_diario(prestacoes_pagas)
