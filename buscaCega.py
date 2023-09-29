from inicarMapa import mapa
from inicarMapa import imprimir_mapa
from inicarMapa import objetivo, posicao
from distancia2Pontos import calcular_distancia_pontos
import math
import time 

mapa
# objetivo0
# posicao
type(posicao)
filaDeEstados = [] # locais já explorados
listafechada = [] # caminho percorrido
borda = [] # já explorados mas não pecorrido
#back track
#arvore
#Line , colon.  Busca gulosa 
#estrela, glurosa
def sucessores(posicao, objetivo,mapa):
    #esta função exploras os pontos ao redor
    if posicao == 200:
        for i in range(len(listafechada)):
            mapa[listafechada[i][0]][listafechada[i][1]] = 300
        imprimir_mapa(mapa)
        return
    #fazer a verificação de blocos validos(inexporaveis e borda) aqui
    descobertaAtual = []
    
    #Este primeiro laço "calcula as bordas"
    for i in range(len(filaDeEstados)):
        # print(listafechada)
        # print(filaDeEstados)
        if filaDeEstados[i] not in listafechada:
            # print("add na borda")
            # print(filaDeEstados[i])
            borda.append(filaDeEstados[i])

    #mostra os detalhes da busca 
    print(f"borda: {borda}")
    print(f"lista fechada {listafechada}")


    #explora os sucessores ao redor
    if len(posicao) > 0:

        if posicao[0] - 1 > 0:
            l = posicao[0] - 1
            c = posicao[1]
            for i in range(-1, 2):
                if c+i>0 or c+i<11:
                    if mapa[l][c+i] == 0 or (l,c+i) in borda:
                            mapa[l][c+i] = 400
                            if (l,c+i) not in filaDeEstados:
                                filaDeEstados.append((l,c+i))
                            if mapa[l][c+i] not in listafechada:
                                descobertaAtual.append((l,c+i))
                    
                    if mapa[l][c+i] == 200:
                        for i in range(len(listafechada)):
                            mapa[listafechada[i][0]][listafechada[i][1]] = 300
                        imprimir_mapa(mapa)
                        return
        
        l = posicao[0]
        c = posicao[1]
        for i in range(-1, 2):
            if c+i>0 or c+i<11:
                if i!= 0 and mapa[l][c+i] == 0 or (l,c+i) in borda:
                        mapa[l][c+i] = 400
                        if (l,c+i) not in filaDeEstados:
                                filaDeEstados.append((l,c+i))
                        if mapa[l][c+i] not in listafechada:
                            descobertaAtual.append((l,c+i))
                
                if mapa[l][c+i] == 200:
                        mapa[listafechada[i][0]][listafechada[i][1]] = 300
                        imprimir_mapa(mapa)
                        return

        if posicao[0] + 1 < 11:
            l = posicao[0] + 1
            c = posicao[1]
            for i in range(-1, 2):
                if c+i>0 or c+i<11:
                    if mapa[l][c+i] == 0 or (l,c+i) in borda:
                            mapa[l][c+i] = 400
                            if (l,c+i) not in filaDeEstados:
                                filaDeEstados.append((l,c+i))
                            if mapa[l][c+i] not in listafechada:
                                descobertaAtual.append((l,c+i))
                    
                    if mapa[l][c+i] == 200:
                        mapa[listafechada[i][0]][listafechada[i][1]] = 300
                        imprimir_mapa(mapa)
                        return
                        

        

        imprimir_mapa(mapa)
        buscaHeuristica(posicao, descobertaAtual,mapa,objetivo)

    

def buscaHeuristica(posicao, descobertaAtual,mapa,objetivo):
    #buscaHeuristica: Esta funão verifica qual posição tem a menor distancia reta ate o obj
    # e chama a função susessores para explorar apartid desse ponto
    
    #colocar a carinha na pisão atual
   
    distancias = []

    # print(len(descobertaAtual))
    print(f"Descoberta atual {descobertaAtual}")
        
    if len(descobertaAtual) > 0:
        for i in range(len(descobertaAtual)):
            distancias.append(math.floor(calcular_distancia_pontos(mapa, descobertaAtual[i], objetivo)))
            
        for i in range(len(distancias)):
            #da merda pq é fica em 2 loops ao msm tempo, provavelmente quando da 2 min
            if distancias[i] == min(distancias) and distancias[i] not in listafechada:
                # print(f"lista fechada {listafechada}") 
                iDoMenorDist = i
                print(f"Escolheu {descobertaAtual[iDoMenorDist]}")
                # mapa[descobertaAtual[iDoMenorDist][0]][descobertaAtual[iDoMenorDist][1]] = 300
                listafechada.append(descobertaAtual[iDoMenorDist])
                # funBorda(filaDeEstados, listafechada)
                # print("avança")
                time.sleep(3)  
                # print("sucessores")
                # print(descobertaAtual[iDoMenorDist], objetivo,mapa)
                sucessores(descobertaAtual[iDoMenorDist], objetivo,mapa) 
                return  
        return
    return
          


sucessores(posicao, objetivo,mapa)       
    
         


        
       



 
    

