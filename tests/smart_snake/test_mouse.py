from python_arcade.games.smart_snake.domain.mouse import (
    Mouse,
    MouseDirection,
    MouseRouteState,
)


# Resumo: valida se o rato armazena corretamente sua posição inicial.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_stores_initial_position() -> None:
    mouse = Mouse(
        position_x=320.0,
        position_y=240.0,
        home_position_y=240.0,
        direction=MouseDirection.DOWN,
    )

    assert mouse.position_x == 320.0
    assert mouse.position_y == 240.0


# Resumo: valida se o rato armazena sua orientação vertical.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_stores_vertical_direction() -> None:
    mouse = Mouse(
        position_x=320.0,
        position_y=240.0,
        home_position_y=240.0,
        direction=MouseDirection.UP,
    )

    assert mouse.direction == MouseDirection.UP


# Resumo: valida se o rato inicia sua trajetória afastando-se do arbusto.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_starts_route_moving_away_from_bush() -> None:
    mouse = Mouse(
        position_x=320.0,
        position_y=240.0,
        home_position_y=240.0,
        direction=MouseDirection.DOWN,
    )

    assert mouse.route_state == MouseRouteState.MOVING_AWAY_FROM_BUSH

# Resumo: valida se o rato mantém registrada a posição vertical de seu arbusto.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_stores_home_position() -> None:
    mouse = Mouse(
        position_x=320.0,
        position_y=240.0,
        home_position_y=240.0,
        direction=MouseDirection.DOWN,
    )

    mouse.position_y = 500.0

    assert mouse.home_position_y == 240.0