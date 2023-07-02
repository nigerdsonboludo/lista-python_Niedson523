#Lista de Exercício 7 - Questão 8
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        if len(self.bucho) == 0:
            print(f"{self.nome} está com o bucho vazio.")
        else:
            print(f"{self.nome} tem no bucho: {', '.join(self.bucho)}")

    def digerir(self):
        if len(self.bucho) == 0:
            print(f"{self.nome} não tem nada para digerir.")
        else:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
            print(f"{self.nome} digeriu tudo.")

# Teste interativo

macaco1 = Macaco("Coco")
macaco2 = Macaco("Banana")

print("Alimentando Coco...")
macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Laranja")
macaco1.ver_bucho()

print("Alimentando Banana...")
macaco2.comer("Amendoim")
macaco2.comer("Uva")
macaco2.ver_bucho()

print("Digerindo Coco...")
macaco1.digerir()
macaco1.ver_bucho()

print("Digerindo Banana...")
macaco2.digerir()
macaco2.ver_bucho()

