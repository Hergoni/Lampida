"""""sssssssss
 pygame

from screen import Screen  # Importe la classe Screen du module screen.py
from tool import Tool  # Importe la classe Tool du module tool.py


class Entity(pygame.sprite.Sprite):
    def __init__(self, screen: Screen, x: int, y: int):
        super().__init__()
        self.screen: Screen = screen
        self.spritesheet: pygame.image = pygame.image.load("../../assets/sprite/sprite_lucas.png")
        self.image: pygame.image = Tool.split_image(self.spritesheet, 0, 0, 24, 32)
        self.position: pygame.math.Vector2 = pygame.math.Vector2(x, y)
        self.rect: pygame.Rect = self.image.get_rect()
        self.all_images: dict[str, list[pygame.image]] = self.get_all_images(self.spritesheet)
        self.index_image: int = 0  # Indice de l'image actuelle
        self.image_part: int = 0  # Partie de l'animation de l'image actuelle
        self.reset_animation: bool = False  # Indique si l'animation doit être réinitialisée
        self.hitbox: pygame.Rect = pygame.Rect(0, 0, 16, 16)  # Boîte de collision de l'entité
        self.step: int = 0  # Étape de l'animation de l'entité
        self.animation_walk: bool = False  # Indique si l'entité est en mouvement
        self.direction: str = "down"  # Direction actuelle de l'entité
        self.animation_step_time: float = 0.0  # Temps écoulé depuis la dernière animation
        self.action_animation: int = 16  # Durée entre chaque étape de l'animation
        self.speed: int = 2  # Vitesse de déplacement de l'entité

    def update(self) -> None:
        # Met à jour l'entité à chaque itération de la boucle principale
        self.animation_sprite()  # Gère l'animation de l'entité
        self.move()  # Déplace l'entité
        self.rect.center = self.position  # Centre le rectangle autour de la position de l'entité
        self.hitbox.midbottom = self.rect.midbottom  # Ajuste la boîte de collision à la position de l'entité
        self.image = self.all_images[self.direction][self.index_image]  # Met à jour l'image affichée

    # Méthodes pour déplacer l'entité dans différentes directions
    def move_left(self) -> None:
        self.animation_walk = True
        self.direction = "left"

    def move_right(self) -> None:
        self.animation_walk = True
        self.direction = "right"

    def move_up(self) -> None:
        self.animation_walk = True
        self.direction = "up"

    def move_down(self) -> None:
        self.animation_walk = True
        self.direction = "down"

    def animation_sprite(self) -> None:
        if int(self.step // 8) + self.image_part >= 4:
            self.image_part = 0
            self.reset_animation = True
        self.index_image = int(self.step // 8) + self.image_part



    def move(self) -> None:
        # Déplace l'entité
        if self.animation_walk:
            self.animation_step_time += self.screen.get_delta_time()
            if self.step < 16 and self.animation_step_time >= self.action_animation:
                self.step += self.speed
                if self.direction == "left":
                    self.position.x -= self.speed
                elif self.direction == "right":
                    self.position.x += self.speed
                elif self.direction == "up":
                    self.position.y -= self.speed
                elif self.direction == "down":
                    self.position.y += self.speed
                self.animation_step_time = 0
            elif self.step >= 16:
                self.step = 0
                self.animation_walk = False
                if self.reset_animation:
                    self.reset_animation = False
                else:
                    if self.image_part == 0:
                        self.image_part = 2
                    else:
                        self.image_part = 0

    def align_hitbox(self) -> None:
        # Ajuste la boîte de collision pour qu'elle soit alignée avec la grille de la carte
        self.position.x += 16
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.x % 16 != 0:
            self.rect.x -= 1
            self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.y % 16 != 0:
            self.rect.y -= 1
            self.hitbox.midbottom = self.rect.midbottom
        self.position = pygame.math.Vector2(self.rect.center)

    def get_all_images(self, spritesheet) -> dict[str, list[pygame.image]]:
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": [],
        }

        width: int = spritesheet.get_width() // 3  # 3 colonnes
        height: int = spritesheet.get_height() // 4  # 4 lignes

        for j, direction in enumerate(all_images.keys()):
            for i in range(3):
                # Découpe l'image à la position correspondante dans la feuille de sprite
                image = Tool.split_image(spritesheet, i * width, j * height, width, height)
                all_images[direction].append(image)

        return all_images
"""
import pygame

from screen import Screen
from tool import Tool


class Entity(pygame.sprite.Sprite):
    def __init__(self, screen: Screen, x: int, y: int):
        super().__init__()
        self.screen: Screen = screen
        self.spritesheet: pygame.image = pygame.image.load("../../assets/sprite/hero_01_red_m_walk.png")
        self.image: pygame.image = Tool.split_image(self.spritesheet, 0, 0, 24, 32)
        self.position: pygame.math.Vector2 = pygame.math.Vector2(x, y)
        self.rect: pygame.Rect = self.image.get_rect()
        self.all_images: dict[str, list[pygame.image]] = self.get_all_images(self.spritesheet)
        self.index_image: int = 0
        self.image_part: int = 0
        self.reset_animation: bool = False
        self.hitbox: pygame.Rect = pygame.Rect(0, 0, 16, 16)

        self.step: int = 0
        self.animation_walk: bool = False
        self.direction: str = "down"

        self.animtion_step_time: float = 0.0
        self.action_animation: int = 16

        self.speed: int = 3

    def update(self) -> None:
        self.animation_sprite()
        self.move()
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        self.image = self.all_images[self.direction][self.index_image]

    def move_left(self) -> None:
        self.animation_walk = True
        self.direction = "left"

    def move_right(self) -> None:
        self.animation_walk = True
        self.direction = "right"

    def move_up(self) -> None:
        self.animation_walk = True
        self.direction = "up"

    def move_down(self) -> None:
        self.animation_walk = True
        self.direction = "down"

    def animation_sprite(self) -> None:
        if int(self.step // 8) + self.image_part >= 4:
            self.image_part = 0
            self.reset_animation = True
        self.index_image = int(self.step // 8) + self.image_part

    def move(self) -> None:
        if self.animation_walk:
            self.animtion_step_time += self.screen.get_delta_time()
            if self.step < 16 and self.animtion_step_time >= self.action_animation:
                self.step += self.speed
                if self.direction == "left":
                    self.position.x -= self.speed
                elif self.direction == "right":
                    self.position.x += self.speed
                elif self.direction == "up":
                    self.position.y -= self.speed
                elif self.direction == "down":
                    self.position.y += self.speed
                self.animtion_step_time = 0
            elif self.step >= 16:
                self.step = 0
                self.animation_walk = False
                if self.reset_animation:
                    self.reset_animation = False
                else:
                    if self.image_part == 0:
                        self.image_part = 2
                    else:
                        self.image_part = 0

    def align_hitbox(self) -> None:
        self.position.x += 16
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.x % 16 != 0:
            self.rect.x -= 1
            self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.y % 16 != 0:
            self.rect.y -= 1
            self.hitbox.midbottom = self.rect.midbottom
        self.position = pygame.math.Vector2(self.rect.center)

    def get_all_images(self, spritesheet) -> dict[str, list[pygame.image]]:
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": []
        }

        width: int = spritesheet.get_width() // 4
        height: int = spritesheet.get_height() //4
        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(spritesheet, i * width, j * height, 24, 32))
        return all_images


