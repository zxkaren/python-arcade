from dataclasses import dataclass
from enum import Enum


class HunterDirection(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


# Representa o estado de um Hunter comum durante o gameplay.
@dataclass
class Hunter:
    hunter_id: str
    position_x: float
    position_y: float
    direction: HunterDirection = HunterDirection.UP