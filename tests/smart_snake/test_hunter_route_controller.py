from python_arcade.games.smart_snake.controllers.hunter_movement_controller import (
    HunterMovementController,
)
from python_arcade.games.smart_snake.controllers.hunter_route_controller import (
    HunterRouteController,
)
from python_arcade.games.smart_snake.domain.hunter import (
    Hunter,
    HunterDirection,
)


# Resumo: garante que o Hunter inverta a direção ao atingir o limite superior.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_hunter_changes_direction_at_upper_patrol_limit() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=430.0,
        direction=HunterDirection.UP,
    )

    movement_controller = HunterMovementController()
    route_controller = HunterRouteController(
        movement_controller=movement_controller,
    )

    route_controller.update_vertical(
        hunter=hunter,
        minimum_position_y=420.0,
        maximum_position_y=610.0,
        movement_speed=120.0,
        delta_time=0.1,
    )

    assert hunter.position_x == 1050.0
    assert hunter.position_y == 420.0
    assert hunter.direction == HunterDirection.DOWN


# Resumo: garante que o Hunter inverta para a direita no limite esquerdo.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_hunter_changes_direction_at_left_patrol_limit() -> None:
    hunter = Hunter(
        hunter_id="hunter_02",
        position_x=710.0,
        position_y=500.0,
        direction=HunterDirection.LEFT,
    )

    movement_controller = HunterMovementController()
    route_controller = HunterRouteController(
        movement_controller=movement_controller,
    )

    route_controller.update_horizontal(
        hunter=hunter,
        minimum_position_x=700.0,
        maximum_position_x=1100.0,
        movement_speed=120.0,
        delta_time=0.1,
    )

    assert hunter.position_x == 700.0
    assert hunter.position_y == 500.0
    assert hunter.direction == HunterDirection.RIGHT


# Resumo: garante que o Hunter inverta para a esquerda no limite direito.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_hunter_changes_direction_at_right_patrol_limit() -> None:
    hunter = Hunter(
        hunter_id="hunter_02",
        position_x=1090.0,
        position_y=500.0,
        direction=HunterDirection.RIGHT,
    )

    movement_controller = HunterMovementController()
    route_controller = HunterRouteController(
        movement_controller=movement_controller,
    )

    route_controller.update_horizontal(
        hunter=hunter,
        minimum_position_x=700.0,
        maximum_position_x=1100.0,
        movement_speed=120.0,
        delta_time=0.1,
    )

    assert hunter.position_x == 1100.0
    assert hunter.position_y == 500.0
    assert hunter.direction == HunterDirection.LEFT


# Resumo: garante que o Hunter inverta para cima no limite inferior.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_hunter_changes_direction_at_lower_patrol_limit() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=600.0,
        direction=HunterDirection.DOWN,
    )

    movement_controller = HunterMovementController()
    route_controller = HunterRouteController(
        movement_controller=movement_controller,
    )

    route_controller.update_vertical(
        hunter=hunter,
        minimum_position_y=420.0,
        maximum_position_y=610.0,
        movement_speed=120.0,
        delta_time=0.1,
    )

    assert hunter.position_x == 1050.0
    assert hunter.position_y == 610.0
    assert hunter.direction == HunterDirection.UP