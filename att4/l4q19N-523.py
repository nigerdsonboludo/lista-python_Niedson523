#Lista de Exercício 4 - Questão 19
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Enquete:
    def __init__(self):
        self.opcoes = {
            1: "Windows Server",
            2: "Unix",
            3: "Linux",
            4: "Netware",
            5: "Mac OS",
            6: "Outro"
        }
        self.votos = [0] * 7

    def registrar_voto(self, opcao):
        if opcao >= 1 and opcao <= 6:
            self.votos[opcao] += 1
        else:
            print("Opção inválida. Tente novamente.")

    def calcular_percentual(self, votos_opcao, total_votos):
        return (votos_opcao / total_votos) * 100

    def exibir_resultados(self):
        total_votos = sum(self.votos)
        
        print("Sistema Operacional     Votos   %")
        print("-------------------     -----   ---")
        
        for opcao, votos_opcao in enumerate(self.votos[1:], start=1):
            percentual = self.calcular_percentual(votos_opcao, total_votos)
            print(f"{self.opcoes[opcao]:<23}{votos_opcao:<7}{percentual:.0f}%")
        
        print("-------------------     -----   -----")
        print(f"Total                    {total_votos}\n")
        
        vencedor = max(range(1, 7), key=lambda x: self.votos[x])
        votos_vencedor = self.votos[vencedor]
        percentual_vencedor = self.calcular_percentual(votos_vencedor, total_votos)
        
        print(f"O Sistema Operacional mais votado foi o {self.opcoes[vencedor]}, "
              f"com {votos_vencedor} votos, correspondendo a {percentual_vencedor:.0f}% dos votos.")


enquete = Enquete()

print("Qual o melhor Sistema Operacional para uso em servidores?")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- Mac OS")
print("6- Outro")
print("Informe o número da opção (0 para encerrar): ")

opcao = int(input())

while opcao != 0:
    enquete.registrar_voto(opcao)
    print("Informe o número da opção (0 para encerrar): ")
    opcao = int(input())

enquete.exibir_resultados()
