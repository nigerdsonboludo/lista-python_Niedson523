#Lista de Exercício 7 - Questão 9
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)


def modificar_retangulo(retangulo):
    x = float(input("Digite a coordenada x do ponto inicial: "))
    y = float(input("Digite a coordenada y do ponto inicial: "))
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

    retangulo.ponto_inicial.x = x
    retangulo.ponto_inicial.y = y
    retangulo.largura = largura
    retangulo.altura = altura


def imprimir_menu():
    print("1. Criar retângulo")
    print("2. Modificar retângulo")
    print("3. Imprimir centro do retângulo")
    print("4. Sair")


retangulo = None

while True:
    imprimir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        x = float(input("Digite a coordenada x do ponto inicial: "))
        y = float(input("Digite a coordenada y do ponto inicial: "))
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        ponto_inicial = Ponto(x, y)
        retangulo = Retangulo(ponto_inicial, largura, altura)
        print("Retângulo criado com sucesso!")

    elif opcao == "2":
        if retangulo is not None:
            modificar_retangulo(retangulo)
            print("Retângulo modificado com sucesso!")
        else:
            print("Crie um retângulo primeiro!")

    elif opcao == "3":
        if retangulo is not None:
            centro = retangulo.encontrar_centro()
            print("Centro do retângulo:")
            centro.imprimir()
        else:
            print("Crie um retângulo primeiro!")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
