from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_AREA_01,
    RIVERBANK_INITIAL_AREA_ID,
    RIVERBANK_STAGE_AREAS,
)


# Resumo: valida a configuração da primeira e única área da Riverbank.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_riverbank_area_configuration() -> None:
    assert RIVERBANK_AREA_01.area_id == "riverbank_area_01"
    assert RIVERBANK_AREA_01.background_asset_name == "riverbank_background.png"
    assert RIVERBANK_AREA_01.player_spawn_x == 65.0
    assert RIVERBANK_AREA_01.player_spawn_y == 490.0

    assert RIVERBANK_STAGE_AREAS == [
        RIVERBANK_AREA_01,
    ]

    assert RIVERBANK_INITIAL_AREA_ID == "riverbank_area_01"