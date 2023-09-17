import math
from inicarMapa import objetivo, posicao, inicializar_mapa

def calcular_distancia_pontos(matriz, ponto1, ponto2):

    x1, y1 = ponto1
    x2, y2 = ponto2

    # Verifica se as coordenadas dos pontos estão dentro da matriz
    if x1 < 1 or x1 >= 11 or y1 < 0 or y1 >= 11 or x2 < 1 or x2 >= 11 or y2 < 1 or y2 >= 11:
        raise ValueError("Coordenadas dos pontos estão fora da matriz")

    # Calcula a distância em linha reta usando a fórmula da distância euclidiana
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # arredondaDist =  
    return distancia


# Calcula a distância entre os pontos na matriz
distancia = calcular_distancia_pontos(inicializar_mapa, ponto1, ponto2)
print(f"A distância entre {ponto1} e {ponto2} na matriz é: {distancia:.2f}")