from python_arcade.games.smart_snake.config.game_settings import SCREEN_WIDTH
from python_arcade.games.smart_snake.domain.hunter import Hunter
from python_arcade.games.smart_snake.world.collision_box import CollisionBox
from python_arcade.games.smart_snake.world.hunter_attack import HunterAttack
from python_arcade.games.smart_snake.world.hunter_patrol import (
    HunterPatrol,
    HunterPatrolAxis,
)
from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)
from python_arcade.games.smart_snake.world.stage_area import StageArea
from python_arcade.games.smart_snake.world.walkable_area import (
    WalkableArea,
    WalkableRegion,
)


RIVERBANK_ROAD_MINIMUM_Y = 370.0
RIVERBANK_ROAD_MAXIMUM_Y = 650.0

RIVERBANK_HUNTER_PATROL_MINIMUM_Y = 380.0
RIVERBANK_HUNTER_PATROL_MAXIMUM_Y = 520.0
RIVERBANK_HUNTER_MOVEMENT_SPEED = 120.0

RIVERBANK_HUNTER_ATTACK_RANGE_X = 220.0
RIVERBANK_HUNTER_ATTACK_RANGE_Y = 100.0

RIVERBANK_HUNTER_ATTACK_ANIMATION_FRAME_DURATION = 0.30
RIVERBANK_HUNTER_ATTACK_DURATION = 0.60

RIVERBANK_HUNTER_ATTACK_COOLDOWN_DURATION = 1.0


ROCK_01_COLLISION_BOX = CollisionBox(
    width=120.0,
    height=70.0,
    offset_y=20.0,
)


TREE_02_COLLISION_BOX = CollisionBox(
    width=60.0,
    height=30.0,
    offset_y=70.0,
)


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


RIVERBANK_HUNTERS = (
    Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
    ),
)


RIVERBANK_HUNTER_PATROLS = (
    HunterPatrol(
        hunter_id="hunter_01",
        axis=HunterPatrolAxis.VERTICAL,
        minimum_position=RIVERBANK_HUNTER_PATROL_MINIMUM_Y,
        maximum_position=RIVERBANK_HUNTER_PATROL_MAXIMUM_Y,
        movement_speed=RIVERBANK_HUNTER_MOVEMENT_SPEED,
    ),
)


RIVERBANK_HUNTER_ATTACKS = (
    HunterAttack(
        hunter_id="hunter_01",
        range_x=RIVERBANK_HUNTER_ATTACK_RANGE_X,
        range_y=RIVERBANK_HUNTER_ATTACK_RANGE_Y,
        attack_duration=RIVERBANK_HUNTER_ATTACK_DURATION,
        animation_frame_duration=(
            RIVERBANK_HUNTER_ATTACK_ANIMATION_FRAME_DURATION
        ),
        cooldown_duration=RIVERBANK_HUNTER_ATTACK_COOLDOWN_DURATION,
    ),
)

RIVERBANK_SCENERY_OBJECTS = (
    SceneryObject(
        object_id="bush_01_instance_01",
        asset_name="bush_01.png",
        position_x=380.0,
        position_y=400.0,
        render_width=110,
    ),
    SceneryObject(
        object_id="bush_01_instance_02",
        asset_name="bush_01.png",
        position_x=380.0,
        position_y=650.0,
        render_width=110,
    ),
    SceneryObject(
        object_id="bush_01_instance_03",
        asset_name="bush_01.png",
        position_x=645.0,
        position_y=400.0,
        render_width=110,
    ),
    SceneryObject(
        object_id="bush_01_instance_04",
        asset_name="bush_01.png",
        position_x=685.0,
        position_y=650.0,
        render_width=110,
    ),
    SceneryObject(
        object_id="bush_01_instance_05",
        asset_name="bush_01.png",
        position_x=885.0,
        position_y=400.0,
        render_width=110,
    ),
    SceneryObject(
        object_id="bush_01_instance_06",
        asset_name="bush_01.png",
        position_x=940.0,
        position_y=645.0,
        render_width=110,
    ),
    SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=1135.0,
        position_y=600.0,
        render_width=170,
        blocks_movement=True,
        collision_box=ROCK_01_COLLISION_BOX,
    ),
    SceneryObject(
        object_id="tree_02_instance_01",
        asset_name="tree_02.png",
        position_x=1180.0,
        position_y=305.0,
        render_width=180,
        blocks_movement=True,
        collision_box=TREE_02_COLLISION_BOX,
    ),
    SceneryObject(
        object_id="tree_02_instance_02",
        asset_name="tree_02.png",
        position_x=1230.0,
        position_y=510.0,
        render_width=180,
        blocks_movement=True,
        collision_box=TREE_02_COLLISION_BOX,
    ),
)


RIVERBANK_AREA_01 = StageArea(
    area_id="riverbank_area_01",
    background_asset_name="riverbank_background.png",
    player_spawn_x=65.0,
    player_spawn_y=490.0,
    walkable_area=RIVERBANK_WALKABLE_AREA,
    scenery_objects=RIVERBANK_SCENERY_OBJECTS,
    hunters=RIVERBANK_HUNTERS,
    hunter_patrols=RIVERBANK_HUNTER_PATROLS,
    hunter_attacks=RIVERBANK_HUNTER_ATTACKS,
)


RIVERBANK_STAGE_AREAS = [
    RIVERBANK_AREA_01,
]


RIVERBANK_INITIAL_AREA_ID = RIVERBANK_AREA_01.area_id