#Lista de Exercício 7 - Questão 6
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def alterar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print("Canal alterado para:", novo_canal)
        else:
            print("Canal inválido")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print("Volume aumentado para:", self.volume)
        else:
            print("Volume máximo")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume diminuído para:", self.volume)
        else:
            print("Volume mínimo")


# Exemplo de uso da classe TV
tv = TV()
tv.alterar_canal(5)  # Altera para o canal 5
tv.aumentar_volume()  # Aumenta o volume em 1
tv.diminuir_volume()  # Diminui o volume em 1

tv.alterar_canal(150)  # Tenta alterar para um canal inválido
tv.aumentar_volume()  # Aumenta o volume além do máximo
tv.diminuir_volume()  # Diminui o volume além do mínimo
