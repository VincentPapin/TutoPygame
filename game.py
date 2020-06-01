import pygame
from player import Player
from monster import Monster

class Game:

    def __init__(self):
        #définir si le jeu a commencé ou non
        self.is_playing = False
        #Générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.player.rect.x = 400

    def game_over(self):
        # remettre le jeu à neuf, retiorer les monstres, remettre le joueur à 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        #Appliquer l'image du joueur
        screen.blit(self.player.image,(self.player.rect))

        #actualiser la bare de PV du player
        self.player.update_health_bar(screen)
    
        #Recup des projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        #recup les mosntres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        #Appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        #Appliquer l'ensemble des images de mon groupes de monstres
        self.all_monsters.draw(screen)

        #verifier si le joeuer veut aller à droite ou gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1080:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        #elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        #    game.player.move_up()
        #elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < 500:
        #    game.player.move_down()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)