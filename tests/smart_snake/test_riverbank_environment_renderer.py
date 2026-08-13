from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.config.game_settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from python_arcade.games.smart_snake.ui.riverbank_environment_renderer import (
    RiverbankEnvironmentRenderer,
)
from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_AREA_01,
)


# Resumo: prepara o Pygame para testar o renderer sem abrir uma janela real.
# Parâmetros: monkeypatch permite configurar temporariamente o driver de vídeo.
# Retorno: ambiente do Pygame disponível durante os testes.
@pytest.fixture
def pygame_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> Generator[None, None, None]:
    monkeypatch.setenv("SDL_VIDEODRIVER", "dummy")

    pygame.init()
    pygame.display.set_mode((1, 1))

    try:
        yield
    finally:
        pygame.quit()


# Resumo: valida se o background da Riverbank é dimensionado para a tela do jogo.
# Parâmetros: pygame_environment garante que o Pygame esteja inicializado.
# Retorno: nenhum.
def test_riverbank_environment_renderer_matches_screen_size(
    pygame_environment: None,
) -> None:
    renderer = RiverbankEnvironmentRenderer(
    background_asset_name=RIVERBANK_AREA_01.background_asset_name,
)

    assert renderer.background_surface.get_size() == (
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
    )