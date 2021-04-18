import pygame 
import time
import random


pygame.init()
HEIGHT=550
WIDTH=550
SIZE=(550,550)

#colours
BLACK = (0,0,0)
WHITE=(255,255,255)
RED =(255,0,0)

win=pygame.display.set_mode(SIZE)

pygame.display.set_caption('Space Shooter')



class Brick:
    def __init__(self):
        self.width = 60
        self.height = 60
        self.surface = pygame.transform.scale(pygame.image.load("pictures/brick.png"),(self.width,self.height))
        self.y = 0
        self.x= random.randint(0,WIDTH-60)
        
    
    def drawBrick(self):
        win.blit(self.surface,(self.x,self.y))
    
    def clearBrick(self):
        pygame.draw.rect(win, BLACK, pygame.Rect(self.x, self.y-10, self.width, self.height))



class Rocket:
    def __init__(self):
        self.width = 60
        self.height = 60
        self.surface =  pygame.transform.scale(pygame.image.load("pictures/rocket.png"),(self.width,self.height))
        self.x = (WIDTH/2)-30
        self.y = 490
  
    def drawRocket(self):
        win.blit(self.surface,(self.x,self.y))
    
    def move(self,pos):
        if(self.x+pos<=WIDTH-self.width and self.x+pos>=0):
            self.x+=pos
        self.drawRocket()

    def clearRocket(self):
        pygame.draw.rect(win, BLACK, pygame.Rect(self.x, self.y, self.width,self.height))

class Bullet:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=5
        self.height=5

    def drawBullet(self):
        pygame.draw.rect(win, WHITE, pygame.Rect(self.x,self.y,self.width,self.height))

    def clearBullet(self):
        pygame.draw.rect(win, BLACK, pygame.Rect(self.x, self.y, self.width,self.height))

    
font = pygame.font.Font('freesansbold.ttf', 32)
GAMEOVER = font.render('GAME OVER', True, RED, WHITE)


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
    
        for brick in bricks:
            #when a brick drops to the bottom
            if(brick.y>=HEIGHT-brick.height or ((rocket.x+rocket.width)-rocket.x in range(brick.x,brick.x+brick.width+1) and brick.y >= HEIGHT- rocket.height+brick.height)):
                win.fill(BLACK)
                win.blit(GAMEOVER,((WIDTH//3)-30,HEIGHT/2))
                pygame.display.update()
                pygame.time.delay(5000)
                run = False
        if(var==60):
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

        for bullet in bullets:
            for brick in bricks:
                if(bullet.x in range(brick.x,brick.x+61) and bullet.y == brick.y):
                    brick.clearBrick()
                    bricks.remove(brick)
                    bullet.y=1000
                    bullets.remove(bullet)
                    try:
                        bricks.remove(brick)
                    except:
                        print("no brick to remove")
            bullet.clearBullet()
            bullet.y -=10
            bullet.drawBullet()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
          
        pygame.display.update()
        var+=1

main()