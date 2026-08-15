from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.ui.hunter_renderer import (
    HUNTER_RENDER_WIDTH,
    HunterRenderer,
)


# Resumo: prepara o Pygame para os testes do renderer sem abrir uma janela real.
# Parâmetros: monkeypatch permite configurar temporariamente o driver de vídeo.
# Retorno: ambiente temporário do Pygame durante os testes.
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


# Resumo: valida se o sprite parado do Hunter mantém a largura configurada.
# Parâmetros: pygame_environment garante que o Pygame esteja inicializado.
# Retorno: nenhum.
def test_hunter_renderer_preserves_idle_render_width(
    pygame_environment: None,
) -> None:
    renderer = HunterRenderer()

    assert (
        renderer.idle_sprite_surface.get_width()
        == HUNTER_RENDER_WIDTH
    )
    assert renderer.idle_sprite_surface.get_height() > 0