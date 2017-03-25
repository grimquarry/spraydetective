import pygame

pygame.init()

window = pygame.display.set_mode ((1300, 630))

pygame.display.set_caption("Spray Detective")

black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)

#The video that shows what you want!: https://www.youtube.com/watch?v=qgs9Y-lxHA0

#https://www.reddit.com/r/pygame/comments/2mrbme/boundaries_in_my_game/
moveX=0
moveY=0

clock = pygame.time.Clock()



class Horizontal_Wall(pygame.sprite.Sprite):
    def __init__(self, color = white, width = 1300, height = 25):
        super(Horizontal_Wall, self).__init__()

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery
    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

class Vertical_Wall(pygame.sprite.Sprite):
    def __init__(self, color = white, width = 25, height = 630):
        super(Vertical_Wall, self).__init__()

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery
    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y


        


#http://pygame.org/project-Rect+Collision+Response-1061-.html
#Border Variables
left_wall = Vertical_Wall(white, 0,0)
left_wall.set_position(100,100)

top_wall = Horizontal_Wall()
top_wall.set_position(100,0)
                     
right_wall = Vertical_Wall()
right_wall.set_position(1150, 0)

bottom_wall = Horizontal_Wall()
bottom_wall.set_position(0, 475)
                

wall_group = pygame.sprite.Group()
wall_group.add(left_wall, top_wall, right_wall, bottom_wall)              


gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):
            gameLoop=False



    #if player.x == 25 and direction == "left" :
        #moveX = 0
    #if player.x == 25 and direction == "right" :
        #moveX += speed - speed

    #if player.y == -25 and direction == "up":
        #moveY = 0
    #if player.y == -25 and direction == "down":
        #moveY += speed - speed

    #if player.x == 1080 and direction == "right":
        #moveX = 0
    #if player.x == 1080 and direction == "left":
        #moveX -= speed - speed

    #if player.y == 390 and direction == "down":
        #moveY = 0
    #if player.y == 390 and direction == "up":
        #moveY -= speed - speed"""

    wall_group.draw(window)
    




        
    pygame.display.update()
    

    clock.tick(60)



pygame.quit()
