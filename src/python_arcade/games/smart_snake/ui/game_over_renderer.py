from pathlib import Path

import pygame

from python_arcade.games.smart_snake.config.game_settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


GAME_OVER_IMAGE_PATH = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "ui"
    / "game_over.png"
)


# Renderiza a tela visual de Game Over da Smart Snake.
class GameOverRenderer:

    # Resumo: carrega e dimensiona a arte de Game Over para preencher toda a tela.
    def __init__(self) -> None:
        self.game_over_surface = self.load_game_over_image()

    # Resumo: carrega a arte e ajusta seu tamanho para as dimensões do jogo.
    # Retorno: superfície de Game Over pronta para ocupar toda a tela.
    def load_game_over_image(self) -> pygame.Surface:
        original_surface = pygame.image.load(
            GAME_OVER_IMAGE_PATH,
        )

        return pygame.transform.scale(
            original_surface,
            (
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
            ),
        )

    # Resumo: renderiza a arte de Game Over cobrindo toda a superfície do jogo.
    # Parâmetros: screen representa a superfície principal do jogo.
    def render(
        self,
        screen: pygame.Surface,
    ) -> None:
        screen.blit(
            self.game_over_surface,
            (0, 0),
        )