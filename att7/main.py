numeroQuestao = 1
quantidadeQuestao = 17
numeroLista = 7

for i in range(quantidadeQuestao):
    with open(f"l{numeroLista}q{numeroQuestao}N-523.py", "w", encoding="utf-8") as arq:
        arq.write(f"#Lista de Exercício {numeroLista} - Questão {numeroQuestao}\n"
                  "#Dupla: 2021324069 - Niedson David\n"
                  "#Disciplina: Programação Web\n"
                  "#Professor: Italo Arruda")
    numeroQuestao += 1