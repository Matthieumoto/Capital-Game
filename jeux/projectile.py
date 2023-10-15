from settings import *

class Projectile(pygame.sprite.Sprite):
    """Classe qui permet de creer des projectiles"""

    def __init__(self,game, taille, x, y, speed_x):
        """Initialisation de la classe et récupération du constructeur de la classe pygame.sprite.Sprite"""
        super().__init__()
        self.game = game
        self.image = pygame.Surface((taille[0],taille[1]))
        self.image.blit(game.img_projectile_g, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = speed_x

    def update(self):
        """Méthode qui permet d'update la position du projectile"""
        self.rect.x += self.speed_x

        if self.rect.right < 0 or self.rect.left > self.game.settings.WIDTH:
            self.kill()