from python_arcade.games.smart_snake.world.collision_box import CollisionBox
from python_arcade.games.smart_snake.world.scenery_collision_checker import (
    SceneryCollisionChecker,
)
from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)


# Resumo: valida se uma colisão com objeto bloqueante impede a posição.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_collision_checker_identifies_blocked_position() -> None:
    scenery_collision_checker = SceneryCollisionChecker()

    snake_collision_box = CollisionBox(
        width=80.0,
        height=50.0,
    )

    blocking_object = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=150.0,
        position_y=100.0,
        blocks_movement=True,
        collision_box=CollisionBox(
            width=100.0,
            height=80.0,
        ),
    )

    is_position_blocked = scenery_collision_checker.is_position_blocked(
        collision_box=snake_collision_box,
        position_x=100.0,
        position_y=100.0,
        scenery_objects=(blocking_object,),
    )

    assert is_position_blocked is True


# Resumo: valida se objetos não bloqueantes são ignorados na verificação.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_collision_checker_ignores_non_blocking_objects() -> None:
    scenery_collision_checker = SceneryCollisionChecker()

    snake_collision_box = CollisionBox(
        width=80.0,
        height=50.0,
    )

    non_blocking_object = SceneryObject(
        object_id="bush_01_instance_01",
        asset_name="bush_01.png",
        position_x=100.0,
        position_y=100.0,
        blocks_movement=False,
        collision_box=CollisionBox(
            width=100.0,
            height=80.0,
        ),
    )

    is_position_blocked = scenery_collision_checker.is_position_blocked(
        collision_box=snake_collision_box,
        position_x=100.0,
        position_y=100.0,
        scenery_objects=(non_blocking_object,),
    )

    assert is_position_blocked is False


# Resumo: valida se objetos bloqueantes distantes não impedem a posição.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_collision_checker_allows_free_position() -> None:
    scenery_collision_checker = SceneryCollisionChecker()

    snake_collision_box = CollisionBox(
        width=80.0,
        height=50.0,
    )

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

    is_position_blocked = scenery_collision_checker.is_position_blocked(
        collision_box=snake_collision_box,
        position_x=100.0,
        position_y=100.0,
        scenery_objects=(blocking_object,),
    )

    assert is_position_blocked is False