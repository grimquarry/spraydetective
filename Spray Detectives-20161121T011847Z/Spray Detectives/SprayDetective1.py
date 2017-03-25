import pygame

pygame.init()

window = pygame.display.set_mode ((1300, 630))

pygame.display.set_caption("Spray Detective")

black = (0,0,0)
white = (255, 255, 255)

x=0
y=0

movex=0
movey=0

clock = pygame.time.Clock()

detfr = pygame.image.load('Sprites\detForwardRest.png')
detflu = pygame.image.load('Sprites\\flu.png')
detfru = pygame.image.load ('Sprites\\fru.png')

detectiveCurrentImage = 1

gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):
            gameLoop=False

    window.fill(white)
    
    if (detectiveCurrentImage==1):
        window.blit(detflu, (10, 10))

    if (detectiveCurrentImage==2):
        window.blit (detfru, (10,10))

    if (detectiveCurrentImage == 2):
        detectiveCurrentImage=1

    else:
        detectiveCurrentImage +=1;
        
    pygame.display.flip()

    clock.tick(5)

pygame.quit()
