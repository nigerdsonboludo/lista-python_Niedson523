#Lista de Exercício 4 - Questão 22
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Mouse:
    def __init__(self, identificacao, situacao):
        self.identificacao = identificacao
        self.situacao = situacao


def registrar_sucatas_mouses():
    situacoes = {
        1: "necessita da esfera",
        2: "necessita de limpeza",
        3: "necessita troca do cabo ou conector",
        4: "quebrado ou inutilizado"
    }

    mouses = []

    while True:
        try:
            identificacao = int(input("Número de identificação do mouse (0 para encerrar): "))
            if identificacao == 0:
                break

            situacao = int(input("Situação do mouse (1 a 4): "))
            if situacao not in situacoes:
                raise ValueError("Situação inválida.")

            mouse = Mouse(identificacao, situacao)
            mouses.append(mouse)

        except ValueError as e:
            print("Erro:", str(e))

    return mouses


def gerar_relatorio(mouses):
    quantidade_mouses = len(mouses)
    quantidade_situacoes = {1: 0, 2: 0, 3: 0, 4: 0}

    for mouse in mouses:
        quantidade_situacoes[mouse.situacao] += 1

    print("\nRelatório de Sucatas de Mouses")
    print("Quantidade de mouses:", quantidade_mouses)
    print("\nSituação                               Quantidade     Percentual")
    print("----------------------------------------------------------------")

    for situacao, quantidade in quantidade_situacoes.items():
        percentual = (quantidade / quantidade_mouses) * 100
        print(f"{situacoes[situacao]:<38}{quantidade:<14}{percentual:>7.1f}%")


mouses = registrar_sucatas_mouses()
gerar_relatorio(mouses)
