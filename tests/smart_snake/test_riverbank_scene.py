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
from python_arcade.games.smart_snake.content.smart_snake_collision import (
    SMART_SNAKE_COLLISION_BOX,
)
from python_arcade.games.smart_snake.domain.mouse import MouseDirection
from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)
from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    MOUSE_PROJECTILE_CLEANUP_MARGIN,
    MOUSE_PROJECTILE_MOVEMENT_SPEED,
    SMART_SNAKE_ANIMATION_FRAME_DURATION,
    RiverbankScene,
)
from python_arcade.games.smart_snake.domain.player_life_event import (
    PlayerLifeEvent,
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


# Resumo: valida se a RiverbankScene renderiza todos os ratos com seus estados atuais.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch intercepta o renderer.
# Retorno: nenhum.
def test_riverbank_scene_renders_mice(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered_mouse_states = []

    def capture_mouse_render(
        screen: pygame.Surface,
        position_x: float,
        position_y: float,
        direction: MouseDirection,
    ) -> None:
        rendered_mouse_states.append(
            (
                position_x,
                position_y,
                direction,
            )
        )

    monkeypatch.setattr(
        riverbank_scene.mouse_renderer,
        "render",
        capture_mouse_render,
    )

    screen = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    riverbank_scene.render(screen)

    expected_mouse_states = [
        (
            mouse.position_x,
            mouse.position_y,
            mouse.direction,
        )
        for mouse in riverbank_scene.mice
    ]

    assert rendered_mouse_states == expected_mouse_states


# Resumo: valida se a RiverbankScene movimenta verticalmente um rato superior.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de teclas pressionadas.
# Retorno: nenhum.
def test_riverbank_scene_updates_mouse_position(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mouse = next(
        mouse
        for mouse in riverbank_scene.mice
        if mouse.direction == MouseDirection.DOWN
    )

    initial_position_x = mouse.position_x
    initial_position_y = mouse.position_y

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(delta_time=1.0)

    assert mouse.position_x == initial_position_x
    assert mouse.position_y == initial_position_y + 100.0
    assert mouse.direction == MouseDirection.DOWN


# Resumo: valida se a RiverbankScene cria ratos utilizando os arbustos da área ativa.
# Parâmetros: riverbank_scene fornece a cena inicializada.
# Retorno: nenhum.
def test_riverbank_scene_creates_mice_from_bushes(
    riverbank_scene: RiverbankScene,
) -> None:
    active_area = riverbank_scene.stage_area_manager.get_active_area()

    bush_positions = [
        (
            scenery_object.position_x,
            scenery_object.position_y,
        )
        for scenery_object in active_area.scenery_objects
        if scenery_object.asset_name == "bush_01.png"
    ]

    mouse_positions = [
        (
            mouse.position_x,
            mouse.position_y,
        )
        for mouse in riverbank_scene.mice
    ]

    assert isinstance(riverbank_scene.mice, list)
    assert mouse_positions == bush_positions


# Resumo: valida se a RiverbankScene remove um rato consumido pela Smart Snake.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento.
# Retorno: nenhum.
def test_riverbank_scene_consumes_colliding_mouse(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mouse = riverbank_scene.mice[0]

    riverbank_scene.smart_snake.position_x = mouse.position_x
    riverbank_scene.smart_snake.position_y = mouse.position_y

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    initial_mouse_count = len(riverbank_scene.mice)
    initial_stored_mice = riverbank_scene.player_state.stored_mice

    riverbank_scene.update(delta_time=0.0)

    assert mouse not in riverbank_scene.mice
    assert len(riverbank_scene.mice) == initial_mouse_count - 1
    assert (
        riverbank_scene.player_state.stored_mice
        == initial_stored_mice + 1
    )


# Resumo: valida se um rato consumido recupera a vida da Smart Snake quando ela está ferida.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento.
# Retorno: nenhum.
def test_riverbank_scene_restores_health_when_injured_snake_consumes_mouse(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mouse = riverbank_scene.mice[0]

    riverbank_scene.smart_snake.position_x = mouse.position_x
    riverbank_scene.smart_snake.position_y = mouse.position_y

    riverbank_scene.player_state.current_health = 50

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(delta_time=0.0)

    assert mouse not in riverbank_scene.mice
    assert riverbank_scene.player_state.current_health == 75
    assert riverbank_scene.player_state.stored_mice == 0


# Resumo: valida se a RiverbankScene renderiza a barra de vida com o estado atual.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch intercepta o renderer do HUD.
# Retorno: nenhum.
def test_riverbank_scene_renders_player_health_bar(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered_current_health = None
    rendered_maximum_health = None

    def capture_health_bar_render(
        screen: pygame.Surface,
        current_health: int,
        maximum_health: int,
    ) -> None:
        nonlocal rendered_current_health
        nonlocal rendered_maximum_health

        rendered_current_health = current_health
        rendered_maximum_health = maximum_health

    monkeypatch.setattr(
        riverbank_scene.player_hud_renderer,
        "render_health_bar",
        capture_health_bar_render,
    )

    screen = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    riverbank_scene.render(screen)

    assert rendered_current_health == riverbank_scene.player_state.current_health
    assert rendered_maximum_health == riverbank_scene.player_state.maximum_health


# Resumo: valida se a RiverbankScene renderiza o estoque visual de ratos.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch intercepta o renderer do HUD.
# Retorno: nenhum.
def test_riverbank_scene_renders_mouse_inventory(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered_stored_mice = None

    def capture_mouse_inventory_render(
        screen: pygame.Surface,
        stored_mice: int,
    ) -> None:
        nonlocal rendered_stored_mice

        rendered_stored_mice = stored_mice

    monkeypatch.setattr(
        riverbank_scene.player_hud_renderer,
        "render_mouse_inventory",
        capture_mouse_inventory_render,
    )

    screen = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    riverbank_scene.render(screen)

    assert (
        rendered_stored_mice
        == riverbank_scene.player_state.stored_mice
    )


# Resumo: valida se a RiverbankScene inicializa o sistema de projéteis sem disparos ativos.
# Parâmetros: riverbank_scene fornece a cena inicializada.
# Retorno: nenhum.
def test_riverbank_scene_initializes_mouse_projectile_controller(
    riverbank_scene: RiverbankScene,
) -> None:
    assert (
        riverbank_scene.mouse_projectile_controller.active_projectiles
        == []
    )


# Resumo: valida se SPACE lança um rato armazenado na última direção da Smart Snake.
# Parâmetros: riverbank_scene fornece a cena inicializada.
# Retorno: nenhum.
def test_riverbank_scene_launches_mouse_projectile_with_space(
    riverbank_scene: RiverbankScene,
) -> None:
    riverbank_scene.player_state.stored_mice = 2

    riverbank_scene.smart_snake.last_direction_x = 1.0
    riverbank_scene.smart_snake.last_direction_y = 0.0

    space_key_event = pygame.event.Event(
        pygame.KEYDOWN,
        key=pygame.K_SPACE,
    )

    riverbank_scene.handle_events(
        events=[space_key_event],
    )

    active_projectiles = (
        riverbank_scene.mouse_projectile_controller.active_projectiles
    )

    assert len(active_projectiles) == 1
    assert riverbank_scene.player_state.stored_mice == 1

    launched_projectile = active_projectiles[0]

    assert (
        launched_projectile.position_x
        == riverbank_scene.smart_snake.position_x
    )
    assert (
        launched_projectile.position_y
        == riverbank_scene.smart_snake.position_y
    )
    assert launched_projectile.direction_x == 1.0
    assert launched_projectile.direction_y == 0.0


# Resumo: valida se outras teclas não lançam ratos armazenados.
# Parâmetros: riverbank_scene fornece a cena inicializada.
# Retorno: nenhum.
def test_riverbank_scene_does_not_launch_projectile_with_other_key(
    riverbank_scene: RiverbankScene,
) -> None:
    riverbank_scene.player_state.stored_mice = 2

    riverbank_scene.smart_snake.last_direction_x = 1.0
    riverbank_scene.smart_snake.last_direction_y = 0.0

    other_key_event = pygame.event.Event(
        pygame.KEYDOWN,
        key=pygame.K_RETURN,
    )

    riverbank_scene.handle_events(
        events=[other_key_event],
    )

    assert (
        riverbank_scene.mouse_projectile_controller.active_projectiles
        == []
    )
    assert riverbank_scene.player_state.stored_mice == 2


# Resumo: valida se os projéteis ativos são movimentados durante o update da cena.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento do jogador.
# Retorno: nenhum.
def test_riverbank_scene_updates_mouse_projectiles(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    riverbank_scene.player_state.stored_mice = 1
    riverbank_scene.smart_snake.last_direction_x = 1.0
    riverbank_scene.smart_snake.last_direction_y = 0.0

    space_key_event = pygame.event.Event(
        pygame.KEYDOWN,
        key=pygame.K_SPACE,
    )

    riverbank_scene.handle_events(
        events=[space_key_event],
    )

    mouse_projectile = (
        riverbank_scene.mouse_projectile_controller.active_projectiles[0]
    )
    initial_position_x = mouse_projectile.position_x
    initial_position_y = mouse_projectile.position_y

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    delta_time = 0.5

    riverbank_scene.update(
        delta_time=delta_time,
    )

    expected_position_x = (
        initial_position_x
        + MOUSE_PROJECTILE_MOVEMENT_SPEED * delta_time
    )

    assert mouse_projectile.position_x == expected_position_x
    assert mouse_projectile.position_y == initial_position_y


# Resumo: valida se a RiverbankScene renderiza todos os projéteis ativos.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch intercepta o renderer.
# Retorno: nenhum.
def test_riverbank_scene_renders_active_mouse_projectiles(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mouse_projectile = MouseProjectile(
        position_x=320.0,
        position_y=480.0,
        direction_x=1.0,
        direction_y=0.0,
    )

    riverbank_scene.mouse_projectile_controller.active_projectiles.append(
        mouse_projectile
    )

    rendered_projectiles: list[
        tuple[float, float, float, float]
    ] = []

    def capture_projectile_render(
        screen: pygame.Surface,
        position_x: float,
        position_y: float,
        direction_x: float,
        direction_y: float,
    ) -> None:
        rendered_projectiles.append(
            (
                position_x,
                position_y,
                direction_x,
                direction_y,
            )
        )

    monkeypatch.setattr(
        riverbank_scene.mouse_projectile_renderer,
        "render",
        capture_projectile_render,
    )

    screen = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    riverbank_scene.render(
        screen=screen,
    )

    assert rendered_projectiles == [
        (
            320.0,
            480.0,
            1.0,
            0.0,
        )
    ]


# Resumo: valida se projéteis são removidos somente após ultrapassarem a margem da tela.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento do jogador.
# Retorno: nenhum.
def test_riverbank_scene_removes_projectile_after_leaving_screen(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    projectile_still_leaving_screen = MouseProjectile(
        position_x=SCREEN_WIDTH + 20.0,
        position_y=500.0,
        direction_x=0.0,
        direction_y=0.0,
    )
    projectile_completely_outside_screen = MouseProjectile(
        position_x=(
            SCREEN_WIDTH
            + MOUSE_PROJECTILE_CLEANUP_MARGIN
            + 1.0
        ),
        position_y=500.0,
        direction_x=0.0,
        direction_y=0.0,
    )

    riverbank_scene.mouse_projectile_controller.active_projectiles.extend(
        [
            projectile_still_leaving_screen,
            projectile_completely_outside_screen,
        ]
    )

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert (
        riverbank_scene.mouse_projectile_controller.active_projectiles
        == [projectile_still_leaving_screen]
    )

# Resumo: valida se consumir um rato adiciona sua pontuação ao jogador.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento.
# Retorno: nenhum.
def test_riverbank_scene_adds_score_when_mouse_is_consumed(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mouse = riverbank_scene.mice[0]

    riverbank_scene.smart_snake.position_x = mouse.position_x
    riverbank_scene.smart_snake.position_y = mouse.position_y

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    initial_score = riverbank_scene.player_state.score

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert mouse not in riverbank_scene.mice
    assert riverbank_scene.player_state.score == initial_score + 50

# Resumo: valida se a RiverbankScene renderiza a pontuação atual do jogador.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch intercepta o renderer do score.
# Retorno: nenhum.
def test_riverbank_scene_renders_player_score(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered_score = None

    def capture_score_render(
        screen: pygame.Surface,
        score: int,
    ) -> None:
        nonlocal rendered_score
        rendered_score = score

    monkeypatch.setattr(
        riverbank_scene.player_score_renderer,
        "render",
        capture_score_render,
    )

    riverbank_scene.player_state.score = 150

    screen = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    riverbank_scene.render(
        screen=screen,
    )

    assert rendered_score == 150

# Resumo: valida se alcançar 3000 pontos ao consumir um rato concede uma vida extra.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento.
# Retorno: nenhum.
def test_riverbank_scene_grants_extra_life_at_score_milestone(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mouse = riverbank_scene.mice[0]

    riverbank_scene.smart_snake.position_x = mouse.position_x
    riverbank_scene.smart_snake.position_y = mouse.position_y

    riverbank_scene.player_state.score = 2950

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert riverbank_scene.player_state.score == 3000
    assert riverbank_scene.player_state.lives == 4
    assert riverbank_scene.extra_lives_granted_this_update == 1


# Resumo: valida se o gatilho de vida extra permanece ativo somente no update da concessão.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento.
# Retorno: nenhum.
def test_riverbank_scene_resets_extra_life_trigger_on_next_update(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mouse = riverbank_scene.mice[0]

    riverbank_scene.smart_snake.position_x = mouse.position_x
    riverbank_scene.smart_snake.position_y = mouse.position_y
    riverbank_scene.player_state.score = 2950

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert riverbank_scene.extra_lives_granted_this_update == 1

    riverbank_scene.smart_snake.position_x = 0.0
    riverbank_scene.smart_snake.position_y = 500.0

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert riverbank_scene.extra_lives_granted_this_update == 0

# Resumo: valida se a RiverbankScene renderiza a quantidade atual de vidas.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch intercepta o renderer das vidas.
# Retorno: nenhum.
def test_riverbank_scene_renders_player_lives(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered_lives = None

    def capture_lives_render(
        screen: pygame.Surface,
        lives: int,
    ) -> None:
        nonlocal rendered_lives
        rendered_lives = lives

    monkeypatch.setattr(
        riverbank_scene.player_lives_renderer,
        "render",
        capture_lives_render,
    )

    riverbank_scene.player_state.lives = 4

    screen = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    riverbank_scene.render(
        screen=screen,
    )

    assert rendered_lives == 4

# Resumo: valida se HP zerado produz o gatilho de perda de vida durante o update.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento.
# Retorno: nenhum.
def test_riverbank_scene_sets_life_lost_event_when_health_is_depleted(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    riverbank_scene.player_state.current_health = 0
    riverbank_scene.smart_snake.position_x = 0.0
    riverbank_scene.smart_snake.position_y = 500.0

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert (
        riverbank_scene.player_life_event_this_update
        == PlayerLifeEvent.LIFE_LOST
    )
    assert riverbank_scene.player_state.lives == 2
    assert (
        riverbank_scene.player_state.current_health
        == riverbank_scene.player_state.maximum_health
    )

# Resumo: valida se o gatilho de perda de vida é limpo no update seguinte.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento.
# Retorno: nenhum.
def test_riverbank_scene_resets_life_event_on_next_update(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    riverbank_scene.player_state.current_health = 0
    riverbank_scene.smart_snake.position_x = 0.0
    riverbank_scene.smart_snake.position_y = 500.0

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert (
        riverbank_scene.player_life_event_this_update
        == PlayerLifeEvent.LIFE_LOST
    )

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert (
        riverbank_scene.player_life_event_this_update
        == PlayerLifeEvent.NONE
    )

# Resumo: valida se perder a última vida produz o gatilho de Game Over.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento.
# Retorno: nenhum.
def test_riverbank_scene_sets_game_over_event_after_last_life(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    riverbank_scene.player_state.current_health = 0
    riverbank_scene.player_state.lives = 1

    riverbank_scene.smart_snake.position_x = 0.0
    riverbank_scene.smart_snake.position_y = 500.0

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert (
        riverbank_scene.player_life_event_this_update
        == PlayerLifeEvent.GAME_OVER
    )
    assert riverbank_scene.player_state.lives == 0
    assert riverbank_scene.player_state.current_health == 0
    assert riverbank_scene.is_game_over is True

# Resumo: valida se o gatilho de Game Over ocorre apenas no update da derrota final.
# Parâmetros: riverbank_scene fornece a cena e monkeypatch simula ausência de movimento.
# Retorno: nenhum.
def test_riverbank_scene_does_not_repeat_game_over_event(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    riverbank_scene.player_state.current_health = 0
    riverbank_scene.player_state.lives = 1

    riverbank_scene.smart_snake.position_x = 0.0
    riverbank_scene.smart_snake.position_y = 500.0

    pressed_keys = defaultdict(bool)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: pressed_keys,
    )

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert (
        riverbank_scene.player_life_event_this_update
        == PlayerLifeEvent.GAME_OVER
    )

    riverbank_scene.update(
        delta_time=0.0,
    )

    assert (
        riverbank_scene.player_life_event_this_update
        == PlayerLifeEvent.NONE
    )
    assert riverbank_scene.player_state.lives == 0
    assert riverbank_scene.is_game_over is True

def test_riverbank_scene_renders_hunters(
    riverbank_scene: RiverbankScene,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered_hunters = []

    def capture_hunter_render(
        screen: pygame.Surface,
        position_x: float,
        position_y: float,
        direction,
        frame_index: int,
    ) -> None:
        rendered_hunters.append(
            (
                position_x,
                position_y,
                direction,
                frame_index,
            )
        )

    monkeypatch.setattr(
        riverbank_scene.hunter_renderer,
        "render",
        capture_hunter_render,
    )

    screen = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    riverbank_scene.render(
        screen=screen,
    )

    active_area = riverbank_scene.stage_area_manager.get_active_area()

    expected_rendered_hunters = [
        (
            hunter.position_x,
            hunter.position_y,
            hunter.direction,
            riverbank_scene.hunter_animation_frame_indices.get(
                hunter.hunter_id,
                0,
            ),
        )
        for hunter in active_area.hunters
    ]

    assert rendered_hunters == expected_rendered_hunters