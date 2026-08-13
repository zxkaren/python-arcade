from pathlib import Path

import pygame

SMART_SNAKE_SPRITES_DIRECTORY = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "characters"
    / "smart_snake"
)

SMART_SNAKE_SPRITE_PATHS = (
    SMART_SNAKE_SPRITES_DIRECTORY / "smart_snake_walk0.png",
    SMART_SNAKE_SPRITES_DIRECTORY / "smart_snake_walk1.png",
)

SMART_SNAKE_RENDER_WIDTH = 180

# Responsável pela representação visual da Smart Snake durante o gameplay.
class SmartSnakeRenderer:

    # Resumo: carrega e dimensiona os frames da Smart Snake preservando suas proporções.
    def __init__(self) -> None:
        self.sprite_surfaces = [
            self.load_and_scale_sprite(sprite_path)
            for sprite_path in SMART_SNAKE_SPRITE_PATHS
        ]

    # Resumo: carrega e redimensiona um sprite preservando sua proporção original.
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

        scale_ratio = SMART_SNAKE_RENDER_WIDTH / original_width
        render_height = int(original_height * scale_ratio)

        return pygame.transform.scale(
            original_sprite_surface,
            (SMART_SNAKE_RENDER_WIDTH, render_height),
        )

    # Resumo: desenha o frame solicitado da Smart Snake usando sua posição como centro.
    def render(
        self,
        screen: pygame.Surface,
        position_x: float,
        position_y: float,
        frame_index: int = 0,
    ) -> None:
        normalized_frame_index = (
            frame_index % len(self.sprite_surfaces)
        )

        sprite_surface = self.sprite_surfaces[
            normalized_frame_index
        ]

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

    # Resumo: retorna a quantidade de frames disponíveis para a Smart Snake.
    def get_frame_count(self) -> int:
        return len(self.sprite_surfaces)

    # Resumo: retorna as maiores dimensões utilizadas pelos frames renderizados.
    def get_sprite_size(self) -> tuple[int, int]:
        maximum_width = max(
            sprite_surface.get_width()
            for sprite_surface in self.sprite_surfaces
        )

        maximum_height = max(
            sprite_surface.get_height()
            for sprite_surface in self.sprite_surfaces
        )

        return maximum_width, maximum_height