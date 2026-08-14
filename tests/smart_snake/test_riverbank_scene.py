from collections import defaultdict
from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.config.game_settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_AREA_01,
    RIVERBANK_ROAD_MAXIMUM_Y,
    RIVERBANK_ROAD_MINIMUM_Y,
)
from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    SMART_SNAKE_ANIMATION_FRAME_DURATION,
    RiverbankScene,
)
from python_arcade.games.smart_snake.content.smart_snake_collision import (
    SMART_SNAKE_COLLISION_BOX,
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


# Resumo: valida se a Smart Snake permanece dentro do limite esquerdo da área caminhável.
# Parâmetros: riverbank_scene fornece a cena testada.
# Retorno: nenhum.
def test_riverbank_scene_constrains_left_boundary(
    riverbank_scene: RiverbankScene,
) -> None:
    sprite_width, _ = riverbank_scene.smart_snake_renderer.get_sprite_size()

    riverbank_scene.smart_snake.position_x = -1000.0
    riverbank_scene.constrain_smart_snake_to_walkable_area()

    expected_position_x = sprite_width / 2

    assert riverbank_scene.smart_snake.position_x == expected_position_x


# Resumo: valida se a Smart Snake permanece dentro do limite direito da área caminhável.
# Parâmetros: riverbank_scene fornece a cena testada.
# Retorno: nenhum.
def test_riverbank_scene_constrains_right_boundary(
    riverbank_scene: RiverbankScene,
) -> None:
    sprite_width, _ = riverbank_scene.smart_snake_renderer.get_sprite_size()

    riverbank_scene.smart_snake.position_x = SCREEN_WIDTH + 1000.0
    riverbank_scene.constrain_smart_snake_to_walkable_area()

    expected_position_x = SCREEN_WIDTH - (sprite_width / 2)

    assert riverbank_scene.smart_snake.position_x == expected_position_x


# Resumo: valida se a Smart Snake permanece abaixo da margem superior da estrada.
# Parâmetros: riverbank_scene fornece a cena testada.
# Retorno: nenhum.
def test_riverbank_scene_constrains_road_top_boundary(
    riverbank_scene: RiverbankScene,
) -> None:
    _, sprite_height = riverbank_scene.smart_snake_renderer.get_sprite_size()

    riverbank_scene.smart_snake.position_y = 0.0
    riverbank_scene.constrain_smart_snake_to_walkable_area()

    expected_position_y = (
        RIVERBANK_ROAD_MINIMUM_Y
        + (sprite_height / 2)
    )

    assert riverbank_scene.smart_snake.position_y == expected_position_y


# Resumo: valida se a Smart Snake permanece acima da margem inferior da estrada.
# Parâmetros: riverbank_scene fornece a cena testada.
# Retorno: nenhum.
def test_riverbank_scene_constrains_road_bottom_boundary(
    riverbank_scene: RiverbankScene,
) -> None:
    _, sprite_height = riverbank_scene.smart_snake_renderer.get_sprite_size()

    riverbank_scene.smart_snake.position_y = SCREEN_HEIGHT
    riverbank_scene.constrain_smart_snake_to_walkable_area()

    expected_position_y = (
        RIVERBANK_ROAD_MAXIMUM_Y
        - (sprite_height / 2)
    )

    assert riverbank_scene.smart_snake.position_y == expected_position_y


# Resumo: valida se o update aplica os limites caminháveis após o movimento.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula o teclado.
# Retorno: nenhum.
def test_riverbank_scene_constrains_movement_during_update(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, sprite_height = riverbank_scene.smart_snake_renderer.get_sprite_size()

    minimum_position_y = (
        RIVERBANK_ROAD_MINIMUM_Y
        + (sprite_height / 2)
    )

    riverbank_scene.smart_snake.position_y = minimum_position_y + 1.0

    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_w] = True

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(delta_time=0.5)

    assert riverbank_scene.smart_snake.position_y == minimum_position_y


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


# Resumo: valida se a RiverbankScene utiliza o renderer do ambiente durante a renderização.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch intercepta a renderização do fundo.
# Retorno: nenhum.
def test_riverbank_scene_renders_environment(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    environment_was_rendered = False

    def capture_environment_render(
        screen: pygame.Surface,
    ) -> None:
        nonlocal environment_was_rendered
        environment_was_rendered = True

    monkeypatch.setattr(
        riverbank_scene.riverbank_environment_renderer,
        "render_background",
        capture_environment_render,
    )

    screen = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    riverbank_scene.render(screen)

    assert environment_was_rendered is True


# Resumo: valida se a RiverbankScene utiliza a configuração da área ativa.
# Parâmetros: riverbank_scene fornece a cena inicializada.
# Retorno: nenhum.
def test_riverbank_scene_uses_active_stage_area(
    riverbank_scene: RiverbankScene,
) -> None:
    active_area = riverbank_scene.stage_area_manager.get_active_area()

    assert active_area == RIVERBANK_AREA_01

    assert (
        riverbank_scene.smart_snake.position_x
        == active_area.player_spawn_x
    )

    assert (
        riverbank_scene.smart_snake.position_y
        == active_area.player_spawn_y
    )

# Resumo: valida se a RiverbankScene renderiza os objetos da área ativa.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch intercepta o renderer.
# Retorno: nenhum.
def test_riverbank_scene_renders_active_area_scenery_objects(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered_scenery_objects = None

    def capture_scenery_render(
        screen: pygame.Surface,
        scenery_objects,
    ) -> None:
        nonlocal rendered_scenery_objects
        rendered_scenery_objects = scenery_objects

    monkeypatch.setattr(
        riverbank_scene.scenery_renderer,
        "render",
        capture_scenery_render,
    )

    screen = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    riverbank_scene.render(screen)

    active_area = riverbank_scene.stage_area_manager.get_active_area()

    assert rendered_scenery_objects == active_area.scenery_objects

# Resumo: valida se a RiverbankScene impede movimento contra obstáculos do cenário.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula o teclado.
# Retorno: nenhum.
def test_riverbank_scene_blocks_movement_against_scenery(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    active_area = riverbank_scene.stage_area_manager.get_active_area()

    rock_object = next(
        scenery_object
        for scenery_object in active_area.scenery_objects
        if scenery_object.asset_name == "rock_01.png"
    )

    assert rock_object.collision_box is not None

    (
        rock_minimum_x,
        _,
        rock_minimum_y,
        _,
    ) = rock_object.collision_box.calculate_bounds(
        position_x=rock_object.position_x,
        position_y=rock_object.position_y,
    )

    snake_horizontal_margin = SMART_SNAKE_COLLISION_BOX.width / 2

    previous_position_x = (
        rock_minimum_x
        - SMART_SNAKE_COLLISION_BOX.offset_x
        - snake_horizontal_margin
    )
    previous_position_y = (
        rock_minimum_y
        - SMART_SNAKE_COLLISION_BOX.offset_y
    )

    riverbank_scene.smart_snake.position_x = previous_position_x
    riverbank_scene.smart_snake.position_y = previous_position_y

    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_d] = True

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(delta_time=0.04)

    assert riverbank_scene.smart_snake.position_x == previous_position_x
    assert riverbank_scene.smart_snake.position_y == previous_position_y