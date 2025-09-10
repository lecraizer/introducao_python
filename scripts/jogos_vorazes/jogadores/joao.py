import random

# Função que define a estratégia do João
def estrategia_joao(vida, num_jogadores_vivos, rodada):
    if vida > 70:
        return "atacar"
    else:
        return "defender"
