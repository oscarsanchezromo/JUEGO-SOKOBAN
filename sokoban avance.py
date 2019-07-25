'''
   0-personaje
   1-cajas
   2-paredes
   3-metas
   4-pasillo
   5-cajas/metas
   6-personaje/metas
'''
mapa=[[2,2,2,2,2],
      [2,4,4,4,2],
      [2,4,4,4,2],
      [2,2,2,2,2]]  
print (mapa)
position_x=4

while True:
      print (mapa)
      tem_x=position_x
      move = input("a -left,d -rigt")
      if move =='d' and mapa[position_x+1]!=2:
          position_x=position_x+1
      elif move =='a' and mapa[position_x-1]!=2:
           position_x=position_x-1

      mapa[tem_x]=4
      mapa[position_x]=0
mapa=[[2,2,2,2,2],
      [2,4,4,4,2],
      [2,4,4,4,2],
      [2,2,2,2,2]]
mapa[1][3]=0
   position_row=1
   position_col=3
a-left position_col=position_col-1
d-rigth position_col=position_col+1
w-up position_row=position_row-1
s-down position_row=position_row+1
mapa [position_row][position_col]=0


