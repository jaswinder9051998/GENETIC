import pygame
import random
import math

import numpy as np
import pandas as pd
import warnings
import time

warnings.simplefilter("ignore")

WIDTH=800
WIDTHGAME=400
HEIGHT=500
HEIGHTGAME=500
GAMEMIN=50
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)
BOUN=(165,42,42)
PINK=(255,192,203)

targetx=380
targety=460
tw=40
th=40
    












def draw_enviroment(pp,hurd,td,game_display):
    game_display.fill(WHITE)
    pygame.draw.line(game_display,(0,0,0),(0,GAMEMIN),(WIDTH,GAMEMIN))
    pygame.draw.rect(game_display,(0,0,0),[td.targetx,td.targety,td.tw,td.th])
    for i in range(len(hurd)):
        pygame.draw.rect(game_display,RED,[hurd[i].lx,hurd[i].ly,hurd[i].rx-hurd[i].lx,hurd[i].ry-hurd[i].ly])
    for obj in pp.pop:
        
        pygame.draw.circle(game_display,obj.color,[(int)(obj.x),(int)(obj.y)],obj.size)
        
        
    pygame.display.update()

def drawtarget(td,game_display):
    #game_display.fill(WHITE)
    pygame.draw.line(game_display,(0,0,0),(0,GAMEMIN),(WIDTH,GAMEMIN))
    pygame.draw.rect(game_display,(0,0,0),[td.targetx,td.targety,td.tw,td.th])
    pygame.display.update()



class hurdle(object):
    def __init__(self,lx,ly,rx,ry):
        self.lx=lx
        self.ly=ly
        self.rx=rx
        self.ry=ry
        self.lrx=rx
        self.lry=ly
        self.rlx=lx
        self.rly=ry

class targetd:
    def __init__(self,targetx,targety,tw,th):
        self.targetx=targetx
        self.targety=targety
        self.tw=tw
        self.th=th
    def change(self,targetx,targety):
        self.targetx=targetx
        self.targety=targety
        
    
class ball(object):
    def __init__(self,moves,velocity):
        self.moves=moves
        self.angle=[]
        self.x=WIDTH/2
        self.y=50
        self.v=velocity
        self.color=BLUE
        self.size=2
    def create(self,):
        for i in range(self.moves):
            self.angle.append(random.randint(0,360))
    def move(self,xinc,yinc,hurd,td):
        self.x+=xinc
        self.y+=yinc
        for t in range(len(hurd)):
            if((self.x>hurd[t].lx and self.x<hurd[t].rx) and (self.y>hurd[t].ly and self.y<hurd[t].ry)):
                self.y=hurd[t].ly
            if((self.x>td.targetx and self.x<td.targetx+td.tw) and (self.y>td.targety and self.y<td.targety+td.th)):
                self.color=GREEN
            else:
                self.color=BLUE
    
        

class population:
    def __init__(self,popu,mutR,moves,velocity,targetx,targety):
        self.popu=popu
        self.moves=moves
        self.mutR=mutR
        self.pop=[]
        self.fit=[]
        self.targetx=targetx
        self.v=velocity
        self.targety=targety
        self.matingp=[]
        self.reward=[]
    def create(self,):
        for i in range(self.popu):
            self.pop.append(ball(self.moves,self.v))
        for obj in self.pop:
            obj.create()

    def ct(self,targetx,targety):
        self.targetx=targetx
        self.targety=targety
        
        
    def fitness(self,):
        self.fit=[]
        for obj in self.pop:
            self.fit.append(1/(((self.targetx-obj.x)**2+(self.targety-obj.y)**2))**2)
    def mating(self,):
        self.fitness()
        self.matingp=[]
        maxx=max(self.fit)
        i=0
        for obj in self.pop:
            n=(int)((self.fit[i])/(maxx)*100)
            for j in range(n):
                self.matingp.append(obj)
            i+=1
        
    def reprod(self,pp1):
        self.mating()
        for i in range(self.popu):
            m=random.randint(0,len(self.matingp)-1)
            n=random.randint(0,len(self.matingp)-1)
            obj1=self.matingp[m]
            obj2=self.matingp[n]
            child=ball(self.moves,self.v)
            child.create()
            mid=random.randint(0,self.moves-1)
            for j in range(self.moves):
                if(j>mid):
                    child.angle[j]=obj1.angle[j]
                else:
                    child.angle[j]=obj2.angle[j]
            for k in range(self.moves):
                if(random.random()<self.mutR):
                    child.angle[k]=random.randint(0,360)
            pp1.pop[i]=child
        return pp1
                    
            
            
            
        

def main():
    
    pygame.init()
    game_display=pygame.display.set_mode((WIDTH,HEIGHTGAME))
    
    targetx=380
    targety=460
    tw=40
    th=40

    moves=60
    td=targetd(targetx,targety,tw,th)
    pp=population(1000,0.03,moves,11,td.targetx+td.tw/2,td.targety+td.th/2)
    pp.create()
    h1=hurdle(300,240,500,260)
    hurd=[]
    hurd.append(h1)
    gen=0
    flag=0
    clock=pygame.time.Clock()
    while True:
        
        
            


        for i in range(moves):
            for obj in pp.pop:
                obj.move(math.cos(math.pi*obj.angle[i]/180)*pp.v,math.sin(math.pi*obj.angle[i]/180)*pp.v,hurd,td)
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
            pygame.event.get()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos=pygame.mouse.get_pos()
                    ttx=pos[0]
                    tty=pos[1]
                    hz=hurdle(ttx-20,tty-20,ttx+20,tty+20)
                    hurd.append(hz)
            key=pygame.key.get_pressed()
            if key[pygame.K_w]:
                td.targety-=td.th/4
                drawtarget(td,game_display)
            if key[pygame.K_s]:
                td.targety+=td.th/4
                drawtarget(td,game_display)
            if key[pygame.K_a]:
                td.targetx-=td.tw/4
                drawtarget(td,game_display)
            if key[pygame.K_f]:
                td.targetx+=td.tw/4
                drawtarget(td,game_display)
            
                
                
                    
  
            draw_enviroment(pp,hurd,td,game_display)
        gen+=1
        pp1=population(1000,0.03,moves,11,td.targetx+td.tw/2,td.targety+td.th/2)
        pp1.create()
        pp.fitness();
        print("gen : ",gen,"->",max(pp.fit))
        pp=pp.reprod(pp1)
        
        clock.tick(60)
            

    
if __name__=='__main__':
  main()





