import pygame

pygame.init()

displayWidth = 1350
displayHeight = 675

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0,255,0)
blue = (0, 0, 255)



detectiveFaceForward = pygame.image.load('Sprites\detForwardRest.png')


def detective(x,y):
    gameDisplay.blit(detectiveFaceForward, (x,y))

x = (displayWidth * 0.45)
y = (displayHeight * .5)

x_change = 0
y_change = 0
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Spray Detectives')

clock = pygame.time.Clock()

dead = False

while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
            
    x+= x_change
    y+= y_change

    gameDisplay.fill (white)
    detective (x,y)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
