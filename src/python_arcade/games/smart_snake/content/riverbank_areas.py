from python_arcade.games.smart_snake.world.stage_area import StageArea


RIVERBANK_AREA_01 = StageArea(
    area_id="riverbank_area_01",
    background_asset_name="riverbank_background.png",
    player_spawn_x=65.0,
    player_spawn_y=490.0,
)

RIVERBANK_STAGE_AREAS = [
    RIVERBANK_AREA_01,
]

RIVERBANK_INITIAL_AREA_ID = RIVERBANK_AREA_01.area_id