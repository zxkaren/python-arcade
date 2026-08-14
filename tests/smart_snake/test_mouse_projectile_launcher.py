from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake
from python_arcade.games.smart_snake.services.mouse_projectile_launcher import (
    MouseProjectileLauncher,
)


# Resumo: valida se um rato armazenado é convertido em projétil.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_launcher_creates_projectile() -> None:
    smart_snake = SmartSnake(
        position_x=300.0,
        position_y=450.0,
        movement_speed=250.0,
        last_direction_x=1.0,
        last_direction_y=0.0,
    )
    player_state = PlayerState(
        stored_mice=2,
    )
    projectile_launcher = MouseProjectileLauncher()

    mouse_projectile = projectile_launcher.launch(
        smart_snake=smart_snake,
        player_state=player_state,
    )

    assert mouse_projectile is not None
    assert mouse_projectile.position_x == 300.0
    assert mouse_projectile.position_y == 450.0
    assert mouse_projectile.direction_x == 1.0
    assert mouse_projectile.direction_y == 0.0
    assert player_state.stored_mice == 1


# Resumo: valida se nenhum projétil é criado quando não há ratos armazenados.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_launcher_does_not_launch_without_ammunition() -> None:
    smart_snake = SmartSnake(
        position_x=300.0,
        position_y=450.0,
        movement_speed=250.0,
        last_direction_x=-1.0,
        last_direction_y=0.0,
    )
    player_state = PlayerState(
        stored_mice=0,
    )
    projectile_launcher = MouseProjectileLauncher()

    mouse_projectile = projectile_launcher.launch(
        smart_snake=smart_snake,
        player_state=player_state,
    )

    assert mouse_projectile is None
    assert player_state.stored_mice == 0


# Resumo: valida se um rato não é consumido quando ainda não existe direção de lançamento.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_launcher_does_not_consume_mouse_without_direction() -> None:
    smart_snake = SmartSnake(
        position_x=300.0,
        position_y=450.0,
        movement_speed=250.0,
    )
    player_state = PlayerState(
        stored_mice=2,
    )
    projectile_launcher = MouseProjectileLauncher()

    mouse_projectile = projectile_launcher.launch(
        smart_snake=smart_snake,
        player_state=player_state,
    )

    assert mouse_projectile is None
    assert player_state.stored_mice == 2