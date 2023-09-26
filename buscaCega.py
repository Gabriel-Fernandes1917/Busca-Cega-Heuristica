from inicarMapa import mapa
from inicarMapa import imprimir_mapa
from inicarMapa import objetivo, posicao
from distancia2Pontos import calcular_distancia_pontos
import math
import time 

mapa
objetivo
posicao
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
    
    #fazer a verificação de blocos validos(inexporaveis e borda) aqui
    descobertaAtual = []
    
    #Este primeiro laço "calcula as bordas"
    for i in range(len(filaDeEstados)):
        # print(listafechada)
        # print(filaDeEstados)
        # print(borda)
        if filaDeEstados[i] not in listafechada:
            # print("add na borda")
            # print(filaDeEstados[i])
            borda.append(filaDeEstados[i])
            # print(f"borda {borda}")


    #explora os sucessores ao redor
    if len(posicao) > 0:

        if posicao[0] - 1 > 0:
            l = posicao[0] - 1
            c = posicao[1]
            for i in range(-1, 2):
                if c+i>0 or c+i<11:
                    if mapa[l][c+i] == 0 or (l,c+i) in borda:
                        mapa[l][c+i] = 300
                        filaDeEstados.append((l,c+i))
                        descobertaAtual.append((l,c+i))
                    
                    if mapa[l][c+i] == 200:
                        imprimir_mapa(mapa)
                        return
        
        l = posicao[0]
        c = posicao[1]
        for i in range(-1, 2):
            if c+i>0 or c+i<11:
                if i!= 0 and mapa[l][c+i] == 0 or (l,c+i) in borda:
                    mapa[l][c+i] = 300
                    filaDeEstados.append((l,c+i))
                    descobertaAtual.append((l,c+i))
                
                if mapa[l][c+i] == 200:
                        imprimir_mapa(mapa)
                        return

        if posicao[0] + 1 < 11:
            l = posicao[0] + 1
            c = posicao[1]
            for i in range(-1, 2):
                if c+i>0 or c+i<11:
                    if mapa[l][c+i] == 0 or (l,c+i) in borda:
                        mapa[l][c+i] = 300
                        filaDeEstados.append((l,c+i))
                        descobertaAtual.append((l,c+i))
                    
                    if mapa[l][c+i] == 200:
                        imprimir_mapa(mapa)
                        return
                        
                    

        imprimir_mapa(mapa)
        buscaHeuristica(descobertaAtual,mapa,objetivo)

    

def buscaHeuristica(descobertaAtual,mapa,objetivo):
    #buscaHeuristica: Esta funão verifica qual posição tem a menor distancia reta ate o obj
    # e chama a função susessores para explorar apartid desse ponto
    
    #colocar a carinha na pisão atual
   
    distancias = []

    print(len(descobertaAtual))
    print(descobertaAtual)
        
    if len(descobertaAtual) > 0:
        for i in range(len(descobertaAtual)):
            distancias.append(math.floor(calcular_distancia_pontos(mapa, descobertaAtual[i], objetivo)))
            
        for i in range(len(distancias)):
            #da merda pq é fica em 2 loops ao msm tempo, provavelmente quando da 2 min
            if distancias[i] == min(distancias):
                iDoMenorDist = i
                print(descobertaAtual[iDoMenorDist])
                listafechada.append(descobertaAtual[iDoMenorDist])
                # funBorda(filaDeEstados, listafechada)
                print("avança")
                time.sleep(1)  
                sucessores(descobertaAtual[iDoMenorDist], objetivo,mapa) 
                return  
   

sucessores(posicao, objetivo,mapa)       
    
         


        
       



 
    

