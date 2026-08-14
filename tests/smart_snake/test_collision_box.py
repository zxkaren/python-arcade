from python_arcade.games.smart_snake.world.collision_box import (
    CollisionBox,
)


# Resumo: valida o cálculo dos limites absolutos de uma área de colisão.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_collision_box_calculates_bounds_with_offset() -> None:
    collision_box = CollisionBox(
        width=80.0,
        height=40.0,
        offset_x=10.0,
        offset_y=20.0,
    )

    minimum_x, maximum_x, minimum_y, maximum_y = (
        collision_box.calculate_bounds(
            position_x=300.0,
            position_y=500.0,
        )
    )

    assert minimum_x == 270.0
    assert maximum_x == 350.0
    assert minimum_y == 500.0
    assert maximum_y == 540.0