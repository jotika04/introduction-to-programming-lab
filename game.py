from pygame import *  #import * from pygame
import menu         #import the menu
import random       #import random
from classes import *   #import * from the classes class




def run_game():                 #function to run the game
    """game play interface"""
    screen = pygame.display.set_mode((800, 600)) #set the height and width of the screen
    display.set_caption("Jet mission")      #gives title for game


    scores = 0          #set scocre to 0 from the start
    theClock = pygame.time.Clock()  #object to track time
    bg_image = Star_bg("star.gif")  #inserts the gif to the background

    #coordinate of moving background
    x = 0               #sets the coordinate x to start from 0
    y = 0               #sets the coordinate y to start from 0
    x1 = bg_image.width #x1 equal to background width
    y1 = 0              #y1 is equal to 0

    pygame.init()       #initialize pygame


    #creating a jet
    jet1 = Jet(screen)      #make object called jetl from the jet class
    Jet_sprites = Group(jet1)

    #create asteroid object group
    asteroid_group = Group()

    #create bullets object Group
    bullets = Group()



    Fps = 60                   #sets fps to 60
    asteroid_timer = pygame.time.get_ticks() #get time for the asteroid timer
    while True:                 #loop if condition is true
        theClock.tick(Fps)      #sets fps to be corenspond with the fps
        Fps += 0.01             #game phase goes faster after every frame

        """background move"""

        x -= 5                  #to make the bacground moves backward
        x1 -= 5                 #to make the bacground moves backward
        bg_image.draw(screen,x,y)   # show the background image according to  x,y coordinate
        bg_image.draw(screen,x1, y1)    # show the background image according to  x1,y1 coordinate
        if x < -bg_image.width:        # if x is less than minus background width, run the code
            x = 0
        if x1 < 0:                  # if x1 is less than 0, run the code
            x1 = bg_image.width

        # create score board
        font=pygame.font.SysFont("Times New Romans",36)     #set font and size
        score_board=font.render("score:"+str(scores),True,(255,255,255)) #update the score
        # update refered to the word's method
        screen.blit(score_board,(10,550)) #draw the score board in game

        Jet_sprites.draw(screen) #draw the jet in game

        bullets.draw(screen)  # draw the bullet

        asteroid_group.draw(screen) #draw the asteroid
        display.update()  #update jet and screen view
        event.get()   #get the event
        """moves the jet according to key pressed"""

        key = pygame.key.get_pressed()  #make variable for pygame.key_pressed
        if key[K_LEFT] and jet1.rect.x>0:   # if key left and jet1.rect x is greater than 0, run the code
            jet1.moveleft()

        if key[K_RIGHT] and jet1.rect.x<=700:   # if key right and jet1.rect x is greater than 0, run the code
            jet1.moveright()

        if key[K_DOWN] and jet1.rect.y<=500:    #if key down and jet1.rect.y is less than 500, run the code
            jet1.movedown()

        if key[K_UP] and jet1.rect.y>0:         # if key up and jet1.rect.y is greater than 0, run the code
            jet1.moveup()

        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000):
            bullet = Bullet(screen, jet1.rect.x+50, jet1.rect.y+42) #set bullet position based on the jet
            bullets.add(bullet)         #add bullets
            pygame.mixer.music.load("LaserBlast.wav") #set the sound when you shoot the bullet
            pygame.mixer.music.play()       #play the sound when you shoot

        if key[K_ESCAPE]:               # if space is pressed, run the code
            menu.menu_screen(Button,run_game)

        if key[K_p]:                    #if p is pressed, run the code
            menu.pause_menu(Button,run_game)


        """generate asteroid randomly"""
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            asteroid = Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20))
            #makes the asteroid spawn randomly
            asteroid_group.add(asteroid)        #add asteroid
            asteroid_timer = pygame.time.get_ticks() # set time to span the asteroid

        """update the movement of asteroid"""
        for asteroid in asteroid_group:
            asteroid.movement()
            if asteroid.rect.right <= 0:    #if asteroid.rect.right is equal or less than, run the code
                asteroid_group.remove(asteroid) #remove after screen
            if groupcollide(Jet_sprites,asteroid_group,dokilla=True,dokillb=True):#checks condition
                menu.lose_menu(Button,run_game,scores)

        """update bullet movement on screen"""
        for bullet in bullets:
            bullet.movement()
            if bullet.rect.left > 800: #if bullet.rect.left is greater tha 800
                bullets.remove(bullet) #remove bullet from screen
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):#checks condion if bullet hit asteroid
                scores += 50       #add the score by 100

menu.menu_screen(Button,run_game) #calls the function

#---------------SPECIAL THANKS to Pier,Excel,georgius,William,Nicander,Nicolas,Andy,Guntur,Adrian-----------------------
"""Acknowledgement:
LaserBlast.wav(shooting sound) http://soundbible.com/472-Laser-Blasts.html
"""
