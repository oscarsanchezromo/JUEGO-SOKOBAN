'''
   0.- personaje
   1.- cajas
   2.- metas
   3.- paredes
   4.- pasillo
   5.- caja/meta
   6.-personaje/meta
'''
mapa=[[3, 3, 3, 3, 3],
      [3, 4, 0, 4, 3],
      [3, 1, 2, 4, 3], 
      [3, 3, 3, 3, 3]]

position_col= 3
position_row= 1

def printMapa():
  for x in range(len(mapa)):
    for y in range(len(mapa[x])):
     print(mapa[x][y], end= " ")
    print()
printMapa()
while True:
  move=input('a_left,d_rigth')
  #derecha
  if move =="d":
    if mapa[position_row][position_col]==0 and mapa[position_row][position_col+1]==4:
       mapa [position_row] [position_col]=4
       mapa [position_row] [position_col +1]=0
       position_col=position_col+1 
    printMapa()