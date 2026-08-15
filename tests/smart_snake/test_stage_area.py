from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)
from python_arcade.games.smart_snake.world.stage_area import StageArea
from python_arcade.games.smart_snake.world.walkable_area import (
    WalkableArea,
    WalkableRegion,
)
from python_arcade.games.smart_snake.domain.hunter import Hunter


# Resumo: valida se uma StageArea preserva sua configuração completa.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_stage_area_stores_area_configuration() -> None:
    walkable_area = WalkableArea(
        regions=(
            WalkableRegion(
                minimum_x=0.0,
                maximum_x=1280.0,
                minimum_y=430.0,
                maximum_y=650.0,
            ),
        ),
    )

    stage_area = StageArea(
        area_id="riverbank_area_01",
        background_asset_name="riverbank_background.png",
        player_spawn_x=65.0,
        player_spawn_y=490.0,
        walkable_area=walkable_area,
    )

    assert stage_area.area_id == "riverbank_area_01"
    assert stage_area.background_asset_name == "riverbank_background.png"
    assert stage_area.player_spawn_x == 65.0
    assert stage_area.player_spawn_y == 490.0
    assert stage_area.walkable_area == walkable_area


# Resumo: valida se uma StageArea preserva sua coleção de objetos do cenário.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_stage_area_stores_scenery_objects() -> None:
    walkable_area = WalkableArea(
        regions=(
            WalkableRegion(
                minimum_x=0.0,
                maximum_x=1280.0,
                minimum_y=430.0,
                maximum_y=650.0,
            ),
        ),
    )

    bush = SceneryObject(
        object_id="bush_01_instance_01",
        asset_name="bush_01.png",
        position_x=250.0,
        position_y=400.0,
    )

    rock = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=700.0,
        position_y=520.0,
    )

    scenery_objects = (
        bush,
        rock,
    )

    stage_area = StageArea(
        area_id="riverbank_area_01",
        background_asset_name="riverbank_background.png",
        player_spawn_x=65.0,
        player_spawn_y=490.0,
        walkable_area=walkable_area,
        scenery_objects=scenery_objects,
    )

    assert stage_area.scenery_objects == scenery_objects

# Resumo: valida se uma StageArea preserva sua coleção de Hunters.
def test_stage_area_stores_hunters() -> None:
    walkable_area = WalkableArea(
        regions=(
            WalkableRegion(
                minimum_x=0.0,
                maximum_x=1280.0,
                minimum_y=370.0,
                maximum_y=650.0,
            ),
        ),
    )

    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
    )

    hunters = (hunter,)

    stage_area = StageArea(
        area_id="riverbank_area_01",
        background_asset_name="riverbank_background.png",
        player_spawn_x=65.0,
        player_spawn_y=490.0,
        walkable_area=walkable_area,
        hunters=hunters,
    )

    assert stage_area.hunters == hunters