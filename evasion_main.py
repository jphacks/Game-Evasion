
import pygame, sys
import badball
import time
import Bullet
import collision
from badball import *
from Bullet import *
from pygame.locals import *
from collision import *


bif = "background.jpg"  
mif = "ball.png"
bballimage = "badball.png"
bballdimage = "badballdefeated1.png"
bballd2image = "badballdefeated2.png"
bulletimage = "bullet.png"
reversebulletimage = "bulletreverse.png"
balldefeatedimage = "balldefeated.png"
                    
pygame.init()


screen = pygame.display.set_mode((1000,714),0,32)
background = pygame.image.load(bif).convert()
mouse_c = pygame.image.load(mif).convert_alpha()
bullet = pygame.image.load(bulletimage).convert_alpha()
reversebullet = pygame.image.load(reversebulletimage).convert_alpha()
bball = pygame.image.load(bballimage).convert_alpha()
bball2 = pygame.image.load(bballimage).convert_alpha()
bballdefeated = pygame.image.load(bballdimage).convert_alpha()
bballdefeated2 = pygame.image.load(bballd2image).convert_alpha()
balldefeated = pygame.image.load(balldefeatedimage).convert_alpha()

badball_1 = badball()
firebullet = False
existball = True
existbball = True
existbball2 = True
bball_x, bball_y = 0,0
bball2_x, bball2_y = 0,0
bball_dx,bball_dy = 1, 1
bball2_dx,bball2_dy = 1, 1
listbball = [[bball_x, bball_y],[bball2_x, bball2_y]]
clock = pygame.time.Clock()                        
fpsi = 0

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit
        if event.type == MOUSEBUTTONDOWN:            
            firebullet = True
            mbdx,mbdy = pygame.mouse.get_pos()
            posy = mbdy
            posx = mbdx
            bullet_x = x            
        
    screen.blit(background, (0,0))

    if existball == True:
        x,y = pygame.mouse.get_pos() 
        x = x - mouse_c.get_width()/2
        y = y - mouse_c.get_height()/2
        screen.blit(mouse_c,(x,y))
        pygame.mouse.set_visible(False)
        existball = collision(listbball,x,y)        
    if existball == False:
        screen.blit(balldefeated,(x,y))
        
        
        
    if existbball == True:
        if existball == True:
            bball_x,bball_y = badball_1.move(bball_x, bball_y, x, y)
            listbball[0] = [bball_x,bball_y]
            screen.blit(bball,(bball_x, bball_y))
            if firebullet == True:
                if abs(bullet_x - bball_x)<30 and abs(bullet_y-bball_y)<30:
                    existbball = False
                    firebullet = False                    
    if existbball == False:
        screen.blit(bballdefeated,(bball_x, bball_y))                
    if existball == False and existbball == True:
        bball_x = bball_x + bball_dx
        bball_y = bball_y + bball_dy
        if bball_x < 0 or bball_x > 970:
            bball_dx = -bball_dx
        if bball_y <0 or bball_y > 684:
            bball_dy = -bball_dy
        screen.blit(bball,(bball_x, bball_y))               
                  
               
    time = pygame.time.get_ticks()    
    if time > 5000 and existbball2 == True and existball == True:
        badball_2 = badball()
        bball2_x, bball2_y = badball_2.move(bball2_x, bball2_y, x ,y)
        listbball[1] = [bball2_x,bball2_y]
        screen.blit(bball2,(bball2_x, bball2_y))
        if firebullet == True:
            if abs(bullet_x - bball2_x)<35 and abs(bullet_y-bball2_y)<35:
                existbball2 = False
                firebullet = False                
    if existbball2 == False:
        screen.blit(bballdefeated,(bball2_x, bball2_y))
    if existball == False and existbball2 == True:
        bball2_x = bball2_x + bball2_dx
        bball2_y = bball2_y + bball2_dy
        if bball2_x < 0 or bball2_x > 970:
            bball2_dx = -bball2_dx
        if bball2_y <0 or bball2_y > 684:
            bball2_dy = -bball2_dy
        screen.blit(bball2,(bball2_x, bball2_y))
        

    if firebullet == True:
        bullet_1 = Bullet()      
        bullet_x, bullet_y = bullet_1.shoot(bullet_x, posx, posy)
        if bullet_x < 0 or bullet_x > 1000:
            firebullet = False
            del bullet_1
        if posx < 500:
            screen.blit(bullet,(bullet_x, bullet_y))
        if posx > 500:
            screen.blit(reversebullet,(bullet_x, bullet_y))

    fpsi = fpsi + 1
    if fpsi%200 == 0:
        print "FPS:",clock.get_fps()#print FPS every 50 loops/frames.
    clock.tick(70) #FPS
    
    pygame.display.update() 












