from dataclasses import dataclass


from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)
from python_arcade.games.smart_snake.world.walkable_area import WalkableArea


# Representa uma área navegável pertencente a uma fase do jogo.
@dataclass(frozen=True)
class StageArea:
    area_id: str
    background_asset_name: str
    player_spawn_x: float
    player_spawn_y: float
    walkable_area: WalkableArea
    scenery_objects: tuple[SceneryObject, ...] = ()