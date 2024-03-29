import pygame
pygame.init()
pygame.font.init()
pygame.display.init()
pygame.display.set_mode((1024, 768))


from keylistener import KeyListener
from map import Map
from player import Player
from screen import Screen
from controller import Controller
from option import Option
from Objectives import Objectifs


class Game:
    def __init__(self) -> None:
        """""
        self.objectives = Objectifs(["Objectif 1", "Objectif 2", "Objectif 3"], font_size=20, font_color=(255, 255, 255))
        """
        self.running: bool = True
        """"
        self.objective_images = []  # Liste des images des objectifs
        self.load_objective_images()  # Charger les images des objectifs
        """
        self.screen: Screen = Screen()
        self.controller = Controller()
        self.map: Map = Map(self.screen, self.controller)
        self.keylistener: KeyListener = KeyListener()
        self.player: Player = Player(self.screen, self.controller, 208.72, 72.75, self.keylistener)
        self.map.add_player(self.player)
        self.option = Option(self.screen, self.controller, self.map, "fr",  self.keylistener)

    def run(self) -> None:
        while self.running:
            self.handle_input()
            """
            self.objectives.display_objectives(self.screen.get_display())
            """
            if not self.player.menu_option:
                self.map.update()

            else:
                self.option.update()
            self.screen.update()
    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.keylistener.add_key(event.key)
            elif event.type == pygame.KEYUP:
                self.keylistener.remove_key(event.key)

    """
    def load_objective_images(self):
        # Charger les images des objectifs
        objective1_image = pygame.image.load("../../assets/Images/image_objectif.png").convert_alpha()
        # Ajouter les images chargées à la liste des images des objectifs
        self.objective_images = [objective1_image, ]

    def display_objectives(self):
        # Dessiner les images des objectifs à l'écran
        for i, objective_image in enumerate(self.objective_images):
            x = 20  # Coordonnée x de l'image de l'objectif
            y = 20 + i * 50  # Coordonnée y de l'image de l'objectif
            self.screen.blit(objective_image, (x, y))
    """



