class Charger:
    def __init__(self):
        self.maps=[[]]
        self.position_row=0
        self.position_col=0
        self.tem_row=0
        self.tem_col=0
        self.caja_row=0
        self.caja_col=0
    def create(self):
        self.maps=[
          [2,2,2,2,2,2,2,2,2,2,2,2],
          [2,4,4,4,4,4,4,4,4,4,4,2],
          [2,4,4,4,4,4,4,4,4,4,4,2],
          [2,4,4,4,4,4,4,4,4,4,4,2],
          [2,4,4,4,4,4,4,4,4,4,4,2],
          [2,2,2,2,2,2,2,2,2,2,2,2]]
         
#imprimir mapa
    
    def mapa(self):
        cont=0
        for cont in range(len(self.maps)):
          print(self.maps[cont])
          cont=cont+1

    def posicion(self):
      for a in range(len(self.maps)):
        for b in range (len(self.maps[a])):
          if self.maps[a][b]==0:
             self.position_row=a
             self.position_col=b
             self.tem_row=self.position_row
             self.tem_col=self.position_col

#movimiento hacia la Izquierda
    def move_left (self):
        if self.maps[self.position_row][self.position_col-1]==4:
            self.tem_col=self.position_col
            self.position_col=self.position_col-1
            self.maps[self.tem_row][self.tem_col]=4
            self.maps[self.position_col][self.position_row]=0

#movimiento hacia la Derecha
    def move_right (self):
        if self.maps[self.position_row][self.position_col+1]==4:
            self.position_col=self.position_col+1
            self.maps[self.tem_row][self.tem_col]=4
            self.maps[self.position_col][self.position_row]=0
            self.tem_col=self.position_col

#ARRIBA
    def move_up (self):
         if self.maps[self.position_row-1][self.position_col]==4:
             self.position_row=self.position_row-1
             self.maps[self.tem_row][self.tem_col]=4
             self.maps[self.position_col][self.position_row]=0
             self.tem_row=self.position_row

#Abajo
    def move_down (self):
         if self.maps[self.position_row+1][self.position_col]==4:
             self.position_row=self.position_row+1
             self.maps[self.tem_row][self.tem_col]=4
             self.maps[self.position_col][self.position_row]=0
             self.tem_row=self.position_row
    
    
    def jugar(self):
        self.create()
        self.posicion()
        while True:
            self.mapa()
            move=raw_input("D-right,A-left,W-up,S-down")
            if move == "d" or move=="D" :
                self.move_right()
            elif move=="a" or move=="A":
                self.move_left()
            elif move=="w" or move=="W" :
                self.move_up()
            elif move=="S" or move=="S" :
                self.move_down()

oscar=Charger()
oscar.jugar()

