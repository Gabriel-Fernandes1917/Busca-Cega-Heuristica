from inicarMapa import mapa
from inicarMapa import imprimir_mapa
from inicarMapa import objetivo, posicao
from distancia2Pontos import calcular_distancia_pontos
import math
import time 
from backTrack import backTrack

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
    descobertaAtual =[]
    
    
    if posicao[0] - 1 > 0:
        l = posicao[0] - 1
        c = posicao[1]
        for i in range(-1, 2):
            if c+i>0 or c+i<11:
                if mapa[l][c+i] == 0:
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
            if i!= 0 and mapa[l][c+i] == 0:
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
                if mapa[l][c+i] == 0:
                    mapa[l][c+i] = 300
                    filaDeEstados.append((l,c+i))
                    descobertaAtual.append((l,c+i))
                
                if mapa[l][c+i] == 200:
                    imprimir_mapa(mapa)
                    return
                    
                

    imprimir_mapa(mapa)
    buscaHeuristica(descobertaAtual,mapa,objetivo,filaDeEstados)
    

def buscaHeuristica(descobertaAtual,mapa,objetivo,filaDeEstados):
    #buscaHeuristica: Esta funão verifica qual posição tem a menor distancia reta ate o obj
    # e chama a função susessores para explorar apartid desse ponto
    
    #colocar a carinha na pisão atual
    global ibacktack
    ibacktack = 0
    distancias = []
    print(descobertaAtual)
    if len(descobertaAtual) > 0 :
        ibacktack = 0
        for i in range(len(descobertaAtual)):
            distancias.append(math.floor(calcular_distancia_pontos(mapa, descobertaAtual[i], objetivo)))
        
        for i in range(len(distancias)):
            if distancias[i] == min(distancias):
                iDoMenorDist = i
                print(descobertaAtual[iDoMenorDist])
                listafechada.append(descobertaAtual[iDoMenorDist])
                sucessores(descobertaAtual[iDoMenorDist], objetivo,mapa) 
        time.sleep(5)
    else:
        print("voltando")
        ibacktack+1
        # for e in filaDeEstados[::-1]:
        #    filaDeEstados[ibacktack]
        #    sucessores(e[ibacktack], objetivo,mapa) 



    #aqui da o erro quando não á mais quadradros brancos para prosseguir.
    #Usar o try: except: para tentar chamar a funcao, se der ruim chama a funcao de voltar 
    #posições anteriores na fila de estados
    # try:
    #     ibacktack = 1
    #     sucessores(descobertaAtual[iDoMenorDist], objetivo,mapa) 
    # except:
    #     #funçaao voltar posicao
    #     backTrack(filaDeEstados, ibacktack)
    #     ibacktack = ibacktack+1
    

