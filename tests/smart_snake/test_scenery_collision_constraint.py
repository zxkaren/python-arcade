from python_arcade.games.smart_snake.world.collision_box import CollisionBox
from python_arcade.games.smart_snake.world.scenery_collision_constraint import (
    SceneryCollisionConstraint,
)
from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)


# Resumo: valida se uma posição bloqueada mantém a posição anterior.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_collision_constraint_keeps_previous_position_when_blocked() -> None:
    scenery_collision_constraint = SceneryCollisionConstraint()

    blocking_object = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=200.0,
        position_y=100.0,
        blocks_movement=True,
        collision_box=CollisionBox(
            width=100.0,
            height=80.0,
        ),
    )

    constrained_position_x, constrained_position_y = (
        scenery_collision_constraint.constrain_position(
            previous_position_x=100.0,
            previous_position_y=100.0,
            target_position_x=160.0,
            target_position_y=100.0,
            collision_box=CollisionBox(
                width=80.0,
                height=50.0,
            ),
            scenery_objects=(blocking_object,),
        )
    )

    assert constrained_position_x == 100.0
    assert constrained_position_y == 100.0


# Resumo: valida se uma posição livre permite alcançar a posição alvo.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_collision_constraint_allows_free_position() -> None:
    scenery_collision_constraint = SceneryCollisionConstraint()

    blocking_object = SceneryObject(
        object_id="tree_02_instance_01",
        asset_name="tree_02.png",
        position_x=400.0,
        position_y=400.0,
        blocks_movement=True,
        collision_box=CollisionBox(
            width=70.0,
            height=60.0,
        ),
    )

    constrained_position_x, constrained_position_y = (
        scenery_collision_constraint.constrain_position(
            previous_position_x=100.0,
            previous_position_y=100.0,
            target_position_x=140.0,
            target_position_y=100.0,
            collision_box=CollisionBox(
                width=80.0,
                height=50.0,
            ),
            scenery_objects=(blocking_object,),
        )
    )

    assert constrained_position_x == 140.0
    assert constrained_position_y == 100.0