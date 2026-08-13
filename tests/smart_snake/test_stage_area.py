from python_arcade.games.smart_snake.world.stage_area import StageArea


# Resumo: valida se uma StageArea preserva sua identificação, background e spawn.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_stage_area_stores_area_configuration() -> None:
    stage_area = StageArea(
        area_id="riverbank_area_01",
        background_asset_name="riverbank_background.png",
        player_spawn_x=65.0,
        player_spawn_y=490.0,
    )

    assert stage_area.area_id == "riverbank_area_01"
    assert stage_area.background_asset_name == "riverbank_background.png"
    assert stage_area.player_spawn_x == 65.0
    assert stage_area.player_spawn_y == 490.0