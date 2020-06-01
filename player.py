import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect =  self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

    def launch_projectile(self):
        #creation d'une nouvelle instance
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        #que si le joueur n'est pas en collision avec une entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
    
    def update_health_bar(self,surface):
        #dessin de la jauge d'arière plan
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x+50, self.rect.y+20, self.max_health, 5])
        #dessin de la jauge
        pygame.draw.rect(surface, (111, 210, 46),[self.rect.x+50, self.rect.y+20, self.health, 5])

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
