from pathlib import Path

import pygame

from python_arcade.games.smart_snake.ui.player_hud_renderer import (
    HEALTH_BAR_POSITION_X,
    HEALTH_BAR_POSITION_Y,
)


HEART_SPRITE_PATH = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "ui"
    / "heart.png"
)

HEART_RENDER_SIZE = 20
HEART_SPACING = 4
HEART_MARGIN_FROM_HEALTH_BAR = 4

HEART_POSITION_X = HEALTH_BAR_POSITION_X
HEART_POSITION_Y = (
    HEALTH_BAR_POSITION_Y
    - HEART_RENDER_SIZE
    - HEART_MARGIN_FROM_HEALTH_BAR
)


class PlayerLivesRenderer:

    # Resumo: inicializa o sprite utilizado para representar as vidas do jogador.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        self.heart_surface = self.load_heart_sprite()

    # Resumo: carrega e redimensiona a arte do coração para utilização no HUD.
    # Parâmetros: nenhum.
    # Retorno: superfície do coração dimensionada para o HUD.
    def load_heart_sprite(self) -> pygame.Surface:
        original_heart_surface = pygame.image.load(
            HEART_SPRITE_PATH,
        )

        return pygame.transform.scale(
            original_heart_surface,
            (
                HEART_RENDER_SIZE,
                HEART_RENDER_SIZE,
            ),
        )

    # Resumo: calcula a posição horizontal de um coração conforme seu índice.
    # Parâmetros: heart_index representa a posição do coração na sequência.
    # Retorno: coordenada horizontal calculada.
    def calculate_heart_position_x(
        self,
        heart_index: int,
    ) -> int:
        return (
            HEART_POSITION_X
            + heart_index
            * (
                HEART_RENDER_SIZE
                + HEART_SPACING
            )
        )

    # Resumo: renderiza um coração para cada vida atual do jogador.
    # Parâmetros: screen recebe os desenhos e lives representa a quantidade de vidas.
    # Retorno: nenhum.
    def render(
        self,
        screen: pygame.Surface,
        lives: int,
    ) -> None:
        for heart_index in range(lives):
            screen.blit(
                self.heart_surface,
                (
                    self.calculate_heart_position_x(
                        heart_index=heart_index,
                    ),
                    HEART_POSITION_Y,
                ),
            )