import pygame

class Tool:
    @staticmethod
    def split_image(spritesheet: pygame.Surface, x: int, y: int, width: int, height: int) -> pygame.Surface:
        # Méthode pour découper une image à partir d'une spritesheet
        return spritesheet.subsurface(pygame.Rect(x, y, width, height))

    @staticmethod
    def blur(background, param):
        # Méthode pour appliquer un effet de flou à une image
        for i in range(param):
            background = pygame.transform.smoothscale(background, (background.get_width() // 2, background.get_height() // 2))
            background = pygame.transform.smoothscale(background, (background.get_width() * 2, background.get_height() * 2))
        return background
