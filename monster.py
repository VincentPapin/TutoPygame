import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.2
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1,2)

    def damage(self, amount):
        #infilger les dégats
        self.health -= amount

        #verifier si le nouveau nombre de PV <=0
        if self.health <= 0:
            #réapparition
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1,2)
            self.health = self.max_health

    def update_health_bar(self,surface):
        #dessin de la jauge d'arière plan
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x+10, self.rect.y-20, self.max_health, 5])
        #dessin de la jauge
        pygame.draw.rect(surface, (111, 210, 46),[self.rect.x+10, self.rect.y-20, self.health, 5])       

    def forward(self):
        # le deplamcenet ne se fait que si il n ya pas de collision avec le joeuer
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else: # en collision
            #infliger des dégats au player
            self.game.player.damage(self.attack)
            
    