from pathlib import Path

import pygame

from python_arcade.games.smart_snake.domain.hunter import HunterDirection


HUNTER_ASSETS_DIRECTORY = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "characters"
    / "hunter"
)

HUNTER_IDLE_SPRITE_PATH = HUNTER_ASSETS_DIRECTORY / "hunter.png"

HUNTER_WALK_SPRITE_PATHS = (
    HUNTER_ASSETS_DIRECTORY / "hunter_walk0.png",
    HUNTER_ASSETS_DIRECTORY / "hunter_walk1.png",
)

HUNTER_BACK_SPRITE_PATHS = (
    HUNTER_ASSETS_DIRECTORY / "hunter_back0.png",
    HUNTER_ASSETS_DIRECTORY / "hunter_back1.png",
)

HUNTER_RENDER_WIDTH = 400
HUNTER_BACK_RENDER_WIDTH = 310


# Responsável pela representação visual do Hunter comum durante o gameplay.
class HunterRenderer:

    # Resumo: carrega e prepara os sprites disponíveis para o Hunter.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        self.idle_sprite_surface = self.load_and_scale_sprite(
            sprite_path=HUNTER_IDLE_SPRITE_PATH,
        )

        self.walk_left_sprite_surfaces = tuple(
            self.load_and_scale_sprite(sprite_path=sprite_path)
            for sprite_path in HUNTER_WALK_SPRITE_PATHS
        )

        self.walk_right_sprite_surfaces = tuple(
            pygame.transform.flip(
                sprite_surface,
                True,
                False,
            )
            for sprite_surface in self.walk_left_sprite_surfaces
        )

        self.back_sprite_surfaces = tuple(
            self.load_and_scale_sprite(
                sprite_path=sprite_path,
                render_width=HUNTER_BACK_RENDER_WIDTH,
            )
            for sprite_path in HUNTER_BACK_SPRITE_PATHS
        )

    # Resumo: carrega e redimensiona o sprite do Hunter preservando sua proporção.
    # Parâmetros: sprite_path representa o caminho da imagem e render_width sua largura final.
    # Retorno: sprite dimensionado para o gameplay.
    def load_and_scale_sprite(
        self,
        sprite_path: Path,
        render_width: int = HUNTER_RENDER_WIDTH,
    ) -> pygame.Surface:
        original_sprite_surface = pygame.image.load(
            sprite_path
        ).convert_alpha()

        original_width, original_height = (
            original_sprite_surface.get_size()
        )

        scale_ratio = render_width / original_width
        render_height = int(original_height * scale_ratio)

        return pygame.transform.scale(
            original_sprite_surface,
            (render_width, render_height),
        )

    # Resumo: seleciona o sprite correspondente à direção e ao frame atual.
    # Parâmetros: direction representa a direção e frame_index o frame da animação.
    # Retorno: superfície correspondente ao estado visual do Hunter.
    def get_sprite_surface(
        self,
        direction: HunterDirection | None,
        frame_index: int,
    ) -> pygame.Surface:
        if direction is None:
            return self.idle_sprite_surface

        if direction == HunterDirection.UP:
            sprite_surfaces = self.back_sprite_surfaces
        elif direction == HunterDirection.RIGHT:
            sprite_surfaces = self.walk_right_sprite_surfaces
        else:
            sprite_surfaces = self.walk_left_sprite_surfaces

        normalized_frame_index = frame_index % len(sprite_surfaces)

        return sprite_surfaces[normalized_frame_index]

    # Resumo: desenha o Hunter utilizando direção, posição e frame atual.
    # Parâmetros: screen, posição, direção e índice do frame da animação.
    # Retorno: nenhum.
    def render(
        self,
        screen: pygame.Surface,
        position_x: float,
        position_y: float,
        direction: HunterDirection | None = None,
        frame_index: int = 0,
    ) -> None:
        sprite_surface = self.get_sprite_surface(
            direction=direction,
            frame_index=frame_index,
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