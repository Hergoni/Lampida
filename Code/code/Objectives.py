import pygame
pygame.init()
pygame.font.init()
class Objectifs:
    def __init__(self, objectives: list[str], font_size: int = 20, font_color: tuple[int, int, int] = (255, 255, 255), font_path: str = None) -> None:
        self.objectives = objectives
        self.font_size = font_size
        self.font_color = font_color
        self.font_path = font_path
        self.font = None
        self.load_font()

    def load_font(self) -> None:
        if self.font_path:
            self.font = pygame.font.Font(self.font_path, self.font_size)
        else:
            self.font = pygame.font.SysFont("Arial", self.font_size)

    def display_objectives(self, screen: pygame.Surface) -> None:
        y_offset = 20
        for objective in self.objectives:
            text_surface = self.font.render(objective, True, self.font_color)
            text_rect = text_surface.get_rect(topright=(screen.get_width() - 20, y_offset))
            screen.blit(text_surface, text_rect)
            y_offset += self.font_size + 5
