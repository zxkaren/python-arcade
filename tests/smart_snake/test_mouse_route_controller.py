from python_arcade.games.smart_snake.controllers.mouse_movement_controller import (
    MouseMovementController,
)
from python_arcade.games.smart_snake.controllers.mouse_route_controller import (
    MouseRouteController,
)
from python_arcade.games.smart_snake.domain.mouse import (
    Mouse,
    MouseDirection,
    MouseRouteState,
)


# Resumo: cria o controller de rota utilizado nos testes.
# Parâmetros: nenhum.
# Retorno: controller configurado com o movimento do rato.
def create_mouse_route_controller() -> MouseRouteController:
    movement_controller = MouseMovementController()

    return MouseRouteController(
        movement_controller=movement_controller,
    )


# Resumo: valida se um rato superior se afasta do arbusto movimentando-se para baixo.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_route_moves_down_from_upper_bush() -> None:
    mouse = Mouse(
        position_x=300.0,
        position_y=400.0,
        home_position_y=400.0,
        direction=MouseDirection.DOWN,
    )

    route_controller = create_mouse_route_controller()

    route_controller.update(
        mouse=mouse,
        away_target_y=650.0,
        movement_speed=100.0,
        delta_time=1.0,
    )

    assert mouse.position_x == 300.0
    assert mouse.position_y == 500.0
    assert mouse.direction == MouseDirection.DOWN
    assert mouse.route_state == MouseRouteState.MOVING_AWAY_FROM_BUSH


# Resumo: valida se o rato superior inicia o retorno ao alcançar o limite inferior.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_route_turns_up_at_lower_boundary() -> None:
    mouse = Mouse(
        position_x=300.0,
        position_y=620.0,
        home_position_y=400.0,
        direction=MouseDirection.DOWN,
    )

    route_controller = create_mouse_route_controller()

    route_controller.update(
        mouse=mouse,
        away_target_y=650.0,
        movement_speed=100.0,
        delta_time=1.0,
    )

    assert mouse.position_y == 650.0
    assert mouse.direction == MouseDirection.UP
    assert mouse.route_state == MouseRouteState.RETURNING_TO_BUSH


# Resumo: valida se o rato reinicia o ciclo ao retornar ao arbusto superior.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_route_restarts_at_upper_bush() -> None:
    mouse = Mouse(
        position_x=300.0,
        position_y=450.0,
        home_position_y=400.0,
        direction=MouseDirection.UP,
        route_state=MouseRouteState.RETURNING_TO_BUSH,
    )

    route_controller = create_mouse_route_controller()

    route_controller.update(
        mouse=mouse,
        away_target_y=650.0,
        movement_speed=100.0,
        delta_time=1.0,
    )

    assert mouse.position_y == 400.0
    assert mouse.direction == MouseDirection.DOWN
    assert mouse.route_state == MouseRouteState.MOVING_AWAY_FROM_BUSH


# Resumo: valida se um rato inferior se afasta do arbusto movimentando-se para cima.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_route_moves_up_from_lower_bush() -> None:
    mouse = Mouse(
        position_x=900.0,
        position_y=620.0,
        home_position_y=620.0,
        direction=MouseDirection.UP,
    )

    route_controller = create_mouse_route_controller()

    route_controller.update(
        mouse=mouse,
        away_target_y=370.0,
        movement_speed=100.0,
        delta_time=1.0,
    )

    assert mouse.position_x == 900.0
    assert mouse.position_y == 520.0
    assert mouse.direction == MouseDirection.UP
    assert mouse.route_state == MouseRouteState.MOVING_AWAY_FROM_BUSH


# Resumo: valida se o rato inferior inicia o retorno ao alcançar o limite superior.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_route_turns_down_at_upper_boundary() -> None:
    mouse = Mouse(
        position_x=900.0,
        position_y=420.0,
        home_position_y=620.0,
        direction=MouseDirection.UP,
    )

    route_controller = create_mouse_route_controller()

    route_controller.update(
        mouse=mouse,
        away_target_y=370.0,
        movement_speed=100.0,
        delta_time=1.0,
    )

    assert mouse.position_y == 370.0
    assert mouse.direction == MouseDirection.DOWN
    assert mouse.route_state == MouseRouteState.RETURNING_TO_BUSH