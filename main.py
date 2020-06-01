import pygame
from game import Game
import math
# import package.module as module #Utilisé pour activer l'auto completion

pygame.init() 

# generer la fenêtre
pygame.display.set_caption("test")
screen = pygame.display.set_mode((1080, 720))

# Importer le background
background = pygame.image.load('assets/bg.jpg')

# importer la bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Importer le bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# Chargement du jeu
game = Game()

running = True

#Boucle du jeu
while running: 
    
    #Applique l'arriere plan
    screen.blit(background,(0,-200))

    #vérifier si e jeu a commencé ou non
    if game.is_playing:
        #déclencher les instructions de la partie
        game.update(screen)
    else:
        #ajouter l'écran de bienvenue
        screen.blit(play_button,play_button_rect)
        screen.blit(banner,banner_rect)
        

    #MAJ de l'écran
    pygame.display.flip()

    for event in pygame.event.get():
        #si il quitte
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            
        #Detecter si un jouer lache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            #si la touche espace est enclenchée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                game.start()