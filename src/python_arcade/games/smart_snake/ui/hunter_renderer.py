from pathlib import Path

import pygame


HUNTER_ASSETS_DIRECTORY = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "characters"
    / "hunter"
)

HUNTER_IDLE_SPRITE_PATH = HUNTER_ASSETS_DIRECTORY / "hunter.png"

HUNTER_RENDER_WIDTH = 400


# Responsável pela representação visual do Hunter comum durante o gameplay.
class HunterRenderer:

    # Resumo: carrega e prepara o sprite parado do Hunter.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        self.idle_sprite_surface = self.load_and_scale_sprite(
            sprite_path=HUNTER_IDLE_SPRITE_PATH,
        )

    # Resumo: carrega e redimensiona o sprite do Hunter preservando sua proporção.
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

        scale_ratio = HUNTER_RENDER_WIDTH / original_width
        render_height = int(original_height * scale_ratio)

        return pygame.transform.scale(
            original_sprite_surface,
            (HUNTER_RENDER_WIDTH, render_height),
        )

    # Resumo: desenha o Hunter parado utilizando sua posição como centro.
    # Parâmetros: screen representa a tela e position_x e position_y representam a posição do Hunter.
    # Retorno: nenhum.
    def render(
        self,
        screen: pygame.Surface,
        position_x: float,
        position_y: float,
    ) -> None:
        sprite_rectangle = self.idle_sprite_surface.get_rect(
            center=(
                round(position_x),
                round(position_y),
            )
        )

        screen.blit(
            self.idle_sprite_surface,
            sprite_rectangle,
        )