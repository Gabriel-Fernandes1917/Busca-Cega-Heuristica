import math

def calcular_distancia_pontos(matriz, ponto1, ponto2):

    x1, y1 = ponto1
    x2, y2 = ponto2

    # Verifica se as coordenadas dos pontos estão dentro da matriz
    if x1 < 1 or x1 >= 11 or y1 < 0 or y1 >= 11 or x2 < 1 or x2 >= 11 or y2 < 1 or y2 >= 11:
        raise ValueError("Coordenadas dos pontos estão fora da matriz")

    # Calcula a distância em linha reta usando a fórmula da distância euclidiana
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def inicializar_mapa(linhas, colunas, valor_padrao=0):
    return [[valor_padrao for _ in range(colunas)] for _ in range(linhas)]

def imprimir_mapa(mapa):
    for linha in mapa:
        for celula in linha:
# Cubos
          if celula == 0:
            print('⬜', end=' ')  # Cubo branco
          elif celula == 100:
            print('⬛', end=' ')  # Cubo preto
          elif celula == 200:
            print('🟥', end=' ')  # Cubo vermelho
          elif celula == 300:
            print('🟦', end=' ')  # Cubo azul
          elif celula == 400:
            print('🤓', end=' ')  # Aluno cesupa
# Cubo 1 a 10
          elif celula == 1:
            print('1️⃣', end=' ')  # Cubo 1
          elif celula == 2:
            print('2️⃣', end=' ')  # Cubo 2
          elif celula == 3:
            print('3️⃣', end=' ')  # Cubo 3
          elif celula == 4:
            print('4️⃣', end=' ')  # Cubo 4
          elif celula == 5:
            print('5️⃣', end=' ')  # Cubo 5
          elif celula == 6:
            print('6️⃣', end=' ')  # Cubo 6
          elif celula == 7:
            print('7️⃣', end=' ')  # Cubo 7
          elif celula == 8:
            print('8️⃣', end=' ')  # Cubo 8
          elif celula == 9:
            print('9️⃣', end=' ')  # Cubo 9
          elif celula == 10:
            print('🔟', end=' ')  # Cubo 10
# Cubo A a J
          elif celula == 11:
            print(' A', end=' ')  # Cubo A
          elif celula == 12:
            print(' B ', end=' ')  # Cubo B
          elif celula == 13:
            print(' C', end=' ')  # Cubo C
          elif celula == 14:
            print(' D ', end=' ')  # Cubo D
          elif celula == 15:
            print(' E ', end=' ')  # Cubo E
          elif celula == 16:
            print('F', end=' ')  # Cubo F
          elif celula == 17:
            print(' G ', end=' ')  # Cubo G
          elif celula == 18:
            print(' H ', end=' ')  # Cubo H
          elif celula == 19:
            print(' I ', end=' ')  # Cubo I
          elif celula == 20:
            print(' J ', end=' ')  # Cubo J
        print()  # Nova linha para a próxima linha do mapa

# Tamanho do mapa
linhas = 11
colunas = 11

# Inicializa o mapa com os cubos
mapa = inicializar_mapa(linhas, colunas)

# numeros
mapa[1][0] = 1
mapa[2][0] = 2
mapa[3][0] = 3
mapa[4][0] = 4
mapa[5][0] = 5
mapa[6][0] = 6
mapa[7][0] = 7
mapa[8][0] = 8
mapa[9][0] = 9
mapa[10][0] = 10
# letras
mapa[0][1] = 11
mapa[0][2] = 12
mapa[0][3] = 13
mapa[0][4] = 14
mapa[0][5] = 15
mapa[0][6] = 16
mapa[0][7] = 17
mapa[0][8] = 18
mapa[0][9] = 19
mapa[0][10] = 20
# cubos pretos:
mapa[0][0] = 100
mapa[1][6] = 100
mapa[2][6] = 100
mapa[3][6] = 100
mapa[3][5] = 100
mapa[3][4] = 100
mapa[3][3] = 100
mapa[4][3] = 100
mapa[5][3] = 100
mapa[6][3] = 100
mapa[5][5] = 100
mapa[6][5] = 100
mapa[7][5] = 100
mapa[8][5] = 100
mapa[8][4] = 100
mapa[9][4] = 100
mapa[10][4] = 100
# cubos vermelho:
mapa[2][5] = 200
# cubos azul:
mapa[10][5] = 300
# Aluno cesupa:
#mapa[0][0] = 400

# Pontos para calcular a distância
ponto1 = (2, 5)
ponto2 = (10, 5)

# Imprime o mapa
print("Mapa com cubos:")
imprimir_mapa(mapa)



x = [(1,2),(3,6),(6,5)]

mapa[]

spli