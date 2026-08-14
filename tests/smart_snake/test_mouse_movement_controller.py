from python_arcade.games.smart_snake.controllers.mouse_movement_controller import (
    MouseMovementController,
)
from python_arcade.games.smart_snake.domain.mouse import (
    Mouse,
    MouseDirection,
)


# Resumo: valida se o controller movimenta o rato conforme direção e velocidade.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_movement_controller_updates_mouse_position() -> None:
    mouse = Mouse(
        position_x=100.0,
        position_y=200.0,
        home_position_y=200.0,
        direction=MouseDirection.DOWN,
    )

    movement_controller = MouseMovementController()

    movement_controller.move(
        mouse=mouse,
        direction_x=1.0,
        direction_y=0.0,
        movement_speed=50.0,
        delta_time=1.0,
    )

    assert mouse.position_x == 150.0
    assert mouse.position_y == 200.0