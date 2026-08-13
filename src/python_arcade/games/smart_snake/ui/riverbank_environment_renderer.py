from pathlib import Path

import pygame

from python_arcade.games.smart_snake.config.game_settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


RIVERBANK_ASSETS_DIRECTORY = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "environments"
    / "riverbank"
)

RIVERBANK_BACKGROUND_PATH = (
    RIVERBANK_ASSETS_DIRECTORY
    / "riverbank_background.png"
)


# Responsável pela representação visual do cenário Riverbank.
class RiverbankEnvironmentRenderer:

    # Resumo: carrega e dimensiona o background da Riverbank preservando sua proporção.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        original_background_surface = pygame.image.load(
            RIVERBANK_BACKGROUND_PATH
        ).convert()

        self.background_surface = self.resize_background_to_screen(
            original_background_surface
        )

    # Resumo: redimensiona o background para preencher a tela sem deformar a imagem.
    # Parâmetros: background_surface representa a imagem original do cenário.
    # Retorno: superfície dimensionada e recortada no tamanho da tela.
    def resize_background_to_screen(
        self,
        background_surface: pygame.Surface,
    ) -> pygame.Surface:
        original_width, original_height = background_surface.get_size()

        scale_ratio = SCREEN_WIDTH / original_width

        scaled_width = SCREEN_WIDTH
        scaled_height = round(original_height * scale_ratio)

        scaled_background_surface = pygame.transform.scale(
            background_surface,
            (scaled_width, scaled_height),
        )

        vertical_crop_position = max(
            0,
            (scaled_height - SCREEN_HEIGHT) // 2,
        )

        background_rectangle = pygame.Rect(
            0,
            vertical_crop_position,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
        )

        cropped_background_surface = scaled_background_surface.subsurface(
            background_rectangle
        ).copy()

        return cropped_background_surface

    # Resumo: renderiza o background da Riverbank ocupando toda a tela.
    # Parâmetros: screen representa a superfície principal do jogo.
    # Retorno: nenhum.
    def render_background(
        self,
        screen: pygame.Surface,
    ) -> None:
        screen.blit(
            self.background_surface,
            (0, 0),
        )