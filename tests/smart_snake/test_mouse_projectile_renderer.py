from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.ui.mouse_projectile_renderer import (
    MouseProjectileRenderer,
)


# Resumo: prepara o Pygame para os testes do renderer sem abrir uma janela real.
# Parâmetros: monkeypatch permite configurar temporariamente o driver de vídeo.
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


# Resumo: valida se a direção para cima utiliza o sprite traseiro do rato.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_mouse_projectile_renderer_uses_up_sprite() -> None:
    renderer = MouseProjectileRenderer()

    selected_sprite = renderer.get_sprite_surface(
        direction_x=0.0,
        direction_y=-1.0,
    )

    assert selected_sprite is renderer.up_sprite_surface


# Resumo: valida se a direção para baixo utiliza o sprite frontal do rato.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_mouse_projectile_renderer_uses_down_sprite() -> None:
    renderer = MouseProjectileRenderer()

    selected_sprite = renderer.get_sprite_surface(
        direction_x=0.0,
        direction_y=1.0,
    )

    assert selected_sprite is renderer.down_sprite_surface


# Resumo: valida se a direção para esquerda utiliza o sprite horizontal correspondente.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_mouse_projectile_renderer_uses_left_sprite() -> None:
    renderer = MouseProjectileRenderer()

    selected_sprite = renderer.get_sprite_surface(
        direction_x=-1.0,
        direction_y=0.0,
    )

    assert selected_sprite is renderer.left_sprite_surface


# Resumo: valida se a direção para direita utiliza o sprite horizontal correspondente.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_mouse_projectile_renderer_uses_right_sprite() -> None:
    renderer = MouseProjectileRenderer()

    selected_sprite = renderer.get_sprite_surface(
        direction_x=1.0,
        direction_y=0.0,
    )

    assert selected_sprite is renderer.right_sprite_surface