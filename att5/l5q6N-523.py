#Lista de Exercício 5 - Questão 6
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class ConversorHora:
    def converter_para_12_horas(self, hora, minuto):
        if not isinstance(hora, int) or not isinstance(minuto, int):
            raise ValueError("As horas e minutos devem ser números inteiros")
        if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
            raise ValueError("Horário inválido")
        
        periodo = 'A.M.' if hora < 12 else 'P.M.'
        hora = hora % 12
        if hora == 0:
            hora = 12
        
        return hora, minuto, periodo


def exibir_hora(hora, minuto, periodo):
    print(f"{hora}:{minuto:02d} {periodo}")


def main():
    try:
        while True:
            hora = int(input("Digite a hora (0-23): "))
            minuto = int(input("Digite os minutos (0-59): "))
            
            conversor = ConversorHora()
            hora_12, minuto, periodo = conversor.converter_para_12_horas(hora, minuto)
            exibir_hora(hora_12, minuto, periodo)
            
            opcao = input("Deseja converter outro horário? (S/N) ")
            if opcao.lower() != 's':
                break
    except ValueError as e:
        print(f"Erro: {str(e)}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")


if __name__ == "__main__":
    main()
