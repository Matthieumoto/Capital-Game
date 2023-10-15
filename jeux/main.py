from settings import *
from player import *
from platforme import *
from projectile import *
from menus import *


class Game:

    """Initialisation de toutes les attribus du jeu"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.FramePerSec = pygame.time.Clock()
        self.img2 = pygame.image.load('ressource/herbe.jpeg')
        self.img3 = pygame.image.load("ressource/nuage.png")
        self.img_player_g = pygame.image.load("ressource/perso_g.png")
        self.img_player_d = pygame.image.load("ressource/perso_d.png")
        self.img_player_saut = pygame.image.load("ressource/perso_saute.png")
        self.img_player_chute = pygame.image.load("ressource/perso_chute.png")
        self.img_projectile_g = pygame.image.load("ressource/boule_g.png")
        self.img_projectile_d = pygame.image.load("ressource/boule_d.png")
        self.billet = pygame.image.load("ressource/billet.png")
        self.sol_bg = pygame.transform.scale(self.img2, (self.settings.WIDTH, self.settings.HEIGHT - 10))
        self.plt_bg = pygame.transform.scale(self.img3, (100, 50))
        icone = pygame.image.load("ressource/icone.png")
        pygame.display.set_icon(icone)

        self.jouer_btn_nn_presse = pygame.image.load("ressource/jouer_nn_presse.png")
        self.rect_btn_jouer_nn_presse = self.jouer_btn_nn_presse.get_rect(center=(self.settings.WIDTH // 2, self.settings.HEIGHT // 3))

        self.info_btn_nn_presse = pygame.image.load("ressource/info_nn_presse.png")
        self.rect_btn_info_nn_presse = self.jouer_btn_nn_presse.get_rect(center=(self.settings.WIDTH // 2, self.settings.HEIGHT // 2))
        
        self.quitter_btn_nn_presse = pygame.image.load("ressource/quitter_nn_presse.png")
        self.rect_btn_quitter_nn_presse = self.quitter_btn_nn_presse.get_rect(center=(self.settings.WIDTH // 2, self.settings.HEIGHT // 1.5))

        self.continuer_btn = pygame.image.load("ressource/recomencer_presse.png")
        self.rect_continuer_btn = self.continuer_btn.get_rect(center=(self.settings.WIDTH // 2, self.settings.HEIGHT // 2))

        self.score_btn = pygame.image.load("ressource/score_btn.png")
        self.rect_score_btn = self.continuer_btn.get_rect(center=(self.settings.WIDTH // 2, self.settings.HEIGHT // 1.1))

        self.coeur_r = pygame.image.load("ressource/coeur_r.png")

        self.displaysurface = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))

        pygame.display.set_caption("Capital Game !") 

        self.projectile_timer = 0
        self.points = 0
        self.vie = 5
        self.projectile_rec = 120
        self.lst_touche = []
        self.lst_mort = []
        self.cheat_combinaison = [pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_b, pygame.K_a]
        self.mort_combinaison = [pygame.K_m,pygame.K_o,pygame.K_r,pygame.K_t]

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.all_projectiles = pygame.sprite.Group()
        self.billet_group = pygame.sprite.Group()
        self.player = Player(self)

        self.all_sprites.add(self.player)
        self.player_group.add(self.player)

        sol = Plateforme((0, self.settings.HEIGHT - 10), self.settings.WIDTH, 50, self.sol_bg)
        self.platforms.add(sol)
        self.all_sprites.add(sol)

        self.menu = Menu(self)

        for i in range(15):
            plateforme = Plateforme((random.randint(200, 1600), random.randint(200, 700)), 100, 50, self.plt_bg)
            self.platforms.add(plateforme)
            self.all_sprites.add(plateforme)

        self.shoot = pygame.mixer.Sound("ressource/shoot.mp3")
        self.shoot.set_volume(0.10)
        self.ouch = pygame.mixer.Sound("ressource/mort.mp3")
        self.argent = pygame.mixer.Sound("ressource/argent.mp3")
        self.mort = pygame.mixer.Sound("ressource/jsp.mp3")
        self.bg_musique = pygame.mixer.Sound("ressource/attente.mp3")
        self.win = pygame.mixer.Sound("ressource/win.mp3")
        self.win.set_volume(4)
        self.bg_musique.play(-1)
    
 
    def data(self):

        """Chargement et sauvegarde de toutes les scores des joueurs dans le fichier JSON"""

        with open("static/info.json", 'r') as f:
            donnees = json.load(f)
        
        if len(donnees) >= 7:
            dernier_joueur = list(donnees.keys())[-1]
            del donnees[dernier_joueur]

        if self.name not in donnees:
            donnees[self.name] = {"nom" : self.name,"best_score": 0}

        if self.points > donnees[self.name]["best_score"]:
            donnees[self.name]["best_score"] = self.points
            self.best_score = self.points

        with open("static/info.json", 'w') as f:
            json.dump(donnees, f,indent=4, ensure_ascii=False)

    def reinit(self):

        """Réinitialisation du jeu"""

        self.all_sprites.empty()
        self.platforms.empty()
        self.player_group.empty()
        self.all_projectiles.empty()
        self.billet_group.empty()
        
        self.projectile_rec = 120
        self.points = 0
        self.vie = 5
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.player_group.add(self.player)

        for i in range(15):
            plateforme = Plateforme((random.randint(100, 1500), random.randint(100, 700)), 100, 50, self.plt_bg)
            self.platforms.add(plateforme)
            self.all_sprites.add(plateforme)
        
        sol = Plateforme((0, self.settings.HEIGHT - 10), self.settings.WIDTH, 50, self.sol_bg)
        self.platforms.add(sol)
        self.all_sprites.add(sol)

    def dessiner_coeur(self):

        """Dessiner les coeurs"""

        x, y = 10, 10
        coeur_spacing = 40

        for _ in range(self.vie):
            self.displaysurface.blit(self.coeur_r, (x, y))
            x += coeur_spacing
    
    def dessiner_billet(self):

        """Dessiner le compteur de billets"""

        x, y = self.settings.WIDTH - 120, 10
        argent_text = f" : {self.points} €"
        font = pygame.font.Font(None, 36)
        text = font.render(argent_text, True, (255, 255, 255))
        self.displaysurface.blit(text, (x, y))
        self.displaysurface.blit(self.billet, (x - 100, y))


    def run(self):

        """Lancement du jeu"""

        self.menu.name_menu()
        self.menu.main_menu()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.bg_musique.stop()
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.lst_touche.append(event.key)
                    self.lst_mort.append(event.key)
                    if event.key == K_UP:
                        self.player.jump(-15, self.platforms)
                        self.player.surf.blit(self.img_player_saut, (0, 0))
                    if event.key == K_p:
                        self.menu.menu_pause()
                    if event.key == K_ESCAPE:
                        self.menu.main_menu()
                    if event.key == K_c:
                        self.lst_touche = []
                        self.lst_mort = []
                if len(self.lst_touche) == len(self.cheat_combinaison):
                    if self.lst_touche == self.cheat_combinaison:
                        self.vie = 100
                        self.projectile_rec = 1
                    else:
                        self.lst_touche = []
                if len(self.lst_mort) == len(self.mort_combinaison):
                    if self.lst_mort == self.mort_combinaison:
                        self.bg_musique.stop()
                        self.mort.play(-1)
                    else:
                        self.lst_mort = []
            if self.points >= 100000:
                self.bg_musique.stop()
                self.win.play()
                self.menu.win()
                self.bg_musique.play(-1)


            self.displaysurface.fill((0, 162, 232))

            self.dessiner_coeur()
            self.dessiner_billet()

            self.all_projectiles.update()
            self.all_projectiles.draw(self.displaysurface)

            self.billet_group.update()
            self.billet_group.draw(self.displaysurface)

            self.player.update(self.platforms, self.all_projectiles, self.billet_group)
            self.player.move(self.settings.ACC)

            self.projectile_timer += 1

            if self.projectile_timer % 60 == 0:
                projectile_left = Projectile(self,(40,40), 100, random.randint(0, self.settings.WIDTH), random.randint(2, 30))
                projectile_left.image.blit(self.img_projectile_d, (0, 0))
                self.all_projectiles.add(projectile_left)

                projectile_right = Projectile(self,(40,40), self.settings.WIDTH -100, random.randint(0, self.settings.HEIGHT - 30),
                                               random.randint(-30, -2))
                projectile_right.image.blit(self.img_projectile_g, (0, 0))
                self.all_projectiles.add(projectile_right)

                self.shoot.play()

            if self.projectile_timer % self.projectile_rec == 0:
                billet_left = Projectile(self,(100,50), 0, random.randint(100, self.settings.WIDTH - 100), random.randint(2, 20))
                billet_left.image.blit(self.billet, (0, 0))
                self.billet_group.add(billet_left)

                billet_right = Projectile(self,(100,50), self.settings.WIDTH, random.randint(100, self.settings.HEIGHT - 100),random.randint(-20, -2))
                billet_right.image.blit(self.billet, (0, 0))
                self.billet_group.add(billet_right)

                self.shoot.play()
            
            for entity in self.all_sprites:
                self.displaysurface.blit(entity.surf, entity.rect)


            pygame.display.update()
            self.FramePerSec.tick(self.settings.FPS)

        pygame.quit()


# Lancement du jeu lorsque le main.py est execute
if __name__ == "__main__":
    game = Game()
    game.run()