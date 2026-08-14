from unittest.mock import Mock

import pygame

from python_arcade.games.smart_snake.ui.player_hud_renderer import (
    HEALTH_BAR_WIDTH,
    MAX_VISIBLE_MOUSE_ICONS,
    PlayerHudRenderer,
)

# Resumo: valida se a largura da barra representa proporcionalmente a vida atual.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_hud_renderer_calculates_health_fill_width() -> None:
    player_hud_renderer = PlayerHudRenderer()

    health_fill_width = (
        player_hud_renderer.calculate_health_fill_width(
            current_health=50,
            maximum_health=100,
        )
    )

    assert health_fill_width == HEALTH_BAR_WIDTH // 2

# Resumo: valida se o HUD limita a quantidade visual de ratos ao máximo permitido.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_hud_renderer_limits_visible_mouse_icons() -> None:
    player_hud_renderer = PlayerHudRenderer()

    screen = Mock(
        spec=pygame.Surface,
    )

    player_hud_renderer.render_mouse_inventory(
        screen=screen,
        stored_mice=8,
    )

    assert screen.blit.call_count == MAX_VISIBLE_MOUSE_ICONS