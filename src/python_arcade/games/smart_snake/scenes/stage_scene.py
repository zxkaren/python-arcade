import pygame

from python_arcade.games.smart_snake.scenes.base_scene import BaseScene


BACKGROUND_COLOR = (37, 76, 45)
TITLE_COLOR = (255, 255, 255)
SUBTITLE_COLOR = (205, 225, 190)


# Representa uma fase jogável da aventura da Smart Snake.
class StageScene(BaseScene):

    # Inicializa os elementos visuais básicos da fase.
    def __init__(self, stage_number: int, stage_name: str) -> None:
        self.stage_number = stage_number
        self.stage_name = stage_name

        self.title_font = pygame.font.Font(None, 64)
        self.subtitle_font = pygame.font.Font(None, 36)

    # Processa os eventos recebidos durante a fase.
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        if not events:
            return

    # Atualiza o estado da fase.
    def update(self, delta_time: float) -> None:
        return

    # Renderiza a apresentação inicial da fase.
    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BACKGROUND_COLOR)

        stage_title = f"STAGE {self.stage_number:02d}"

        title_surface = self.title_font.render(
            stage_title,
            True,
            TITLE_COLOR,
        )

        subtitle_surface = self.subtitle_font.render(
            self.stage_name,
            True,
            SUBTITLE_COLOR,
        )

        screen_center_x = screen.get_rect().centerx
        screen_center_y = screen.get_rect().centery

        title_position = title_surface.get_rect(
            center=(screen_center_x, screen_center_y - 30)
        )

        subtitle_position = subtitle_surface.get_rect(
            center=(screen_center_x, screen_center_y + 35)
        )

        screen.blit(title_surface, title_position)
        screen.blit(subtitle_surface, subtitle_position)