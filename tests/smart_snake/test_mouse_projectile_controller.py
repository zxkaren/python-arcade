from python_arcade.games.smart_snake.controllers.mouse_projectile_controller import (
    MouseProjectileController,
)
from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake
from python_arcade.games.smart_snake.services.mouse_projectile_launcher import (
    MouseProjectileLauncher,
)
from python_arcade.games.smart_snake.controllers.mouse_projectile_movement_controller import (
    MouseProjectileMovementController,
)
from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)


# Resumo: valida se um projétil lançado é armazenado entre os projéteis ativos.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_controller_stores_launched_projectile() -> None:
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
    projectile_controller = MouseProjectileController(
        projectile_launcher=projectile_launcher,
        movement_controller=MouseProjectileMovementController(),
    )

    mouse_projectile = projectile_controller.launch_projectile(
        smart_snake=smart_snake,
        player_state=player_state,
    )

    assert mouse_projectile is not None
    assert len(projectile_controller.active_projectiles) == 1
    assert (
        projectile_controller.active_projectiles[0]
        is mouse_projectile
    )
    assert player_state.stored_mice == 1


# Resumo: valida se um lançamento inválido não adiciona projéteis ativos.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_controller_does_not_store_invalid_projectile() -> None:
    smart_snake = SmartSnake(
        position_x=300.0,
        position_y=450.0,
        movement_speed=250.0,
        last_direction_x=1.0,
        last_direction_y=0.0,
    )
    player_state = PlayerState(
        stored_mice=0,
    )
    projectile_launcher = MouseProjectileLauncher()
    projectile_controller = MouseProjectileController(
        projectile_launcher=projectile_launcher,
        movement_controller=MouseProjectileMovementController(),
    )

    mouse_projectile = projectile_controller.launch_projectile(
        smart_snake=smart_snake,
        player_state=player_state,
    )

    assert mouse_projectile is None
    assert projectile_controller.active_projectiles == []

# Resumo: valida se todos os projéteis ativos são movimentados durante a atualização.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_controller_updates_active_projectiles() -> None:
    smart_snake = SmartSnake(
        position_x=100.0,
        position_y=200.0,
        movement_speed=250.0,
        last_direction_x=1.0,
        last_direction_y=0.0,
    )
    player_state = PlayerState(
        stored_mice=2,
    )
    projectile_controller = MouseProjectileController(
        projectile_launcher=MouseProjectileLauncher(),
        movement_controller=MouseProjectileMovementController(),
    )

    first_projectile = projectile_controller.launch_projectile(
        smart_snake=smart_snake,
        player_state=player_state,
    )

    smart_snake.last_direction_x = 0.0
    smart_snake.last_direction_y = -1.0

    second_projectile = projectile_controller.launch_projectile(
        smart_snake=smart_snake,
        player_state=player_state,
    )

    projectile_controller.update_projectiles(
        movement_speed=300.0,
        delta_time=0.5,
    )

    assert first_projectile is not None
    assert second_projectile is not None

    assert first_projectile.position_x == 250.0
    assert first_projectile.position_y == 200.0

    assert second_projectile.position_x == 100.0
    assert second_projectile.position_y == 50.0

# Resumo: valida se projéteis fora dos limites são removidos da coleção ativa.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_controller_removes_projectiles_outside_bounds() -> None:
    projectile_controller = MouseProjectileController(
        projectile_launcher=MouseProjectileLauncher(),
        movement_controller=MouseProjectileMovementController(),
    )

    projectile_inside_bounds = MouseProjectile(
        position_x=640.0,
        position_y=360.0,
        direction_x=1.0,
        direction_y=0.0,
    )
    projectile_outside_right = MouseProjectile(
        position_x=1300.0,
        position_y=360.0,
        direction_x=1.0,
        direction_y=0.0,
    )
    projectile_outside_top = MouseProjectile(
        position_x=640.0,
        position_y=-20.0,
        direction_x=0.0,
        direction_y=-1.0,
    )

    projectile_controller.active_projectiles.extend(
        [
            projectile_inside_bounds,
            projectile_outside_right,
            projectile_outside_top,
        ]
    )

    projectile_controller.remove_projectiles_outside_bounds(
        minimum_x=0.0,
        maximum_x=1280.0,
        minimum_y=0.0,
        maximum_y=720.0,
    )

    assert projectile_controller.active_projectiles == [
        projectile_inside_bounds
    ]