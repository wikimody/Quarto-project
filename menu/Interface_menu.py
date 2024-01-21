import pygame

pygame.init()
window = pygame.display.set_mode((1280,720))

menu = pygame.image.load("Menu.png")    # Obraz tła
menu = pygame.transform.scale(menu, (1280, 720))


# nazwy przycisków
smallfont = pygame.font.SysFont('Corbel', 35)
but1 = smallfont.render('Gra z graczem', True, (1,1,1))
but2 = smallfont.render('Gra z komputerem', True, (1,1,1))
but3 = smallfont.render('Gra przez internet', True, (1,1,1))
but4 = smallfont.render('Łatwy', True, (1,1,1))
but5 = smallfont.render('Średni', True, (1,1,1))
but6 = smallfont.render('Trudny', True, (1,1,1))




window.blit(menu, (0, 0))
pygame.display.flip()

def WindowOne (): #pierwsze menu
    run =True
    while run:
        pygame.time.Clock().tick(60) #ograniczenie pętli do 60 powturzeń na secundę
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #przyciski
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 <= mouse[0] <= 820 and 390 <= mouse[1] <= 450:
                    pygame.quit()#zamień na grę z innym graczem
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 <= mouse[0] <= 820 and 470 <= mouse[1] <= 530:
                    pygame.display.quit()
                    WindowTwo() #przejście do drugiego menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 <= mouse[0] <= 820 and 555 <= mouse[1] <= 615:
                    pygame.quit()#zamień na grę przez internet

        #rysowanie napisów
        window.blit(but1, (550, 400))
        window.blit(but2, (525, 485))
        window.blit(but3, (525, 570))
        pygame.display.update()
        pass


def WindowTwo (): #drugie menu
    window2 = pygame.display.set_mode((1280, 720))
    window2.blit(menu, (0, 0))
    run2 =True
    while run2:
        pygame.time.Clock().tick(60)
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 <= mouse[0] <= 820 and 390 <= mouse[1] <= 450:
                    pygame.quit()#zamień na grę z łatwym botem
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 <= mouse[0] <= 820 and 470 <= mouse[1] <= 530:
                    pygame.quit()#zamień na grę z średnim botem
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 480 <= mouse[0] <= 820 and 555 <= mouse[1] <= 615:
                    pygame.quit()#zamień na grę z trudnym botem


        window2.blit(but4, (600, 400))
        window2.blit(but5, (600, 485))
        window2.blit(but6, (600, 570))
        pygame.display.update()
        pass


WindowOne()
