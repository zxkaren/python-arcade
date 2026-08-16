from python_arcade.games.smart_snake.controllers.hunter_movement_controller import (
    HunterMovementController,
)
from python_arcade.games.smart_snake.domain.hunter import Hunter


# Resumo: garante que o Hunter seja movimentado conforme direção, velocidade e tempo.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_move_hunter_upward() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
    )
    movement_controller = HunterMovementController()

    movement_controller.move(
        hunter=hunter,
        direction_x=0.0,
        direction_y=-1.0,
        movement_speed=120.0,
        delta_time=0.5,
    )

    assert hunter.position_x == 1050.0
    assert hunter.position_y == 440.0