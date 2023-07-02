#Lista de Exercício 6 - Questão 14
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class LeetTranslator:
    def __init__(self):
        self.translation_table = {
            'A': '4',
            'E': '3',
            'G': '6',
            'I': '1',
            'O': '0',
            'S': '5',
            'T': '7'
        }

    def translate_text(self, text):
        translated_text = ''
        for char in text:
            translated_char = self.translation_table.get(char.upper(), char)
            translated_text += translated_char
        return translated_text

    def handle_input(self):
        try:
            text = input('Digite um texto: ')
            translated_text = self.translate_text(text)
            print(f'Texto traduzido para Leet Speak: {translated_text}')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')


def main():
    translator = LeetTranslator()
    translator.handle_input()


if __name__ == '__main__':
    main()
