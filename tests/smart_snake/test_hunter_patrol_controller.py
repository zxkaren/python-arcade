from python_arcade.games.smart_snake.controllers.hunter_movement_controller import (
    HunterMovementController,
)
from python_arcade.games.smart_snake.controllers.hunter_patrol_controller import (
    HunterPatrolController,
)
from python_arcade.games.smart_snake.controllers.hunter_route_controller import (
    HunterRouteController,
)
from python_arcade.games.smart_snake.domain.hunter import (
    Hunter,
    HunterDirection,
)
from python_arcade.games.smart_snake.world.hunter_patrol import (
    HunterPatrol,
    HunterPatrolAxis,
)


# Resumo: garante que o controlador execute uma patrulha vertical configurada.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_update_vertical_hunter_patrol() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=430.0,
        direction=HunterDirection.UP,
    )

    hunter_patrol = HunterPatrol(
        hunter_id="hunter_01",
        axis=HunterPatrolAxis.VERTICAL,
        minimum_position=420.0,
        maximum_position=610.0,
        movement_speed=120.0,
    )

    movement_controller = HunterMovementController()
    route_controller = HunterRouteController(
        movement_controller=movement_controller,
    )
    patrol_controller = HunterPatrolController(
        route_controller=route_controller,
    )

    patrol_controller.update(
        hunters=(hunter,),
        hunter_patrols=(hunter_patrol,),
        delta_time=0.1,
    )

    assert hunter.position_x == 1050.0
    assert hunter.position_y == 420.0
    assert hunter.direction == HunterDirection.DOWN