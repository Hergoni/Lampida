import pygame
from screen import Screen
import button

# Charger l'image du bouton "Retour"
back_img = pygame.image.load('../../assets/Images/button_back.png').convert_alpha()

# Créer un bouton pour revenir en arrière
back_button = button.Button(480, 490, back_img, 1)

# Initialiser l'état du menu
menu_state = "main"


class FPSChanger:
    def __init__(self, screen: Screen, menu_state: str):
        self.menu_state = menu_state
        self.screen = screen
        self.menu_state = menu_state  # Définir l'état initial du menu
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Charger l'image de fond pour la modification des FPS
        self.background_image = pygame.image.load("../../assets/Images/background_video.png").convert()
        self.background_rect = self.background_image.get_rect()

        # Définir la police de caractères et le texte
        self.font = pygame.font.Font(None, 32)
        self.text = ""

        # Définir la zone de saisie pour les FPS
        self.input_rect = pygame.Rect(self.WINDOW_WIDTH // 2 - 70, self.WINDOW_HEIGHT // 2 - 50, 140, 32)

        # Définir la couleur du cadre de la zone de saisie
        self.color = pygame.Color('lightskyblue3')

        # Rendre le texte "Changer les FPS"
        self.text_change_fps = self.font.render("Changer les FPS", True, self.BLACK)
        self.text_change_fps_rect = self.text_change_fps.get_rect()
        self.text_change_fps_rect.topleft = (self.input_rect.left - self.text_change_fps.get_width() - 10,
                                             self.input_rect.centery - self.text_change_fps.get_height() // 2)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            new_fps = int(self.text)
                            pygame.time.Clock().tick(new_fps)
                        except ValueError:
                            print("Veuillez saisir un nombre valide pour les FPS.")
                        self.text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        self.menu_state = "main"

            # Afficher l'image de fond
            self.screen.blit(self.background_image, (0, 0))

            # Dessiner la zone de saisie des FPS
            pygame.draw.rect(self.screen, self.color, self.input_rect, 2)
            text_surface = self.font.render(self.text, True, self.BLACK)
            self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

            # Afficher le texte "Changer les FPS"
            self.screen.blit(self.text_change_fps, self.text_change_fps_rect)

            # Afficher le bouton "Retour"
            self.screen.blit(back_img, (480, 490))

            # Vérifier si le bouton "Retour" est cliqué
            if back_button.draw(self.screen):
                menu_state = "main"
                running = False

            pygame.display.flip()

        pygame.quit()


# Créer un objet Screen
screen = Screen()

# Utiliser la classe FPSChanger
if __name__ == "__main__":
    menu_state = "main"
    fps_changer = FPSChanger(screen, menu_state)
    fps_changer.run()
