#Lista de Exercício 4 - Questão 13
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class TemperaturaAnual:
    def __init__(self):
        self.temperaturas = []

    def adicionar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_media_anual(self):
        if len(self.temperaturas) > 0:
            soma = sum(self.temperaturas)
            media = soma / len(self.temperaturas)
            return media
        else:
            return 0

    def listar_temperaturas_acima_media(self):
        media_anual = self.calcular_media_anual()
        temperaturas_acima_media = []
        for i, temperatura in enumerate(self.temperaturas):
            if temperatura > media_anual:
                temperaturas_acima_media.append((i+1, temperatura))
        return temperaturas_acima_media

def temperatura_por_extenso(mes):
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    return meses.get(mes, "")

def calcular_temperaturas_acima_media():
    try:
        temperatura_anual = TemperaturaAnual()

        for mes in range(1, 13):
            temperatura = float(input(f"Digite a temperatura média de {temperatura_por_extenso(mes)}: "))
            temperatura_anual.adicionar_temperatura(temperatura)

        temperaturas_acima_media = temperatura_anual.listar_temperaturas_acima_media()

        print("Temperaturas acima da média anual:")
        for mes, temperatura in temperaturas_acima_media:
            print(f"{temperatura_por_extenso(mes)}: {temperatura}")

    except ValueError:
        print("Valor inválido. Certifique-se de digitar apenas números reais.")

calcular_temperaturas_acima_media()
