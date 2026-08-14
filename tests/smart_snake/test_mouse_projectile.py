from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)


# Resumo: valida se o projétil armazena corretamente sua posição inicial.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_stores_initial_position() -> None:
    mouse_projectile = MouseProjectile(
        position_x=320.0,
        position_y=480.0,
        direction_x=1.0,
        direction_y=0.0,
    )

    assert mouse_projectile.position_x == 320.0
    assert mouse_projectile.position_y == 480.0


# Resumo: valida se o projétil armazena corretamente sua direção de lançamento.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_projectile_stores_launch_direction() -> None:
    mouse_projectile = MouseProjectile(
        position_x=320.0,
        position_y=480.0,
        direction_x=-1.0,
        direction_y=0.0,
    )

    assert mouse_projectile.direction_x == -1.0
    assert mouse_projectile.direction_y == 0.0