from python_arcade.games.smart_snake.world.collision_box import CollisionBox
from python_arcade.games.smart_snake.world.collision_detector import (
    CollisionDetector,
)


# Resumo: valida a identificação de sobreposição entre duas áreas de colisão.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_collision_detector_identifies_overlapping_boxes() -> None:
    collision_detector = CollisionDetector()

    first_collision_box = CollisionBox(
        width=80.0,
        height=80.0,
    )

    second_collision_box = CollisionBox(
        width=100.0,
        height=100.0,
    )

    are_colliding = collision_detector.are_colliding(
        first_collision_box=first_collision_box,
        first_position_x=100.0,
        first_position_y=100.0,
        second_collision_box=second_collision_box,
        second_position_x=150.0,
        second_position_y=100.0,
    )

    assert are_colliding is True


# Resumo: valida que áreas de colisão separadas não são consideradas sobrepostas.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_collision_detector_identifies_separated_boxes() -> None:
    collision_detector = CollisionDetector()

    first_collision_box = CollisionBox(
        width=80.0,
        height=80.0,
    )

    second_collision_box = CollisionBox(
        width=100.0,
        height=100.0,
    )

    are_colliding = collision_detector.are_colliding(
        first_collision_box=first_collision_box,
        first_position_x=100.0,
        first_position_y=100.0,
        second_collision_box=second_collision_box,
        second_position_x=300.0,
        second_position_y=100.0,
    )

    assert are_colliding is False


# Resumo: valida que áreas apenas encostadas pelas bordas não estão sobrepostas.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_collision_detector_allows_boxes_to_touch_edges() -> None:
    collision_detector = CollisionDetector()

    first_collision_box = CollisionBox(
        width=100.0,
        height=100.0,
    )

    second_collision_box = CollisionBox(
        width=100.0,
        height=100.0,
    )

    are_colliding = collision_detector.are_colliding(
        first_collision_box=first_collision_box,
        first_position_x=100.0,
        first_position_y=100.0,
        second_collision_box=second_collision_box,
        second_position_x=200.0,
        second_position_y=100.0,
    )

    assert are_colliding is False