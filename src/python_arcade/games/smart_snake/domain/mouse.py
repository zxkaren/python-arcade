from dataclasses import dataclass
from enum import Enum


class MouseDirection(Enum):
    UP = "up"
    DOWN = "down"


class MouseRouteState(Enum):
    MOVING_AWAY_FROM_BUSH = "moving_away_from_bush"
    RETURNING_TO_BUSH = "returning_to_bush"


# Representa o estado de um rato durante o gameplay.
@dataclass
class Mouse:
    position_x: float
    position_y: float
    home_position_y: float
    direction: MouseDirection
    route_state: MouseRouteState = MouseRouteState.MOVING_AWAY_FROM_BUSH