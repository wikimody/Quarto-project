import pygame

pygame.init()
window = pygame.display.set_mode((1300,720))

plansza = pygame.image.load("Plansza.png")    # Obraz plaszy
plansza = pygame.transform.scale(plansza, (720, 720))

class Pawn:
    def __init__(self,x,y,look):
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

    def draw (self):
        x = self.cor_x
        y = self.cor_y
        window.blit(self.image,(x,y))

    def locking(self):
        self.state = False
    def unlocking(self):
        self.state = True

    def update_cords(self,x,y):
        if not self.state:
            return
        if self.size:
            self.cor_x = x-60
            self.cor_y = y-60
        else:
            self.cor_x = x - 40
            self.cor_y = y - 40

    def place (self):
        if self.size:
            return self.cor_x ,self.cor_x+120,self.cor_y,self.cor_y+120
        else:
            return self.cor_x ,self.cor_x+80,self.cor_y,self.cor_y+80

    def snap (self):
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


    def snap_prep (self):
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

    def stage_snap(self,stage,number):
        if stage == -1:
            if 1070 < self.cor_x < 1300 and 480 < self.cor_y < 700:
                self.update_cords(1200, 590)
                self.locking()
                return number
        return stage




def add_pawns():
    pawns = []
    pawns.append(Pawn(770,10,'WKPM.png'))
    pawns.append(Pawn(750,105,'WKPD.png'))
    pawns.append(Pawn(770,240,'WKDM.png'))
    pawns.append(Pawn(750, 340, 'WKDD.png'))
    pawns.append(Pawn(770, 480, 'WOPM.png'))
    pawns.append(Pawn(750, 580, 'WOPD.png'))
    pawns.append(Pawn(950, 10, 'WODM.png'))
    pawns.append(Pawn(930, 105, 'WODD.png'))
    pawns.append(Pawn(950, 240, 'BKPM.png'))
    pawns.append(Pawn(930, 340, 'BKPD.png'))
    pawns.append(Pawn(950, 480, 'BKDM.png'))
    pawns.append(Pawn(930, 580, 'BKDD.png'))
    pawns.append(Pawn(1120, 10, 'BOPM.png'))
    pawns.append(Pawn(1100, 105, 'BOPD.png'))
    pawns.append(Pawn(1120, 240, 'BODM.png'))
    pawns.append(Pawn(1100, 340, 'BODD.png'))
    return pawns

pawns = add_pawns()

def activate_pawn(number):
    pawns[number].unlocking()
    pawns[number].update_cords(1180,590)

def moving_pawns(event,presed,wchich,table):
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

def moving_choice(event,presed,wchich,stage):
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
        stage = pawns[wchich].stage_snap(stage,wchich)
    return presed,stage

def choice (table):
    stage = -1
    for n in pawns:
        n.unlocking()
    for n in range(16):
        for i in range(4):
            if n in table[i]:
                pawns[n].locking()

    run = True
    presed = False

    while run:
        pygame.time.Clock().tick(100)  # ograniczenie pętli do 60 powturzeń na secundę

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            for n in range(16):
                presed, stage = moving_choice(event, presed, n,stage)

        window.fill((1, 1, 1))
        window.blit(plansza, (0, 0))
        pygame.draw.rect(window, (0, 0, 255), pygame.Rect(1070, 480, 220, 220))

        for n in pawns:
            n.draw()

        pygame.display.update()
        for n in range(16):
            if n == stage:
                run = False

        pass

    WindowOne(stage,table)
    return table,




def ending ():
    run = True
    while run:
        pygame.time.Clock().tick(30) #ograniczenie pętli do 60 powturzeń na secundę
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

def WindowOne (wchich,table): #pierwsze menu
    run =True
    activate_pawn(wchich)
    presed = False

    while run:
        pygame.time.Clock().tick(100) #ograniczenie pętli do 60 powturzeń na secundę


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
    choice(table)
    return table

table = [[-1]*4 for _ in range(4)]


WindowOne(0,table)

ending()

