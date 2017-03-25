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

class Detective(pygame.sprite.Sprite):
    def __init__(self,x=50,y=75):
        super(Detective, self).__init__()
        self.x= x
        self.y= y
        #self.width=50
        #self.height=50
        self.image = pygame.Surface((x, y))
        self.set_properties()
        self.hspeed = 0
        self.vspeed = 0



        self.detfr = pygame.image.load('Sprites\detForwardRest.png')
        self.detflu = pygame.image.load('Sprites\\flu.png')
        self.detfru = pygame.image.load ('Sprites\\fru.png')
        self.detlld = pygame.image.load ('Sprites\\lld.png')
        self.detlr = pygame.image.load ('Sprites\\lr.png')
        self.detlru = pygame.image.load ('Sprites\\lru.png')
        self.detrlu = pygame.image.load ('Sprites\\rlu.png')
        self.detrr = pygame.image.load ('Sprites\\rr.png')
        self.detrrd = pygame.image.load ('Sprites\\rrd.png')
        self.detulu = pygame.image.load ('Sprites\\ulu.png')
        self.detur = pygame.image.load ('Sprites\\ur.png')
        self.deturu = pygame.image.load ('Sprites\\uru.png')
        self.detaflu = pygame.image.load ('Sprites\\aflu.png')
        self.detafr1 = pygame.image.load ('Sprites\\afr1.png')
        self.detafr2 = pygame.image.load ('Sprites\\afr2.png')
        self.detafru = pygame.image.load ('Sprites\\afru.png')
        self.detallu = pygame.image.load ('Sprites\\allu.png')
        self.detalr1 = pygame.image.load ('Sprites\\alr1.png')
        self.detalr2 = pygame.image.load ('Sprites\\alr2.png')
        self.detalru = pygame.image.load ('Sprites\\alru.png')
        self.detarlu = pygame.image.load ('Sprites\\arlu.png')
        self.detarr1 = pygame.image.load ('Sprites\\arr1.png')
        self.detarr2 = pygame.image.load ('Sprites\\arr2.png')
        self.detarru = pygame.image.load ('Sprites\\arru.png')
        self.detaulu = pygame.image.load ('Sprites\\aulu.png')
        self.detaur1 = pygame.image.load ('Sprites\\aur1.png')
        self.detaur2 = pygame.image.load ('Sprites\\aur2.png')
        self.detauru = pygame.image.load ('Sprites\\auru.png')
        self.timeTarget=10
        self.timeNum=0
        self.currentImage=0
        self.direction="RestDown"
        self.attack="NoAttack"
        #self.sound = pygame.mixer.Sound("step.wav")
        

    #def play_step(self):
        #self.sound.play()

    def set_properties (self):

        self.rect = self.image.get_rect()

        self.origin_x = self.rect.x
        self.origin_y = self.rect.y


    def set_position(self, x , y):
        self.rect.x = x - self.origin_x 
        self.rect.y = y - self.origin_y 

    def change_speed(self, hspeed, vspeed):
        self.hspeed += hspeed
        self.vspeed += vspeed

    def update (self, collidable):


        self.timeNum+=1
        

        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_DOWN):
                self.direction="down"
            if (event.key==pygame.K_UP):
                self.direction="up"
            if (event.key==pygame.K_RIGHT):
                self.direction="right"
            if (event.key==pygame.K_LEFT):
                self.direction="left"
            if (event.key==pygame.K_SPACE):
                self.attack="attack"


        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_DOWN):
                self.direction="RestDown"
            if (event.key==pygame.K_UP):
                self.direction="RestUp"
            if (event.key==pygame.K_RIGHT):
                self.direction="RestRight"
            if (event.key==pygame.K_LEFT):
                self.direction="RestLeft"
            if (event.key==pygame.K_SPACE):
                self.attack="NoAttack"

        self.rect.x += self.hspeed
        collision_list = pygame.sprite.spritecollide(self, collidable, False)

        for collided_object in collision_list:
            if (self.hspeed > 0 and self.direction == "right"):
                self.rect.right = collided_object.rect.left
            elif (self.hspeed < 0 and self.direction == "left"):
                self.rect.left = collided_object.rect.right
                
        self.rect.y += self.vspeed
        collistion_list = pygame.sprite.spritecollide(self, collidable, False)
        for collided_object in collision_list:
            if (self.vspeed > 0 and self.direction == "down"):
                self.rect.bottom = collided_object.rect.top
            elif (self.vspeed < 0 and self.direction == "up"):
                self.rect.top = collided_object.rect.bottom
            

        if (self.timeNum==self.timeTarget):

            if (self.currentImage==0):
                self.currentImage+=1

            else:
                self.currentImage=0
            self.timeNum=0


        self.detfr    
        self.render()
        

    def render(self):

        self.align = 75

        #Run Animation
        if (self.direction=="down" and not self.attack=="attack"):
            if (self.currentImage==0):
                window.blit(self.detflu, (self.rect.x - self.align, self.rect.y - self.align))
                #self.play_step()
            else:
                window.blit(self.detfru, (self.rect.x - self.align, self.rect.y - self.align))
                #self.play_step()

        if (self.direction=="up" and not self.attack=="attack"):
            if (self.currentImage==0):
                window.blit(self.detulu, (self.rect.x - self.align, self.rect.y - self.align))
                #self.play_step()
            else:
                window.blit(self.deturu, (self.rect.x - self.align, self.rect.y - self.align))
                #self.play_step()    
        if (self.direction=="left" and not self.attack=="attack"):
            if (self.currentImage==0):
                window.blit(self.detlld, (self.rect.x - self.align, self.rect.y - self.align))
                #self.play_step()
            else:
                window.blit(self.detlru, (self.rect.x - self.align, self.rect.y - self.align))
                #self.play_step()
        if (self.direction=="right" and not self.attack=="attack"):
            if (self.currentImage==0):
                window.blit(self.detrlu, (self.rect.x - self.align, self.rect.y - self.align))
                #self.play_step()
            else:
                window.blit(self.detrrd, (self.rect.x - self.align, self.rect.y - self.align))
                #self.play_step()

            #Run and attack animations
        if (self.attack=="attack" and self.direction=="down"):
                if (self.currentImage==0):
                    window.blit(self.detaflu, (self.rect.x - self.align, self.rect.y - self.align))
                else:         
                    window.blit(self.detafru, (self.rect.x - self.align, self.rect.y - self.align))

        if (self.attack=="attack" and self.direction=="up"):
            if (self.currentImage==0):
                window.blit(self.detaulu, (self.rect.x - self.align, self.rect.y - self.align))
            else:
                window.blit(self.detauru, (self.rect.x - self.align, self.rect.y - self.align))

        if (self.attack=="attack" and self.direction=="right"):
            if (self.currentImage==0):
                window.blit (self.detarlu, (self.rect.x - self.align, self.rect.y - self.align))
            else:
                window.blit (self.detarru, (self.rect.x - self.align, self.rect.y - self.align))

        if (self.attack=="attack" and self.direction=="left"):
            if (self.currentImage==0):
                window.blit (self.detallu, (self.rect.x - self.align, self.rect.y - self.align))
            else:
                window.blit (self.detalru, (self.rect.x - self.align, self.rect.y - self.align))

        #Attack Standing Still
        if (self.attack=="attack" and self.direction=="RestDown"):
            if (self.currentImage==0):
                window.blit (self.detafr1, (self.rect.x - self.align, self.rect.y - self.align))
            else:
                window.blit (self.detafr2, (self.rect.x - self.align, self.rect.y - self.align))

        if (self.attack=="attack" and self.direction=="RestUp"):
            if (self.currentImage==0):
                window.blit (self.detaur1, (self.rect.x - self.align, self.rect.y - self.align))
            else:
                window.blit (self.detaur2, (self.rect.x - self.align, self.rect.y - self.align))

        if (self.attack=="attack" and self.direction=="RestRight"):
            if (self.currentImage==0):
                window.blit (self.detarr1, (self.rect.x - self.align, self.rect.y - self.align))
            else:
                window.blit (self.detarr2, (self.rect.x - self.align, self.rect.y - self.align))

        if (self.attack=="attack" and self.direction=="RestLeft"):
            if (self.currentImage==0):
                window.blit (self.detalr1, (self.rect.x - self.align, self.rect.y - self.align))
            else:
                window.blit (self.detalr2, (self.rect.x - self.align, self.rect.y - self.align))
                    
        #At Rest Graphics
        if (self.direction=="RestDown" and not self.attack=="attack"):
                window.blit(self.detfr, (self.rect.x - self.align, self.rect.y - self.align))
        if (self.direction=="RestUp" and not self.attack=="attack"):
                window.blit(self.detur, (self.rect.x - self.align, self.rect.y - self.align))
        if (self.direction=="RestLeft" and not self.attack=="attack"):
                window.blit(self.detlr, (self.rect.x - self.align, self.rect.y - self.align))
        if (self.direction=="RestRight" and not self.attack=="attack"):
                window.blit(self.detrr, (self.rect.x - self.align, self.rect.y - self.align))
            #if (event.key==pygame.K_SPACE and self.direction=="RestDown"):
                #window.blit (self.detfr, (self.x, self.y))
            #if (event.key==pygame.K_SPACE and self.direction=="RestUp"):
                #window.blit (self.detur, (self.x, self.y))
            #if (event.key==pygame.K_SPACE and self.direction=="RestRight"):
                #window.blit (self.detrr, (self.x, self.y))
            #if (event.key==pygame.K_SPACE and self.direction=="RestLeft"):
                #window.blit (self.detlr, (self.x, self.y))
            #if (event.key==pygame.K_SPACE and self.direction=="down"):
                #if (self.currentImage==0):
                    #window.blit(self.detflu, (self.x, self.y))
                #else:
                    #window.blit(self.detfru, (self.x, self.y))

class Horizontal_Wall(pygame.sprite.Sprite):
    def __init__(self, color = black, width = 1300, height = 10):
        super(Horizontal_Wall, self).__init__()

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.x
        self.origin_y = self.rect.y
    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

class Vertical_Wall(pygame.sprite.Sprite):
    def __init__(self, color = black, width = 10, height = 630):
        super(Vertical_Wall, self).__init__()

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.origin_x = self.rect.x
        self.origin_y = self.rect.y
    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y


        


#http://pygame.org/project-Rect+Collision+Response-1061-.html
#Border Variables
player = Detective()
player.set_position(300, 300)


left_wall = Vertical_Wall()
left_wall.set_position(70,0)

top_wall = Horizontal_Wall()
top_wall.set_position(0,35)
                     
right_wall = Vertical_Wall()
right_wall.set_position(1220, 0)

bottom_wall = Horizontal_Wall()
bottom_wall.set_position(0, 555)

wall_group = pygame.sprite.Group()
wall_group.add(left_wall, top_wall, right_wall, bottom_wall, player)
                


collidable_objects = pygame.sprite.Group()
collidable_objects.add (left_wall, top_wall, right_wall, bottom_wall)


speed=5
detectiveCurrentImage = 1
background_image = pygame.image.load('background.png').convert()

gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):
            gameLoop=False

        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                player.change_speed(-5, 0)
                direction = "left"
            if (event.key==pygame.K_RIGHT):
                player.change_speed(5, 0)
                direction = "right"
            if (event.key==pygame.K_UP):
                player.change_speed(0, -5)
                direction = "up"
            if (event.key==pygame.K_DOWN):
                player.change_speed(0, 5)
                direction = "down"

        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_LEFT):
                player.change_speed(5, 0)
            if (event.key==pygame.K_RIGHT):
                player.change_speed(-5, 0)
            if (event.key==pygame.K_UP):
                player.change_speed(0, 5)
            if (event.key==pygame.K_DOWN):
                player.change_speed(0, -5)


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

    window.blit(background_image, [0,0])

    #player.x+=moveX
    #player.y+=moveY
    player.update(collidable_objects)


    wall_group.draw(window)   
    pygame.display.update()
    

    clock.tick(60)



pygame.quit()
