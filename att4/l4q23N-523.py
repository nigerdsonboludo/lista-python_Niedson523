#Lista de Exercício 4 - Questão 23
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Usuario:
    def __init__(self, nome, espaco_utilizado):
        self.nome = nome
        self.espaco_utilizado = espaco_utilizado


def ler_arquivo_usuarios(nome_arquivo):
    usuarios = []

    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split()
                nome = dados[0]
                espaco_utilizado = int(dados[1])
                usuario = Usuario(nome, espaco_utilizado)
                usuarios.append(usuario)

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IndexError:
        print("Erro: Formato do arquivo inválido.")

    return usuarios


def converter_bytes_para_megabytes(bytes):
    megabytes = bytes / (1024 * 1024)
    return round(megabytes, 2)


def calcular_percentual_uso(espaco_utilizado, espaco_total):
    percentual = (espaco_utilizado / espaco_total) * 100
    return round(percentual, 2)


def gerar_relatorio(usuarios):
    total_uso = sum(usuario.espaco_utilizado for usuario in usuarios)
    espaco_medio = total_uso / len(usuarios)

    print("ACME Inc.               Uso do espaço em disco pelos usuários")
    print("-------------------------------------------------------------")
    print("Nr.  Usuário        Espaço utilizado     % do uso")
    print()

    for i, usuario in enumerate(usuarios, 1):
        espaco_mb = converter_bytes_para_megabytes(usuario.espaco_utilizado)
        percentual = calcular_percentual_uso(usuario.espaco_utilizado, total_uso)

        print(f"{i:<4}{usuario.nome:<15}{espaco_mb:>16.2f} MB{percentual:>17.2f}%")

    total_uso_mb = converter_bytes_para_megabytes(total_uso)
    espaco_medio_mb = converter_bytes_para_megabytes(espaco_medio)

    print("\nEspaço total ocupado:", total_uso_mb, "MB")
    print("Espaço médio ocupado:", espaco_medio_mb, "MB")


usuarios = ler_arquivo_usuarios("usuarios.txt")
if usuarios:
    gerar_relatorio(usuarios)
