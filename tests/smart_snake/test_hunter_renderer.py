from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.domain.hunter import (
    HunterDirection,
    HunterState,
)
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


# Resumo: garante que cada direção selecione o conjunto visual esperado.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_get_sprite_surface_uses_expected_direction_frames() -> None:
    hunter_renderer = HunterRenderer.__new__(HunterRenderer)

    idle_sprite_surface = object()
    walk_left_sprite_surfaces = (
        object(),
        object(),
    )
    walk_right_sprite_surfaces = (
        object(),
        object(),
    )
    back_sprite_surfaces = (
        object(),
        object(),
    )

    hunter_renderer.idle_sprite_surface = idle_sprite_surface
    hunter_renderer.walk_left_sprite_surfaces = (
        walk_left_sprite_surfaces
    )
    hunter_renderer.walk_right_sprite_surfaces = (
        walk_right_sprite_surfaces
    )
    hunter_renderer.back_sprite_surfaces = back_sprite_surfaces

    assert (
        hunter_renderer.get_sprite_surface(
            direction=HunterDirection.UP,
            frame_index=1,
        )
        is back_sprite_surfaces[1]
    )

    assert (
        hunter_renderer.get_sprite_surface(
            direction=HunterDirection.DOWN,
            frame_index=0,
        )
        is walk_left_sprite_surfaces[0]
    )

    assert (
        hunter_renderer.get_sprite_surface(
            direction=HunterDirection.LEFT,
            frame_index=1,
        )
        is walk_left_sprite_surfaces[1]
    )

    assert (
        hunter_renderer.get_sprite_surface(
            direction=HunterDirection.RIGHT,
            frame_index=0,
        )
        is walk_right_sprite_surfaces[0]
    )

    assert (
        hunter_renderer.get_sprite_surface(
            direction=None,
            frame_index=0,
        )
        is idle_sprite_surface
    )


# Resumo: garante que o estado de ataque tenha prioridade sobre a direção.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_get_sprite_surface_uses_attack_frames_when_attacking() -> None:
    hunter_renderer = HunterRenderer.__new__(HunterRenderer)

    hunter_renderer.idle_sprite_surface = object()
    hunter_renderer.walk_left_sprite_surfaces = (
        object(),
        object(),
    )
    hunter_renderer.walk_right_sprite_surfaces = (
        object(),
        object(),
    )
    hunter_renderer.back_sprite_surfaces = (
        object(),
        object(),
    )

    attack_sprite_surfaces = (
        object(),
        object(),
    )
    hunter_renderer.attack_sprite_surfaces = attack_sprite_surfaces

    selected_sprite_surface = hunter_renderer.get_sprite_surface(
        direction=HunterDirection.UP,
        frame_index=1,
        state=HunterState.ATTACKING,
    )

    assert selected_sprite_surface is attack_sprite_surfaces[1]

# Resumo: garante que um Hunter derrotado utilize o sprite parado.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_get_sprite_surface_uses_idle_sprite_when_defeated() -> None:
    hunter_renderer = HunterRenderer.__new__(HunterRenderer)

    idle_sprite_surface = object()

    hunter_renderer.idle_sprite_surface = idle_sprite_surface
    hunter_renderer.walk_left_sprite_surfaces = (
        object(),
        object(),
    )
    hunter_renderer.walk_right_sprite_surfaces = (
        object(),
        object(),
    )
    hunter_renderer.back_sprite_surfaces = (
        object(),
        object(),
    )
    hunter_renderer.attack_sprite_surfaces = (
        object(),
        object(),
    )

    selected_sprite_surface = hunter_renderer.get_sprite_surface(
        direction=HunterDirection.UP,
        frame_index=1,
        state=HunterState.DEFEATED,
    )

    assert selected_sprite_surface is idle_sprite_surface