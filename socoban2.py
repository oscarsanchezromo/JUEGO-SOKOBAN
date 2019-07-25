'''
   0=personaje
   1=cajas
   2=paredes
   3=metas
   4=pasillo
   5=cajas/metas
   6=personaje/metas
'''
mapa=[[2,2,2,2,2,2,2],
      [2,4,4,0,4,4,2],
      [2,4,4,4,4,4,2],
      [2,2,2,2,2,2,2],]
for row in range(len(mapa)):
    for col in range (len(mapa[row])):
        print(mapa[row][col], end=" " )
    
    print("")
    mapa[1][3]=0
   position_row=1
   position_col=3
a-left position_col=position_col-1
d-rigth position_col=position_col+1
w-up position_row=position_row-1
s-down position_row=position_row+1
mapa [position_row][position_col]=0

>>> Left movement rules

if mapa[position_row][position_col]==6 and mapa[position_col][position]==1
      mapa[position_row][position_col]==0 and mapa[position_col][position_row]==4
      mapa[position_row][position_col]==1
      position_col=position_col+1