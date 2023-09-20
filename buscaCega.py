from inicarMapa import mapa
from inicarMapa import imprimir_mapa
from inicarMapa import objetivo, posicao

mapa
objetivo
posicao
type(posicao)
filaDeEstados = []
listafechada = []
#back track
#arvore
#Line , colon.  Busca gulosa 
#estrela, glurosa
def sucessores(posicao, objetivo,mapa):
    
    if posicao[0] - 1 > 0:
        l = posicao[0] - 1
        c = posicao[1]
        for i in range(-1, 2):
            if c+i>0 or c+i<11:
                if mapa[l][c+i] == 0:
                    #add a condicional que se der o ponto
                    #vermelho ele termina a operação
                    mapa[l][c+i] = 300
                    filaDeEstados.append((l,c+i))
    
    l = posicao[0]
    c = posicao[1]
    for i in range(-1, 2):
        if c+i>0 or c+i<11:
            if i!= 0 and mapa[l][c+i] == 0:
                mapa[l][c+i] = 300
                filaDeEstados.append((l,c+i))

    if posicao[0] + 1 < 11:
        l = posicao[0] + 1
        c = posicao[1]
        for i in range(-1, 2):
            if c+i>0 or c+i<11:
                if mapa[l][c+i] == 0:
                    mapa[l][c+i] = 300
                    filaDeEstados.append((l,c+i))

    
    mapaBuca = mapa
    imprimir_mapa(mapa)
    return mapaBuca

def buscaHeuristica(filaDeEstados):
    #colocar a carinha na pisão atual
    #medir a posiçao com menor caminha reta
    #se chegar em um ponto que não tem saida ele volta
    

    return

