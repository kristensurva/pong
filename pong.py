import pygame
from time import sleep, time
 
def ristkülik1():
    global rectangle1
    rectangle1 = pygame.Rect(25, y_pos1, 25, 140)
    pygame.draw.rect(ekraani_pind, (250,250,250), rectangle1)
 
def ristkülik2():
    global rectangle2
    rectangle2 = pygame.Rect(750, y_pos2, 25, 140)
    pygame.draw.rect(ekraani_pind, (250,250,250), rectangle2)
   
def ball():
    global ruut
    global x_ballpos
    global y_ballpos
    global y_ball_move
    ruut = pygame.Rect(x_ballpos, y_ballpos, 25, 25)
    pygame.draw.rect(ekraani_pind, (250, 250, 250), ruut)
    if y_ballpos>570:
        y_ballpos=570
        rectangle_hit_blip.play()
        y_ball_move=-(y_ball_move)
    elif y_ballpos<0:
        y_ballpos=0
        rectangle_hit_blip.play()
        y_ball_move=-(y_ball_move)
 
def score():
    global p1_score
    global p2_score
    global x_ballpos
    global y_ballpos
    global y_ball_move
    global x_ball_move
    global newround
    global start
    global startside
    counttime=0
    if x_ballpos<-30:
        scorep2.play()
        p2_score+=1
        x_ballpos=380
        y_ballpos=285
        y_ball_move=0
        x_ball_move=0
        start=time()
        newround=True
        startside=0
    elif x_ballpos>820:
        scorep1.play()
        p1_score+=1
        x_ballpos=380
        y_ballpos=285
        y_ball_move=0
        x_ball_move=0
        start=time()
        newround=True
        startside=1
   
    if newround==True:
        newtime=time()
        counttime=newtime-start
        if counttime>1.5:
            #Startside to make it so the side who scores doesn't get to start with ball
            if startside==1:
                x_ball_move=-8
            elif startside==0:
                x_ball_move=8
            counttime=0
            start=0
            newround=False
 
   
       
       
   
def up1():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        global y_pos1
        y_pos1-=6
        if y_pos1>570:
            y_pos1=570
        elif y_pos1<0:
            y_pos1=0
    else:
        return False
 
def down1():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_s]:
        global y_pos1
        y_pos1+=6
        if y_pos1>460:
            y_pos1=460
        elif y_pos1<0:
            y_pos1=0
    else:
        return False
   
def up2():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        global y_pos2
        y_pos2-=6
        if y_pos2>570:
            y_pos2=570
        elif y_pos2<0:
            y_pos2=0
    else:
        return False
def down2():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        global y_pos2
        y_pos2+=6
        if y_pos2>460:
            y_pos2=460
        elif y_pos2<0:
            y_pos2=0
    else:
        return False
   
 
clock = pygame.time.Clock()    
pygame.mixer.init(18000, -8, 2, 128)
pygame.font.init()
#Sounds
rectangle_hit_blip=pygame.mixer.Sound('blip.wav')
rectangle_hit_blip.set_volume(1)
scorep1=pygame.mixer.Sound('scorep1.wav')
scorep2=pygame.mixer.Sound('scorep2.wav')
#Text
font = pygame.font.SysFont("arial", 70)
 
ekraani_pind = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
ekraani_pind.fill((205,200,180))
y_pos1=220
y_pos2=220
x_ballpos=380
y_ballpos=285
x_ball_move=8
y_ball_move=0
p1_score=0
p2_score=0
newround=False
print(pygame.font.get_fonts())
while True:
    score()
    up1()
    down1()
    up2()
    down2()
   
    ekraani_pind.fill((205,200,180))
    textp1 = font.render(str(p1_score), True, (255,255,180))
    textp2 = font.render(str(p2_score), True, (255,255,180))
 
    ekraani_pind.blit(textp1, (75, 0))
    ekraani_pind.blit(textp2, (688,0))
    ristkülik1()
    ristkülik2()
    ball()
   
   
 
    clock.tick(60)
    x_ballpos-=x_ball_move
    y_ballpos+=y_ball_move
    if pygame.Rect.colliderect(ruut, rectangle1)==True:
        rectangle_hit_blip.play()
        x_ballpos=50
        x_ball_move=-(x_ball_move)
        if up1()==None:
            y_ball_move=-4
        if down1()==None:
            y_ball_move=4
   
    if pygame.Rect.colliderect(ruut, rectangle2)==True:
        rectangle_hit_blip.play()
        x_ballpos=725
        x_ball_move=-(x_ball_move)
        if up2()==None:
            y_ball_move=-4
        if down2()==None:
            y_ball_move=4
    event = pygame.event.poll()
    pygame.display.flip()
    if event.type == pygame.QUIT:
        break
 
pygame.quit()