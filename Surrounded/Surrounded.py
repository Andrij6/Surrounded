from random import randint
from time import *
import pygame
import json 
import os
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)


WIN_WIDTH=500
WIN_HEIGHT=500
pygame.mixer.music.load('fon_sound.ogg')
pygame.mixer.music.play()
New=(141,255,128)
New1 = (113,231,104)
WHITE =(255,255,255)
grey_outline = (165,165,165)
GRAY = (200,200,200)
New_outline = (77,191,107)
New_pause = (82,206,114)
mw = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))  #окно программы (main window)
pygame.display.set_caption("Surrounded")
clock = pygame.time.Clock()
BLUE = (0,0,255)
font_2 = pygame.font.SysFont('arial',70)
pause = font_2.render("PAUSE",True,BLUE)
adds = 0
cards = []
draw_all_resolution = False
num_cards = 15
x_map = -2370
y_map = -2720
giants = True
WIN_WIDTH_in_game = 2560
WIN_HEIGHT_in_game = 1440
loadint1 = pygame.transform.scale(pygame.image.load('loading_1.png'),(500,500)).convert()

mw.blit(loadint1,(0,0))

pygame.display.update()
clock.tick(60)
 
background = pygame.transform.scale(pygame.image.load('karta_beta.png'),(7000,7000)).convert()
loadint2 = pygame.transform.scale(pygame.image.load('loading_2.png'),(500,500)).convert()
min_x = 10000
min_y = 10000
a = 0
while a != 10:
    mw.blit(loadint2,(0,0))
    a+=1
    pygame.display.update()
    clock.tick(60)
timer_for_music = 0
timer_for_music_second = 0
timer = 0
game_over = False
eskape = False
s=5
white = (255,255,255)
grass = (0, 170, 0)
klas_=0
volume = 0.5
adsdsd = 1
Name='Name'
stop=0
sloz = 0
autosav1 = 0
autosav2 =0
jazikn =2
zvykn = 5
a=0
switch=0
move_right = False
move_left = False
alll = list()
zombie = list()
doors = list()
house = list()
bullets = list()
RED = (255, 51, 0)
RED2= (240, 52, 5)
grey = (202, 224, 227)
blue = (111, 157, 163)
GREEN=(0, 255, 0)
GREEN_outline=(0, 245, 0)
GRAY = (191, 192, 194)
return_to_game = False
BLACK = (0,0,0)
dsasasasas = 1
game = ''

class Area():
    def __init__(self, x=0, y=0, width=20, height=10, color=None):
        self.rect = pygame.Rect((x, y), (width, height))
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color
 
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    
    def outline(self, flame_color, thickness):
        pygame.draw.rect(mw, flame_color, self.rect, thickness)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont("verdana", fsize).render(text,True,text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Picture(Area):
   def __init__(self, filename, x=0, y=0, width=10, height=10):
       Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
       self.image = pygame.image.load(filename)
      
   def draw(self):
       mw.blit(self.image, (self.rect.x, self.rect.y))



class bullet():
    def __init__(self,to_x,to_y,w,h,klas_bulet):
        self.w = w
        self.h = h
        self.to_x = to_x
        self.to_y = to_y
        self.x = (WIN_WIDTH_in_game//3)-25
        self.y = (WIN_HEIGHT_in_game//3)-25
        self.y = 345
        self.chtoplus_x = 1
        self.chtoplus_y = 1
        bullets.append(self)
        alll.append(self)
        if klas_bulet == 'fireball':
            self.bullet = pygame.transform.scale(pygame.image.load('fireball.png'),(w,h)).convert_alpha()
        if player.direction == 'left':
            gradus = 180
            self.y = (WIN_HEIGHT_in_game//3)-10
            self.direction = 'left'
        if player.direction == 'right':
            gradus = 0
            self.x = (WIN_WIDTH_in_game//3)-10
            self.y = (WIN_HEIGHT_in_game//3)-10
            self.direction = 'right'
        if player.direction == 'up':
            self.x = (WIN_WIDTH_in_game//3)-10
            gradus = 90
            self.direction = 'up'
        if player.direction == 'down':
            gradus = 270
            self.direction = 'down'
            self.y = (WIN_HEIGHT_in_game//3)
        if player.direction == 'upleft':
            gradus = 135
            self.direction = 'upleft'
        if player.direction == 'upright':
            gradus = 45
            self.direction = 'upright'
        if player.direction == 'downleft':
            gradus = 225
            self.direction = 'downleft'
        if player.direction == 'downright':
            gradus = 315
            self.direction = 'downright'

        self.bullet = pygame.transform.rotate(self.bullet,gradus)
        
        '''if self.to_x > self.x:
            if self.to_y < self.y:
                gradus = ((self.to_x - self.x) + (self.y - self.to_y)) / 16.25
                self.chtoplus_x = (self.to_x - self.x)/(self.y-self.to_y)
                self.kyda = 'right_top'
                player.direction = 'right'

            if self.to_y > self.y:
                gradus = ((self.to_x - self.x) + (self.to_y - self.y)) / 16.25 + 270
                self.chtoplus_x = (self.to_x - self.x)/(self.to_y - self.y)
                self.kyda = 'right_down'
                player.direction = 'right'
        if self.to_x < self.x:
            if self.to_y < self.y:
                gradus = ((self.x - self.to_x) + (self.y - self.to_y)) / 16.25 + 90
                self.chtoplus_x = (self.x - self.to_x)/(self.y-self.to_y)
                self.kyda = 'left_top'
                player.direction = 'left'
            if self.to_y > self.y:
                gradus = ((self.x - self.to_x) + (self.to_y - self.y)) / 16.25 + 180
                
                self.chtoplus_x = (self.x - self.to_x)/(self.to_y - self.y)
                self.kyda = 'left_down'
                player.direction = 'left'
        if self.to_x == self.x:
            if self.to_x > self.x: 
                self.chtoplus_x = (self.x - self.to_x)/(self.y-self.to_y)
                gradus = 0
            if self.to_x < self.x:
                self.chtoplus_x = (self.to_x - self.x)/(self.y-self.to_y)
                gradus = 180
        if self.to_y == self.y:
            if self.to_y > self.y:
                if self.to_x < self.x:
                    self.chtoplus_x = (self.to_x - self.x)/(self.y-self.to_y) 
                if self.to_x > self.x:
                    self.chtoplus_x = (self.x - self.to_x)/(self.y-self.to_y)
                gradus = 270
            if self.to_y < self.y:
                if self.to_x < self.x:
                    self.chtoplus_x = (self.to_x - self.x)/(self.y-self.to_y) 
                if self.to_x > self.x:
                    self.chtoplus_x = (self.x - self.to_x)/(self.y-self.to_y)
                gradus = 90

        while (int(self.chtoplus_x) + int(self.chtoplus_y)) // 8 != 1:   
                    if int(self.chtoplus_x) + int(self.chtoplus_y) > 8:
                        self.chtoplus_x=self.chtoplus_x * 0.75
                        self.chtoplus_y=self.chtoplus_y * 0.75
                    if int(self.chtoplus_x) + int(self.chtoplus_y) < 8:
                        self.chtoplus_x=self.chtoplus_x * 2
                        self.chtoplus_y=self.chtoplus_y * 2'''

                    


    def update(self):
        window.blit(self.bullet,(self.x,self.y))
        if self.direction == 'upleft':
            self.x -= 7.5
            self.y -= 7.5
        elif self.direction == 'upright':
            self.x += 7.5
            self.y -= 7.5
        elif self.direction == 'downleft':
            self.x -= 7.5
            self.y += 7.5
        elif self.direction == 'downright':
            self.x += 7.5
            self.y += 7.5
        elif self.direction == 'left':
            self.x -= 10
        elif self.direction == 'right':
            self.x += 10
        elif self.direction == 'up':
            self.y -= 10
        elif self.direction == 'down':
            self.y += 10
        for i in zombie:  
            if self.x+i.w-10 > i.x and self.x-i.w < i.x and self.y+i.h > i.y and self.y-i.h < i.y:
                i.hp -= player.atack_power
                bullets.remove(self)
        if self.x > 2000:
            bullets.remove(self)
        if self.x < -2000:
            bullets.remove(self)
        if self.y > 2000:
            bullets.remove(self)
        if self.y < -2000:
            bullets.remove(self)

        

            
class armor():
    def __init__(self,w,h):
        self.w = w
        self.h = h
        if klas_ == 3:
            self.run_up = pygame.transform.scale(pygame.image.load('kingalrun.png'),(w,h)).convert_alpha()
            self.atack_up= pygame.transform.scale(pygame.image.load('kingalatack.png'),(w,h)).convert_alpha()
        if klas_ == 2:
            self.run_up = pygame.transform.scale(pygame.image.load('posohrun_up.png'),(w,h)).convert_alpha()
            self.atack_up= pygame.transform.scale(pygame.image.load('posohatack_up.png'),(w,h)).convert_alpha()
        
        self.run_down = pygame.transform.rotate(self.run_up,180)
        self.run_left= pygame.transform.rotate(self.run_up,90)
        self.run_right= pygame.transform.rotate(self.run_up,270)

        self.atack_down = pygame.transform.rotate(self.atack_up,180)
        self.atack_left= pygame.transform.rotate(self.atack_up,90)
        self.atack_right= pygame.transform.rotate(self.atack_up,270)

    def update(self,direction,atack):
        if direction == 'left':
            if atack == '':
                mw.blit(self.run_left,(player.x-50,player.y))
            if atack == 'atack':
                mw.blit(self.atack_left,(player.x-50,player.y))
        if direction == 'right':
            if atack == '':
                mw.blit(self.run_right,(player.x+50,player.y))
            if atack == 'atack':
                mw.blit(self.atack_right,(player.x+50,player.y))
        if direction == 'up' or direction == 'upleft' or direction == 'upright':
            if atack == '':
                mw.blit(self.run_up,(player.x,player.y-50))
            if atack == 'atack':
                mw.blit(self.atack_up,(player.x,player.y-50))
        if direction == 'down' or direction == 'downleft' or direction == 'downright':
            if atack == '':
                mw.blit(self.run_down,(player.x,player.y+50))
            if atack == 'atack':
                mw.blit(self.atack_down,(player.x,player.y+50))
        



class PlayerName():
    def __init__(self):
        self.font_35 = pygame.font.SysFont('arial',35)

        self.text_enterName = self.font_35.render(vved,True,WHITE)
        self.user_name = ''
        self.btn_go = pygame.image.load('text_go.png').convert_alpha()
        self.btn_go_rect = self.btn_go.get_rect(center = (400, 400))
                                                          
    def update(self):
        
        mw.blit(self.text_enterName,(30,200))
        self.text_user_name = self.font_35.render(self.user_name,True,WHITE)
        mw.blit(self.text_user_name,(300,200))
        if len(self.user_name) > 4:
            mw.blit(self.btn_go,self.btn_go_rect)





class GameSprite():
    def __init__(self, pl_image, pl_x, pl_y, pl_speed,pl_w,pl_h):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(pl_image),(pl_w,pl_h))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Player():  
    def __init__(self,x,y,w,h,color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = 100
        self.regen_hp_timer = 0
        self.regen_hp_timer_max = 300
        self.color = color
        if klas_ == 3:
            self.atack_power = 4
            self.couldown = 20
        elif klas_ == 2:
            self.atack_power = 7
            self.couldown = 80
            self.atack_for_far = 5
        self.direction = 'up'
        self.rect = pygame.Rect((x, y), (w, h)) 
        self.atack = ''
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.block_left = False
        self.block_right = False
        self.block_up = False
        self.block_down = False
        self.level = 0
    def update(self):   
        global x_map, y_map, switch, health, mw
        asasin_.update(self.direction,self.atack)
        pygame.draw.rect(mw, self.color, self.rect)
        keys_p = pygame.key.get_pressed()

        if keys_p[pygame.K_a] and x_map < -280 and keys_p[pygame.K_s]and y_map > -5383:
            x_map +=6*0.75
            y_map -=6*0.75
            for i in alll:
                i.x += 6*0.75
                i.y -= 6*0.75
            self.direction = 'downleft'
        elif keys_p[pygame.K_a] and x_map < -280 and keys_p[pygame.K_w]and y_map < -655:
            x_map +=6*0.75
            y_map +=6*0.75
            for i in alll:
                i.x += 6*0.75
                i.y += 6*0.75
            self.direction = 'upleft'
        elif keys_p[pygame.K_d] and x_map > -5010 and keys_p[pygame.K_s]and y_map > -5383:
            x_map -=6*0.75
            y_map -=6*0.75
            for i in alll:
                i.x -= 6*0.75
                i.y -= 6*0.75
            self.direction = 'downright'
        elif keys_p[pygame.K_d] and x_map > -5010 and keys_p[pygame.K_w] and y_map < -655:
            x_map -=6*0.75
            y_map +=6*0.75
            for i in alll:
                i.x -= 6*0.75
                i.y += 6*0.75
            self.direction = 'upright'

        elif keys_p[pygame.K_a] and x_map < -280:
            x_map +=6
            for i in alll:
                i.x += 6
            self.direction = 'left'
        elif keys_p[pygame.K_d]and x_map > -5010:
            x_map -=6
            for i in alll:
                i.x -= 6
            self.direction = 'right'
        elif keys_p[pygame.K_w] and y_map < -655:
            y_map +=6
            for i in alll:
                i.y += 6
            self.direction = 'up'
        elif keys_p[pygame.K_s] and y_map > -5383:
            y_map -=6
            for i in alll:  
                i.y -= 6
            self.direction = 'down'
        
        
        if self.hp < 100:
            self.regen_hp_timer +=1 
            if self.regen_hp_timer >= self.regen_hp_timer_max:
                self.hp += 1
                self.regen_hp_timer -= 5
            if self.hp == 100:
                self.regen_hp_timer = 0
        if self.hp <= 0:
            self.hp = 100
            self.x,self.y = (WIN_WIDTH_in_game//3)-25,(WIN_HEIGHT_in_game//3)-25
            for i in alll:
                if x_map > -2370:
                    x_tp = -2370 - x_map
                    i.x = i.x + x_tp
                if x_map < -2370:
                    x_tp = x_map + 2370
                    i.x = i.x - x_tp
                if y_map > -2720:
                    y_tp = -2720 - y_map
                    i.y = i.y + y_tp
                if y_map < -2720:
                    y_tp = y_map + 2720
                    i.y = i.y - y_tp

            x_map = -2370
            y_map = -2720
            if health != 'inf':
                health -= 1
        if health == -1:
            switch = 0
            WIN_WIDTH=500
            WIN_HEIGHT=500
            mw = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))



class zombi():
    def __init__(self,x,y,klas_zombi):
        self.rect = pygame.Rect((x, y), (50, 50)) 
        zombie.append(self)
        alll.append(self)
        self.x = x
        self.y = y
        self.hp = hp
        self.klas_zombi = klas_zombi
        self.time_waite = 0
        self.waite = False
        self.time_waite_max = randint(120,300)
        self.direction = 'left'
        self.px_go = randint(100,250)
        self.px_go_continiu = 0
        self.walking = True
        self.time_spawn_zombi = 0
        self.time_spawn_zombi_max = 120
        if self.klas_zombi == 'normal':
            self.hp = 20
            self.speed = 3
            self.w = 50
            self.h = 50
            self.atack_power = 5
            self.couldaun_atack = 59
            self.couldaun_atack_max = 60
            self.x_find = 550
            self.y_find = 350
            self.x_find_2 = 850
            self.y_find_2 = 650
            self.color = (randint(0,50),randint(90,120),randint(0,40))

        if self.klas_zombi == 'fast':
            self.hp = 15
            self.speed = 6
            self.w = 50
            self.h = 50
            self.atack_power = 3
            self.couldaun_atack = 29
            self.couldaun_atack_max = 30
            self.x_find = 600
            self.y_find = 400
            self.x_find_2 = 900
            self.y_find_2 = 700
            self.color = (randint(0,135),randint(150,200),255)

        if self.klas_zombi == 'giant':
            self.hp = 50
            self.speed = 2
            self.w = 75
            self.h = 75
            self.atack_power = 15
            self.couldaun_atack = 119
            self.couldaun_atack_max = 120
            self.x_find = 600
            self.y_find = 400
            self.x_find_2 = 1000
            self.y_find_2 = 800
            self.color = (randint(0,50),randint(90,120),randint(0,40))
            
        self.atackplayer = False

        
    def update(self):
        global giants, min_x, min_y, k_komy
        self.rect = pygame.Rect((self.x, self.y), (self.w, self.h)) 
        pygame.draw.rect(mw, self.color, self.rect)

        for i in zombie:
            if i != self:
                if self.x+self.w > i.x and self.x-self.w < i.x and self.y+self.h > i.y and self.y-self.h < i.y:
                    if self.direction == 'left':
                        self.x += self.speed
                    if self.direction == 'right':
                        self.x -= self.speed
                    if self.direction == 'up':
                        self.y += self.speed
                    if self.direction == 'down':
                        self.y -= self.speed 
        if self.hp <= 0:
            zombie.remove(self)
            alll.remove(self)
        if self.atackplayer:
            if self.x+self.w+5 > player.x and self.x-self.w-5 < player.x and self.y+self.h+5 > player.y and self.y-self.h-5 < player.y:
                self.couldaun_atack += 1
                if self.couldaun_atack >= self.couldaun_atack_max:
                    player.hp -= self.atack_power
                    player.regen_hp_timer = 0
                    self.couldaun_atack = 0
            else:
                if self.x > player.x and self.y > player.y:
                    self.x -= 0.5*self.speed
                    self.y -= 0.5*self.speed
                elif self.x > player.x and self.y < player.y:
                    self.x -= 0.5*self.speed
                    self.y += 0.5*self.speed
                elif self.x < player.x and self.y > player.y:
                    self.x += 0.5*self.speed
                    self.y -= 0.5*self.speed
                elif self.x < player.x and self.y < player.y:   
                    self.x += 0.5*self.speed
                    self.y += 0.5*self.speed
                elif self.x > player.x:
                    self.x -= self.speed
                elif self.x < player.x:
                    self.x += self.speed
                elif self.y > player.y:
                    self.y -= self.speed
                elif self.y < player.y:
                    self.y += self.speed
        if self.x+self.x_find > player.x and self.x-self.x_find < player.x and self.y+self.y_find > player.y and self.y-self.y_find < player.y:
            self.walking = False
            self.atackplayer = True
        else:
            if self.x+self.x_find_2 > player.x and self.y+self.y_find_2 > player.y or self.x+self.x_find_2 > player.x and self.y-self.y_find_2 < player.y or self.x-self.x_find_2 < player.x and self.y+self.y_find_2 > player.y or self.x-self.x_find_2 < player.x and self.y-self.y_find_2 < player.y:
                self.walking = True
                self.atackplayer = False
        if self.walking:
                if self.waite:
                    self.time_waite +=1
                    if self.time_waite > self.time_waite_max:
                        a = randint(1,4)
                        self.px_g = randint(50,150)
                        if a == 1:
                            self.direction = 'left'
                        if a == 2:
                            self.direction = 'right'
                        if a == 3:
                            self.direction = 'up'
                        if a == 4:
                            self.direction = 'down'
                        self.waite = False
                        self.time_waite = 0
                        self.px_go_continiu = 0
                if self.waite == False:
                    if self.direction == 'left':
                        self.x -= self.speed // 1.5
                        self.px_go_continiu -= 5
                    if self.direction == 'right':
                        self.x += self.speed // 1.5
                        self.px_go_continiu += 5
                    if self.direction == 'up':
                        self.y -= self.speed // 1.5
                        self.px_go_continiu -= 5
                    if self.direction == 'down':
                        self.y += self.speed // 1.5
                        self.px_go_continiu += 5

                    if self.px_go_continiu >= self.px_go or self.px_go_continiu <= self.px_go*2*-1:
                        self.waite = True
            


class Level():
    def __init__(self):
        pass          
    def update():
        for object in alll:
            if not object in zombie: 
                if not object in doors:  
                    if not object in bullets:
                        if object.level > player.level or object.level == 'river':
                            if player.x-object.w-20 < object.x and player.x > object.x:
                                player.block_left = True
                            else:
                                player.block_left = False

                            if player.x+object.w+20 > object.x and player.x < object.x:
                                player.block_right = True
                            else:
                                player.block_right = False

                            if player.y-object.h-20 < object.y and player.y > object.y:
                                player.block_up = True
                            else:
                                player.block_up = False
                                
                            if player.y+object.h+20 > object.y and player.y < object.y:
                                player.block_down = True 
                            else:
                                player.block_down = False       

                    
                    
                    
                       
    

class Hp():
    def __init__(self):
        self.rect_black = pygame.Rect((20, 20), (420, 40)) 
        self.rect_green = pygame.Rect((30, 30), (400, 20)) 
    def update(self,hp_player):
        self.rect_black = pygame.Rect((20, 20), (420, 40)) 
        pygame.draw.rect(mw, BLACK, self.rect_black)

        self.rect_green = pygame.Rect((30, 30), (400-(100-hp_player)*4, 20)) 
        pygame.draw.rect(mw, GREEN, self.rect_green)


hp = Hp()



for i in range(10):
    zombie_ = zombi(randint(-1100,3000),-randint(-1300,3000),'normal')
for i in range(5):
    zombie_ = zombi(randint(-1100,3000),-randint(-1300,3000),'fast')
for i in range(3): 
    zombie_ = zombi(randint(-1100,3000),-randint(-1300,3000),'giant')



 

'''
dict_saves = {
    'clas': '', 
    'oruzie': ['','обычное'], 
    'glava': [1,1], 
    'zombi': 1,
    'zombixy': [
        500,500 
    ], 
    'nocden': ['den'],
    'name': ''
        }   
with open('saves.json','r',encoding='utf-8') as results:
        dict_saves = json.load(results)
with open('saves.json','w',encoding='utf-8') as results:
        json.dump(dict_saves,results,sort_keys=False,ensure_ascii=False)'''

with open('saves.json','r',encoding='utf-8') as results:
    dict_saves = json.load(results)
with open('saves.json','w',encoding='utf-8') as results:
    json.dump(dict_saves,results,sort_keys=False,ensure_ascii=False)

def import_db(p_list,file_name):
    with open(file_name,'r',encoding='utf-8') as results:
        dict_load = json.load(results)
    for i in range(len(p_list)):
        name = list(p_list.keys())
        p_list[name[i]] = dict_name[name[i]]

def export_db(list,list_list,dict_name,dict_path,p_list,**kwargs):
    if list:
        for i in range(len(list_list)):
            score_all = 0
            name_list = list(list_list.keys())
            if list_list[name_list[i-1]][1] == 'syma':
                for a in list_list[name_list[i-1]][0]:
                    score_all += int(a)
            if list_list[name_list[i-1]][1] == 'kol':
                for a in list_list[name_list[i-1]][0]:
                    score_all += int(a)
            dict_name[name_list[i]] = list_list[name_list[i]]
    for i in range(len(p_list)):
        name = list(p_list.keys())
        dict_name[name[i]] = p_list[name[i]]
    with open(dict_path,'w',encoding='utf-8')as result:
        json.dump(dict_name,result,sort_keys=True,ensure_ascii=False) 




vved = "Введіть ім'я"
language = 'eng'
def jazikklas():
    global language
    global vved
    if jazikn==0:
        language='ukr'
        vved ="Введіть ім'я"
        nastr.set_text('Налаштування', 40)
        sloztxt.set_text('Складність', 30)
        autosave1.set_text('Автозбереження', 25)
        autosave2.set_text('Автозбереження', 25)
        jaziknat.set_text('Мова', 30)
        zvyk.set_text('Гучність', 30)
        klas.set_text('Вибір класса', 35)
        skins.set_text('Колір', 60)
        display.set_text('Роздільність монітора', 25)
        ready.set_text('Готово', 45)
        k1.set_text('Почати', 35)
        k2.set_text('Налаштування', 20)
        k3.set_text('Збереження', 10)
        k4.set_text('Вийти', 15)
        savess.set_text('Збереженя', 50)
        resume.set_text('Продовжити', 25)
        settings.set_text('Налаштування', 25)
        exit_to_menu.set_text('Вихід у меню', 25)
    if jazikn==1:
        language='pol'
        vved = "Wpisz imię"
        nastr.set_text('Ustawienia', 40)
        sloztxt.set_text('Złożoność', 30)
        autosave1.set_text('Autozapisywanie', 25)
        autosave2.set_text('Autozapisywanie', 25)
        jaziknat.set_text('Język', 30)
        zvyk.set_text('Głośność', 30)
        klas.set_text('Wybór klasy', 35)
        skins.set_text('Kolor', 60)
        display.set_text('Rozdzielczość monitora', 25)
        ready.set_text('Gotowy', 40)
        k1.set_text('Rozpocząć', 30)
        k2.set_text('Ustawienia', 30)
        k3.set_text('Zapis', 13)
        k4.set_text('Wychodzić', 10)
        savess.set_text('Ratować', 50)
        resume.set_text('Kontynuować', 25)
        settings.set_text('Ustawienia', 30)
        exit_to_menu.set_text('Wyjdź do menu', 25)
    if jazikn==2:
        language='eng'
        vved = "Enter your name"
        nastr.set_text('Settings', 40)
        sloztxt.set_text('Difficulty', 30)
        autosave1.set_text('Autosave', 30)
        autosave2.set_text('Autosave', 30)
        jaziknat.set_text('Language', 30)
        zvyk.set_text('Volume', 30)
        klas.set_text('Choosing a class', 35)
        skins.set_text('Colour', 50)
        display.set_text('Monitor resolution', 28)
        ready.set_text('Ready', 45)
        k1.set_text('Start', 35)
        k2.set_text('Settings', 30)
        k3.set_text('Save', 20)
        k4.set_text('Exit', 20)
        savess.set_text('Save', 50)
        resume.set_text('Continue', 30)
        settings.set_text('Settings', 40)
        exit_to_menu.set_text('Exit to menu', 30) 

playername = PlayerName()
    
loadint3 = pygame.transform.scale(pygame.image.load('loading_3.png'),(500,500)).convert()

a = 0
while a != 5:
    mw.blit(loadint3,(0,0))
    a+=1
    pygame.display.update()
    clock.tick(60)
 

 

exit = Label(25, 25,30, 30, New)
exit.color(New)
exit.set_text('<', 35)

nastr = Label(120, 20,80, 55, New)
nastr.color(New)
nastr.set_text('Налаштування', 40)

resume = Label(535, 270, 250, 80, New_pause)
resume.color(New_pause)
resume.set_text('Continue', 30)

settings = Label(535, 390,250, 80, New_pause)
settings.color(New_pause)
settings.set_text('Settings', 40)

exit_to_menu = Label(535, 510, 250, 80, New_pause)
exit_to_menu.color(New_pause)
exit_to_menu.set_text('Exit to menu', 30) 

sloztxt = Label(50, 90,80, 55, New)
sloztxt.color(New)
sloztxt.set_text('Складність', 30)

left2 = Label(240, 80,50, 50, New)
left2.color(New)
left2.set_text('<', 50)

slozn = Label(300, 90,80, 55, New)
slozn.color(New)
slozn.set_text('', 30)

right2 = Label(450, 80,50, 50, New)
right2.color(New)
right2.set_text('>', 50)


autosave1 = Label(20, 150,80, 55, New)
autosave1.color(New)
autosave1.set_text('Автозбереження', 25)

left3 = Label(240, 140,50, 50, New)
left3.color(New)
left3.set_text('<', 50)

autos1 = Label(285, 150,80, 55, New)
autos1.color(New)
autos1.set_text('', 30)

right3 = Label(450, 140,50, 50, New)
right3.color(New)
right3.set_text('>', 50)


autosave2 = Label(20, 210,80, 55, New)
autosave2.color(New)
autosave2.set_text('Автозбереження', 25)

left4 = Label(240, 200,50, 50, New)
left4.color(New)
left4.set_text('<', 50)

autos2 = Label(285, 210,80, 55, New)
autos2.color(New)
autos2.set_text('', 30)

right4 = Label(450, 200,50, 50, New)
right4.color(New)
right4.set_text('>', 50)


jaziknat = Label(50, 260,80, 55, New)
jaziknat.color(New)
jaziknat.set_text('Мова', 30)

left5 = Label(240, 250,50, 50, New)
left5.color(New)
left5.set_text('<', 50)

jazikmen = Label(285, 260,80, 55, New)
jazikmen.color(New)
jazikmen.set_text('', 30)

right5 = Label(450, 250,50, 50, New)
right5.color(New)
right5.set_text('>', 50)


zvyk = Label(20, 310,80, 55, New)
zvyk.color(New)
zvyk.set_text('Гучність', 30)

left6 = Label(240, 300,50, 50, New)
left6.color(New)
left6.set_text('<', 50)

zvyka = Label(285, 310,80, 55, New)
zvyka.color(New)
zvyka.set_text('', 30)

right6 = Label(450, 300,50, 50, New)
right6.color(New)
right6.set_text('>', 50)

display = Label(20, 360,80, 55, New)
display.color(New)
display.set_text('Display', 50)

a1024_768 = Label(310, 365,115, 25, New)
a1024_768.color(New)
a1024_768.set_text('1024x768', 20)

a1280_1024 = Label(310, 390,115, 25, New)
a1280_1024.color(New)
a1280_1024.set_text('1280x1024', 20)

a1600_900 = Label(310, 415,115, 25, New)
a1600_900.color(New)
a1600_900.set_text('1600x900', 20)

a1920_1080 = Label(310, 440,115, 25, New)
a1920_1080.color(New)
a1920_1080.set_text('1920x1080', 20)

a2560_1440 = Label(310, 465,115, 25, New1)
a2560_1440.color(New1)
a2560_1440.set_text('2560x1440', 20)

open_resolution = Label(424, 365,25, 25, New)
open_resolution.color(New)
open_resolution.set_text('\/', 20)


ready = Label(155, 350,200, 70, GREEN)
ready.color(GREEN)
ready.set_text('Готово', 50)

savess = Label(150, 10, 80, 70, New)
savess.color(New)
savess.set_text('Збереженя', 50)

klas = Label(145, 50,80, 70, New)
klas.color(New)
klas.set_text('Вибір класса', 35)

klas2 = Label(130, 120,80, 55, New)
klas2.color(New)
klas2.set_text('', 30)

skins = Label(185, 50,80, 70, New)
skins.color(New)
skins.set_text('Колір', 60)

leftt = Label(80, 215,80, 70, New)
leftt.color(New)
leftt.set_text('<--', 50)

rightt = Label(350, 215,80, 70, New)
rightt.color(New)
rightt.set_text('-->', 50)

k1 = Label(150, 150,200, 70, RED)
k1.color(RED)
k1.set_text('Почати', 35)

k2 = Label(150, 250,200, 70, RED)
k2.color(RED)
k2.set_text('Налаштування', 20)

k3 = Label(150, 350,80, 70, RED)
k3.color(RED)
k3.set_text('Збереженя', 10)

k4 = Label(270, 350,80, 70, RED)
k4.color(RED)
k4.set_text('Вийти', 15)




assasinklas = Picture('kingal.png',210,200,100,100)
magklas = Picture('posoh.png',210,200,100,100)

spic=[
    (255, 255, 255),
    (0, 0, 0),
    (0, 252, 164),
    (252, 193, 0),
    (255, 255, 0),
    (255, 0, 0),
    (81, 255, 0),
    (0, 255, 238),
    (0, 68, 255),
    (236, 0, 252),

]
klassp={
    'ukr':[
        'Мечний',
        'Лучник',
        'Маг',
        'Ассасин'
    ],
    'pol':[
        'Miecznik',
        'Łucznik',
        'Mag',
        'Morderca'
    ],
    'eng':[
        'Sworder',
        'Archer',
        'Mag',
        'Assassin'
    ]

}


sloznost={
    'ukr':[
        'Легка',
        'Середня',
        'Складна',
        'HARD'
    ],
    'pol':[
        'Łatwy',
        'Średni',
        'Trudny',
        'HARD'
    ],
    'eng':[
        'Easy',
        'Average',
        'Difficult',
        'HARD'
    ]

}

autossp1={
    'ukr':[
        'Включено',
        'Виключено'
    ],
    'pol':[
        'Włączony',
        'Wyłączony'
    ],
    'eng':[
        'On',
        'Off'
    ]

}
 
autossp2=[
    '20s',
    '1m',
    '5m',
    '15m'
]
jazik=[
    'Україньска',
    'Polski',
    'English'
]
klas_for_zvyk={
    'ukr':[
        'вимкн',
        '10%',
        '20%',
        '30%',
        '40%',
        '50%',
        '60%',
        '70%',
        '80%',
        '90%',
        '100%'
    ],
    'eng':[
        'off',
        '10%',
        '20%',
        '30%',
        '40%',
        '50%',
        '60%',
        '70%',
        '80%',
        '90%',
        '100%'
    ],
    'pol':[
        'wył',
        '10%',
        '20%',
        '30%',
        '40%',
        '50%',
        '60%',
        '70%',
        '80%',
        '90%',
        '100%'
    ]
}
loadint4 = pygame.transform.scale(pygame.image.load('loading_4.png'),(500,500)).convert()
a = 0
while a != 10:
    mw.blit(loadint4,(0,0))
    a+=1
    pygame.display.update()
    clock.tick(60)

jazikklas()
while not game_over: 
    playername.text_enterName = playername.font_35.render(vved,True,WHITE)    
    if timer_for_music == 60:
        timer_for_music_second += 1 
        timer_for_music = 0
    timer_for_music += 1

    if timer_for_music_second == 60:
        pygame.mixer.music.load('fon_sound.ogg')
        pygame.mixer.music.play() 
    if switch==0:
        mw.fill(New)
        t = Label(50,50,100,50,New)
        t.set_text('Surrounded',70,RED)
        t.draw(-10,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                
                if k1.collidepoint(x,y):
                    switch = 1.1
                        
                elif k2.collidepoint(x,y):
                    switch = 2
                elif k3.collidepoint(x,y):
                    switch = 3
                elif k4.collidepoint(x,y):
                    game_over = True
                    mw.fill(white)

        if jazikn == 0:
            k1.draw(33,10) #ukr start
        if jazikn == 1:
            k1.draw(25,10) #pol
        if jazikn == 2:
            k1.draw(49,10) #eng
        k1.outline(RED2,10) 
        if jazikn == 0:
            k2.draw(20,20) #ukr settings
        if jazikn == 1:
            k2.draw(20,15) #pol
        if jazikn == 2:
            k2.draw(30,13) #eng
        k2.outline(RED2,10) 
        k3.draw(10,20)
        k3.outline(RED2,10) 
        k4.draw(15,20)
        k4.outline(RED2,10) 
#--------------------------NASTROIKI-------------------------------               
    if switch == 2:
        mw.fill(New)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if exit.collidepoint(x,y):
                    if return_to_game:
                        switch=1.3
                        window = pygame.display.set_mode((WIN_WIDTH_in_game,WIN_HEIGHT_in_game), pygame.FULLSCREEN)
                    else:
                        switch = 0
                if left2.collidepoint(x,y):
                        if sloz == 0:
                            break
                        sloz-=1
                elif right2.collidepoint(x,y):
                        if sloz == 3:
                            break
                        sloz+=1
                if left3.collidepoint(x,y):
                        if autosav1 == 0:
                            break
                        autosav1-=1
                elif right3.collidepoint(x,y):
                        if autosav1 == 1:
                            break
                        autosav1+=1
                if left4.collidepoint(x,y):
                        if autosav2 == 0:
                            break
                        autosav2-=1
                elif right4.collidepoint(x,y):
                        if autosav2 == 3:
                            break
                        autosav2+=1
                if left5.collidepoint(x,y):
                        jazikn-=1
                        if jazikn == -1:
                            jazikn=2
                        jazikklas()
                elif right5.collidepoint(x,y):
                        jazikn+=1
                        if jazikn == 3:
                            jazikn=0
                        jazikklas()
                if left6.collidepoint(x,y):
                        if zvykn == 0:
                            break
                        zvykn-=1
                        
                        volume-=0.1
                elif right6.collidepoint(x,y):
                        if zvykn == 10:
                            break
                        zvykn+=1
                        volume+=0.1
                if a1024_768.collidepoint(x,y):
                    if draw_all_resolution:
                        WIN_WIDTH_in_game = 1024
                        WIN_HEIGHT_in_game = 768
                        a1024_768.color(New1)
                        a1280_1024.color(New)
                        a1600_900.color(New)
                        a1920_1080.color(New)
                        a2560_1440.color(New)
                        draw_all_resolution = False
                    else:
                        if a1024_768.rect.y == 365 and a1280_1024.rect.y != 365 and a1600_900.rect.y != 365 and a1920_1080.rect.y != 365 and a2560_1440.rect.y != 365:
                            draw_all_resolution = True
                if a1280_1024.collidepoint(x,y):
                    if draw_all_resolution:
                        WIN_WIDTH_in_game = 1280
                        WIN_HEIGHT_in_game = 1024
                        a1024_768.color(New)
                        a1280_1024.color(New1)
                        a1600_900.color(New)
                        a1920_1080.color(New)
                        a2560_1440.color(New)
                        draw_all_resolution = False
                    else:
                        if a1280_1024.rect.y == 365:
                            draw_all_resolution = True
                if a1600_900.collidepoint(x,y):
                    if draw_all_resolution:
                        WIN_WIDTH_in_game = 1600
                        WIN_HEIGHT_in_game = 900
                        a1024_768.color(New)
                        a1280_1024.color(New)
                        a1600_900.color(New1)
                        a1920_1080.color(New)
                        a2560_1440.color(New)
                        draw_all_resolution = False
                    else:
                        if a1600_900.rect.y == 365:
                            draw_all_resolution = True
                if a1920_1080.collidepoint(x,y):
                    if draw_all_resolution:
                        WIN_WIDTH_in_game = 1920
                        WIN_HEIGHT_in_game = 1080
                        a1024_768.color(New)
                        a1280_1024.color(New)
                        a1600_900.color(New)
                        a1920_1080.color(New1)
                        a2560_1440.color(New)
                        draw_all_resolution = False
                    else:
                        if a1920_1080.rect.y == 365:
                            draw_all_resolution = True
                if a2560_1440.collidepoint(x,y):
                    if draw_all_resolution:
                        WIN_WIDTH_in_game = 2560
                        WIN_HEIGHT_in_game = 1340
                        a1024_768.color(New)
                        a1280_1024.color(New)
                        a1600_900.color(New)
                        a1920_1080.color(New)
                        a2560_1440.color(New1)
                        draw_all_resolution = False
                    else:
                        if a2560_1440.rect.y == 365:
                            draw_all_resolution = True
                if open_resolution.collidepoint(x,y):
                    if draw_all_resolution: 
                        open_resolution.set_text('\/',20)
                        draw_all_resolution = False
                    else:
                        open_resolution.set_text("/\ ",20)
                        draw_all_resolution = True

        pygame.mixer.music.set_volume(volume)
        
        slozn.set_text(sloznost[language][sloz],30) 
         
        left2.draw()
        right2.draw()
        if sloz == 0:
            slozn.draw(20,0)
        elif sloz == 3:
            slozn.draw(25,0)    
        elif sloz == 2 and language == 'pol':
            slozn.draw(20,0)  
        else:
            slozn.draw()      
        sloztxt.draw()
        
        autos1.set_text(autossp1[language][autosav1],30)  
        left3.draw()
        right3.draw()
            
        if language == 'eng':
            autosave1.draw(50,0)
            autos1.draw(50,0)  
        elif language == 'pol':
            autosave1.draw() 
            if autosav1 == 1:
                autos1.draw(10,0)
            else:
                autos1.draw(20,0) 
        else:
            autosave1.draw()
            autos1.draw()  
        if autosav1 == 0:
            autos2.set_text(autossp2[autosav2],30)  
            left4.draw()
            right4.draw()
            autos2.draw(50,0)      
            if language == 'eng':
                autosave2.draw(30,0)
            else:
                autosave2.draw()
        
          

        jazikmen.set_text(jazik[jazikn],30)  
        left5.draw()
        right5.draw()
        if jazikn == 0:
            jazikmen.draw(5,0)      
        else:
            jazikmen.draw(30,0) 
        jaziknat.draw(10,0)    

        zvyka.set_text(klas_for_zvyk[language][zvykn],30)  
        left6.draw()
        right6.draw()
        zvyk.draw(40,0)      
        zvyka.draw(40,0)
        display.draw() 
        if WIN_WIDTH_in_game == 1024 or draw_all_resolution:
            a1024_768.draw(5,-1) 
            a1024_768.outline(BLACK,1)

        if WIN_WIDTH_in_game == 1280 or draw_all_resolution: 
            if draw_all_resolution:
                a1280_1024.rect.y = 390
            else:
                a1280_1024.rect.y = 365
            a1280_1024.draw(0,-1) 
            a1280_1024.outline(BLACK,1)

        if WIN_WIDTH_in_game == 1600 or draw_all_resolution:
            if draw_all_resolution:
                a1600_900.rect.y = 415
            else:
                a1600_900.rect.y = 365
            a1600_900.draw(5,-1) 
            a1600_900.outline(BLACK,1)

        if WIN_WIDTH_in_game == 1920 or draw_all_resolution:
            if draw_all_resolution:
                a1920_1080.rect.y = 440
            else:
                a1920_1080.rect.y = 365
            a1920_1080.draw(0,-1) 
            a1920_1080.outline(BLACK,1)

        if WIN_WIDTH_in_game == 2560 or draw_all_resolution:
            if draw_all_resolution:
                a2560_1440.rect.y = 465
            else:

                a2560_1440.rect.y = 365
            a2560_1440.draw(0,-1) 
            a2560_1440.outline(BLACK,1)

        open_resolution.draw(3,-1)
        open_resolution.outline(BLACK,1)
        exit.draw()
        if jazikn == 0:
            nastr.draw(0,0)
        else:
            nastr.draw(40,0)
#------------------VIBOR PERSONASA-----------------------------------------
    if switch == 1.1:
        mw.fill(New)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if playername.btn_go_rect.collidepoint(x,y):
                    if len(playername.user_name) > 4:
                        switch =1.11
                if exit.collidepoint(x,y):
                    switch=0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    playername.user_name = playername.user_name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(playername.user_name) > 4:
                        switch =1.11         
                elif len(playername.user_name) < 10:
                    playername.user_name += event.unicode
        playername.update()            
        exit.draw()
    if switch==1.11:
        mw.fill(New)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if True:
                    if exit.collidepoint(x,y):
                        switch=1.1
                    if ready.collidepoint(x,y):
                        switch=1.2
                    if leftt.collidepoint(x,y):
                        s+=1
                        if s == 10:
                            s=0

                        player2.color(spic[s])
                    elif rightt.collidepoint(x,y):
                        s-=1
                        if s == -1:
                            s=9
                        
                        player2.color(spic[s])
        
        player2 = Label(210, 200,100, 100, spic[s])
        
        


        player2.set_text('',1)
        player2.draw()
            
        
        leftt.draw()
        rightt.draw()
        ready.draw(30,0)
        ready.outline(GREEN_outline,10) 
        skins.draw(-10,20)
        exit.draw()
    if switch == 1.2:
        mw.fill(New)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if True:
                    if exit.collidepoint(x,y):
                        switch=1.11
                    if ready.collidepoint(x,y):
                        switch=1.3
                    if leftt.collidepoint(x,y):
                        klas_+=1
                        if klas_ == 4:
                            klas_=0
            
                    elif rightt.collidepoint(x,y):
                        klas_-=1
                        if klas_ == -1:
                            klas_=3
        if klas_ == 0:
            pass
            #swordklas.draw()
        elif klas_ == 1:
            pass
            #bowklas.draw()
        elif klas_ == 2:
            pass
            magklas.draw()
        else:
            assasinklas.draw()

        
            
    
        klas2.set_text(klassp[language][klas_], 40) 
        if klas_ == 2:
            klas2.draw(85,0)   
        else:
            klas2.draw(50,0)  
        exit.draw()          
        klas.draw()
        leftt.draw()
        rightt.draw()         
        ready.draw(30,0)
        ready.outline(GREEN_outline,10) 
    if switch == 3:
        mw.fill(New)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if True:
                    if exit.collidepoint(x,y):
                        switch=0
            if event.type == pygame.QUIT:
                game_over = True
        savess.draw()
        exit.draw()
    if switch == 1.3:
        #------------------START GAME----------------------------------
        if adsdsd == 1:
            asasin_ = armor(50,50)
            player = Player((WIN_WIDTH_in_game//3)-25,(WIN_HEIGHT_in_game//3)-25,50,50,spic[s])
            window = pygame.display.set_mode((WIN_WIDTH_in_game,WIN_HEIGHT_in_game), pygame.FULLSCREEN)
            adsdsd +=1 
            if sloz == 0:
                health = 'inf'
            if sloz == 1:
                health = 3
            if sloz == 2:
                health = 1
            if sloz == 3:
                health = 0

        if eskape:
            mw.blit(background,(x_map,y_map))
            esk_w = pygame.Rect((485, 130), (350, 475)) 
            pygame.draw.rect(mw, GRAY, esk_w)
            pygame.draw.rect(mw, grey_outline, esk_w, 10)


            if language == 'pol' or language == 'ukr':
                resume.draw(40,15)
            else:
                resume.draw(40,15)

            resume.outline(New_outline,10) 

            mw.blit(pause,(540,160))

            settings.draw(30,10)
            settings.outline(New_outline,10) 
        
            exit_to_menu.draw(30,20)
            exit_to_menu.outline(New_outline,10) 
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if eskape:
                                game = ''
                                eskape = False 
                            else: 
                                game = 'stop'
                                eskape = True  
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if player.atack != 'atack':
                        player.atack = 'atack'
                        timer = 0
                        if klas_ == 0 or klas_ == 3:
                            for i in zombie:
                                if player.direction == 'left':
                                    if player.x-i.w-20 < i.x and player.x > i.x:
                                        i.hp -= player.atack_power
                                if player.direction == 'right':
                                    if player.x+i.w+20 > i.x and player.x < i.x:
                                        i.hp -= player.atack_power
                                if player.direction == 'up':
                                    if player.y-i.h-20 < i.y and player.y > i.y:
                                        i.hp -= player.atack_power
                                if player.direction == 'down':
                                    if player.y+i.h+20 > i.y and player.y < i.y:
                                        i.hp -= player.atack_power
                        else:
                            fireball = bullet((WIN_WIDTH_in_game//3)-25,(WIN_HEIGHT_in_game//3)-25,40,40,'fireball')    
                            


                            #if player.x+i.w > i.x and player.x-i.w < i.x and player.y+i.h > i.y and player.y-i.h < i.y:
                             #   i.hp -= player.atack_power
                    
                
                    if eskape:
                        if resume.collidepoint(x,y):
                                game = ''
                                eskape = False 
                        elif settings.collidepoint(x,y): 
                            adsdsd = 1    
                            switch = 2
                            return_to_game = True
                            WIN_WIDTH=500
                            WIN_HEIGHT=500
                            mw = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
                        elif exit_to_menu.collidepoint(x,y):
                            adsdsd = 1
                            switch = 0
                            WIN_WIDTH=500
                            WIN_HEIGHT=500
                            mw = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        if game != 'stop':
            mw.blit(background,(x_map,y_map))
            for i in zombie:
                i.update()
            player.update()
            hp.update(player.hp)
            for i in bullets:
                i.update()

            if timer < player.couldown:
                timer +=2
                if timer == player.couldown:
                    player.atack = ''
            
            

    pygame.display.update()
    clock.tick(60)
 