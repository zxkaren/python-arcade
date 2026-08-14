import pygame

from python_arcade.games.smart_snake.ui.mouse_renderer import MouseRenderer


# Responsável pela representação visual dos ratos lançados como projéteis.
class MouseProjectileRenderer:

    # Resumo: prepara os sprites utilizados nas quatro direções de lançamento.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        mouse_renderer = MouseRenderer()

        self.up_sprite_surface = mouse_renderer.up_sprite_surface
        self.down_sprite_surface = mouse_renderer.down_sprite_surface

        self.left_sprite_surface = pygame.transform.rotate(
            self.down_sprite_surface,
            -90,
        )
        self.right_sprite_surface = pygame.transform.rotate(
            self.down_sprite_surface,
            90,
        )

    # Resumo: seleciona o sprite correspondente à direção do projétil.
    # Parâmetros: direction_x e direction_y representam a direção do lançamento.
    # Retorno: sprite correspondente à direção informada.
    def get_sprite_surface(
        self,
        direction_x: float,
        direction_y: float,
    ) -> pygame.Surface:
        if direction_y < 0.0:
            return self.up_sprite_surface

        if direction_y > 0.0:
            return self.down_sprite_surface

        if direction_x < 0.0:
            return self.left_sprite_surface

        return self.right_sprite_surface

    # Resumo: desenha o rato lançado na posição e direção atuais.
    # Parâmetros: screen é a superfície; position_x, position_y e direções definem o projétil.
    # Retorno: nenhum.
    def render(
        self,
        screen: pygame.Surface,
        position_x: float,
        position_y: float,
        direction_x: float,
        direction_y: float,
    ) -> None:
        sprite_surface = self.get_sprite_surface(
            direction_x=direction_x,
            direction_y=direction_y,
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