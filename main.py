import pygame
from game import Game

pygame.init()

#generer la fenêtre
pygame.display.set_caption("test")
screen = pygame.display.set_mode((1080, 720))

#Importer le background
background = pygame.image.load('assets/bg.jpg')

#Chargement du jeu
game = Game()

running = True

#Boucle du jeu
while running:
    
    #Applique l'arriere plan
    screen.blit(background,(0,-200))

    #Appliquer l'image du joeur
    screen.blit(game.player.image,(game.player.rect))

    #verifier si le joeuer veut aller à droite ou gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < 1080:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False