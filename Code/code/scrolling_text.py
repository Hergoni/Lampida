import pygame

pygame.init()  # Initialisation de Pygame


class ScrollingText:
    def __init__(self, messages, font_path='freesansbold.ttf', font_size=24, screen_size=(1280, 720), speed=3):
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

    def update(self):
        # Effacer l'écran
        self.screen.fill('dark gray')

        # Réguler le framerate
        self.timer.tick(60)

        # Dessiner un rectangle noir en bas de l'écran
        pygame.draw.rect(self.screen, 'black', [0, 500, 1500, 250])

        # Vérifier si le texte doit être défilé
        if self.counter < self.speed * len(self.message):
            self.counter += 1
        elif self.counter >= self.speed * len(self.message):
            self.done = True

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.done and self.active_message < len(self.messages):
                    # Passer au message suivant si la touche "Entrée" est enfoncée et si le défilement est terminé
                    self.active_message += 1
                    self.done = False
                    self.message = self.messages[self.active_message]
                    self.counter = 0

        # Rendre le texte progressivement
        snip = self.font.render(self.message[0:self.counter // self.speed], True, 'white')

        # Afficher le texte
        self.screen.blit(snip, (10, 500))

        # Mettre à jour l'affichage
        pygame.display.flip()
        # Vérifier si tous les messages ont été affichés
        if self.active_message == len(self.messages) - 1 and self.done:
            return False  # Arrêter la boucle de mise à jour

        return True

    def run(self):
        running = True
        while running:
            running = self.update()  # Appeler la méthode update() dans une boucle tant que le jeu est en cours
        pygame.quit()  # Quitter Pygame lorsque la boucle est terminée




