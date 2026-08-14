from python_arcade.games.smart_snake.domain.mouse import (
    Mouse,
    MouseDirection,
)
from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake
from python_arcade.games.smart_snake.services.mouse_consumption_service import (
    MouseConsumptionService,
)


# Resumo: valida se apenas o rato em contato com a Smart Snake é consumido.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_consumption_service_consumes_only_colliding_mouse() -> None:
    smart_snake = SmartSnake(
        position_x=500.0,
        position_y=500.0,
        movement_speed=250.0,
    )

    colliding_mouse = Mouse(
        position_x=500.0,
        position_y=500.0,
        home_position_y=400.0,
        direction=MouseDirection.DOWN,
    )

    distant_mouse = Mouse(
        position_x=900.0,
        position_y=500.0,
        home_position_y=400.0,
        direction=MouseDirection.DOWN,
    )

    mice = [
        colliding_mouse,
        distant_mouse,
    ]

    mouse_consumption_service = MouseConsumptionService()

    consumed_mouse = mouse_consumption_service.consume_colliding_mouse(
        smart_snake=smart_snake,
        mice=mice,
    )

    assert consumed_mouse is colliding_mouse
    assert mice == [distant_mouse]