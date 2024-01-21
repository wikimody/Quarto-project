import pygame

pygame.init()
window = pygame.display.set_mode((1300,720))

plansza = pygame.image.load("Plansza.png")    # Obraz plaszy
plansza = pygame.transform.scale(plansza, (720, 720))

class Pawn:
    def __init__(self,x,y,look,identy):
        self.cor_x = x
        self.cor_y = y
        self.state = False
        look2 = pygame.image.load(look)
        if look[3]== 'D':
            self.image = pygame.transform.scale(look2, (120, 120))
            self.size = True
        else:
            self.image = pygame.transform.scale(look2, (80, 80))
            self.size = False
        self.id = identy

    def draw (self):  #rysuje pionek
        x = self.cor_x
        y = self.cor_y
        window.blit(self.image,(x,y))

    def locking(self):  # nie morze się ruszać
        self.state = False
    def unlocking(self): #morze się ruszać
        self.state = True
    def find_state(self): #sprawdza czy morze się ruszać
        return self.state

    def update_cords(self,x,y): # rusza pionek
        if not self.state:
            return
        if self.size:
            self.cor_x = x-60
            self.cor_y = y-60
        else:
            self.cor_x = x - 40
            self.cor_y = y - 40

    def place (self):   # zwraca koedynaty zajmowane przez pionek
        if self.size:
            return self.cor_x ,self.cor_x+120,self.cor_y,self.cor_y+120
        else:
            return self.cor_x ,self.cor_x+80,self.cor_y,self.cor_y+80

    def snap (self):     #przenosi pionak na miejsce w planszy
        if self.state:
            if self.size:
                for x in range(4):
                    for y in range(4):
                        if x * 170  < self.cor_x < x * 170 + 110 and y * 170  < self.cor_y < y * 170 + 110:
                            self.update_cords(x * 170 + 110, y * 170 + 110)
                            self.locking()

            else:
                for x in range(4):
                    for y in range (4):
                        if  x*170 +20<self.cor_x <x*170 +140 and  y*170 +20<self.cor_y<y*170 +140:
                            self.update_cords(x*170+110,y*170+110)
                            self.locking()


    def snap_prep (self):   #sprawdza czy pionek jest na miejscu w planszy
        if self.state:
            if self.size:
                for x in range(4):
                    for y in range(4):
                        if x * 170  < self.cor_x < x * 170 + 110 and y * 170  < self.cor_y < y * 170 + 110:
                            return x,y

            else:
                for x in range(4):
                    for y in range (4):
                        if  x*170 +20<self.cor_x <x*170 +140 and  y*170 +20<self.cor_y<y*170 +140:
                            return x,y
        return

    def updating (self,table):  #dostosowanie pionków do tablicy
        for a in range(4):
            for b in range(4):
                if table[a][b]== self.id:
                    if self.size:
                        self.cor_x = a * 170 + 50
                        self.cor_y = b * 170 + 50
                    else:
                        self.cor_x = a * 170 + 70
                        self.cor_y = b * 170 + 70
                    self.locking()





def add_pawns():    #metoda na dodanie wszystkich pionków
    pawns = []
    pawns.append(Pawn(770,10,'WKPM.png',0))
    pawns.append(Pawn(750,105,'WKPD.png',1))
    pawns.append(Pawn(770,240,'WKDM.png',2))
    pawns.append(Pawn(750, 340, 'WKDD.png',3))
    pawns.append(Pawn(770, 480, 'WOPM.png',4))
    pawns.append(Pawn(750, 580, 'WOPD.png',5))
    pawns.append(Pawn(950, 10, 'WODM.png',6))
    pawns.append(Pawn(930, 105, 'WODD.png',7))
    pawns.append(Pawn(950, 240, 'BKPM.png',8))
    pawns.append(Pawn(930, 340, 'BKPD.png',9))
    pawns.append(Pawn(950, 480, 'BKDM.png',10))
    pawns.append(Pawn(930, 580, 'BKDD.png',11))
    pawns.append(Pawn(1120, 10, 'BOPM.png',12))
    pawns.append(Pawn(1100, 105, 'BOPD.png',13))
    pawns.append(Pawn(1120, 240, 'BODM.png',14))
    pawns.append(Pawn(1100, 340, 'BODD.png',15))
    return pawns

pawns = add_pawns() #tworzenie najwarzniejszej listy w programie

def activate_pawn(number): #metoda na przygotowanie pionka do ruchu
    pawns[number].unlocking()
    pawns[number].update_cords(1180,590)

def moving_pawns(event,presed,wchich,table): # metoda na ruszanie pionków
    mouse = pygame.mouse.get_pos()
    # czy myszka jest wciśnięta
    if event.type == pygame.MOUSEBUTTONDOWN:
        presed = True
    if event.type == pygame.MOUSEBUTTONUP:
        presed = False

    if presed and event.type == pygame.MOUSEMOTION:
        a, b, c, d = pawns[wchich].place()
        if a <= mouse[0] <= b and c <= mouse[1] <= d:
            pawns[wchich].update_cords(mouse[0], mouse[1])

    if event.type == pygame.KEYDOWN:
        try:
            a,b = pawns[wchich].snap_prep()
            if table[a][b] == -1:
                pawns[wchich].snap()
                table[a][b]= wchich

        except:
            pass



    return presed,table

def moving_choice(event,wchich,stage):  # metoda na wybieranie pionków
    mouse = pygame.mouse.get_pos()

    if event.type == pygame.KEYDOWN:
        if pawns[wchich].find_state():
            if stage==-1:
                a,b,c,d = pawns[wchich].place()
                if a <= mouse[0] <= b and c <= mouse[1] <= d:
                    stage =wchich
    return stage

def choice (table): #plansza na wybieranie pionka przeciwnika
    stage = -1
    for n in pawns:
        n.unlocking()
    for n in range(16):
        for i in range(4):
            if n in table[i]:
                pawns[n].locking()

    run = True

    while run:
        pygame.time.Clock().tick(100)  # ograniczenie pętli do 60 powturzeń na secundę

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            for n in range(16):
                stage = moving_choice(event, n ,stage)

        window.fill((1, 1, 1))
        window.blit(plansza, (0, 0))
        pygame.draw.rect(window, (0, 0, 255), pygame.Rect(1070, 480, 220, 220))

        for n in pawns:
            n.draw()

        pygame.display.update()
        if 0<=stage<=15:
            run = False

        pass

    for n in pawns:
        n.locking()
    Move(stage,table)# to delete in final version
    return table,stage




def ending (table):     # Plansza na wyświetlanie końcowej planszy
    for n in pawns:
        n.updating(table)
    run = True
    while run:
        pygame.time.Clock().tick(60) #ograniczenie pętli do 60 powturzeń na secundę
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill((1,1,1))
        window.blit(plansza, (0, 0))
        pygame.draw.rect(window,(0, 0, 255),pygame.Rect(1070, 480, 220, 220))
        for n in pawns:
            n.draw()
        pygame.display.update()
        pass

def Move (wchich, table): # Plansza na rozgrywanie twojego ruchu
    run =True
    activate_pawn(wchich)
    presed = False
    for n in pawns:
        n.updating(table)

    while run:
        pygame.time.Clock().tick(100) #ograniczenie pętli do 100 powturzeń na secundę


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            presed, table = moving_pawns(event,presed,wchich,table)

        window.fill((1,1,1))
        window.blit(plansza, (0, 0))
        pygame.draw.rect(window,(0, 0, 255),pygame.Rect(1070, 480, 220, 220))

        for n in pawns:
            n.draw()


        pygame.display.update()
        for n in range(4):
            if wchich in table[n]:
                run=False

        pass
    table,stage =choice(table)# to get next move
    return table , stage


table = [[-1]*4 for _ in range(4)]# to delete in final version


table=Move(0,table)# to delete in final version

ending(table)# to delete in final version
