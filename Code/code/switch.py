import pygame

class Switch:
    def __init__(self, type: str, name: str, hitbox: pygame.Rect, port: int):
        # Initialisation des attributs du switch
        self.type: str = type
        self.name: str = name
        self.hitbox: pygame.Rect = hitbox
        self.port: port = port
        # self.events: dict = {}  # Ajout de l'attribut pour stocker les événements associés à chaque pièce

    def check_collision(self, temp_hitbox) -> bool:
        # Vérifie la collision
        return self.hitbox.colliderect(temp_hitbox)


"""
 def trigger_event(self, event_name):
     if event_name in self.events:
         # Exécutez l'événement associé si présent dans le dictionnaire des événements
         self.events[event_name]()
 """
