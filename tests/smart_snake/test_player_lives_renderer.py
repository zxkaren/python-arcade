from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.ui.player_lives_renderer import (
    HEART_RENDER_SIZE,
    HEART_SPACING,
    PlayerLivesRenderer,
)


# Resumo: prepara o Pygame para os testes do renderer sem abrir uma janela real.
# Parâmetros: monkeypatch configura temporariamente o driver de vídeo.
# Retorno: ambiente temporário do Pygame durante os testes.
@pytest.fixture
def pygame_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> Generator[None, None, None]:
    monkeypatch.setenv(
        "SDL_VIDEODRIVER",
        "dummy",
    )

    pygame.init()
    pygame.display.set_mode((1, 1))

    try:
        yield
    finally:
        pygame.quit()


# Resumo: valida se o coração é redimensionado para o tamanho definido no HUD.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_player_lives_renderer_scales_heart_sprite() -> None:
    player_lives_renderer = PlayerLivesRenderer()

    assert player_lives_renderer.heart_surface.get_size() == (
        HEART_RENDER_SIZE,
        HEART_RENDER_SIZE,
    )


# Resumo: valida o espaçamento horizontal entre os corações do HUD.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_player_lives_renderer_calculates_heart_spacing() -> None:
    player_lives_renderer = PlayerLivesRenderer()

    first_heart_position_x = (
        player_lives_renderer.calculate_heart_position_x(
            heart_index=0,
        )
    )
    second_heart_position_x = (
        player_lives_renderer.calculate_heart_position_x(
            heart_index=1,
        )
    )

    assert (
        second_heart_position_x
        - first_heart_position_x
        == HEART_RENDER_SIZE + HEART_SPACING
    )