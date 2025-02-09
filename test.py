def cantidad_columnas(Matriz):
  for i in Matriz:
    columnas=len(i)
    return columnas
  
def matriz_transpuesta(Matriz):
  columnas=cantidad_columnas(Matriz)
  num_columna=0
  Matriz_t=[] # Estaba iniciandola en cada iteracion
  while num_columna <= columnas-1:
    Columna=[]
    
    for fila in Matriz:
      Columna.append(fila[num_columna])
    print(Columna)
    Matriz_t.append(Columna)
    num_columna+=1

  return Matriz_t
  
if __name__ =="__main__":
  A=[[2,4,6],[3,6,8],[8,1,2],[1,2,3]]
  transpuesta=matriz_transpuesta(A)
  print(transpuesta)