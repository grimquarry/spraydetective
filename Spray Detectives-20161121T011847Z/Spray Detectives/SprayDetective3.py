import pygame

pygame.init()

window = pygame.display.set_mode ((1300, 630))

pygame.display.set_caption("Spray Detective")

black = (0,0,0)
white = (255, 255, 255)



moveX=0
moveY=0

clock = pygame.time.Clock()

class Detective:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=50
        self.height=50

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
        #Border Variables
        self.left_wall = 80
        self.top_wall = 21
        self.right_wall = 1217
        self.bottom_wall = 554


    def update (self):
        self.timeNum+=1
        
        if (self.timeNum==self.timeTarget):

            if (self.currentImage==0):
                self.currentImage+=1

            else:
                self.currentImage=0
            self.timeNum=0

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



        self.detfr    
        self.render()
        

    def render(self):

        #Run Animation
        if (self.direction=="down" and not self.attack=="attack"):
            if (self.currentImage==0):
                window.blit(self.detflu, (self.x, self.y))
            else:
                window.blit(self.detfru, (self.x, self.y))

        if (self.direction=="up" and not self.attack=="attack"):
            if (self.currentImage==0):
                window.blit(self.detulu, (self.x, self.y))
            else:
                window.blit(self.deturu, (self.x, self.y))
                    
        if (self.direction=="left" and not self.attack=="attack"):
            if (self.currentImage==0):
                window.blit(self.detlld, (self.x, self.y))
            else:
                window.blit(self.detlru, (self.x, self.y))

        if (self.direction=="right" and not self.attack=="attack"):
            if (self.currentImage==0):
                window.blit(self.detrlu, (self.x, self.y))
            else:
                window.blit(self.detrrd, (self.x, self.y))

            #Run and attack animations
        if (self.attack=="attack" and self.direction=="down"):
                if (self.currentImage==0):
                    window.blit(self.detaflu, (self.x, self.y))
                else:         
                    window.blit(self.detafru, (self.x, self.y))

        if (self.attack=="attack" and self.direction=="up"):
            if (self.currentImage==0):
                window.blit(self.detaulu, (self.x, self.y))
            else:
                window.blit(self.detauru, (self.x, self.y))

        if (self.attack=="attack" and self.direction=="right"):
            if (self.currentImage==0):
                window.blit (self.detarlu, (self.x, self.y))
            else:
                window.blit (self.detarru, (self.x, self.y))

        if (self.attack=="attack" and self.direction=="left"):
            if (self.currentImage==0):
                window.blit (self.detallu, (self.x, self.y))
            else:
                window.blit (self.detalru, (self.x, self.y))

        #Attack Standing Still
        if (self.attack=="attack" and self.direction=="RestDown"):
            if (self.currentImage==0):
                window.blit (self.detafr1, (self.x, self.y))
            else:
                window.blit (self.detafr2, (self.x, self.y))

        if (self.attack=="attack" and self.direction=="RestUp"):
            if (self.currentImage==0):
                window.blit (self.detaur1, (self.x, self.y))
            else:
                window.blit (self.detaur2, (self.x, self.y))

        if (self.attack=="attack" and self.direction=="RestRight"):
            if (self.currentImage==0):
                window.blit (self.detarr1, (self.x, self.y))
            else:
                window.blit (self.detarr2, (self.x, self.y))

        if (self.attack=="attack" and self.direction=="RestLeft"):
            if (self.currentImage==0):
                window.blit (self.detalr1, (self.x, self.y))
            else:
                window.blit (self.detalr2, (self.x, self.y))
                    
        #At Rest Graphics
        if (self.direction=="RestDown" and not self.attack=="attack"):
                window.blit(self.detfr, (self.x, self.y))
        if (self.direction=="RestUp" and not self.attack=="attack"):
                window.blit(self.detur, (self.x, self.y))
        if (self.direction=="RestLeft" and not self.attack=="attack"):
                window.blit(self.detlr, (self.x, self.y))
        if (self.direction=="RestRight" and not self.attack=="attack"):
                window.blit(self.detrr, (self.x, self.y))
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
        if self.x == self.left_wall:
            window.blit (self.detlr, (self.left_wall, self.y))

#Border Variables
left_wall = 80
top_wall = 21
right_wall = 1217
bottom_wall = 554
                

                
player = Detective(100,150)


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
                moveX-=speed
            if (event.key==pygame.K_RIGHT):
                moveX+=speed
            if (event.key==pygame.K_UP):
                moveY-=speed
            if (event.key==pygame.K_DOWN):
                moveY+=speed

        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_LEFT):
                moveX=0
            if (event.key==pygame.K_RIGHT):
                moveX=0
            if (event.key==pygame.K_UP):
                moveY=0
            if (event.key==pygame.K_DOWN):
                moveY=0
            
        
        

    window.blit(background_image, [0,0])

    player.x+=moveX
    player.y+=moveY
    player.update()

        
    pygame.display.update()
    

    clock.tick(60)

pygame.quit()
