import pytest

from python_arcade.games.smart_snake.world.walkable_area import (
    WalkableArea,
    WalkableRegion,
)
from python_arcade.games.smart_snake.world.walkable_area_constraint import (
    WalkableAreaConstraint,
)


# Resumo: cria uma área caminhável retangular reutilizável nos testes.
# Parâmetros: nenhum.
# Retorno: WalkableArea configurada para os cenários de teste.
def create_test_walkable_area() -> WalkableArea:
    return WalkableArea(
        regions=(
            WalkableRegion(
                minimum_x=0.0,
                maximum_x=1280.0,
                minimum_y=400.0,
                maximum_y=650.0,
            ),
        ),
    )


# Resumo: valida se uma posição válida permanece inalterada.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_walkable_area_constraint_preserves_valid_position() -> None:
    constraint = WalkableAreaConstraint()

    position_x, position_y = constraint.constrain_position(
        position_x=500.0,
        position_y=500.0,
        sprite_width=100.0,
        sprite_height=80.0,
        walkable_area=create_test_walkable_area(),
    )

    assert position_x == 500.0
    assert position_y == 500.0


# Resumo: valida se o sprite não ultrapassa o limite superior da região.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_walkable_area_constraint_constrains_top_boundary() -> None:
    constraint = WalkableAreaConstraint()

    position_x, position_y = constraint.constrain_position(
        position_x=500.0,
        position_y=100.0,
        sprite_width=100.0,
        sprite_height=80.0,
        walkable_area=create_test_walkable_area(),
    )

    assert position_x == 500.0
    assert position_y == 440.0


# Resumo: valida se o sprite não ultrapassa o limite inferior da região.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_walkable_area_constraint_constrains_bottom_boundary() -> None:
    constraint = WalkableAreaConstraint()

    position_x, position_y = constraint.constrain_position(
        position_x=500.0,
        position_y=700.0,
        sprite_width=100.0,
        sprite_height=80.0,
        walkable_area=create_test_walkable_area(),
    )

    assert position_x == 500.0
    assert position_y == 610.0


# Resumo: valida se a região mais próxima é utilizada quando existem múltiplas opções.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_walkable_area_constraint_uses_nearest_region() -> None:
    walkable_area = WalkableArea(
        regions=(
            WalkableRegion(
                minimum_x=0.0,
                maximum_x=400.0,
                minimum_y=400.0,
                maximum_y=650.0,
            ),
            WalkableRegion(
                minimum_x=600.0,
                maximum_x=1000.0,
                minimum_y=400.0,
                maximum_y=650.0,
            ),
        ),
    )

    constraint = WalkableAreaConstraint()

    position_x, position_y = constraint.constrain_position(
        position_x=580.0,
        position_y=500.0,
        sprite_width=100.0,
        sprite_height=80.0,
        walkable_area=walkable_area,
    )

    assert position_x == 650.0
    assert position_y == 500.0


# Resumo: valida se uma área incapaz de comportar o sprite é rejeitada.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_walkable_area_constraint_rejects_region_smaller_than_sprite() -> None:
    walkable_area = WalkableArea(
        regions=(
            WalkableRegion(
                minimum_x=0.0,
                maximum_x=50.0,
                minimum_y=0.0,
                maximum_y=50.0,
            ),
        ),
    )

    constraint = WalkableAreaConstraint()

    with pytest.raises(
        ValueError,
        match="Walkable area does not contain a region large enough",
    ):
        constraint.constrain_position(
            position_x=25.0,
            position_y=25.0,
            sprite_width=100.0,
            sprite_height=80.0,
            walkable_area=walkable_area,
        )