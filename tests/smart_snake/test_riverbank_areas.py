from python_arcade.games.smart_snake.config.game_settings import SCREEN_WIDTH
from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_AREA_01,
    RIVERBANK_INITIAL_AREA_ID,
    RIVERBANK_ROAD_MAXIMUM_Y,
    RIVERBANK_ROAD_MINIMUM_Y,
    RIVERBANK_STAGE_AREAS,
    RIVERBANK_WALKABLE_AREA,
)
from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_AREA_01,
    RIVERBANK_SCENERY_OBJECTS,
)


# Resumo: valida a configuração da primeira e única área da Riverbank.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_riverbank_area_configuration() -> None:
    assert RIVERBANK_AREA_01.area_id == "riverbank_area_01"
    assert RIVERBANK_AREA_01.background_asset_name == "riverbank_background.png"
    assert RIVERBANK_AREA_01.player_spawn_x == 65.0
    assert RIVERBANK_AREA_01.player_spawn_y == 490.0
    assert RIVERBANK_AREA_01.walkable_area == RIVERBANK_WALKABLE_AREA

    assert RIVERBANK_STAGE_AREAS == [
        RIVERBANK_AREA_01,
    ]

    assert RIVERBANK_INITIAL_AREA_ID == "riverbank_area_01"


# Resumo: valida os limites caminháveis configurados para a estrada da Riverbank.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_riverbank_walkable_area_configuration() -> None:
    assert len(RIVERBANK_WALKABLE_AREA.regions) == 1

    road_region = RIVERBANK_WALKABLE_AREA.regions[0]

    assert road_region.minimum_x == 0.0
    assert road_region.maximum_x == float(SCREEN_WIDTH)
    assert road_region.minimum_y == RIVERBANK_ROAD_MINIMUM_Y
    assert road_region.maximum_y == RIVERBANK_ROAD_MAXIMUM_Y

# Resumo: valida se a primeira área da Riverbank possui sua coleção de objetos.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_riverbank_area_01_stores_scenery_objects() -> None:
    assert RIVERBANK_AREA_01.scenery_objects == RIVERBANK_SCENERY_OBJECTS
    assert len(RIVERBANK_AREA_01.scenery_objects) == 9

    bush_objects = tuple(
        scenery_object
        for scenery_object in RIVERBANK_AREA_01.scenery_objects
        if scenery_object.asset_name == "bush_01.png"
    )

    rock_objects = tuple(
        scenery_object
        for scenery_object in RIVERBANK_AREA_01.scenery_objects
        if scenery_object.asset_name == "rock_01.png"
    )

    tree_objects = tuple(
        scenery_object
        for scenery_object in RIVERBANK_AREA_01.scenery_objects
        if scenery_object.asset_name == "tree_02.png"
    )

    assert len(bush_objects) == 6
    assert len(rock_objects) == 1
    assert len(tree_objects) == 2

    assert all(
        bush.render_width == 110
        for bush in bush_objects
    )

    assert rock_objects[0].render_width == 170

    assert all(
        tree.render_width == 180
        for tree in tree_objects
    )

# Resumo: valida quais objetos da Riverbank bloqueiam a movimentação da Smart Snake.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_riverbank_area_01_configures_movement_blocking_objects() -> None:
    bush_objects = tuple(
        scenery_object
        for scenery_object in RIVERBANK_AREA_01.scenery_objects
        if scenery_object.asset_name == "bush_01.png"
    )

    rock_objects = tuple(
        scenery_object
        for scenery_object in RIVERBANK_AREA_01.scenery_objects
        if scenery_object.asset_name == "rock_01.png"
    )

    tree_objects = tuple(
        scenery_object
        for scenery_object in RIVERBANK_AREA_01.scenery_objects
        if scenery_object.asset_name == "tree_02.png"
    )

    assert all(
        bush.blocks_movement is False
        for bush in bush_objects
    )

    assert all(
        rock.blocks_movement is True
        for rock in rock_objects
    )

    assert all(
        tree.blocks_movement is True
        for tree in tree_objects
    )

# Resumo: valida se os obstáculos da Riverbank possuem áreas de colisão configuradas.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_riverbank_area_01_configures_collision_boxes_for_obstacles() -> None:
    blocking_objects = tuple(
        scenery_object
        for scenery_object in RIVERBANK_AREA_01.scenery_objects
        if scenery_object.blocks_movement
    )

    non_blocking_objects = tuple(
        scenery_object
        for scenery_object in RIVERBANK_AREA_01.scenery_objects
        if not scenery_object.blocks_movement
    )

    assert len(blocking_objects) == 3

    assert all(
        scenery_object.collision_box is not None
        for scenery_object in blocking_objects
    )

    assert all(
        scenery_object.collision_box is None
        for scenery_object in non_blocking_objects
    )