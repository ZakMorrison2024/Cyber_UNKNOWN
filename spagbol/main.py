import pygame
import os
import random
import math
import asyncio
import sys

# TO DO:
# Add sounds/music
# Small pathfinding for neemies
# display at end
# collision for player



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLUE = (0,0,255)


#------------------------------------------------------------------------------------------------------#
#Globals

splashscr = True
Menu = False     
Cutscene = False
i = 50
j = 0
SCORE = 0
GAMETIMER = 300
GUN = 0
guntimer = 0
KILL = 0
delay = 0
trigger = False
TIME = 0
k = 0
killtime = 0
LIFE = 100
dmgtime = 0
lifetrig = False
GAMEOVER = False
Cutscene2 = False
trig = False
endtime = 0
dt  = 0



#--------------------------------------------------------------------------------------------------------#
# MENU CLASSES
# Draw Front
class Front(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Cyber_Face.png")))
      self.img_org = pygame.transform.scale(self.img_org, (320, 240))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y

   def update(self):
       global Menu, splashscr
       if Menu == False and splashscr == False:
           self.kill()

# Draw Title
class Title(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Title.png")))
      self.img_org = pygame.transform.scale(self.img_org, (640, 100))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y

   def update(self):
       global Menu, splashscr
       if Menu == False and splashscr == False:
           self.kill()

# Play Button
class P_button(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Button_P.png"))) # Image orginal
      self.img_alt = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Button_P_2.png")))  # Image Alternative
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
      self.click = False # Click Variable
      
   def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()): # Check collision with mouse
          self.image = self.img_alt # Alt image
        else : 
          self.image = self.img_org # Orginal image
        
        if self.click == True: # Test if clicked
           if self.rect.collidepoint(pygame.mouse.get_pos()): # If collision
             global Menu, Cutscene, splashscr # Globals
             Menu = False # Menu False
             Cutscene = True
            

        if Menu == False and splashscr == False: # If Menu False
                self.kill() # Kill self


# Play Button
class C_button(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Button_P.png"))) # Image orginal
      self.img_alt = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Button_P_2.png")))  # Image Alternative
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
      self.click = False # Click Variable
      
   def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()): # Check collision with mouse
          self.image = self.img_alt # Alt image
        else : 
          self.image = self.img_org # Orginal image
      
        if self.click == True: # Test if clicked
           if self.rect.collidepoint(pygame.mouse.get_pos()): # If collision
             global Cutscene # Globals
             Cutscene = False
            

        if Cutscene == False: # If Menu False
                self.kill() # Kill self

class cutscenestart(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = [pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Eye_1.png"))),
      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Eye_2.png"))),
      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Eye_3.png"))),
      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Eye_4.png")))]
      self.image = self.img_org[0] # Set Default image
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y
      self.index = 0

      self.animation_time = 0.1
      self.current_time = 0

      self.animation_frames = 4
      self.current_frame = 1

   def update(self,dt):

      if self.index > self.animation_frames:
       self.index = 0

      self.current_time += dt
      if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.img_org)
            self.image = self.img_org[self.index]

      if self.index == 3:
            nexxt = cutscenefinish(0,0,cutscenes)
            self.kill()


class cutscenefinish(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_WIN.png")))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y


class death(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Death.png")))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y

class splash(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_SplashScreen.png")))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect y

   def update(self):
        global TIME, endtime, splashscr

        if TIME > endtime:
             global Menu
             self.kill()
             Menu = True
             splashscr = False
#--------------------------------------------------------------------------------------------------------#
# PLAYER CLASS

class Player(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 

      self.img_org = [pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_1.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_2.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_3.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_2.png")))]# Image orginal
      
      self.img_punch = [pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_Punch_1.png"))),
                        pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_Punch_2.png"))),
                        pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_Punch_3.png"))),
                        pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_Punch_4.png"))),]
      
      self.img_shooting = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_Fire.png")))

      self.image = self.img_org[0]
      self.image_clean = self.image.copy()
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
      self.index = 0
      self.index_punch = 0
      self.punching = False
      self.shooting = False

      self.animation_time = 0.3
      self.current_time = 0

      self.animation_frames = 3
      self.animation_punch_frames = 3
      self.current_frame = 1

      self.moving = False

      self.barrel_x = self.rect.x + self.rect.width/2
      self.barrel_y = self.rect.y + self.rect.height
      self.barrel_xF, self.barrel_yF = 0, 0
 
   def update(self,dt):

      if GUN == 0:
            
            self.img_org = [pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_1.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_2.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_3.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_2.png")))]# Image orginal
            
            if self.shooting == True and delay == False:
               self.img_shooting = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_Fire.png")))
               self.image = self.img_shooting
               self.image_clean = self.image.copy()
            else:
               self.image = self.img_org
               self.image_clean = self.image.copy()

      if GUN == 1:
            self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_SG.png")))
            if self.shooting == True and delay == False:
               self.img_shooting = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_SG_Fire.png")))
               self.image = self.img_shooting
               self.image_clean = self.image.copy()
            else:
               self.image = self.img_org
               self.image_clean = self.image.copy()
      if GUN == 2:
            self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_MG.png")))
            if self.shooting == True:
               self.img_shooting = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Punk_MG_Fire.png")))
               self.image = self.img_shooting
               self.image_clean = self.image.copy()
            else:
               self.image = self.img_org
               self.image_clean = self.image.copy()

      if GUN == 0:
       if self.index > self.animation_frames:
         self.index = 0

      if self.index_punch > self.animation_punch_frames:
       self.index_punch = 0

      if GUN == 0:
       self.current_time += dt
       if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.img_org)

      if GUN == 0 :
       if self.moving == True:
         self.image = self.img_org[self.index]
         self.image_clean = self.image.copy()
       elif self.moving == False:
         self.image = self.img_org[1]
         self.image_clean = self.image.copy()

      self.current_time += dt
      if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index_punch = (self.index_punch + 1) % len(self.img_punch)

      if self.punching == True:
         self.image = self.img_punch[self.index_punch]
         self.image_clean = self.image.copy()
     # elif self.punching == False:
       #  self.image = self.img_org[1]
        # self.image_clean = self.image.copy()

 
      #elif self.punching == False:
       #  self.image = self.img_org[1]
       #  self.image_clean = self.image.copy()


      mx,my = pygame.mouse.get_pos()
      rel_x, rel_y = round(mx - self.rect.x), round(my - self.rect.y)
      angle = round((180 / math.pi) * +math.atan2(rel_x, rel_y) )
      self.image = pygame.transform.rotate(self.image_clean,angle)
      
      self.rect = self.image.get_rect(center=self.rect.center)
     


      b_angle = math.atan2(mx- self.barrel_x, my - self.barrel_y) 
      self.barrel_xF, self.barrel_yF = (self.rect.centerx + 
                                        (((self.rect.width)/2)*math.sin(b_angle)), 
                                        self.rect.centery + 
                                        (((self.rect.height)/2)*math.cos(b_angle)))
     

class Machinegun(pygame.sprite.Sprite): 
        def __init__(self,x,y,*groups): # Intialisation
            super().__init__(*groups) 
            self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Machine_Gun.png"))) # Image orginal
            self.image = self.img_org # Set Default image
            self.rect = self.image.get_rect() # Set Colision Rectangle
            self.rect.x = x # Rect X
            self.rect.y = y # Rect Y

        def update(self):
             if self.rect.collidepoint(player.rect.centerx,player.rect.centery):
                  global GUN, guntimer, k
                  guntimer = 50
                  GUN = 2
                  k -= 1
                  self.kill()

             keys = pygame.key.get_pressed()
             if keys [pygame.K_w] or keys[pygame.K_UP]:
                  if backg.rect.y + player.rect.y >= - 540 and backg.rect.y + player.rect.y <= 290:
                           self.rect.y += 2
             elif keys [pygame.K_d] or keys [pygame.K_RIGHT]:
                  if backg.rect.x + player.rect.x <= 520 and backg.rect.x + player.rect.x >= - 340:
                         self.rect.x -= 2
             elif keys [pygame.K_a] or keys[pygame.K_LEFT]:
                   if backg.rect.x + player.rect.x <= 520 and backg.rect.x + player.rect.x >= - 340:
                         self.rect.x += 2
             elif keys  [pygame.K_s] or keys[ pygame.K_DOWN]:
                   if backg.rect.y + player.rect.y >= - 540 and backg.rect.y + player.rect.y <= 290:
                         self.rect.y -= 2



class Shotgun(pygame.sprite.Sprite): 
        def __init__(self,x,y,*groups): # Intialisation
            super().__init__(*groups) 
            self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Shot_Gun.png"))) # Image orginal
            self.image = self.img_org # Set Default image
            self.rect = self.image.get_rect() # Set Colision Rectangle
            self.rect.x = x # Rect X
            self.rect.y = y # Rect Y

        def update(self):
             if self.rect.collidepoint(player.rect.centerx,player.rect.centery):
                  global GUN, guntimer, k
                  guntimer = 50
                  GUN = 1
                  k -= 1
                  self.kill()
                  
             keys = pygame.key.get_pressed()
             if keys [pygame.K_w] or keys[pygame.K_UP]:
                  if backg.rect.y + player.rect.y >= - 540 and backg.rect.y + player.rect.y <= 290:
                           self.rect.y += 2
             elif keys [pygame.K_d] or keys [pygame.K_RIGHT]:
                  if backg.rect.x + player.rect.x <= 520 and backg.rect.x + player.rect.x >= - 340:
                         self.rect.x -= 2
             elif keys [pygame.K_a] or keys[pygame.K_LEFT]:
                   if backg.rect.x + player.rect.x <= 520 and backg.rect.x + player.rect.x >= - 340:
                         self.rect.x += 2
             elif keys  [pygame.K_s] or keys[ pygame.K_DOWN]:
                   if backg.rect.y + player.rect.y >= - 540 and backg.rect.y + player.rect.y <= 290:
                         self.rect.y -= 2



class health(pygame.sprite.Sprite): 
        def __init__(self,x,y,*groups): # Intialisation
            super().__init__(*groups) 
            self.img_org = [pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Health_1.png"))),
                            pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Health_2.png"))),
                            pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Health_3.png"))),
                            pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Health_4.png"))),
                            pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Health_5.png"))),
                            pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Health_6.png"))),
                            pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Health_7.png")))] # Image orginal
            self.image = self.img_org[0] # Set Default image
            self.rect = self.image.get_rect() # Set Colision Rectangle
            self.rect.x = x # Rect X
            self.rect.y = y # Rect Y
            self.index = 0/7
            self.current_frame = 0

        def update(self):

             if LIFE == 100:
               self.index = 0

             if LIFE < 100:
                 if LIFE < 86:
                  self.index = 1
                  self.image = self.img_org[self.index]
                 if LIFE < 72:
                  self.index = 2
                  self.image = self.img_org[self.index]
                 if LIFE < 58:
                  self.index = 3
                  self.image = self.img_org[self.index]
                 if LIFE < 44:
                  self.index = 4
                  self.image = self.img_org[self.index]
                 if LIFE < 30:
                  self.index = 5
                  self.image = self.img_org[self.index]
                 if LIFE < 16:
                  self.index = 6
                  self.image = self.img_org[self.index]
                 if LIFE < 0:
                      global GAMEOVER
                      GAMEOVER = True   
                  
         
#--------------------------------------------------------------------------------------------------------#
# RADAR CLASS 

class radar_base(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar.png")))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y



class radar_search(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) # rotate img 5
      pic = 2
      if pic < 18:
         pic +=1 

     
      self.img_org = [pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_0.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_1.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_2.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_3.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_4.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_5.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_6.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_7.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_8.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_9.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_10.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_11.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_12.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_13.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_14.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Detec_15.png")))]
      
      self.image = self.img_org[0] # Set Default image
      self.rect = self.image.get_rect()# Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
      self.index = 0

      self.animation_time = 0.1
      self.current_time = 0

      self.animation_frames = 15
      self.current_frame = 1

   def update(self,dt):

      if self.index > self.animation_frames:
       self.index = 0

      self.current_time += dt
      if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.img_org)
            self.image = self.img_org[self.index]

#--------------------------------------------------------------------------------------------------------#
# SPECTRE CLASS

class Spectre(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Radar_Signal.png"))) # Image orginal
      self.image = self.img_org # Set Default image
      self.image_clean = self.image.copy()
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
      self.target = 280,170
 
   def update(self):

      rel_x, rel_y = self.target[0] - self.rect.x, self.target[1]- self.rect.y
      angle = (180 / math.pi) * +math.atan2(rel_x, rel_y) 
      self.image = pygame.transform.rotate(self.image_clean,angle)
      self.rect = self.image.get_rect(center=self.rect.center)
   


      if self.rect.x != self.target[0]:
         if self.rect.x > self.target[0]:
            self.rect.x -= 1
         elif self.rect.x < self.target[0]:
           self.rect.x += 1

      if self.rect.y != self.target[1]:
         if self.rect.y > self.target[1]:
            self.rect.y -= 1
         elif self.rect.y < self.target[1]:
            self.rect.y += 1      

      keys = pygame.key.get_pressed()
      if keys [pygame.K_w] or keys[pygame.K_UP]:
                  if backg.rect.y + player.rect.y >= - 540 and backg.rect.y + player.rect.y <= 290:
                         self.rect.y += 1.5
      elif keys [pygame.K_d] or keys [pygame.K_RIGHT]:
                  if backg.rect.x + player.rect.x <= 520 and backg.rect.x + player.rect.x >= - 340:
                         self.rect.x -= 1.5
      elif keys [pygame.K_a] or keys[pygame.K_LEFT]:
                   if backg.rect.x + player.rect.x <= 520 and backg.rect.x + player.rect.x >= - 340:
                         self.rect.x += 1.5
      elif keys  [pygame.K_s] or keys[ pygame.K_DOWN]:
                   if backg.rect.y + player.rect.y >= - 540 and backg.rect.y + player.rect.y <= 290:
                         self.rect.y -= 1.5


     
      if self.rect.x + backg.rect.x <= -350:
            self.rect.x += 5
      if self.rect.x + backg.rect.x >= 650:
            self.rect.x -= 5
      if self.rect.y + backg.rect.y <= - 550:
            self.rect.y += 5
      if self.rect.y + backg.rect.y >= 300 :
            self.rect.y -= 5
#--------------------------------------------------------------------------------------------------------#
# PROJECTILE CLASSES

class PlayerProjectile(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Bullet.png"))) # Image orginal
      self.image = self.img_org # Set Default image
      self.image_clean = self.image.copy()
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
      self.pos = pygame.mouse.get_pos()
      self.dir = self.pos[0] - self.rect.x, self.pos[1]- self.rect.y

      length = math.hypot(*self.dir)
      if length == 0.0:
             self.dir = (0, -1)
      else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)

   def update(self):

      angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
      self.image = pygame.transform.rotate(self.image_clean,angle)
      self.rect = self.image.get_rect(center=self.rect.center)

      self.rect.x, self.rect.y =  self.rect.x+self.dir[0]*15, self.rect.y+self.dir[1]*15

      keys = pygame.key.get_pressed()
      if keys [pygame.K_w] or keys[pygame.K_UP]:
                         if self.rect.y > 0 + backg.rect.y and self.rect.y < 1000 +  backg.rect.y:
                               self.rect.y += 3
      elif keys [pygame.K_d] or keys [pygame.K_RIGHT]:
                        if self.rect.x > 0 + backg.rect.x and self.rect.x < 1000 +  backg.rect.x:
                         self.rect.x -= 3
      elif keys [pygame.K_a] or keys[pygame.K_LEFT]:
                         if self.rect.x > 0 + backg.rect.x and self.rect.x < 1000 +  backg.rect.x:
                           self.rect.x += 3
      elif keys  [pygame.K_s] or keys[ pygame.K_DOWN]:
                         if self.rect.y > 0 + backg.rect.y and self.rect.y < 1000 +  backg.rect.y:
                              self.rect.y -= 3

      

#--------------------------------------------------------------------------------------------------------#
# FURNI CLASS

class Furni(pygame.sprite.Sprite): 
   def __init__(self,x,y,*groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_Furni.png"))) # Image orginal
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
 
   def update(self):
      keys = pygame.key.get_pressed()
      if keys [pygame.K_w] or keys[pygame.K_UP]:
                         if self.rect.y > 0 + backg.rect.y and self.rect.y < 1000 +  backg.rect.y:
                                if backg.rect.y + player.rect.y <= 290 and backg.rect.y + player.rect.y >= -540:
                                     self.rect.y += 2
      elif keys [pygame.K_d] or keys [pygame.K_RIGHT]:
                        if self.rect.x > 0 + backg.rect.x and self.rect.x < 1000 +  backg.rect.x:
                          if backg.rect.x + player.rect.x <= 520 and backg.rect.x + player.rect.x >= - 340:
                              self.rect.x -= 2
      elif keys [pygame.K_a] or keys[pygame.K_LEFT]:
                         if self.rect.x > 0 + backg.rect.x and self.rect.x < 1000 +  backg.rect.x:
                           if backg.rect.x + player.rect.x >= -340 and backg.rect.x + player.rect.x <= 520:
                                self.rect.x += 2
      elif keys  [pygame.K_s] or keys[ pygame.K_DOWN]:
                         if self.rect.y > 0 + backg.rect.y and self.rect.y < 1000 +  backg.rect.y:
                               if backg.rect.y + player.rect.y >= - 540 and backg.rect.y + player.rect.y <= 290:
                                   self.rect.y -= 2

#--------------------------------------------------------------------------------------------------------#
#Background

class background(pygame.sprite.Sprite): 
   def __init__(self,x,y,*groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","Spr_BG.png"))) # Image orginal
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y


   def update(self):
      keys = pygame.key.get_pressed()
      if keys [pygame.K_w] or keys[pygame.K_UP]:
                        if self.rect.y + player.rect.y > - 550 and self.rect.y + player.rect.y < 300 :
                               self.rect.y += 2
      elif keys [pygame.K_d] or keys [pygame.K_RIGHT]:
                         if self.rect.x + player.rect.x >  - 350 and self.rect.x + player.rect.x < 530:
                            self.rect.x -= 2
      elif keys [pygame.K_a] or keys[pygame.K_LEFT]:
                         if self.rect.x + player.rect.x >  - 350 and self.rect.x + player.rect.x < 530:
                           self.rect.x += 2
      elif keys [pygame.K_s] or keys[ pygame.K_DOWN]:
                         if self.rect.y + player.rect.y > - 550 and self.rect.y + player.rect.y < 300 :
                              self.rect.y -= 2

      if self.rect.x + player.rect.x <= -350:
            self.rect.x += 5
      if self.rect.x + player.rect.x >= 530:
            self.rect.x -= 5
      if self.rect.y + player.rect.y <= - 550:
            self.rect.y += 5
      if self.rect.y + player.rect.y >= 300 :
            self.rect.y -= 5

#--------------------------------------------------------------------------------------------------------#
#init
#--------------------------------------------------------------------------------------------------------#
pygame.init()
#pygame.mixer.init()

#ouch = pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Player_Hurt.mp3")))
#bang = pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Pistol.mp3")))                                        
#shotgun =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Shotgun.mp3")))    
#overkill =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Overkill.mp3")))    
#rampage =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Rampage.mp3")))    
#melee =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Melee_Grunt.mp3")))    
#death_enemy =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_Death_Entities.mp3")))    
#dkill =  pygame.mixer.Sound(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/SFX_DoubleKill.mp3")))    

#pygame.mixer.music.load(os.path.abspath(os.getcwd()+os.path.join("/SFX"+"/MSC_Infraction_AI.mp3")))
#pygame.mixer.music.play()               

# Set the width and height of the screen [width, height]
size = (640, 480)
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

pygame.display.set_caption("Cyber_Unknown")

# Loop until the user clicks the close button.
running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#----------------------------------------------------------------------------------------------------------------#
#Objects
#------------------------------------------------------------------------------------------------------------------#
#Menu sprites/objects
menu_sprites = pygame.sprite.Group()
cut_S = pygame.sprite.Group()
bground = pygame.sprite.Group()

menufront = Front(175,120,menu_sprites)
menubutton_P = P_button(230,370,menu_sprites)
titlelogo = Title(0,0,menu_sprites)

cut_SB = C_button(230,400,cut_S)

backg = background(-350,-260,bground) 



enemy = pygame.sprite.Group()
playing_entities = pygame.sprite.Group()
players = pygame.sprite.Group()
radar = pygame.sprite.Group()
cutscenes = pygame.sprite.Group()
gameover = pygame.sprite.Group()
bar = pygame.sprite.Group()

player = Player(280,170,players)
life = health(270,140,bar)
radar_bases = radar_base(0,0,playing_entities)
radar_scope = radar_search(0,0,radar)
ssplash = pygame.sprite.Group()

furniture = [Furni(-200, -100,playing_entities),
Furni(-200, 500,playing_entities),
 Furni( 200, -100,playing_entities),
 Furni( 300, 350,playing_entities),
 Furni( 140, -500,playing_entities)]

ending = cutscenestart(0,0,cutscenes)
dieded = death(0,0,gameover)
SS = splash(0,0,ssplash)

spectre = []
bullets = [] 



# Goes inside the while loop

async def main():
    global i, SCORE, GAMETIMER, GUN, guntimer, KILL, delay, trigger, j, TIME, k, killtime, LIFE, dmgtime, lifetrig, GAMEOVER, Cutscene2, trig, endtime, dt, splashscr
    # avoid this kind declaration, prefer the way above
    while True:

        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop
        # could be less on some mobile devices
           m_pos = pygame.mouse.get_pos()
           
           if trig == False:
                 endtime = TIME + 3
                 trig = True
# -------- Main Program Loop -----------
    # --- Main event loop
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      pygame.quit()
                      sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and Menu == True:
                      menubutton_P.click = True
                elif event.type == pygame.MOUSEBUTTONUP and Menu == True:
                      menubutton_P.click = False
                elif event.type == pygame.MOUSEBUTTONDOWN and Cutscene == True:
                      cut_SB.click = True
                elif event.type == pygame.MOUSEBUTTONDOWN and Cutscene2 == False:
                      
                      if m_pos[0] > player.rect.x - 50 and m_pos[0] < player.rect.x + 100 and m_pos[1] > player.rect.y - 50 and m_pos[1] < player.rect.y + 100:
                            player.punching = True
                           # pygame.mixer.Sound.play(melee)
                      else:
                           player.shooting = True
                           if GUN == 2:
                                 # pygame.mixer.Sound.play(bang)
                                  bullets.append(PlayerProjectile(player.barrel_xF, player.barrel_yF,playing_entities))
                           if GUN == 0 and delay != True:
                                # pygame.mixer.Sound.play(bang)
                                 bullets.append(PlayerProjectile(player.barrel_xF, player.barrel_yF,playing_entities))
                                 delay = True
                           if GUN == 1 and delay != True:
                              #   pygame.mixer.Sound.play(shotgun)
                                 bullets.append(PlayerProjectile(player.barrel_xF-5, player.barrel_yF-5,playing_entities))
                                 bullets.append(PlayerProjectile(player.barrel_xF-3, player.barrel_yF-3,playing_entities))
                                 bullets.append(PlayerProjectile(player.barrel_xF, player.barrel_yF,playing_entities))
                                 bullets.append(PlayerProjectile(player.barrel_xF+3, player.barrel_yF+3,playing_entities))
                                 bullets.append(PlayerProjectile(player.barrel_xF+5, player.barrel_yF+5,playing_entities))
                                 delay = True
                                 


   
                elif event.type == pygame.MOUSEBUTTONUP :
                    player.shooting = False
             

                elif event.type == pygame.KEYUP:
                           player.moving =  False
                

           if m_pos[0] < player.rect.x - 50 or m_pos[0] > player.rect.x + 100 and m_pos[1] < player.rect.y - 50 or m_pos[1] > player.rect.y + 100:
               player.punching = False
           if m_pos[0] == player.rect.x and m_pos[1] < player.rect.y - 50 or m_pos[1] > player.rect.y + 100:
               player.punching = False
           if m_pos[1] == player.rect.y and m_pos[0] < player.rect.x - 50 or m_pos[0] > player.rect.x + 100:
               player.punching = False

           keys = pygame.key.get_pressed()
           if keys [pygame.K_w] or keys[pygame.K_UP] or keys [pygame.K_d] or keys [pygame.K_RIGHT] or keys [pygame.K_a] or keys[pygame.K_LEFT] or keys  [pygame.K_s] or keys[ pygame.K_DOWN]:
                         player.moving = True
           if keys [pygame.K_p]:
                GAMETIMER = 10



    # --- Game logic should go here    
           if Menu == False and Cutscene == False and Cutscene2 == False and GAMEOVER == False and splashscr == False: #and Gameover == False:
             for bullet in bullets[:]:
                if not screen.get_rect().collidepoint(bullet.rect.x,bullet.rect.y) :
                     if bullet in bullets: 
                           bullet.kill(), bullets.remove(bullet)
                if not backg.rect.collidepoint(bullet.rect.x,bullet.rect.y): 
                     if bullet in bullets: 
                          bullet.kill(), bullets.remove(bullet)


             if len(spectre) <= 5:
              if i <= 0 :
            
               set_spawn_x = [backg.rect.x + 700, backg.rect.x + 300]
               spawn_x = set_spawn_x[random.randint(0,1)]
              
               set_spawn_y = [backg.rect.y + 100,  backg.rect.y + 900]
               spawn_y  = set_spawn_y[random.randint(0,1)]
               spectre.append(Spectre(spawn_x,spawn_y,enemy))
               i = 50

             for sprite in spectre[:]:
               for bullet in bullets[:]:
                    if sprite.rect.collidepoint(bullet.rect.x,bullet.rect.y):
                       if bullet in bullets[:]:
                        bullets.remove(bullet), bullet.kill()
                       if TIME < killtime:
                       #   pygame.mixer.Sound.play(dkill)
                         print("audio")
                       killtime = TIME+0.01
                       SCORE += 10
                       KILL += 1
                      # pygame.mixer.Sound.play(death_enemy)
                       
                       if sprite in spectre[:]:
                        spectre.remove(sprite), sprite.kill()
                       roll = random.randint(0,9)
                       
                       if roll > 8:
                         if k < 3:
                           gun = Machinegun(sprite.rect.x,sprite.rect.y,playing_entities)
                           k += 1
                       
                       if roll > 4 and roll < 8:
                           if k < 3:
                                gun = Shotgun(sprite.rect.x,sprite.rect.y,playing_entities)
                                k+=1
         

             for sprite in spectre[:]:
                if sprite.rect.collidepoint(player.rect.centerx,player.rect.centery):
                   if lifetrig == False:
                      dmgtime = TIME + 0.01
                      lifetrig = True
                   if player.punching == True:
                       SCORE += 5
                       KILL += 1
                      # pygame.mixer.Sound.play(death_enemy)
                       spectre.remove(sprite)
                       sprite.kill()
                   if dmgtime < TIME:
                       # pygame.mixer.Sound.play(ouch)
                        LIFE -= 5
                        lifetrig = False
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
   
    # If you want a background image, replace this clear with blit'ing the
    # background image.
           screen.fill(BLACK)

    # --- Drawing code should go here
           ssplash.draw(screen)
           ssplash.update()

           if Menu == True:
              menu_sprites.draw(screen)
              menu_sprites.update()

           if Cutscene == True:
              
              cut_S.draw(screen)
              cut_S.update()  

              font = pygame.font.SysFont("Verdana", 24)
              tex = "Intializing ..."
              human = "Wait, What ... What happened?!"
              tex2 = "Optical implant malfunction ..."
              human2 = "Why can't I see anything?!"
              tex3 = "Assessing enviroment..."
              human3 = "Radars working ..."
              tex4 = "Hostiles detected!!"
              human4 = "Wait WHAT!!??"


              img = font.render(tex, True, GREEN)
              img2 = font.render(human, True, YELLOW)
              img3 = font.render(tex2, True, GREEN)
              img4 = font.render(human2, True, YELLOW)
              img5 = font.render(tex3, True, GREEN)
              img6 = font.render(human3, True, YELLOW)
              img7 = font.render(tex4, True, GREEN)
              img8 = font.render(human4, True, YELLOW)

              screen.blit(img,(0,0))
              screen.blit(img2,(250,50))
              screen.blit(img3,(0,100))
              screen.blit(img4,(300,150))
              screen.blit(img5,(0,200))
              screen.blit(img6,(400,250))
              screen.blit(img7,(0,300))
              screen.blit(img8,(450,350))

            

           if Menu == False and Cutscene == False and Cutscene2  == False and GAMEOVER == False and splashscr == False :
             menufront.kill()
             menubutton_P.kill()
             
             bground.draw(screen)
             radar.draw(screen)
             playing_entities.draw(screen)
             players.draw(screen)
             enemy.draw(screen)
             bar.draw(screen)

             bground.update()
             radar.update(dt)
             playing_entities.update()
             enemy.update()
             players.update(dt)
             bar.update()

             font = pygame.font.SysFont("verdana", 24)
             timer =  font.render("Time: "+str('%.2f' % GAMETIMER), True, YELLOW)
             screen.blit(timer,(470,440)) 
             score =  font.render("Score: "+str(SCORE), True, YELLOW)
             screen.blit(score,(0,0)) 
             killing =  font.render("Kills: "+str(KILL), True, YELLOW)
             screen.blit(killing,(490,0)) 
             equip =  font.render("GUN CNTDWN: "+str( '%.0f' % guntimer), True, YELLOW)
             screen.blit(equip,(0,440)) 
            
             GAMETIMER -= dt

         

             if GUN !=0:
                  guntimer -= dt

             if guntimer <= 0:
                  GUN = 0

             if KILL == 20:
                   print("audio")
              # pygame.mixer.Sound.play(overkill)

             if KILL == 50:
                   print("audio")
                #  pygame.mixer.Sound.play(rampage)
                    

           if GAMEOVER == True:
               gameover.draw(screen)
               gameover.update(dt)

           if GAMETIMER <= 0:
               Cutscene2 = True

           if Cutscene2 == True:
               for shost in spectre[:]:
                    if shost in spectre:
                         shost.kill()
               cutscenes.draw(screen)
               cutscenes.update(dt)


    # --- Limit to 60 frames per second
           dt = clock.tick(60)/1000
           i -= 1
           TIME += dt
           if delay == True:
                 if trigger == False:
                       if GUN == 0:
                           j = TIME + 0.7
                       if GUN == 1:
                             j = TIME + 1.0
                       trigger = True
                 if TIME >= j:
                       delay = False
                       trigger = False


# Close the window and quit.

         
           pygame.display.flip()

           await asyncio.sleep(0)  # Very important, and keep it 0
 

asyncio.run(main())