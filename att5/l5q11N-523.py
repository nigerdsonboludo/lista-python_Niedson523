#Lista de Exercício 5 - Questão 11
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Data:
    def __init__(self, data):
        self.data = data

    def validarData(self):
        try:
            dia, mes, ano = map(int, self.data.split('/'))
            if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
                return False
            elif mes in [4, 6, 9, 11] and dia > 30:
                return False
            elif mes == 2:
                if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                    if dia > 29:
                        return False
                elif dia > 28:
                    return False
            return True
        except:
            return False

    def obterDataPorExtenso(self):
        try:
            if not self.validarData():
                return None

            dia, mes, ano = map(int, self.data.split('/'))
            meses = [
                'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
            ]
            return f"{dia} de {meses[mes-1]} de {ano}"
        except Exception as e:
            raise ValueError(f"Erro ao obter a data por extenso: {str(e)}")


try:
    data_str = input("Informe uma data no formato DD/MM/AAAA: ")
    data_objeto = Data(data_str)
    data_por_extenso = data_objeto.obterDataPorExtenso()
    
    if data_por_extenso is None:
        print("Data inválida.")
    else:
        print(f"A data por extenso é: {data_por_extenso}")
except ValueError as e:
    print(f"Erro: {str(e)}")
