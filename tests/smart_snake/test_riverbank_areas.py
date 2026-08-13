from python_arcade.games.smart_snake.config.game_settings import SCREEN_WIDTH
from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_AREA_01,
    RIVERBANK_INITIAL_AREA_ID,
    RIVERBANK_ROAD_MAXIMUM_Y,
    RIVERBANK_ROAD_MINIMUM_Y,
    RIVERBANK_STAGE_AREAS,
    RIVERBANK_WALKABLE_AREA,
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