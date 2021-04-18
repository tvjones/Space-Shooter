import pygame 
import time
import random


pygame.init()
HEIGHT=550
WIDTH=550
SIZE=(550,550)

BLACK = (0,0,0)
WHITE=(255,255,255)
#GREEN=(0,255,0)
#RED=(255,0,0)

win=pygame.display.set_mode(SIZE)

pygame.display.set_caption('Space Shooter')

#Background 
BG = pygame.transform.scale(pygame.image.load("pictures/space.jpg"),SIZE)

#Brick
brick =  pygame.transform.scale(pygame.image.load("pictures/brick.png"),(60,60))

#Rocket
rocket = pygame.transform.scale(pygame.image.load("pictures/rocket.png"),(60,60))

def loadBG():
    win.blit(BG,(0,0))




   

class Brick:
    def __init__(self):
        self.surface = pygame.transform.scale(pygame.image.load("pictures/brick.png"),(60,60))
        self.y = 0
        self.x= random.randint(0,WIDTH-60)
        self.width = 60
        self.height = 60
    
    def drawBrick(self):
        win.blit(self.surface,(self.x,self.y))
    
    def clearBrick(self):
        pygame.draw.rect(win, BLACK, pygame.Rect(self.x, self.y-10, self.width, self.height))



class Rocket:
    def __init__(self):
        self.surface =  pygame.transform.scale(pygame.image.load("pictures/rocket.png"),(60,60))
        self.x = (WIDTH/2)-30
        self.y = 490
        self.width = 60
        self.height = 60

    def drawRocket(self):
        win.blit(self.surface,(self.x,self.y))
    
    def move(self,pos):
        if(self.x+pos<=WIDTH-60 and self.x+pos>=0):
            self.x+=pos
        self.drawRocket()

    def clearRocket(self):
        pygame.draw.rect(win, BLACK, pygame.Rect(self.x, self.y, 60,60))

class Bullet:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
  #  def shoot(self,rocket):
   #     self.x = rocket.x
    #    self.y = rocket.y

    def drawBullet(self):
        pygame.draw.rect(win, WHITE, pygame.Rect(self.x,self.y,5,5))

    def clearBullet(self):
        pygame.draw.rect(win, BLACK, pygame.Rect(self.x, self.y, 5,5))
    

    

def main():
    run = True
    FPS = 60
    var = 0
    bricks=[]
    bullets=[]
    clock = pygame.time.Clock()
    rocket = Rocket()
    rocket.drawRocket()
    while(run):
        clock.tick(FPS)
        # loadBG()
        for brick in bricks:
            if(brick.y>=HEIGHT-60 or (rocket.x+60-rocket.x in range(brick.x,brick.x+61) and brick.y >= HEIGHT-120)):
                run = False
        if(var==120):
            newBrick = Brick()
            bricks.append(newBrick)
            for brick in bricks:
                brick.y +=30
                brick.clearBrick()
                brick.drawBrick()   
            var=0
        keys=pygame.key.get_pressed()
          
        if keys[pygame.K_RIGHT]:
           
            rocket.clearRocket()
            rocket.move(5)
        if keys[pygame.K_LEFT]:
            
            rocket.clearRocket()
            rocket.move(-5)
        if keys[pygame.K_SPACE]:
            bullet =Bullet(rocket.x+30,rocket.y)
            bullets.append(bullet)
            bullet.drawBullet()
        #if (var==1):
        for bullet in bullets:
            for brick in bricks:
                if(bullet.x in range(brick.x,brick.x+61) and bullet.y == brick.y):
                    brick.clearBrick()
                    bricks.remove(brick)
                    bullet.y=1000
                    bullets.remove(bullet)
                if(brick.y>=HEIGHT-60 or (rocket.x in range(brick.x,brick.x+61) and brick.y >= HEIGHT-60)):
                    run = False
            bullet.clearBullet()
            bullet.y -=10
            bullet.drawBullet()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
          
        pygame.display.update()
        var+=1
main()
           

