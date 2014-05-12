import pygame

pygame.init()

window = pygame.display.set_mode((800,600))

pygame.display.set_caption("Window")

black = (0,0,0)

white = (255,255,255)

x,y=0,0

gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):

            gameLoop=False

        if (event.type==pygame.KEYDOWN):

            if (event.key==pygame.K_LEFT):

                x-=10

            if (event.key==pygame.K_RIGHT):

                x+=10

            if (event.key==pygame.K_UP):

                y-=10

            if (event.key==pygame.K_DOWN):

                y+=10

    window.fill(black)

    pygame.draw.rect(window,white,(x,y,50,50))

    pygame.display.flip()

pygame.quit()
