from pygame import *        # import * from pygame
from pygame.sprite import *      # import * from pygame.sprite

class Jet(Sprite):      #class for jet
    """initialize the jet"""

    def __init__(self, screen):
        Sprite.__init__(self)
        """initialize the Jet"""
        self.image = image.load("battlejet.png")    #insert picture
        self.image = pygame.transform.scale(self.image, (90, 50)) #size of picture
        self.rect = self.image.get_rect()   #get rectangle for the image
        self.rect.x = 10        #set rectangle to x = 10
        self.rect.y = 50        #set rectange to y = 50
        self.screen = screen
        self.move_speed = 6     #set movement speed to 6
        """bullet"""
        self.firerates = 2       #set rate of fire to 2

    def moveleft(self):
        self.rect.x -= self.move_speed  #decrease rect x by movement speed
        display.flip()

    def moveright(self):
        self.rect.x += self.move_speed #increase self.rect.x += self.move_speed

        display.flip()

    def moveup(self):
        self.rect.y -= self.move_speed  #decrease rect y by move speed
        display.flip()

    def movedown(self):
        self.rect.y += self.move_speed  #increase rect y by move speed
        display.flip()





class Star_bg:      #create star class
    #resourse of the backgound setting
    def __init__(self,background):
        self.background=image.load(background)          #load background image
        self.background=pygame.transform.scale(self.background,(800,600))   # set the size of the background image
        self.background_size=self.background.get_size()  #get background size
        self.background_rect=self.background.get_rect() #get background rectangle
        self.width,self.height=self.background_size #background width and height
    def draw(self,screen,x,y):
        screen.blit(self.background,(x,y))   #creates the background image

class Bullet(Sprite):       #class for bullet
    def __init__(self,screen, startx, starty):
        Sprite. __init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = 20       #set the bullet's speed to 20

        self.image = pygame.image.load("bullets.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.rect.center = (startx,starty)
        self.screen = screen

    def movement(self):  #function to move bullet
        #self.screen.blit(self.image,[self.startx,self.starty])
        self.rect.left += self.speedx

class Asteroid(Sprite): #class for asteroid
    """initialize the Asteroid"""
    def __init__(self, screen, width, height, speedx, startx, starty):
        Sprite.__init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = speedx

        self.image = pygame.image.load("meteor.png")        #inserts meteor image
        self.image = pygame.transform.scale(self.image, (width, height))    # set the size for asteroid
        self.rect = self.image.get_rect()    # get asteroid's rectangle
        self.rect.left = startx
        self.rect.top = starty
        self.screen = screen

    def movement(self):      # function for the movement of asteroid
        """method to move the Asteoid"""
        self.rect.left -= self.speedx


class Button(Sprite):   # make class for button
    """initialize the button"""
    def __init__(self,image):
        Sprite. __init__(self)
        self.button = pygame.image.load(image) # insert the image for button
        self.button = pygame.transform.scale(self.button,(300,150)) #set the button size
