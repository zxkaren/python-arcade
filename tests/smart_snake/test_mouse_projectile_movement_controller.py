from python_arcade.games.smart_snake.controllers.mouse_projectile_movement_controller import (
    MouseProjectileMovementController,
)
from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)


# Resumo: valida o movimento horizontal do rato lançado.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_movement_controller_moves_horizontally() -> None:
    mouse_projectile = MouseProjectile(
        position_x=100.0,
        position_y=200.0,
        direction_x=1.0,
        direction_y=0.0,
    )

    movement_controller = MouseProjectileMovementController()

    movement_controller.move(
        mouse_projectile=mouse_projectile,
        movement_speed=300.0,
        delta_time=0.5,
    )

    assert mouse_projectile.position_x == 250.0
    assert mouse_projectile.position_y == 200.0


# Resumo: valida o movimento vertical do rato lançado.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_movement_controller_moves_vertically() -> None:
    mouse_projectile = MouseProjectile(
        position_x=100.0,
        position_y=200.0,
        direction_x=0.0,
        direction_y=-1.0,
    )

    movement_controller = MouseProjectileMovementController()

    movement_controller.move(
        mouse_projectile=mouse_projectile,
        movement_speed=300.0,
        delta_time=0.5,
    )

    assert mouse_projectile.position_x == 100.0
    assert mouse_projectile.position_y == 50.0