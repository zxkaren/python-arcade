from collections import defaultdict
from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.config.game_settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    SMART_SNAKE_ANIMATION_FRAME_DURATION,
    RiverbankScene,
)

# Resumo: prepara uma RiverbankScene utilizável nos testes sem abrir uma janela real.
# Parâmetros: monkeypatch permite configurar o driver de vídeo temporariamente.
# Retorno: instância da RiverbankScene pronta para os testes.
@pytest.fixture
def riverbank_scene(
    monkeypatch: pytest.MonkeyPatch,
) -> Generator[RiverbankScene, None, None]:
    monkeypatch.setenv("SDL_VIDEODRIVER", "dummy")

    pygame.init()
    pygame.display.set_mode((1, 1))

    scene = RiverbankScene()

    try:
        yield scene
    finally:
        pygame.quit()


# Resumo: valida se a RiverbankScene integra teclado e movimentação da Smart Snake.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula o teclado.
# Retorno: nenhum.
def test_riverbank_scene_updates_smart_snake_movement(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_d] = True

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    initial_position_x = riverbank_scene.smart_snake.position_x
    initial_position_y = riverbank_scene.smart_snake.position_y

    riverbank_scene.update(delta_time=0.5)

    assert riverbank_scene.smart_snake.position_x == initial_position_x + 125
    assert riverbank_scene.smart_snake.position_y == initial_position_y


# Resumo: valida se a Smart Snake permanece dentro do limite esquerdo.
# Parâmetros: riverbank_scene fornece a cena testada.
# Retorno: nenhum.
def test_riverbank_scene_constrains_left_boundary(
    riverbank_scene: RiverbankScene,
) -> None:
    sprite_width, _ = riverbank_scene.smart_snake_renderer.get_sprite_size()

    riverbank_scene.smart_snake.position_x = -1000
    riverbank_scene.constrain_smart_snake_to_screen()

    assert riverbank_scene.smart_snake.position_x == sprite_width / 2


# Resumo: valida se a Smart Snake permanece dentro do limite direito.
# Parâmetros: riverbank_scene fornece a cena testada.
# Retorno: nenhum.
def test_riverbank_scene_constrains_right_boundary(
    riverbank_scene: RiverbankScene,
) -> None:
    sprite_width, _ = riverbank_scene.smart_snake_renderer.get_sprite_size()

    riverbank_scene.smart_snake.position_x = SCREEN_WIDTH + 1000
    riverbank_scene.constrain_smart_snake_to_screen()

    expected_position_x = SCREEN_WIDTH - (sprite_width / 2)

    assert riverbank_scene.smart_snake.position_x == expected_position_x


# Resumo: valida se a Smart Snake permanece dentro do limite superior.
# Parâmetros: riverbank_scene fornece a cena testada.
# Retorno: nenhum.
def test_riverbank_scene_constrains_top_boundary(
    riverbank_scene: RiverbankScene,
) -> None:
    _, sprite_height = riverbank_scene.smart_snake_renderer.get_sprite_size()

    riverbank_scene.smart_snake.position_y = -1000
    riverbank_scene.constrain_smart_snake_to_screen()

    assert riverbank_scene.smart_snake.position_y == sprite_height / 2


# Resumo: valida se a Smart Snake permanece dentro do limite inferior.
# Parâmetros: riverbank_scene fornece a cena testada.
# Retorno: nenhum.
def test_riverbank_scene_constrains_bottom_boundary(
    riverbank_scene: RiverbankScene,
) -> None:
    _, sprite_height = riverbank_scene.smart_snake_renderer.get_sprite_size()

    riverbank_scene.smart_snake.position_y = SCREEN_HEIGHT + 1000
    riverbank_scene.constrain_smart_snake_to_screen()

    expected_position_y = SCREEN_HEIGHT - (sprite_height / 2)

    assert riverbank_scene.smart_snake.position_y == expected_position_y

# Resumo: valida se o update aplica o limite da tela após movimentar a Smart Snake.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula o teclado.
# Retorno: nenhum.
def test_riverbank_scene_constrains_movement_during_update(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sprite_width, _ = riverbank_scene.smart_snake_renderer.get_sprite_size()

    maximum_position_x = SCREEN_WIDTH - (sprite_width / 2)

    riverbank_scene.smart_snake.position_x = maximum_position_x - 1

    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_d] = True

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(delta_time=0.5)

    assert riverbank_scene.smart_snake.position_x == maximum_position_x

# Resumo: valida se a animação avança enquanto a Smart Snake está em movimento.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula o teclado.
# Retorno: nenhum.
def test_riverbank_scene_advances_animation_while_moving(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_d] = True

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(
        delta_time=SMART_SNAKE_ANIMATION_FRAME_DURATION,
    )

    assert riverbank_scene.current_animation_frame_index == 1


# Resumo: valida se a animação retorna ao primeiro frame quando o movimento termina.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula o teclado.
# Retorno: nenhum.
def test_riverbank_scene_resets_animation_when_stopped(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    moving_keys = defaultdict(bool)
    moving_keys[pygame.K_d] = True

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: moving_keys,
    )

    riverbank_scene.update(
        delta_time=SMART_SNAKE_ANIMATION_FRAME_DURATION,
    )

    stopped_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: stopped_keys,
    )

    riverbank_scene.update(delta_time=0.01)

    assert riverbank_scene.current_animation_frame_index == 0