from settings import *

class Plateforme(pygame.sprite.Sprite):
    """Classe qui permet de creer des platformes"""

    def __init__(self, coordonees, largeur, hauteur, bg):
        """Initialisation de la classe et récupération du constructeur de la classe pygame.sprite.Sprite"""
        super().__init__()
        self.surf = pygame.Surface((largeur, hauteur))
        self.surf.blit(bg, (0, 0))
        self.rect = self.surf.get_rect()
        self.rect.x = coordonees[0]
        self.rect.y = coordonees[1]
