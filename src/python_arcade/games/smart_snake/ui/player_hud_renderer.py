from pathlib import Path

import pygame


HEALTH_BAR_POSITION_X = 30
HEALTH_BAR_POSITION_Y = 30
HEALTH_BAR_WIDTH = 250
HEALTH_BAR_HEIGHT = 24
HEALTH_BAR_BORDER_WIDTH = 3

HEALTH_BAR_BACKGROUND_COLOR = (45, 45, 45)
HEALTH_BAR_FILL_COLOR = (190, 45, 45)
HEALTH_BAR_BORDER_COLOR = (230, 230, 230)

MOUSE_ICON_SPRITE_PATH = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "characters"
    / "mouse"
    / "mouse_walk1.png"
)

MOUSE_ICON_POSITION_X = HEALTH_BAR_POSITION_X -20
MOUSE_ICON_POSITION_Y = (
    HEALTH_BAR_POSITION_Y
    + HEALTH_BAR_HEIGHT
    + -5
)

MOUSE_ICON_RENDER_WIDTH = 80
MOUSE_ICON_SPACING = -35
MAX_VISIBLE_MOUSE_ICONS = 5


class PlayerHudRenderer:

    # Resumo: inicializa os recursos visuais utilizados pelo HUD.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        self.mouse_icon_surface = self.load_mouse_icon()

    # Resumo: calcula a largura preenchida da barra conforme a vida atual.
    # Parâmetros: current_health representa a vida atual e maximum_health a vida máxima.
    # Retorno: largura em pixels que deve ser preenchida na barra.
    def calculate_health_fill_width(
        self,
        current_health: int,
        maximum_health: int,
    ) -> int:
        if maximum_health <= 0:
            return 0

        health_ratio = current_health / maximum_health

        normalized_health_ratio = max(
            0.0,
            min(
                health_ratio,
                1.0,
            ),
        )

        return round(
            HEALTH_BAR_WIDTH
            * normalized_health_ratio
        )

    # Resumo: renderiza a barra de vida do jogador na interface.
    # Parâmetros: screen recebe a superfície e os valores representam a vida do jogador.
    # Retorno: nenhum.
    def render_health_bar(
        self,
        screen: pygame.Surface,
        current_health: int,
        maximum_health: int,
    ) -> None:
        background_rectangle = pygame.Rect(
            HEALTH_BAR_POSITION_X,
            HEALTH_BAR_POSITION_Y,
            HEALTH_BAR_WIDTH,
            HEALTH_BAR_HEIGHT,
        )

        pygame.draw.rect(
            screen,
            HEALTH_BAR_BACKGROUND_COLOR,
            background_rectangle,
        )

        health_fill_width = self.calculate_health_fill_width(
            current_health=current_health,
            maximum_health=maximum_health,
        )

        if health_fill_width > 0:
            health_rectangle = pygame.Rect(
                HEALTH_BAR_POSITION_X,
                HEALTH_BAR_POSITION_Y,
                health_fill_width,
                HEALTH_BAR_HEIGHT,
            )

            pygame.draw.rect(
                screen,
                HEALTH_BAR_FILL_COLOR,
                health_rectangle,
            )

        pygame.draw.rect(
            screen,
            HEALTH_BAR_BORDER_COLOR,
            background_rectangle,
            HEALTH_BAR_BORDER_WIDTH,
        )

    # Resumo: carrega e redimensiona o sprite utilizado no estoque visual de ratos.
    # Parâmetros: nenhum.
    # Retorno: superfície do rato dimensionada para utilização no HUD.
    def load_mouse_icon(self) -> pygame.Surface:
        original_mouse_surface = pygame.image.load(
            MOUSE_ICON_SPRITE_PATH,
        )

        original_width, original_height = (
            original_mouse_surface.get_size()
        )

        scale_ratio = (
            MOUSE_ICON_RENDER_WIDTH
            / original_width
        )

        render_height = round(
            original_height
            * scale_ratio
        )

        return pygame.transform.scale(
            original_mouse_surface,
            (
                MOUSE_ICON_RENDER_WIDTH,
                render_height,
            ),
        )

    # Resumo: renderiza um ícone para cada rato armazenado pelo jogador.
    # Parâmetros: screen recebe a superfície e stored_mice representa o estoque atual.
    # Retorno: nenhum.
    def render_mouse_inventory(
        self,
        screen: pygame.Surface,
        stored_mice: int,
    ) -> None:
        visible_mouse_count = min(
            stored_mice,
            MAX_VISIBLE_MOUSE_ICONS,
        )

        for mouse_index in range(
            visible_mouse_count
        ):
            position_x = (
                MOUSE_ICON_POSITION_X
                + mouse_index
                * (
                    MOUSE_ICON_RENDER_WIDTH
                    + MOUSE_ICON_SPACING
                )
            )

            screen.blit(
                self.mouse_icon_surface,
                (
                    position_x,
                    MOUSE_ICON_POSITION_Y,
                ),
            )