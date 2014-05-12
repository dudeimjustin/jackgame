import pygame

pygame.init()

window = pygame.display.set_mode((800,600))

pygame.display.set_caption("Window")

black = (0,0,0)

white = (255,255,255)

clock = pygame.time.Clock()

# Jack sprites
jack1 = pygame.image.load("images/jack1.png")
jack2 = pygame.image.load("images/jack2.png")

jackCurrentImage = 1


gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):

            gameLoop=False

    window.fill(white)

    if (jackCurrentImage==1):

        window.blit(jack1, (10,10))

    if (jackCurrentImage==2):
        
        window.blit(jack2, (10,10))

    if (jackCurrrentImage==2):

        jackCurrentImage=1

    else:

        jackCurrentImage+=1;

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
