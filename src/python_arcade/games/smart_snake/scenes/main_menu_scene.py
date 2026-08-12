from collections.abc import Callable

import pygame

from python_arcade.games.smart_snake.scenes.base_scene import BaseScene


BACKGROUND_COLOR = (22, 54, 34)
TITLE_COLOR = (255, 255, 255)
INSTRUCTION_COLOR = (190, 220, 190)


# Representa o menu principal da Smart Snake.
class MainMenuScene(BaseScene):

    # Inicializa os elementos visuais e a ação de início do jogo.
    def __init__(self, on_start_game: Callable[[], None]) -> None:
        self.title_font = pygame.font.Font(None, 72)
        self.instruction_font = pygame.font.Font(None, 36)
        self.on_start_game = on_start_game

    # Processa os comandos recebidos durante o menu principal.
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        for game_event in events:
            if (
                game_event.type == pygame.KEYDOWN
                and game_event.key == pygame.K_RETURN
            ):
                self.on_start_game()

    # Atualiza o estado do menu principal.
    def update(self, delta_time: float) -> None:
        return

    # Renderiza os elementos visuais do menu principal.
    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BACKGROUND_COLOR)

        title_surface = self.title_font.render(
            "SMART SNAKE",
            True,
            TITLE_COLOR,
        )

        instruction_surface = self.instruction_font.render(
            "PRESS ENTER TO START",
            True,
            INSTRUCTION_COLOR,
        )

        screen_center_x = screen.get_rect().centerx
        screen_center_y = screen.get_rect().centery

        title_position = title_surface.get_rect(
            center=(screen_center_x, screen_center_y - 40)
        )

        instruction_position = instruction_surface.get_rect(
            center=(screen_center_x, screen_center_y + 40)
        )

        screen.blit(title_surface, title_position)
        screen.blit(instruction_surface, instruction_position)