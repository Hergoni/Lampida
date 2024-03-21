import pygame
import button
from scrolling_text import ScrollingText
from pygame import mixer
from game import Game
pygame.init()

#Create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#Define fonts
font = pygame.font.SysFont("arialblack",40)
font2 = pygame.font.SysFont("segoescript",10)
# Charger l'image de fond + redimension
background_img = pygame.image.load("../../assets/Images/background_menu.PNG").convert()
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

#define colours
TEXT_COL =(255,255,255)
TEXT_COL2 =(200,132,25)

#Variable du jeu
game_pause = False
menu_state = "main"
start_img = pygame.image.load("../../assets/Images/button_start.png").convert_alpha()
options_img = pygame.image.load("../../assets/Images/button_options.png").convert_alpha()
quit_img = pygame.image.load("../../assets/Images/button_quit.png").convert_alpha()
video_img = pygame.image.load('../../assets/Images/button_video.png').convert_alpha()
audio_img = pygame.image.load('../../assets/Images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('../../assets/Images/button_keys.png').convert_alpha()
back_img = pygame.image.load('../../assets/Images/button_back.png').convert_alpha()

#Création d'une instance boutton
start_button = button.Button(550,100,start_img,1 )
options_button = button.Button(550,250,options_img,1 )
quit_button = button.Button(550,400,quit_img,1 )
video_button = button.Button(420,100, video_img, 1)
audio_button = button.Button(420, 220, audio_img, 1)
keys_button = button.Button(420, 350, keys_img, 1)
back_button = button.Button(480, 490, back_img, 1)

def draw_text(text, TRUE , text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
#Game loop
run = True
while run :
    screen.fill((52,  78, 91))
    screen.blit(background_img, (0, 0))
    #Voir si la partie est en pause
    if game_pause == True:
        #Regarde le statut du menu
        if menu_state == "main":
          #affichage des boutons du menu
          if start_button.draw(screen):
              mixer.music.stop()
              if __name__ == "__main__":

                  

                  messages = ['Dossier n°32145-FR'
                              '\nAutorisation de niveau 3 requise '
                              '\nDossier constitué par le Docteur *******'
                              '\nSujet : incident SCP-3201-FR'
                              '\nVictime : 1'
                              '\nLancement de la séquence',
                              'Après avoir acheté quelque bricoles dans une brocante vous rentrez chez vous épuisé',
                              'Vous déposez la lampe dans la librairie',]
                  scrolling_text = ScrollingText(messages)
                  scrolling_text.run()
                  scrolling_done = True

                  game: Game = Game()
                  game.run()


          if options_button.draw(screen):
              menu_state = "options"
          if quit_button.draw(screen):
              run = False
          #regarde si l'écran de menue est ouvert
        if menu_state == "options":
            # draw the different options buttons
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if keys_button.draw(screen):
                print("Change Key Bindings")
            if back_button.draw(screen):
                menu_state = "main"
    else:
        draw_text("LAMPIDA",font2, TEXT_COL2,500,250)
        draw_text("Appuyer sur espace pour jouer", font, TEXT_COL, 300, 350)
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_pause = True
                mixer.music.load("../../assets/Sound/DayofchaosbyKevinMacLeod.mp3")
                mixer.music.play()
        if event.type == pygame.QUIT:
            run = False
            mixer.music.stop
    pygame.display.update()
pygame.quit()
