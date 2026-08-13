from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.ui.smart_snake_renderer import (
    SMART_SNAKE_RENDER_WIDTH,
    SmartSnakeRenderer,
)


# Resumo: prepara o Pygame para os testes do renderer sem abrir uma janela real.
# Parâmetros: monkeypatch permite configurar temporariamente o driver de vídeo.
# Retorno: ambiente do Pygame disponível durante a execução do teste.
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


# Resumo: valida se os dois frames de caminhada são carregados pelo renderer.
# Parâmetros: pygame_environment garante que o Pygame esteja inicializado.
# Retorno: nenhum.
def test_smart_snake_renderer_loads_walk_frames(
    pygame_environment: None,
) -> None:
    renderer = SmartSnakeRenderer()

    assert renderer.get_frame_count() == 2


# Resumo: valida se os sprites mantêm a largura configurada para o gameplay.
# Parâmetros: pygame_environment garante que o Pygame esteja inicializado.
# Retorno: nenhum.
def test_smart_snake_renderer_preserves_render_width(
    pygame_environment: None,
) -> None:
    renderer = SmartSnakeRenderer()

    sprite_width, sprite_height = renderer.get_sprite_size()

    assert sprite_width == SMART_SNAKE_RENDER_WIDTH
    assert sprite_height > 0


# Resumo: valida se os dois frames carregados possuem conteúdo visual diferente.
# Parâmetros: pygame_environment garante que o Pygame esteja inicializado.
# Retorno: nenhum.
def test_smart_snake_renderer_loads_different_frame_images(
    pygame_environment: None,
) -> None:
    renderer = SmartSnakeRenderer()

    first_frame_pixels = pygame.image.tobytes(
        renderer.sprite_surfaces[0],
        "RGBA",
    )

    second_frame_pixels = pygame.image.tobytes(
        renderer.sprite_surfaces[1],
        "RGBA",
    )

    assert first_frame_pixels != second_frame_pixels