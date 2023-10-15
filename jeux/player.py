from settings import *

class Player(pygame.sprite.Sprite):

    """Une classe qui permet de creer un joueur et de gerer plusieurs évenements tel que les déplacements, la mort, les colisions"""

    def __init__(self, game):
        """Initialisation de la classe et récupération du constructeur de la classe pygame.sprite.Sprite"""
        super().__init__()
        self.game = game
        self.surf = pygame.Surface((30, 75))
        self.surf.blit(self.game.img_player_d, (0, 0))
        self.rect = self.surf.get_rect()
        self.pos = pygame.math.Vector2((self.game.settings.WIDTH / 2, self.game.settings.HEIGHT / 2))
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)
        self.game = game

    def move(self, acc_x):
        """Méthode qui permet de gerer les mouvements, la gravité et la colision avec les mors droits et gauche de l'écran"""
        self.acc = pygame.math.Vector2(0, 0.5)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -acc_x
            self.surf.blit(self.game.img_player_g, (0, 0))
        if pressed_keys[K_RIGHT]:
            self.acc.x = acc_x
            self.surf.blit(self.game.img_player_d, (0, 0))

        self.acc.x += self.vel.x * self.game.settings.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > self.game.settings.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.game.settings.WIDTH
        if self.pos.y >= self.game.settings.HEIGHT:
            self.pos.y = self.game.settings.HEIGHT
            self.vel.y = 0
        if self.vel.y > 0.5:
            self.surf.blit(self.game.img_player_chute, (0, 0))

        self.rect.midbottom = self.pos

    def death_screen(self):
        """Fenetre qui s'affiche lorsque le joueur meurt (Que sa vie soit à Zéro)"""
        menu_font = pygame.font.Font(None, 150)
        menu_text1 = menu_font.render("Vous êtes mort ;-;", True, (255, 255, 255))
        menu_rect1 = menu_text1.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 5))

        while True:
            if pygame.get_init():
                self.game.displaysurface.fill((0, 0, 0))
                self.game.displaysurface.blit(menu_text1, menu_rect1)
                self.game.displaysurface.blit(self.game.continuer_btn,self.game.rect_continuer_btn)
                self.game.displaysurface.blit(self.game.quitter_btn_nn_presse,self.game.rect_btn_quitter_nn_presse)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.mixer.music.stop()
                        sys.exit()
                    mouse_pos = pygame.mouse.get_pos()
                    if self.game.rect_continuer_btn.collidepoint(mouse_pos[0],mouse_pos[1]):
                        if event.type == MOUSEBUTTONDOWN:
                            self.game.reinit()
                            return
                    if self.game.rect_btn_quitter_nn_presse.collidepoint(mouse_pos[0],mouse_pos[1]):
                        if event.type == MOUSEBUTTONDOWN:
                            self.game.bg_musique.stop()
                            sys.exit()
                    if event.type == KEYDOWN:
                        self.game.reinit()
                        return

                pygame.display.flip()
                self.game.FramePerSec.tick(self.game.settings.FPS)

    def jump(self, vel_y, platforms):

        """Saut du joueur"""
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = vel_y

    def update(self, platforms, projectile, argent):
        """Update du joueur, colision, vie """
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
        for i in projectile:
            hits = pygame.sprite.spritecollide(self, [i], False)
            if hits:
                self.game.vie -= 1
                self.game.ouch.play()
                i.kill()
        for i in argent:
            hits = pygame.sprite.spritecollide(self, [i], False)
            if hits:
                self.game.points += 100
                self.game.argent.play()
                self.game.data()
                i.kill()
        if self.game.vie <= 0:
            self.game.ouch.play()
            self.death_screen()
