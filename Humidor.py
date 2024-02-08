import sys
import pygame
import random
import math

pygame.mixer.init()
pygame.mixer_music.load("data/tittle_music.mp3")
pygame.mixer_music.play(-1)
laser_sound=pygame.mixer.Sound("data/laser_sound.mp3")
whoosh_sound=pygame.mixer.Sound("data/boss_flyby.mp3")
teleport=pygame.mixer.Sound("data/teleport.mp3")
intro_thunder=pygame.mixer.Sound("data/intro_thunder.mp3")
boss_roar=pygame.mixer.Sound("data/boss_roar.mp3")
thunder_warn=pygame.mixer.Sound("data/thunder_warn.mp3")
side_warn_sound=pygame.mixer.Sound("data/side_warn_sound.mp3")
side_attack_sound=pygame.mixer.Sound("data/side_attack_sound.mp3")
thunder_attack_sound=pygame.mixer.Sound("data/thunder_attack_sound.mp3")
circle_warn_sound=pygame.mixer.Sound("data/circle_warn_sound.mp3")
circle_attack_sound=pygame.mixer.Sound("data/circle_attack_sound.mp3")
pygame.mixer.Sound.set_volume(laser_sound,0.2)

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Humidor")
        self.screen=pygame.display.set_mode((1500,700))
        self.clock=pygame.time.Clock()
        self.bg=pygame.image.load("data/background.png")
        self.bg=pygame.transform.scale(self.bg,(1500,700))
        self.tittle_screen=pygame.image.load("data/tittle_screen.png")
        self.tittle_screen=pygame.transform.scale(self.tittle_screen,(1500,700))

        self.retry_screen=pygame.image.load("data/tittle_screen.png")
        self.retry_screen=pygame.transform.scale(self.retry_screen,(1500,700))

        self.my_font = pygame.font.SysFont('malgungothic', 500,False,True)
        self.text_tittle=self.my_font.render("Humidor", False, (100, 0, 255))
        self.text_tittle=pygame.transform.scale(self.text_tittle,(600,200))

        self.text_tittle_shadow=self.my_font.render("Humidor", False, (0, 0, 0))
        self.text_tittle_shadow=pygame.transform.scale(self.text_tittle_shadow,(600,200))
        
        self.text_retry=self.my_font.render("Never Give Up", False, (100, 0, 255))
        self.text_retry=pygame.transform.scale(self.text_retry,(600,200))

        self.text_retry_shadow=self.my_font.render("Never Give Up", False, (0, 0, 0))
        self.text_retry_shadow=pygame.transform.scale(self.text_retry_shadow,(600,200))

        self.text_retry_button=self.my_font.render("Retry", False, (100, 0, 255))
        self.text_retry_button=pygame.transform.scale(self.text_retry_button,(300,150))

        self.circle_lightning=pygame.image.load("data/circle_lightning.png")

        self.circle_lightning1=pygame.transform.scale(self.circle_lightning,(100,100))
        self.circle_lightning2=pygame.transform.scale(self.circle_lightning,(100,100))
        self.circle_lightning3=pygame.transform.scale(self.circle_lightning,(100,100))

        self.circle_warn=pygame.image.load("data/circle_warn.png")

        self.circle_warn=pygame.transform.rotate(self.circle_warn,90)
        self.circle_warn=pygame.transform.scale(self.circle_warn,(200,200))

        self.text_play=self.my_font.render("Ready?", False, (0, 0, 0))
        self.text_play=pygame.transform.scale(self.text_play,(300,150))
        
        self.player=pygame.image.load("data/sun.png")
        self.player=pygame.transform.scale(self.player,(100,100))

        self.laser=pygame.image.load("data/laser_beam.png")
        self.laser=pygame.transform.scale(self.laser,(1600,70))

        self.roar_lines=pygame.image.load("data/roar_lines.png")
        self.roar_lines=pygame.transform.scale(self.roar_lines,(1500,700))

        self.thunder_warn_shine=pygame.image.load("data/thunder_warn_shine.png")
        self.thunder_warn_shine=pygame.transform.scale(self.thunder_warn_shine,(300,300))

        self.side_warn=pygame.image.load("data/side_warn.png")
        self.side_warn=pygame.transform.scale(self.side_warn,(300,300))

        self.side_warn_left=pygame.transform.rotate(self.side_warn,270)
        self.side_warn_right=pygame.transform.rotate(self.side_warn,90)

        self.side_lightning=pygame.image.load("data/side_lightning.png")
        self.side_lightning=pygame.transform.scale(self.side_lightning,(600,100))

        self.side_attack_light=pygame.image.load("data/side_attack.png")
        self.side_attack_light=pygame.transform.scale(self.side_attack_light,(1500,100))

        self.vertical_tp=pygame.image.load("data/side_lightning.png")
        self.vertical_tp=pygame.transform.rotate(self.vertical_tp,90)
        self.vertical_tp=pygame.transform.scale(self.vertical_tp,(200,700))

        self.left_warn=pygame.transform.rotate(self.side_warn,90)
        self.left_warn=pygame.transform.scale(self.left_warn,(200,200))

        self.right_warn=pygame.transform.rotate(self.side_warn,270)
        self.right_warn=pygame.transform.scale(self.right_warn,(200,200))

        self.ball=pygame.image.load("data/ball.png")
        self.ball=pygame.transform.scale(self.ball,(150,150))

        self.shine=pygame.image.load("data/shine.png")
        self.shine=pygame.transform.scale(self.shine,(150,150))

        self.thunder_lightning=pygame.image.load("data/thunder_attack.png")
        self.thunder_lightning=pygame.transform.scale(self.thunder_lightning,(500,700))

        self.boss_part=pygame.image.load("data/cloud_part.png")
        self.boss_part_left=pygame.transform.scale(self.boss_part,(500,500))
        self.boss_part_mid=pygame.transform.scale(self.boss_part,(500,500))
        self.boss_part_right=pygame.transform.scale(self.boss_part,(500,500))

        self.logo_sun=pygame.image.load("data/logo_sun.png")
        self.logo_sun=pygame.transform.scale(self.logo_sun,(1500,700))

        self.logo_cloud=pygame.image.load("data/logo_cloud.png")
        self.logo_cloud=pygame.transform.scale(self.logo_cloud,(600,200))

        self.boss_side=pygame.image.load("data/side_cloud.png")

        self.boss_left=pygame.transform.rotate(self.boss_side,90)
        self.boss_left=pygame.transform.scale(self.boss_left,(300,700))

        self.boss_up=pygame.transform.scale(self.boss_side,(1500,200))

        self.boss_right=pygame.transform.rotate(self.boss_side,270)
        self.boss_right=pygame.transform.scale(self.boss_right,(300,700))

        self.player_pos=[700,600]
        self.player_movement=[0,0,0,0]

        self.collision_up=pygame.rect.Rect(0,0,1500,1)
        self.collision_down=pygame.rect.Rect(0,700,1500,1)
        self.collision_left=pygame.rect.Rect(0,0,1,700)
        self.collision_right=pygame.rect.Rect(1450,0,1,700)

        self.retry_button=pygame.rect.Rect(600,500,300,150)

        self.tittle=True

        self.clicked=False

        self.boss_music_flag=True

        self.retry_music_flag=True

        self.retry=False

        self.entrance=True

        self.entrance_sounds=True

        self.across_flyby=True

        self.fs=0

        self.upwards_flyby=False

        self.get_into_pos=True

        self.intro_thunder_sound_flag=True

        self.hp=200000

        self.roar_flag=True

        self.idle_flag=True

        self.attack_chose=False

        self.into_thunder_flag=True

        self.init_thunder=False

        self.into_side_flag=True

        self.into_circle_flag=True

        self.col_left=pygame.rect.Rect(0,0,0,0)
        self.col_right=pygame.rect.Rect(0,0,0,0)
        self.col_mid=pygame.rect.Rect(0,0,0,0)

        self.up_c=pygame.rect.Rect(0,0,0,0)

        self.side_left_c=pygame.rect.Rect(0,0,0,0)
        self.side_right_c=pygame.rect.Rect(0,0,0,0)

        self.up_c1=pygame.rect.Rect(0,0,0,0)
        self.up_c2=pygame.rect.Rect(0,0,0,0)
        self.up_c3=pygame.rect.Rect(0,0,0,0)

        self.light_left_c=pygame.rect.Rect(0,0,0,0)
        self.light_right_c=pygame.rect.Rect(0,0,0,0)

        self.circle_c=pygame.rect.Rect(0,0,0,0)
        
        self.t1=pygame.rect.Rect(0,0,0,0)
        self.t2=pygame.rect.Rect(0,0,0,0)
        self.t3=pygame.rect.Rect(0,0,0,0)

    def rotate(self,surface, angle, pivot, offset):

        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
        rotated_offset = offset.rotate(angle)

        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect

    def idle(self):
        if self.idle_flag:
            self.side_lightning=pygame.transform.scale(self.side_lightning,(600,200))
            self.idle_time=0
            self.teleport_sound_flag=True
            self.idle_in_step=0
            self.idle_out_step=0
            self.idle_s=0
            self.idle_flag=False
            self.choise_flag=False

        self.le_time=int(pygame.time.get_ticks()/1000)

        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))

        self.screen.blit(self.player,self.player_pos)
        self.collision_player=pygame.rect.Rect(self.player_pos[0],self.player_pos[1],70,70)

        if self.idle_in:
            self.screen.blit(self.boss_part_left,(200,-600+self.idle_in_step))
            self.screen.blit(self.boss_part_right,(700,-600+self.idle_in_step))
            self.screen.blit(self.boss_part_mid,(450,-700+self.idle_in_step))

            self.col_left=pygame.rect.Rect(250,-650+self.idle_in_step,500,500)
            self.col_right=pygame.rect.Rect(750,-650+self.idle_in_step,500,500)
            self.col_mid=pygame.rect.Rect(500,-750+self.idle_in_step,500,500)

            if self.idle_in_step>=500:
                self.idle_in=False
                self.idle_an=True

            self.idle_in_step+=1

        if self.idle_an:

            if self.le_time%2==0:
                self.idle_s+=1
            else:
                self.idle_s-=1
                        
            self.screen.blit(self.boss_part_left,(200,-100+self.idle_s))
            self.screen.blit(self.boss_part_right,(700,-100+self.idle_s))
            self.screen.blit(self.boss_part_mid,(450,-200+self.idle_s))

            self.col_left=pygame.rect.Rect(250,-50+self.idle_s,500,500)
            self.col_right=pygame.rect.Rect(750,-50+self.idle_s,500,500)
            self.col_mid=pygame.rect.Rect(500,-150+self.idle_s,500,500)

        if self.idle_time>=180 and self.idle_time<200:
            if self.teleport_sound_flag:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound(teleport))
                self.teleport_sound_flag=False

            self.screen.blit(self.side_lightning,(200,self.idle_s))
            self.screen.blit(self.side_lightning,(700,self.idle_s))
            self.screen.blit(self.side_lightning,(450,-100+self.idle_s))

            self.screen.blit(self.side_lightning,(200,self.idle_s+50))
            self.screen.blit(self.side_lightning,(700,self.idle_s+50))
            self.screen.blit(self.side_lightning,(450,-100+self.idle_s+50))

            self.screen.blit(self.side_lightning,(200,self.idle_s-50))
            self.screen.blit(self.side_lightning,(700,self.idle_s-50))
            self.screen.blit(self.side_lightning,(450,-100+self.idle_s-50))

        if self.idle_time>=210:
            self.in_idle=False
            self.attack_chose=True
            self.choise_flag=True

        self.idle_time+=1

        return self.in_idle,self.choise_flag
    
    def thunder_attack(self):
        if self.into_thunder_flag:
            self.side_lightning=pygame.transform.scale(self.side_lightning,(1500,200))
            self.init_thunder=False
            self.thunder_time=70
            self.teleport_sound_flag=True
            self.into_thunder_flag=False
            self.thunder_order=[]
            self.tc=0
            self.tc_s=[]
            self.choise_flag=False
            self.thunder_sound_flag=True
            self.thunder_warn_sound_flag=True

            for i in range(3):
                self.thunder_choise=random.randint(1,3)
                self.thunder_order.append(self.thunder_choise)
            self.intro_thunder_flag=False

            for thunder in self.thunder_order:
                    if thunder==1:
                        self.tc=0
                        self.tc_s.append(self.tc)
                    if thunder==2:
                        self.tc=500
                        self.tc_s.append(self.tc)
                    if thunder==3:
                        self.tc=1000
                        self.tc_s.append(self.tc)

        if self.thunder_time>=70 and self.thunder_time<90:
            if self.teleport_sound_flag:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound(teleport))
                self.teleport_sound_flag=False

            self.screen.blit(self.side_lightning,(0,0))
            self.screen.blit(self.side_lightning,(0,100))
            self.screen.blit(self.side_lightning,(0,200))


        if self.thunder_time>=90 and self.thunder_time<=180:

            self.screen.blit(self.boss_part_left,(0,-100))
            self.screen.blit(self.boss_part_right,(500,-100))
            self.screen.blit(self.boss_part_mid,(1000,-100))

            self.col_left=pygame.rect.Rect(0,-100,500,500)
            self.col_right=pygame.rect.Rect(500,-100,500,500)
            self.col_mid=pygame.rect.Rect(1000,-100,500,500)

            if self.thunder_time>=90 and self.thunder_time<95:
                if self.thunder_warn_sound_flag:
                    pygame.mixer.Channel(2).stop()
                    pygame.mixer.Sound.stop(thunder_warn)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(thunder_warn))
                    self.thunder_warn_sound_flag=False
                
                self.screen.blit(self.thunder_warn_shine,(self.tc_s[0]+100,0))
            if self.thunder_time>=110 and self.thunder_time<115:
                self.thunder_warn_sound_flag=True
                if self.thunder_warn_sound_flag:

                    pygame.mixer.Sound.stop(thunder_warn)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(thunder_warn))
                    self.thunder_warn_sound_flag=False
                self.screen.blit(self.thunder_warn_shine,(self.tc_s[1]+100,0))
            if self.thunder_time>=130 and self.thunder_time<135:
                self.thunder_warn_sound_flag=True
                if self.thunder_warn_sound_flag:

                    pygame.mixer.Sound.stop(thunder_warn)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(thunder_warn))
                    self.thunder_warn_sound_flag=False
                self.screen.blit(self.thunder_warn_shine,(self.tc_s[2]+100,0))
      
        if self.thunder_time==180:
            self.init_thunder=True

        if self.init_thunder:

            self.screen.blit(self.boss_part_left,(0,-100))
            self.screen.blit(self.boss_part_right,(500,-100))
            self.screen.blit(self.boss_part_mid,(1000,-100))

            self.col_left=pygame.rect.Rect(0,-100,500,500)
            self.col_right=pygame.rect.Rect(500,-100,500,500)
            self.col_mid=pygame.rect.Rect(1000,-100,500,500)

            if self.thunder_time>=200 and self.thunder_time<205:
                if self.thunder_sound_flag:

                    pygame.mixer.Sound.stop(thunder_attack_sound)
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound(thunder_attack_sound))
                    self.thunder_sound_flag=False

                self.screen.blit(self.thunder_lightning,(self.tc_s[0],0))
                self.t1=pygame.rect.Rect(self.tc_s[0],0,500,700)

            if self.thunder_time>=205:
                self.t1=pygame.rect.Rect(0,0,0,0)
            
            if self.thunder_time>=265 and self.thunder_time<270:

                self.thunder_sound_flag=True
                if self.thunder_sound_flag:

                    pygame.mixer.Sound.stop(thunder_attack_sound)
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound(thunder_attack_sound))
                    self.thunder_sound_flag=False

                self.screen.blit(self.thunder_lightning,(self.tc_s[1],0))
                self.t2=pygame.rect.Rect(self.tc_s[1],0,500,700)

            if self.thunder_time>=270:
                self.t2=pygame.rect.Rect(0,0,0,0)

            if self.thunder_time>=330 and self.thunder_time<335:

                self.t2=pygame.rect.Rect(0,0,0,0)

                self.thunder_sound_flag=True
                if self.thunder_sound_flag:
                    pygame.mixer.Sound.stop(thunder_attack_sound)
                    pygame.mixer.Channel(3).play(pygame.mixer.Sound(thunder_attack_sound))
                    self.thunder_sound_flag=False

                self.screen.blit(self.thunder_lightning,(self.tc_s[2],0))
                self.t3=pygame.rect.Rect(self.tc_s[2],0,500,700)

            if self.thunder_time==335:
                self.init_thunder=False

        if self.thunder_time>=335:
                self.t3=pygame.rect.Rect(0,0,0,0)

        if self.thunder_time>=335 and self.thunder_time<=395:
            self.teleport_sound_flag=True
            self.screen.blit(self.boss_part_left,(0,-100))
            self.screen.blit(self.boss_part_right,(500,-100))
            self.screen.blit(self.boss_part_mid,(1000,-100))

            self.col_left=pygame.rect.Rect(0,-100,500,500)
            self.col_right=pygame.rect.Rect(500,-100,500,500)
            self.col_mid=pygame.rect.Rect(1000,-100,500,500)


        if self.thunder_time>=395 and self.thunder_time<415:
            if self.teleport_sound_flag:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound(teleport))
                self.teleport_sound_flag=False

            self.screen.blit(self.side_lightning,(0,0))
            self.screen.blit(self.side_lightning,(0,100))
            self.screen.blit(self.side_lightning,(0,200))
            

        if self.thunder_time>=420:
            self.choise_flag=True
            self.into_thunder_flag=True

        self.thunder_time+=1

        return self.choise_flag,self.col_left,self.col_right,self.col_mid
        
    def side_attack(self):

        if self.into_side_flag:
            self.side_time=0
            self.into_side_flag=False
            self.teleport_sound_flag=True
            self.init_side=False
            self.side_timer=0
            self.side_timer_flag=True
            self.side_n=0
            self.side_sound_flag=True
            self.init_timer=0
            self.side_first=True
            self.side_n_n=1
            self.side_final=False

            self.sc=[]
            for i in range(10):
                self.side_y=random.randint(0,600)
                self.sc.append(self.side_y)
        
        if self.side_time<=10:
            if self.teleport_sound_flag:
                pygame.mixer.Channel(6).play(pygame.mixer.Sound(teleport))
                self.screen.blit(self.vertical_tp,(0,0))
                self.screen.blit(self.vertical_tp,(0,0))
                self.screen.blit(self.vertical_tp,(0,0))

                self.screen.blit(self.vertical_tp,(1400,0))
                self.screen.blit(self.vertical_tp,(1300,0))
                self.screen.blit(self.vertical_tp,(1200,0))
                self.teleport_sound_flag=False

        if self.side_time>10 and self.side_time<=20:

            self.screen.blit(self.boss_left,(-100,0))
            self.screen.blit(self.boss_right,(1300,0))
            self.side_left_c=pygame.rect.Rect(-100,0,300,700)
            self.side_right_c=pygame.rect.Rect(1300,0,300,700)
        
        if self.side_time>20 and self.side_time<=620:
                
            if self.side_timer==120:
                self.side_timer=0
                self.side_sound_flag=True
                self.side_n+=2
            
            if self.side_timer>=0 and self.side_timer<60:

                if not(self.side_first):
                    if self.side_sound_flag:
                        pygame.mixer.Channel(4).stop()
                        pygame.mixer.Channel(4).play(pygame.mixer.Sound(side_attack_sound))
                    
                    if self.side_timer>=0 and self.side_timer<10:
                        self.screen.blit(self.side_attack_light,(0,self.sc[self.side_n_n]-25))
                        self.light_left_c=pygame.rect.Rect(0,self.sc[self.side_n_n],1500,50)
                        self.screen.blit(self.left_warn,(150,self.sc[self.side_n_n]-75))

                    else:
                        self.light_left_c=pygame.rect.Rect(0,0,0,0)

                if self.side_sound_flag:
                    pygame.mixer.Channel(2).stop()
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(side_warn_sound))
                    self.side_sound_flag=False

                self.side_warn_right_c=pygame.rect.Rect(0,self.sc[self.side_n],1500,50)
                pygame.draw.rect(self.screen,(0,150,255),self.side_warn_right_c)
                    
                self.screen.blit(self.right_warn,(1150,self.sc[self.side_n]-75))

            if self.side_timer==60:
                self.side_sound_flag=True
                self.side_first=False
                self.side_n_n+=2

            if self.side_timer>=60 and self.side_timer<120:

                if self.side_sound_flag:
                    pygame.mixer.Channel(4).stop()
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound(side_attack_sound))

                if self.side_sound_flag:
                    pygame.mixer.Channel(2).stop()
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(side_warn_sound))
                    self.side_sound_flag=False
        
                if self.side_timer>=60 and self.side_timer<70:
                    self.screen.blit(self.side_attack_light,(0,self.sc[self.side_n]-25))
                    self.light_right_c=pygame.rect.Rect(0,self.sc[self.side_n],1500,50)
                    self.screen.blit(self.right_warn,(1150,self.sc[self.side_n]-75))

                else:
                    self.light_right_c=pygame.rect.Rect(0,0,0,0)

                if self.side_n_n>len(self.sc)-1:
                    self.side_final=True

                if not(self.side_final):

                    self.side_warn_left_c=pygame.rect.Rect(0,self.sc[self.side_n_n],1500,50)
                    pygame.draw.rect(self.screen,(0,150,255),self.side_warn_left_c)

                    self.screen.blit(self.left_warn,(150,self.sc[self.side_n_n]-75))

            self.side_timer+=1

            if self.side_time==640:
                self.teleport_sound_flag=True

            self.screen.blit(self.boss_left,(-100,0))
            self.screen.blit(self.boss_right,(1300,0))
            self.side_left_c=pygame.rect.Rect(-100,0,300,700)
            self.side_right_c=pygame.rect.Rect(1300,0,300,700)

        if self.side_time>640 and self.side_time<650:
            if self.teleport_sound_flag:
                pygame.mixer.Channel(6).play(pygame.mixer.Sound(teleport))
                self.screen.blit(self.vertical_tp,(0,0))
                self.screen.blit(self.vertical_tp,(0,0))
                self.screen.blit(self.vertical_tp,(0,0))

                self.screen.blit(self.vertical_tp,(1400,0))
                self.screen.blit(self.vertical_tp,(1300,0))
                self.screen.blit(self.vertical_tp,(1200,0))
                self.teleport_sound_flag=False

        if self.side_time>=650:
            self.choise_flag=True
            self.into_side_flag=True
            self.side_timer_flag=True

        self.side_time+=1

        return self.choise_flag,self.light_left_c,self.light_right_c

    def circle_attack(self):
        if self.into_circle_flag:
            self.side_lightning=pygame.transform.scale(self.side_lightning,(1500,200))
            self.circle_time=0
            self.circle_timer=0
            self.into_circle_flag=False
            self.circle_sound_flag=True
            self.circle_n1=0
            self.circle_n2=0
            self.circle_n3=0

        if self.circle_time<=10:

            self.screen.blit(self.side_lightning,(0,0))
            self.screen.blit(self.side_lightning,(0,100))
            self.screen.blit(self.side_lightning,(0,-100))

        if self.circle_time>10 and self.circle_time<=330:

            self.screen.blit(self.boss_up,(0,-100))
            self.up_c=pygame.rect.Rect(0,-100,1500,200)

            if self.circle_timer==80:
                self.circle_timer=0
                self.circle_n1=0
                self.circle_n2=0
                self.circle_n3=0

            if self.circle_timer==0 or self.circle_timer==30 or self.circle_timer==60:
                if self.circle_timer==0:
                    self.circle_x1=random.randint(0,1500)
                    self.circle_x2=random.randint(0,1500)
                    self.circle_x3=random.randint(0,1500)
                self.circle_sound_flag=True

            if self.circle_timer>=0 and self.circle_timer<30:
                
                self.cr1=pygame.rect.Rect(self.circle_x1,0,50,700)
                pygame.draw.rect(self.screen,(0,150,150),self.cr1)
                #self.screen.blit(self.circle_warn,(self.circle_x1-100,50))

            if self.circle_timer>=30 and self.circle_timer<60:

                if self.circle_sound_flag:
                    pygame.mixer.Channel(4).stop
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound(circle_attack_sound))
                    self.circle_sound_flag=False

                self.screen.blit(self.circle_lightning1,(self.circle_x1-50,self.circle_n1))
                self.up_c1=pygame.rect.Rect(self.circle_x1-50,self.circle_n1,100,100)

                self.cr2=pygame.rect.Rect(self.circle_x2,0,50,700)
                pygame.draw.rect(self.screen,(0,150,150),self.cr2)

                #self.screen.blit(self.circle_warn,(self.circle_x2-100,50))

                self.circle_n1+=50

            if self.circle_timer>=60 and self.circle_timer<90:

                if self.circle_sound_flag:
                    pygame.mixer.Channel(4).stop
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound(circle_attack_sound))
                    self.circle_sound_flag=False

                self.screen.blit(self.circle_lightning2,(self.circle_x2-50,self.circle_n2))
                self.up_c2=pygame.rect.Rect(self.circle_x2-50,self.circle_n2,100,100)

                self.cr3=pygame.rect.Rect(self.circle_x3,0,50,700)
                pygame.draw.rect(self.screen,(0,150,150),self.cr3)

                #self.screen.blit(self.circle_warn,(self.circle_x3-100,50))

                self.circle_n2+=50

            if self.circle_timer>=90 and self.circle_timer<120:

                if self.circle_sound_flag:
                    pygame.mixer.Channel(4).stop
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound(circle_attack_sound))
                    self.circle_sound_flag=False

                self.screen.blit(self.circle_lightning3,(self.circle_x3-50,self.circle_n3))
                self.up_c3=pygame.rect.Rect(self.circle_x3-50,self.circle_n3,100,100)


                self.circle_n3+=50

            

            self.circle_timer+=1
            

        if self.circle_time>480 and self.circle_time<490:
            self.screen.blit(self.side_lightning,(0,0))
            self.screen.blit(self.side_lightning,(0,100))
            self.screen.blit(self.side_lightning,(0,200))

        if self.circle_time>=490:
            self.choise_flag=True
            self.into_circle_flag=True
            self.circle_timer_flag=True

        self.circle_time+=1

        return self.choise_flag,self.up_c1,self.up_c2,self.up_c3


    def run(self):
        while True:

            while self.tittle:

                self.screen.fill((0,0,0))
                self.screen.blit(self.tittle_screen,(0,0)) 
                self.screen.blit(self.logo_sun,(0,-50))
                self.screen.blit(self.logo_cloud,(400,150))
                self.screen.blit(self.text_tittle_shadow,(455,155))
                self.screen.blit(self.text_tittle,(450,150))
                
                self.text_play=self.my_font.render("Ready?", False, (0, 0, 0))
                self.text_play=pygame.transform.scale(self.text_play,(300,150))
                self.start_button=pygame.rect.Rect(600,500,300,150) 
                self.start_button_shadow=pygame.rect.Rect(595,495,310,160)
                pygame.draw.rect(self.screen,(0,0,255),self.start_button)

                self.screen.blit(self.text_play,(600,490))

                self.mouse_pos=pygame.mouse.get_pos()
                if pygame.rect.Rect.collidepoint(self.start_button,self.mouse_pos):
                    pygame.draw.rect(self.screen,(255,255,255),self.start_button_shadow)
                    pygame.draw.rect(self.screen,(100,0,100),self.start_button)
                    self.text_play=self.my_font.render("Ready?", False, (255, 255, 255))
                    self.text_play=pygame.transform.scale(self.text_play,(300,150))
                    self.screen.blit(self.text_play,(600,490))

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONUP:
                        self.mouse_pos=pygame.mouse.get_pos()
                        if pygame.rect.Rect.collidepoint(self.start_button,self.mouse_pos):
                            pygame.mixer_music.stop()
                            self.tittle=False
                
                pygame.display.flip() 
                pygame.display.update()
                self.clock.tick(60)     
            #end of tittle
            
            while self.retry:

                if self.retry_music_flag:

                    pygame.mixer_music.stop()
                    pygame.mixer_music.load("data/retry_music.mp3")
                    pygame.mixer.music.play(-1)
                    self.retry_music_flag=False

                self.screen.fill((0,0,0))
                self.screen.blit(self.retry_screen,(0,0)) 

                self.player_pos=[700,600]
                self.player_movement=[0,0,0,0]

                self.screen.blit(self.text_retry_shadow,(455,155))
                self.screen.blit(self.text_retry,(450,150))

                pygame.draw.rect(self.screen,(0,0,255),self.retry_button)

                self.mouse_pos=pygame.mouse.get_pos()
                if pygame.rect.Rect.collidepoint(self.retry_button,self.mouse_pos):
                    pygame.draw.rect(self.screen,(255,0,255),self.retry_button)

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONUP:
                        self.mouse_pos=pygame.mouse.get_pos()
                        if pygame.rect.Rect.collidepoint(self.retry_button,self.mouse_pos):
                            pygame.mixer_music.stop()

                            self.retry=False

                            self.retry_music_flag=True

                            self.player_pos=[700,600]
                            self.player_movement=[0,0,0,0]

                            self.collision_up=pygame.rect.Rect(0,0,1500,1)
                            self.collision_down=pygame.rect.Rect(0,700,1500,1)
                            self.collision_left=pygame.rect.Rect(0,0,1,700)
                            self.collision_right=pygame.rect.Rect(1450,0,1,700)

                            self.retry_button=pygame.rect.Rect(600,500,300,150)

                            self.tittle=False

                            self.clicked=False

                            self.boss_music_flag=True

                            self.entrance=True

                            self.entrance_sounds=True

                            self.across_flyby=True

                            self.fs=0

                            self.upwards_flyby=False

                            self.get_into_pos=True

                            self.intro_thunder_sound_flag=True

                            self.hp=200000

                            self.roar_flag=True

                            self.idle_flag=True

                            self.attack_chose=False

                            self.into_thunder_flag=True

                            self.init_thunder=False

                            self.into_side_flag=True

                            self.into_circle_flag=True

                            self.col_left=pygame.rect.Rect(0,0,0,0)
                            self.col_right=pygame.rect.Rect(0,0,0,0)
                            self.col_mid=pygame.rect.Rect(0,0,0,0)

                            self.up_c=pygame.rect.Rect(0,0,0,0)

                            self.side_left_c=pygame.rect.Rect(0,0,0,0)
                            self.side_right_c=pygame.rect.Rect(0,0,0,0)

                            self.light_left_c=pygame.rect.Rect(0,0,0,0)
                            self.light_right_c=pygame.rect.Rect(0,0,0,0)

                            self.circle_c=pygame.rect.Rect(0,0,0,0)

                            self.up_c1=pygame.rect.Rect(0,0,0,0)
                            self.up_c2=pygame.rect.Rect(0,0,0,0)
                            self.up_c3=pygame.rect.Rect(0,0,0,0)
                            
                            self.t1=pygame.rect.Rect(0,0,0,0)
                            self.t2=pygame.rect.Rect(0,0,0,0)
                            self.t3=pygame.rect.Rect(0,0,0,0)

                self.screen.blit(self.text_retry_button,(600,490))

                pygame.display.flip() 
                pygame.display.update()
                self.clock.tick(60)
            #end of retry
            
            while self.entrance:

                if self.entrance_sounds:
                    pygame.mixer.Sound.play(whoosh_sound)
                    pygame.mixer_music.load("data/boss_entrance.mp3")
                    pygame.mixer_music.play()
                    self.entrance_sounds=False

                while self.across_flyby:

                    self.screen.fill((0,0,0))
                    self.screen.blit(self.bg,(0,0))
                
                    self.player_pos=[700,600]
                    self.player_movement=[0,0,0,0]

                    self.screen.blit(self.player,self.player_pos)

                    self.screen.blit(self.boss_part_left,(-800+self.fs,-100))
                    self.screen.blit(self.boss_part_right,(2000-self.fs,100))
                    self.fs+=50
                    if self.fs>=2500:
                        self.across_flyby=False
                        self.upwards_flyby=True
                        self.entrance_sounds=True
                    

                
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    pygame.display.update()
                    self.clock.tick(60)


                if self.entrance_sounds:
                    pygame.mixer.Sound.play(whoosh_sound)
                    self.entrance_sounds=False

                self.fs=0
                while self.upwards_flyby:

                    self.screen.fill((0,0,0))
                    self.screen.blit(self.bg,(0,0))
                
                    self.player_pos=[700,600]
                    self.player_movement=[0,0,0,0]

                    self.screen.blit(self.player,self.player_pos)

                    self.screen.blit(self.boss_part_left,(-500+self.fs,650-self.fs))
                    self.screen.blit(self.boss_part_right,(1500-self.fs,650-self.fs))
                    self.fs+=50
                    if self.fs>=1000:
                        self.upwards_flyby=False
                        self.entrance_sounds=False
                        self.get_ip=True

                
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    pygame.display.update()
                    self.clock.tick(60)
                
                self.fs=0
                while self.get_into_pos:
                    if self.intro_thunder_sound_flag:
                        self.side_lightning=pygame.transform.scale(self.side_lightning,(600,100))
                        pygame.mixer.Sound.play(intro_thunder)
                        self.intro_thunder_sound_flag=False

                    self.screen.fill((0,0,0))
                    self.screen.blit(self.bg,(0,0)) 

                    self.player_pos=[700,600]
                    self.player_movement=[0,0,0,0]

                    self.screen.blit(self.boss_part_left,(200,-600+self.fs))
                    self.screen.blit(self.boss_part_right,(700,-600+self.fs))
                    self.screen.blit(self.boss_part_mid,(450,-700+self.fs))

                    if self.fs==300:
                        self.screen.blit(self.side_lightning,(200,-600+self.fs+250))
                    if self.fs==400:
                        self.screen.blit(self.side_lightning,(700,-600+self.fs+250))
                    if self.fs==450:
                        self.screen.blit(self.side_lightning,(450,-700+self.fs+250))

                    self.screen.blit(self.player,self.player_pos)

                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    pygame.display.update()
                    self.clock.tick(60)
                        
                    if self.fs>=500:
                        self.get_into_pos=False
                        self.roar=True

                    self.fs+=1

                self.fs=0
                while self.roar:
                    
                    if self.roar_flag:
                        pygame.mixer.Sound.play(boss_roar)
                        self.roar_flag=False

                    self.screen.fill((0,0,0))
                    self.shake=random.randint(0,10)
                    self.screen.blit(self.bg,(self.shake,self.shake)) 

                    self.player_pos=[700,600]
                    self.player_movement=[0,0,0,0]

                    self.screen.blit(self.boss_part_left,(200,-100))
                    self.screen.blit(self.boss_part_right,(700,-100))
                    self.screen.blit(self.boss_part_mid,(450,-200))

                    self.screen.blit(self.roar_lines,(0,0))
                    
                    if self.fs==400:
                        pygame.mixer.Sound.stop(boss_roar)
                        self.roar=False
                        self.entrance=False
                        self.in_idle=True
                        self.idle_in=False
                        self.idle_an=True

                    self.screen.blit(self.player,self.player_pos)

                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    self.fs+=2
                    pygame.display.update()
                    self.clock.tick(60)

                self.screen.fill((0,0,0))
                self.screen.blit(self.bg,(0,0)) 

                self.player_pos=[700,600]
                self.player_movement=[0,0,0,0]

                self.screen.blit(self.player,self.player_pos)

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
                self.clock.tick(60)
            #end of entrance

            if self.hp<=0:
                self.victory=True

            if self.boss_music_flag:

                pygame.mixer_music.load("data/boss_music.mp3")
                pygame.mixer_music.set_volume(0.5)
                pygame.mixer_music.play(-1)
                self.boss_music_flag=False

            self.screen.fill((0,0,0))
            self.screen.blit(self.bg,(0,0))

            self.screen.blit(self.player,self.player_pos)
            self.collision_player=pygame.rect.Rect(self.player_pos[0],self.player_pos[1],70,70)

            if self.in_idle:
                self.in_idle,self.choise_flag=self.idle()                

            if self.attack_chose:
                if self.choise_flag:
                    self.choise=random.randint(1,3)
                    self.into_thunder_flag=True
                    self.choise_flag=False
                

                if self.choise==1:
                    self.curent_attack="thunder"
                    self.choise_flag,self.col_left,self.col_right,self.col_mid=self.thunder_attack()

                if self.choise==2:
                    self.curent_attack="side"
                    self.choise_flag,self.light_left_c,self.light_right_c=self.side_attack()

                if self.choise==3:
                    self.curent_attack="circle"
                    self.choise_flag,self.up_c1,self.up_c2,self.up_c3=self.circle_attack()

            if pygame.rect.Rect.colliderect(self.collision_player,self.collision_up):
                self.player_movement[0]=0

            if pygame.rect.Rect.colliderect(self.collision_player,self.collision_down):
                self.player_movement[1]=0
            
            if pygame.rect.Rect.colliderect(self.collision_player,self.collision_left):
                self.player_movement[2]=0

            if pygame.rect.Rect.colliderect(self.collision_player,self.collision_right):
                self.player_movement[3]=0


            if pygame.rect.Rect.colliderect(self.collision_player,self.t1):
                self.retry=True
            
            if pygame.rect.Rect.colliderect(self.collision_player,self.t2):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.t3):
                self.retry=True       

            if pygame.rect.Rect.colliderect(self.collision_player,self.light_left_c):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.light_right_c):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.up_c1):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.up_c2):
                self.retry=True

            if pygame.rect.Rect.colliderect(self.collision_player,self.up_c3):
                self.retry=True

            self.player_pos[0]+=self.player_movement[2]
            self.player_pos[0]+=self.player_movement[3]
            self.player_pos[1]+=self.player_movement[0]
            self.player_pos[1]+=self.player_movement[1]

            self.mouse_pos=pygame.mouse.get_pos()
            self.mouse_x=pygame.mouse.get_pos()[0]
            self.mouse_y=pygame.mouse.get_pos()[1]

            if self.clicked:
                self.mouse_y-=50
                self.mouse_x-=50
                pygame.mixer.Sound.play(laser_sound)
                self.dx=self.mouse_x-self.player_pos[0]
                self.dy=self.mouse_y-self.player_pos[1]
                self.rads=math.atan2(-self.dy,self.dx)
                self.rads%=2*math.pi
                self.degs=math.degrees(self.rads)

                self.of=pygame.math.Vector2(800,0)
                self.rot_laser,self.rect=self.rotate(self.laser,-self.degs,self.player_pos,self.of)
                self.screen.blit(self.rot_laser,(self.rect[0]+50,self.rect[1]+50))
            
                self.screen.blit(self.ball,(self.player_pos[0]-25,self.player_pos[1]-25))

                self.col_l_x=self.player_pos[0]
                self.col_l_y=self.player_pos[1]
                for i in range(100):
                    
                    self.col_rot_laser=pygame.rect.Rect(self.col_l_x,self.col_l_y,100,100)

                    if self.mouse_x>self.player_pos[0]:
                        self.nx=1
                    else:
                        self.nx=-1

                    if self.mouse_y>self.player_pos[1]:
                        self.ny=1
                    else:
                        self.ny=-1
                    self.col_l_x+=(self.nx*self.rect[2])/20
                    self.col_l_y+=(self.ny*self.rect[3])/20

                    if pygame.Rect.colliderect(self.col_rot_laser,self.col_left):
                        self.hp-=1
                    if pygame.Rect.colliderect(self.col_rot_laser,self.col_right):
                        self.hp-=1
                    if pygame.Rect.colliderect(self.col_rot_laser,self.col_mid):
                        self.hp-=1
                    if pygame.Rect.colliderect(self.col_rot_laser,self.side_right_c):
                        self.hp-=1
                    if pygame.Rect.colliderect(self.col_rot_laser,self.side_left_c):
                        self.hp-=1
                    if pygame.Rect.colliderect(self.col_rot_laser,self.up_c):
                        self.hp-=1

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type==pygame.KEYDOWN:
                    if self.clicked:
                        self.f=7
                    else:
                        self.f=10

                    if event.key==pygame.K_w:
                        self.player_movement[0]-=self.f
                    if event.key==pygame.K_s:
                        self.player_movement[1]+=self.f
                    if event.key==pygame.K_a:
                        self.player_movement[2]-=self.f
                    if event.key==pygame.K_d:
                        self.player_movement[3]+=self.f

                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_w:
                        self.player_movement[0]=0
                    if event.key==pygame.K_s:
                        self.player_movement[1]=0
                    if event.key==pygame.K_a:
                        self.player_movement[2]=0
                    if event.key==pygame.K_d:
                        self.player_movement[3]=0

                if event.type==pygame.MOUSEBUTTONDOWN:
                    self.clicked=True
                
                if event.type==pygame.MOUSEBUTTONUP:
                    self.clicked=False

            pygame.display.update()
            self.clock.tick(60)
                                            
Game().run()
