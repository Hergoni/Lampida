import pygame
pygame.init()
class ScrollingText:
    def __init__(self, messages, background_img_for_text, font_path='freesansbold.ttf', font_size=24, screen_size=(1280, 720), speed=2):
        # Initialisation des attributs de la classe
        self.messages = messages  # Liste des messages à faire défiler
        self.font = pygame.font.Font(font_path, font_size)  # Chargement de la police de caractères
        self.screen = pygame.display.set_mode(screen_size)  # Création de la fenêtre d'affichage
        self.timer = pygame.time.Clock()  # Création d'une horloge pour réguler le temps
        self.speed = speed  # Vitesse de défilement du texte
        self.active_message = 0  # Indice du message actuellement affiché
        self.message = self.messages[self.active_message]  # Initialisation du message actif
        self.counter = 0  # Compteur pour contrôler le défilement progressif du texte
        self.done = False  # Indicateur pour savoir si le défilement du texte est terminé

        # Charger l'image d'arrière-plan
        self.background_img_for_text = pygame.image.load(background_img_for_text).convert()
        self.background_img_for_text = pygame.transform.scale(self.background_img_for_text, screen_size)

    def update(self):
        self.screen.blit(self.background_img_for_text, (0, 0))
        self.timer.tick(60)
        pygame.draw.rect(self.screen, 'black', [0, 500, 1500, 250])

        # Vérifier si le texte doit être défilé
        if self.counter < self.speed * len(self.message):
            self.counter += 1
        elif self.counter >= self.speed * len(self.message):
            self.done = True

        # Rendre le texte progressivement
        rendered_lines = []
        lines = self.message.split('\n')
        for i, line in enumerate(lines):
            if self.counter >= self.speed * len(''.join(lines[:i])):
                rendered_lines.append(self.font.render(line, True, 'white'))

        # Afficher le texte
        y_offset = 500
        for rendered_line in rendered_lines:
            self.screen.blit(rendered_line, (10, y_offset))
            y_offset += rendered_line.get_height()  # Ajouter la hauteur de la ligne pour l'espacement

        pygame.display.flip()

        if self.active_message == len(self.messages) - 1 and self.done:
            return False

        return True


    def run(self):
        running = True
        while running:
            running = self.update()  # Appeler la méthode update() dans une boucle tant que le jeu est en cours
        pygame.quit()  # Quitter Pygame lorsque la boucle est terminée

