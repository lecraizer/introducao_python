# Pacotes gerais
import random
import time

# Módulos de jogadores
import jogadores.joao as joao
import jogadores.ana as ana
import jogadores.carlos as carlos
import jogadores.pedro as pedro
# import jogadores.jade as jade
# import jogadores.milena as milena
import jogadores.kamikaze as kamikaze
# import jogadores.mago as mago
# import jogadores.rainha as rainha


# Função para criar um jogador
def criar_jogador(nome, estrategia_func):
    return {
        "nome": nome,
        "vida": 99,  # Vida inicial
        "morto": False,
        "defesa": False,
        "estrategia_func": estrategia_func, # "atacar" ou "defender"
        "bonus_ataque": 1.0  # Bônus de ataque inicial
    }


# Função para aplicar dano a um jogador
def receber_dano(jogador, dano):
    if jogador['defesa']:  # Se o jogador estiver defendendo, recebe menos dano
        dano = dano // 5 # Inteiro da divisão de dano por 5
        jogador['defesa'] = False # Desabilitar a defesa após o dano ser recebido

    if jogador['vida'] > 0: # Se o jogador ainda estiver vivo
        jogador['vida'] -= dano  # Aplicar o dano
        if jogador['vida'] <= 0: # Se o jogador morreu devido ao dano
            jogador['vida'] = 0
            jogador['morto'] = True
            print(f"\nO jogador {jogador['nome']} morreu.")


# Função para realizar um ataque de um jogador a outro
def atacar(jogador, alvo):
    dano = random.randint(1, 6) * jogador['bonus_ataque']
    dano = int(dano)  # Converter para inteiro
    receber_dano(alvo, dano)

    if alvo['vida'] <= 0:
        jogador['bonus_ataque'] += 0.1
        jogador['bonus_ataque'] = round(jogador['bonus_ataque'], 1)
        print(f"O jogador {jogador['nome']} matou o jogador {alvo['nome']}")
        print(f"{jogador['nome']} foi a {jogador['bonus_ataque']:.1f} de dano")
        

# Função para ativar a defesa de um jogador
def defender(jogador):
    jogador['defesa'] = True


# Função para realizar a ação de um jogador
def realizar_acao(jogador, jogadores, rodada, rank):
    if jogador['morto']: # Se o jogador estiver morto, não fazer nada
        return
    
    # Caso contrário, a função continua (não há necessidade do 'else' por causa do 'return')

    # Chama a função de estratégia do jogador, que recebe 3 parâmetros: vida do jogador, quantidade de jogadores vivos e rodada atual
    estrategia = jogador['estrategia_func'](jogador['vida'], len([j for j in jogadores if not j['morto']]), rodada)

    if estrategia == "atacar":
        alvo = random.choice([j for j in jogadores if j != jogador and not j['morto']])  # Escolhe um alvo aleatório
        atacar(jogador, alvo) # Alvo é um jogador (dicionário)
    elif estrategia == "defender":
        defender(jogador) # Ativa a defesa do jogador
    elif estrategia == "atacar_todos":
        # 20% de chance de atacar todos os jogadores
        if random.random() < 0.2:
            for alvo in [j for j in jogadores if j != jogador and not j['morto']]:
                atacar(jogador, alvo)
    elif estrategia == "curar":
        jogador['vida'] += random.randint(1, 2)


# Função principal para rodar o jogo
def jogo():
    
    # Inicializa a lista de jogadores
    jogadores = []

    # Cria jogadores fictícios com suas respectivas estratégias
    jogadores.append(criar_jogador("João", joao.estrategia_joao))
    jogadores.append(criar_jogador("Ana", ana.estrategia_ana))
    jogadores.append(criar_jogador("Carlos", carlos.estrategia_carlos))
    jogadores.append(criar_jogador("Pedro", pedro.estrategia_pedro))
    # jogadores.append(criar_jogador("Jade", jade.estrategia_jade))
    # jogadores.append(criar_jogador("Milena", milena.estrategia_milena))
    jogadores.append(criar_jogador("Kamikaze", kamikaze.estrategia_kamikaze))
    # jogadores.append(criar_jogador("Mago", mago.estrategia_mago))
    # jogadores.append(criar_jogador("Rainha", rainha.estrategia_rainha))


    rodada = 1
    while len([j for j in jogadores if not j['morto']]) > 1:  # Enquanto mais de 1 jogador estiver vivo
        
        # Parte do código para imprimir o estado do jogo a cada 100 rodadas
        time.sleep(0.03)
        if rodada % 100 == 0:
            print(f"\n\n--- Rodada {rodada} ---\n")
            # Imprimir o estado atual dos jogadores que ainda estão vivos

            jogadores = sorted(jogadores, key=lambda x: x['vida'], reverse=True) # ordena a lista de jogadores (key='HP')
            for jogador in jogadores:
                if not jogador['morto']:
                    # print nome e vida do jogador, alinhado à direita, em ordem decrescente de vida assim como ataque atual do jogador
                    print(f"{jogador['nome']}: {jogador['vida']} HP | A: {jogador['bonus_ataque']}".rjust(35))

        # Para cada jogador, realizar uma ação (defender ou atacar)
        for jogador in jogadores: 
            rank = jogadores.index(jogador) # Índice do jogador na lista de jogadores
            realizar_acao(jogador, jogadores, rodada, rank) # Realiza a ação do jogador
        
        rodada += 1

    # Determinar o vencedor
    vencedor = [j for j in jogadores if not j['morto']][0] # Pega a lista de jogadores que não estão mortos (cujo tamanho é 1) e pega o idx=0
    print(f"\n{vencedor['nome']} venceu o jogo com {vencedor['vida']} HP na rodada {rodada}")


# Executar o jogo
if __name__ == "__main__": # Linha de execução principal
    jogo()



### --- Outras possíveis funcionalidades para implementar --- ###

# 1. Função que imprime o estado do jogo a cada N rodadas em ordem decrescente de vida (se possível, sem utilizar a função sort)
# 2. Atributo de bonus de ataque a cada vez que o jogador mata outro jogador (Ex: +1 de dano a cada jogador morto ou +10% de dano)
# 3. Estratégia de ataque arriscado, ou seja, há uma chance do ataque falhar ou então atacar todos os outros jogadores (Pr=0.25 de falhar)
# 4. Função de cura, que aumenta a vida do jogador em +1
# 5. Jogador recebe como parâmetro também o ranking dele em relação aos outros jogadores (no aspecto de vida)