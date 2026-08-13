from pathlib import Path

import pygame

SMART_SNAKE_SPRITE_PATH = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "characters"
    / "smart_snake"
    / "smart_snake_walk0.png"
)

SMART_SNAKE_RENDER_WIDTH = 180

# Responsável pela representação visual da Smart Snake durante o gameplay.
class SmartSnakeRenderer:

    # Inicializa e dimensiona o sprite preservando sua proporção original.
    def __init__(self) -> None:
        original_sprite_surface = pygame.image.load(
            SMART_SNAKE_SPRITE_PATH
        ).convert_alpha()

        original_width, original_height = original_sprite_surface.get_size()

        scale_ratio = SMART_SNAKE_RENDER_WIDTH / original_width
        render_height = int(original_height * scale_ratio)

        self.sprite_surface = pygame.transform.scale(
            original_sprite_surface,
            (SMART_SNAKE_RENDER_WIDTH, render_height),
        )

    # Resumo: desenha a Smart Snake utilizando sua posição como centro do sprite.
    # Parâmetros: screen representa a superfície do jogo; position_x e position_y representam a posição da personagem.
    def render(
        self,
        screen: pygame.Surface,
        position_x: float,
        position_y: float,
    ) -> None:
        sprite_rectangle = self.sprite_surface.get_rect(
            center=(
                round(position_x),
                round(position_y),
            )
        )

        screen.blit(
            self.sprite_surface,
            sprite_rectangle,
        )

    # Resumo: retorna as dimensões atuais do 
    # sprite renderizado da Smart Snake.
    def get_sprite_size(self) -> tuple[int, int]:
        return self.sprite_surface.get_size()