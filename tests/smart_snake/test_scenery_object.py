from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)
from python_arcade.games.smart_snake.world.collision_box import CollisionBox
from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)


# Resumo: valida se um objeto de cenário mantém sua configuração de posicionamento.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_object_stores_configuration() -> None:
    scenery_object = SceneryObject(
        object_id="rock_01",
        asset_name="rock_01.png",
        position_x=320.0,
        position_y=480.0,
    )

    assert scenery_object.object_id == "rock_01"
    assert scenery_object.asset_name == "rock_01.png"
    assert scenery_object.position_x == 320.0
    assert scenery_object.position_y == 480.0


# Resumo: valida se um objeto do cenário preserva sua largura de renderização.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_object_stores_render_width() -> None:
    scenery_object = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=550.0,
        position_y=520.0,
        render_width=80,
    )

    assert scenery_object.render_width == 80


# Resumo: valida se um objeto do cenário pode bloquear a movimentação.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_object_stores_movement_blocking_configuration() -> None:
    scenery_object = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=550.0,
        position_y=520.0,
        blocks_movement=True,
    )

    assert scenery_object.blocks_movement is True


# Resumo: valida se objetos do cenário são não bloqueantes por padrão.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_object_does_not_block_movement_by_default() -> None:
    scenery_object = SceneryObject(
        object_id="bush_01_instance_01",
        asset_name="bush_01.png",
        position_x=400.0,
        position_y=500.0,
    )

    assert scenery_object.blocks_movement is False

# Resumo: valida se um objeto do cenário preserva sua área de colisão.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_object_stores_collision_box() -> None:
    collision_box = CollisionBox(
        width=80.0,
        height=40.0,
        offset_x=0.0,
        offset_y=20.0,
    )

    scenery_object = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=550.0,
        position_y=520.0,
        blocks_movement=True,
        collision_box=collision_box,
    )

    assert scenery_object.collision_box == collision_box