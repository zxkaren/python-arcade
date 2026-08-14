from python_arcade.games.smart_snake.content.smart_snake_collision import (
    SMART_SNAKE_COLLISION_BOX,
)


# Resumo: valida a configuração da área de colisão da Smart Snake.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_smart_snake_collision_box_configuration() -> None:
    (
        minimum_x,
        maximum_x,
        minimum_y,
        maximum_y,
    ) = SMART_SNAKE_COLLISION_BOX.calculate_bounds(
        position_x=100.0,
        position_y=200.0,
    )

    assert minimum_x == 55.0
    assert maximum_x == 145.0
    assert minimum_y == 183.0
    assert maximum_y == 233.0