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
            print('🟥', end=' ')  # Cubo vermelho (final)
          elif celula == 300:
            print('🟦', end=' ')  # Cubo azul (inicial)
          elif celula == 400:
            print('🟨', end=' ')  # Cubo amarelo (buscado)
          elif celula == 500:
            print('🟩', end=' ')  # Cubo verde (caminho)

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
            print('1️⃣', end=' ')  # Cubo 1
          elif celula == 12:
            print('2️⃣', end=' ')  # Cubo 2
          elif celula == 13:
            print('3️⃣', end=' ')  # Cubo 3
          elif celula == 14:
            print('4️⃣', end=' ')  # Cubo 4
          elif celula == 15:
            print('5️⃣', end=' ')  # Cubo 5
          elif celula == 16:
            print('6️⃣', end=' ')  # Cubo 6
          elif celula == 17:
            print('7️⃣', end=' ')  # Cubo 7
          elif celula == 18:
            print('8️⃣', end=' ')  # Cubo 8
          elif celula == 19:
            print('9️⃣', end=' ')  # Cubo 9
          elif celula == 20:
            print('🔟', end=' ')  # Cubo 10
        print()  # Nova linha para a próxima linha do mapa

# Tamanho do mapa
linhas = 11
colunas = 11

# Inicializa o mapa com os cubos
mapa = inicializar_mapa(linhas, colunas)

# numeros (lateral)
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
# letras (em cima)
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
objetivo = (2,5)
# cubos azul:
mapa[10][5] = 500
posicao = (10,5)

# Imprime o mapa
print("Mapa com cubos:")
imprimir_mapa(mapa)

# Pede ao usuário para inserir a quantidade de cubos pretos
quantidade_cubos_pretos = int(input("Insira a quantidade de cubos pretos que deseja adicionar ou remover: "))

for i in range(quantidade_cubos_pretos):
    linha_cubo_preto = int(input(f"Insira a linha para o cubo preto {i+1} (1-11): "))
    coluna_cubo_preto = int(input(f"Insira a coluna para o cubo preto {i+1} (1-11): "))
    # Configura o cubo preto
    mapa[linha_cubo_preto][coluna_cubo_preto] = 100
    print("")
    imprimir_mapa(mapa)

# Pede ao usuário para inserir a quantidade de cubos brancos para substituir os cubos pretos
quantidade_cubos_brancos = int(input("Insira a quantidade de cubos brancos para substituir os cubos pretos: "))

for i in range(quantidade_cubos_brancos):
    linha_cubo_branco = int(input(f"Insira a linha para o cubo branco {i+1} (1-11): "))
    coluna_cubo_branco = int(input(f"Insira a coluna para o cubo branco {i+1} (1-11): "))
    # Configura o cubo branco
    mapa[linha_cubo_branco][coluna_cubo_branco] = 0
    print("")
    imprimir_mapa(mapa)

# Pede ao usuário para inserir a linha e coluna do cubo vermelho
mudar_posicao = input("Deseja mudar a posição do cubo vermelho? (s/n): ").lower()

if mudar_posicao == 's':
    linha_vermelho = int(input("Insira a linha para o cubo vermelho (1-11): "))
    coluna_vermelho = int(input("Insira a coluna para o cubo vermelho (1-11): "))
    mapa[2][5] = 0
    # Configura o cubo vermelho
    mapa[linha_vermelho][coluna_vermelho] = 200
    objetivo = (linha_vermelho,coluna_vermelho)
    print("")
    imprimir_mapa(mapa)

# Pede ao usuário para inserir a linha e coluna do cubo azul
mudar_posicao = input("Deseja mudar a posição do cubo verde ? (s/n): ").lower()

if mudar_posicao == 's':
    linha_azul = int(input("Insira a linha para o cubo azul (1-11): "))
    coluna_azul = int(input("Insira a coluna para o cubo azul (1-11): "))
    mapa[10][5] = 0
    # Configura o cubo azul
    mapa[linha_azul][coluna_azul] = 300
    posicao = (linha_azul,coluna_azul)
    print("")
    imprimir_mapa(mapa)


# Imprime o mapa
print("")
print("Mapa com cubos:")
imprimir_mapa(mapa)
