from pathlib import Path

import pygame

from python_arcade.games.smart_snake.domain.mouse import MouseDirection


MOUSE_ASSETS_DIRECTORY = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "characters"
    / "mouse"
)

MOUSE_UP_SPRITE_PATH = MOUSE_ASSETS_DIRECTORY / "mouse_walk0.png"
MOUSE_DOWN_SPRITE_PATH = MOUSE_ASSETS_DIRECTORY / "mouse_walk1.png"

MOUSE_RENDER_WIDTH = 90


# Responsável pela representação visual dos ratos durante o gameplay.
class MouseRenderer:

    # Resumo: carrega e prepara os sprites utilizados nas orientações verticais.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        self.up_sprite_surface = self.load_and_scale_sprite(
            sprite_path=MOUSE_UP_SPRITE_PATH,
        )
        self.down_sprite_surface = self.load_and_scale_sprite(
            sprite_path=MOUSE_DOWN_SPRITE_PATH,
        )

    # Resumo: carrega e redimensiona um sprite do rato preservando sua proporção original.
    # Parâmetros: sprite_path representa o caminho do arquivo de imagem.
    # Retorno: sprite dimensionado para o gameplay.
    def load_and_scale_sprite(
        self,
        sprite_path: Path,
    ) -> pygame.Surface:
        original_sprite_surface = pygame.image.load(
            sprite_path
        ).convert_alpha()

        original_width, original_height = (
            original_sprite_surface.get_size()
        )

        scale_ratio = MOUSE_RENDER_WIDTH / original_width
        render_height = int(original_height * scale_ratio)

        return pygame.transform.scale(
            original_sprite_surface,
            (MOUSE_RENDER_WIDTH, render_height),
        )

    # Resumo: seleciona o sprite correspondente à direção vertical do rato.
    # Parâmetros: direction informa se o rato está olhando para cima ou para baixo.
    # Retorno: sprite correspondente à direção solicitada.
    def get_sprite_surface(
        self,
        direction: MouseDirection,
    ) -> pygame.Surface:
        if direction == MouseDirection.UP:
            return self.up_sprite_surface

        return self.down_sprite_surface

    # Resumo: desenha o rato utilizando sua posição e direção atuais.
    # Parâmetros: screen, position_x, position_y e direction.
    # Retorno: nenhum.
    def render(
        self,
        screen: pygame.Surface,
        position_x: float,
        position_y: float,
        direction: MouseDirection,
    ) -> None:
        sprite_surface = self.get_sprite_surface(
            direction=direction,
        )

        sprite_rectangle = sprite_surface.get_rect(
            center=(
                round(position_x),
                round(position_y),
            )
        )

        screen.blit(
            sprite_surface,
            sprite_rectangle,
        )

    # Resumo: retorna as dimensões do sprite voltado para baixo utilizado no gameplay.
    # Parâmetros: nenhum.
    # Retorno: largura e altura do sprite.
    def get_sprite_size(self) -> tuple[int, int]:
        return self.down_sprite_surface.get_size()