from python_arcade.games.smart_snake.config.game_settings import SCREEN_WIDTH
from python_arcade.games.smart_snake.world.stage_area import StageArea
from python_arcade.games.smart_snake.world.walkable_area import (
    WalkableArea,
    WalkableRegion,
)


RIVERBANK_ROAD_MINIMUM_Y = 370.0
RIVERBANK_ROAD_MAXIMUM_Y = 650.0

RIVERBANK_WALKABLE_AREA = WalkableArea(
    regions=(
        WalkableRegion(
            minimum_x=0.0,
            maximum_x=float(SCREEN_WIDTH),
            minimum_y=RIVERBANK_ROAD_MINIMUM_Y,
            maximum_y=RIVERBANK_ROAD_MAXIMUM_Y,
        ),
    ),
)

RIVERBANK_AREA_01 = StageArea(
    area_id="riverbank_area_01",
    background_asset_name="riverbank_background.png",
    player_spawn_x=65.0,
    player_spawn_y=490.0,
    walkable_area=RIVERBANK_WALKABLE_AREA,
)

RIVERBANK_STAGE_AREAS = [
    RIVERBANK_AREA_01,
]

RIVERBANK_INITIAL_AREA_ID = RIVERBANK_AREA_01.area_id