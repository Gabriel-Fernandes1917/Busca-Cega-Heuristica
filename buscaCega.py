from inicarMapa import mapa
from inicarMapa import imprimir_mapa
from inicarMapa import objetivo, posicao

mapa
objetivo
posicao
type(posicao)
filaDeEstados = []
#Line , colon
def buscaLargura(posicao, objetivo,mapa):
    
    if posicao[0] - 1 > 0:
        l = posicao[0] - 1
        c = posicao[1]
        for i in range(-1, 2):
            if c+i>0 or c+i<11:
                if mapa[l][c+i] == 0:
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
    return mapaBuca

def buscaHeuristica(filaDeEstados):

    return

buscaLargura(posicao,objetivo,mapa)