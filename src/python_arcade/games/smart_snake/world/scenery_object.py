from dataclasses import dataclass

from python_arcade.games.smart_snake.world.collision_box import CollisionBox


# Representa um objeto estático posicionado em uma área do cenário.
@dataclass(frozen=True)
class SceneryObject:
    object_id: str
    asset_name: str
    position_x: float
    position_y: float
    render_width: int | None = None
    blocks_movement: bool = False
    collision_box: CollisionBox | None = None