import time  # Biblioteca utilizada para controlar o tempo

# Semáforos
S1 = False
S2 = False
S3 = False

# Estados do semáforo / O = aberto e X = fechado
R1 = ''
R2 = ''
R3 = ''

# Função para mostrar o estado atual dos semáforos
def imprimir_estados():
    print("Semáforo 1: {}, Semáforo 2: {}, Semáforo 3: {}".format(R1, R2, R3))

# Função para alternar os estados dos semáforos
def alternar_semaforos():
    global S1, S2, S3, R1, R2, R3

    if S1:
        S1, S2, S3 = False, True, False
    elif S2:
        S1, S2, S3 = False, False, True
    elif S3:
        S1, S2, S3 = True, False, False

    # Atualiza os estados dos semáforos
    if S1:
        R1, R2, R3 = 'O', 'X', 'X'
    elif S2:
        R1, R2, R3 = 'X', 'O', 'X'
    elif S3:
        R1, R2, R3 = 'X', 'X', 'O'

    imprimir_estados()

# Inicia com o semáforo 1
S1 = True
R1 = 'O'
R2 = 'X'
R3 = 'X'
imprimir_estados()

# Loop para alternar
while True:
    time.sleep(5)  # Tempo de espera
    alternar_semaforos()

    # Pergunta ao usuário se há pedestres nas faixas de pedestres
    P1, P2, P3 = '','',''
    P1 = input("Há pedestres na faixa 1? (1 para Sim, 0 para Não): ")

    if P1 == '1':
        S1, S2, S3 = False, False, True  # Abre o semáforo 1
    elif P1 == '0':
        P2 = input("Há pedestres na faixa 2? (1 para Sim, 0 para Não): ")
        if P2 == '1':
            S1, S2, S3 = True, False, False  # Abre o semáforo 2
        elif P2 == '0':
            P3 = input("Há pedestres na faixa 3? (1 para Sim, 0 para Não): ")
            if P3 == '1':
                S1, S2, S3 = False, True, True  # Abre o semáforo 3
    if P3 == '0':
        continuar = input("Nenhum pedestre. continuar? (0 para Não): ")
        if continuar == '0':
            print("FIM!!!")
            break