import pygame
import random
import time
pygame.init()
width=800
height=600
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
skor=0
gamedisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption("Adventures of the Bloodless")
clock=pygame.time.Clock()
avatar=pygame.image.load("avatar.png")
avatar=pygame.transform.scale(avatar,(75,100))
background=pygame.image.load("Background.jpg")

def mesaj(a):
    font = pygame.font.Font('freesansbold.ttf', 35)
    gamedisplay.blit(font.render(a, True, (255, 0, 0)), ((width/ 2)-len(a), height/2))
    pygame.display.update()
    time.sleep(2)
def boru(a,b,c,d):
    pygame.draw.rect(gamedisplay,green,[a,0,c,b])

    pygame.draw.rect(gamedisplay, green, [a,600, c, - d])


def oyunbitti():
    liste=["Soru reddedilmiştir","iyi Günler"]
    mesaj(random.choice(liste))

def car(x,y):
    gamedisplay.blit(kansiz,(x,y))

def game_loop():
    x = width * 0.2
    y = height * 0.4
    boru_x=900
    boru_y=random.randrange(100,175)
    boru_hiz=7
    boru_gen=110
    boru_2y = random.randrange(0, 300)
    boru_2x = 1200
    d2=300-boru_2y
    boru_3y = random.randrange(0, 300)
    boru_3x = 1500
    d3 = 300 - boru_3y
    d =300-boru_y
    crashed = False
    while not crashed:
        crashed = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:

                crashed=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if(y>=100):
                    y=y-120
        gamedisplay.fill(white)
        gamedisplay.blit(background,(-150,0))
        boru(boru_x,boru_y,boru_gen,d)
        boru(boru_3x, boru_3y, boru_gen, d3)
        boru(boru_2x, boru_2y, boru_gen, d2)
        boru_x-=boru_hiz
        boru_2x -= boru_hiz
        boru_3x -= boru_hiz
        car(x,y)
        if boru_x<0:
            boru_x=900
            boru_y = random.randrange(0, 300)
            d=300-boru_y
        if boru_2x<0:
            boru_2x=900
            boru_2y = random.randrange(0, 300)
            d2=300-boru_2y
        if boru_3x<0:
            boru_3x=900
            boru_3y = random.randrange(0, 300)
            d3=300-boru_3y
        if(y>height-100):
            oyunbitti()
            crashed=True
        y=y+10
        if((y<boru_y or y+100>605-d) and ((x>boru_x and x<boru_x+110 )or (x+70>boru_x and x+70<boru_x+110))):
            oyunbitti()
            crashed=True
        if ((y < boru_2y or y + 100 > 605 - d2) and (
            (x > boru_2x and x < boru_2x + 110) or (x + 70 > boru_2x and x + 70 < boru_2x + 110))):
            oyunbitti()
            crashed = True
        if ((y < boru_3y or y + 100 > 605 - d3) and (
            (x > boru_3x and x < boru_3x + 110) or (x + 70 > boru_3x and x + 70 < boru_3x + 110))):
            oyunbitti()
            crashed = True

        pygame.display.update()
        clock.tick(30)
game_loop()
pygame.quit()
quit()