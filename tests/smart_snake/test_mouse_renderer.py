from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.domain.mouse import MouseDirection
from python_arcade.games.smart_snake.ui.mouse_renderer import (
    MOUSE_RENDER_WIDTH,
    MouseRenderer,
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


# Resumo: valida se o sprite voltado para cima mantém a largura configurada.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_mouse_renderer_preserves_up_render_width() -> None:
    renderer = MouseRenderer()

    assert renderer.up_sprite_surface.get_width() == MOUSE_RENDER_WIDTH


# Resumo: valida se o sprite voltado para baixo mantém a largura configurada.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_mouse_renderer_preserves_down_render_width() -> None:
    renderer = MouseRenderer()

    assert renderer.down_sprite_surface.get_width() == MOUSE_RENDER_WIDTH


# Resumo: valida se o renderer utiliza o sprite voltado para cima.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_mouse_renderer_uses_up_sprite() -> None:
    renderer = MouseRenderer()

    selected_sprite = renderer.get_sprite_surface(
        direction=MouseDirection.UP,
    )

    assert selected_sprite is renderer.up_sprite_surface


# Resumo: valida se o renderer utiliza o sprite voltado para baixo.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_mouse_renderer_uses_down_sprite() -> None:
    renderer = MouseRenderer()

    selected_sprite = renderer.get_sprite_surface(
        direction=MouseDirection.DOWN,
    )

    assert selected_sprite is renderer.down_sprite_surface