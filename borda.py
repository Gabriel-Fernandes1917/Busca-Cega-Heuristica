

def funBorda(filaDeEstados, listafechada, borda):

  for i in range(len(filaDeEstados)):
    print(listafechada)
    print(filaDeEstados)
    
    if filaDeEstados[i] in listafechada == False:
      print(f"Já passou por {filaDeEstados[i]}")

  
   
   




filaDeEstados = [(1,2),(1,4),(1,5),(3,9),(4,7)]
listafechada = [(5,4),(6,4),(1,2),(1,5)]
borda = []
  
x = 1
y = 2
funBorda(filaDeEstados, listafechada, borda)

if (x,y) not in listafechada:
  borda.append(filaDeEstados[1])














def funBorda(filaDeEstados, listafechada):
  print("fun borda")
  for i in range(len(filaDeEstados)):
    print(listafechada)
    print(filaDeEstados)
    print(borda)
    if filaDeEstados[i] not in listafechada:
      print("add na borda")
      print(filaDeEstados[i])
      borda.append(filaDeEstados[i])
      print(f"borda {borda}")
      

    return  