#Lista de Exercício 4 - Questão 14
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Suspeito:
    def __init__(self):
        self.respostas = []

    def responder_pergunta(self, resposta):
        self.respostas.append(resposta)

    def classificar_suspeito(self):
        num_respostas_positivas = sum(resposta.lower() == "sim" for resposta in self.respostas)

        if num_respostas_positivas == 5:
            return "Assassino"
        elif num_respostas_positivas >= 3:
            return "Cúmplice"
        elif num_respostas_positivas >= 2:
            return "Suspeito"
        else:
            return "Inocente"

def fazer_perguntas():
    try:
        perguntas = [
            "Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"
        ]

        suspeito = Suspeito()

        for pergunta in perguntas:
            resposta = input(pergunta + " (sim ou não): ")
            if resposta.lower() not in ["sim", "não"]:
                raise ValueError("Resposta inválida. Digite apenas 'sim' ou 'não'.")
            suspeito.responder_pergunta(resposta)

        classificacao = suspeito.classificar_suspeito()
        print("Classificação:", classificacao)

    except ValueError as e:
        print("Erro:", str(e))

fazer_perguntas()
