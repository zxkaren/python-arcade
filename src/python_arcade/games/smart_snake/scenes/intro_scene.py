from collections.abc import Callable

import pygame

from python_arcade.games.smart_snake.scenes.base_scene import BaseScene


# Representa a cena inicial da aventura da Smart Snake.
class IntroScene(BaseScene):

    # Inicializa os recursos visuais básicos e a ação de continuação.
    def __init__(self, on_continue: Callable[[], None]) -> None:
        self.background_color = (0, 0, 0)
        self.title_font = pygame.font.Font(None, 72)
        self.on_continue = on_continue

    # Processa os comandos recebidos durante a introdução.
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        for game_event in events:
            if (
                game_event.type == pygame.KEYDOWN
                and game_event.key == pygame.K_RETURN
            ):
                self.on_continue()

    # Atualiza o estado da cena de introdução.
    def update(self, delta_time: float) -> None:
        return

    # Renderiza a primeira apresentação visual da Smart Snake.
    def render(self, screen: pygame.Surface) -> None:
        screen.fill(self.background_color)

        title_surface = self.title_font.render(
            "SMART SNAKE",
            True,
            (255, 255, 255),
        )

        title_position = title_surface.get_rect(
            center=screen.get_rect().center
        )

        screen.blit(title_surface, title_position)