import random

# Função que define a estratégia da Ana
def estrategia_ana(vida, num_jogadores_vivos, rodada):
    if vida > 60:
        return "atacar"
    else:
        return "defender"
