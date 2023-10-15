from settings import *

class Menu:

    """Classe qui permet d'afficher plusieurs sortes de menus"""

    def __init__(self,game) -> None:
        """Initialisation et récupération du self de la classe Game"""
        self.game = game

    def win(self):
        """Fenetre qui s'affiche lorsque l'on a gagné"""
        menu_font = pygame.font.Font(None, 90)
        menu_text1 = menu_font.render("Vous avez Récupérer 100 000$", True, (255, 255, 255))
        menu_rect1 = menu_text1.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 5))
        menu_text2 = menu_font.render("Vous avez gagné le respect de votre famille", True, (255, 255, 255))
        menu_rect2 = menu_text2.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 3))

        while True:
            if pygame.get_init():
                self.game.displaysurface.fill((0, 0, 0))
                self.game.displaysurface.blit(menu_text1, menu_rect1)
                self.game.displaysurface.blit(menu_text2, menu_rect2)
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
    
    def info(self):
        """Fenetre qui s'affiche lorsque lon clique sur la boutton 'Info' dans le menu principal"""
        font = pygame.font.Font(None,40)
        font2 = pygame.font.Font(None,30)
        text1 = font.render("Informatation", True,(255, 255, 255))
        rect1 = text1.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 8))

        text3 = font.render("Le but du jeu est simple !", True,(255, 255, 255))
        rect3 = text3.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 4))

        text4 = font.render("Vous êtes à la place d'un capitaliste à la recherche d'argent", True,(255, 255, 255))
        rect4 = text4.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 2))

        texte6 = font.render("Votre obectif est simple : récupérer le plus d'argent sans vous prendre les balles des communistes !",True,(255,255,255))
        rect6 = texte6.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 1.75))
        
        texte7 = font.render("Vous devez voler 100 000 $ pour gagner le respect des autes",True,(255,255,255))
        rect7 = texte7.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 1.50))

        text2 = font2.render("Appuiyez sur n'importe quelle touche pour retourner en arrière !", True,(255, 255, 255))
        rect2 = text2.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 1.25))

        while True:
            if pygame.get_init():
                self.game.displaysurface.fill((0, 0, 0))
                self.game.displaysurface.blit(text1, rect1)
                self.game.displaysurface.blit(text2, rect2)
                self.game.displaysurface.blit(text3, rect3)
                self.game.displaysurface.blit(text4, rect4)
                self.game.displaysurface.blit(texte6,rect6)
                self.game.displaysurface.blit(texte7,rect7)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.game.bg_musique.stop()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        self.game.bg_musique.set_volume(1)
                        return

                pygame.display.flip()
                self.game.FramePerSec.tick(self.game.settings.FPS)

    def main_menu(self):
        """Menu principal qui s'execute lors du lancement du jeu"""
        menu_font = pygame.font.Font(None, 100)
        menu_text = menu_font.render("Capital Game !", True, (255, 255, 255))
        menu_rect = menu_text.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 10))

        while True:
            self.game.displaysurface.fill((0, 0, 0))
            self.game.displaysurface.blit(menu_text, menu_rect)
            self.game.displaysurface.blit(self.game.jouer_btn_nn_presse,self.game.rect_btn_jouer_nn_presse)
            self.game.displaysurface.blit(self.game.info_btn_nn_presse,self.game.rect_btn_info_nn_presse)
            self.game.displaysurface.blit(self.game.quitter_btn_nn_presse,self.game.rect_btn_quitter_nn_presse)
            self.game.displaysurface.blit(self.game.score_btn,self.game.rect_score_btn)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game.bg_musique.stop()
                    sys.exit()
                mouse_pos = pygame.mouse.get_pos()
                if self.game.rect_btn_jouer_nn_presse.collidepoint(mouse_pos[0],mouse_pos[1]):
                    if event.type == MOUSEBUTTONDOWN:
                        return
                    
                if self.game.rect_btn_info_nn_presse.collidepoint(mouse_pos[0],mouse_pos[1]):
                    if event.type == MOUSEBUTTONDOWN:
                        self.info()
                    
                if self.game.rect_btn_quitter_nn_presse.collidepoint(mouse_pos[0],mouse_pos[1]):
                    if event.type == MOUSEBUTTONDOWN:
                        self.game.bg_musique.stop()
                        sys.exit()    
                if self.game.rect_score_btn.collidepoint(mouse_pos[0],mouse_pos[1]):
                    if event.type == MOUSEBUTTONDOWN:
                        os.system("start chrome http://localhost:5000")
                        os.system("start /min python app.py")
                            
            pygame.display.flip()
            self.game.FramePerSec.tick(self.game.settings.FPS)

    def menu_pause(self):

        """Menu pause qui s'ouvre lorsque on appuie sur la touche 'P' quand on joue"""

        self.game.data()

        menu_font = pygame.font.Font(None, 50)
        menu_font2 = pygame.font.Font(None, 60)

        menu_text = menu_font2.render("Pause", True,(255, 255, 255))
        menu_rect = menu_text.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 8))

        menu_text2 = menu_font.render(f"Vous avez gagné {self.game.points} d'argent ! | best score de '{self.game.name}' : {self.game.best_score}", True,(255, 255, 255))
        menu_rect2 = menu_text2.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 4))

        menu_text3 = menu_font.render(f"Attention il vous reste plus que {self.game.vie} vie !", True,(255, 255, 255))
        menu_rect3 = menu_text3.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 2))
        
        while True:
            if pygame.get_init():
                self.game.bg_musique.set_volume(0.25)
                self.game.displaysurface.fill((0, 0, 0))
                self.game.displaysurface.blit(menu_text, menu_rect)
                self.game.displaysurface.blit(menu_text2, menu_rect2)
                self.game.displaysurface.blit(menu_text3, menu_rect3)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.game.bg_musique.stop()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        self.game.bg_musique.set_volume(1)
                        return

                pygame.display.flip()
                self.game.FramePerSec.tick(self.game.settings.FPS)
    
    def name_menu(self):

        """Menu qui permet d'entrer son nom dès le démarrage du jeu"""

        texte_saisi = ""

        police = pygame.font.Font(None, 36)

        menu_text = police.render("Entrez votre nom :", True, (255, 255, 255))
        menu_rect = menu_text.get_rect(center=(self.game.settings.WIDTH // 2, self.game.settings.HEIGHT // 10))

        texte_affiche = police.render(texte_saisi, True, (255, 255, 255))
        position_texte = texte_affiche.get_rect()
        position_texte.centerx = self.game.displaysurface.get_rect().centerx
        position_texte.centery = self.game.displaysurface.get_rect().centery

        while True:
            self.game.displaysurface.fill((0, 0, 0))
            self.game.displaysurface.blit(menu_text,menu_rect)
            texte_affiche = police.render(texte_saisi, True, (255, 255, 255))
            self.game.displaysurface.blit(texte_affiche, position_texte)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        texte_saisi = texte_saisi[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.game.name = texte_saisi
                        self.game.data()
                        with open("static/info.json", 'r') as f:
                            donnees = json.load(f)
                        self.game.best_score = donnees[self.game.name]["best_score"]
                        txt = f"Capital Game | {self.game.name}"
                        pygame.display.set_caption(txt)
                        return
                    else:
                        texte_saisi += event.unicode
            
            pygame.display.flip()