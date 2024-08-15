import time # Biblioteca utilizada para controlar o tempo 

# Semáforos
S1 = False
S2 = False
S3 = False

# Estados do semáforo / O = aberto e X = fechado
R1 = ''
R2 = ''
R3 = ''

# Mostra o estado atual dos semáforos
def imprimir_estados():
    print("Semáforo 1: {}, Semáforo 2: {}, Semáforo 3: {}".format(R1, R2, R3))

# Alternando os estados dos semáforos
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
        R1, R2, R3 = 'O','X','X'
    if S2:
        R1, R2, R3 = 'X','O','X'
    if S3:
        R1, R2, R3 = 'X','X','O'

    imprimir_estados()

# Inicia com o semáforo 1
S1 = True
R1 = 'O'
R2 = 'X'
R3 = 'X'
imprimir_estados()

# Ciclos da aplicação
ciclos = 0

# Loop para alternar
while True:
    time.sleep(5)  # Tempo de espera
    alternar_semaforos()
    
    ciclos += 1

    if ciclos % 5 == 0:
        continuar = input("Continuar? (0 para Não): ")
        if continuar == '0':
            print("FIM!!!")
            break