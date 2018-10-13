from pygame import *     # import * from pygame
import sys              #import sys
import pygame       #import pygame

def menu_screen(Button,run_game):           #function for screen menu
    """make the screen for menu"""
    display.set_caption("Jet Mission")          #gives title for game
    screen = pygame.display.set_mode((800, 600)) #set the height and width of the screen
    #object button for quit and start
    start_button = Button("New Piskel.png")         #insert the start button image
    quit_button = Button("quit button.png")         #insert the quit button image
    #image for the menu's backgound
    bg_image=pygame.image.load("asteroid_wall.jpg")    #give background image
    bg_image=pygame.transform.scale(bg_image, (800, 600))   #give scaling to the image


    pygame.init()   #intialize pygame

    while True:
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))  #set a rectangle when game start
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))  #set a rectangle when game end
        screen.blit(bg_image,(0,0))

        screen.blit(start_button.button,(250,200))      #start button size
        screen.blit(quit_button.button,(250,300))       #quit button size

        ev=event.wait()     #set amount of pause time

        if ev.type == MOUSEBUTTONDOWN:       #if you mouse click run code
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        if ev.type == QUIT:          # if you press quit, run the code
            sys.exit()

        display.update()

def pause_menu(Button,run_game):      # function for pause menu
    """pause_menu"""
    #make the screen display
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))

    # object button for quit and start
    start_button = Button("quit button.png")    #start button image
    return_button = Button("pause button.png")  #quit button image

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))     #backgroudn size


    pygame.init()
    paused=True #pause flag
    while paused:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #set rectangle in pause screen
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image, (0, 0))   # call background image at  0,0

        screen.blit(start_button.button, (250, 200))    # set start button's size
        screen.blit(return_button.button, (250, 300))   # set quit button's size

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                menu_screen(Button,run_game)
            if rect_return.collidepoint(mouse.get_pos()):
                paused = False #flag become  False

        if ev.type == QUIT:
            sys.exit()


        display.update()

def lose_menu(Button,run_game,score):
    """make the screen for menu"""
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))
    font=pygame.font.SysFont("times new roman",100) #font type and size
    text=font.render("Replay?",True,(255,255,255))  #ask if u wan to replay
    score_text=font.render("score:"+str(score),True,(255,255,255)) #display soce

    # object button for quit and start
    start_button = Button("New Piskel.png")
    quit_button = Button("quit button.png")

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    pygame.init()

    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image, (0, 0))
        screen.blit(text,(200,10))
        screen.blit(start_button.button, (250, 200))
        screen.blit(quit_button.button, (250, 300))
        screen.blit(score_text,(200,400))

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN:      #if you click mouse button run code
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        if ev.type == QUIT:
            sys.exit() #if quit run code

        display.update()
