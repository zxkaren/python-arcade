from dataclasses import dataclass
from enum import Enum


class HunterPatrolAxis(Enum):
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"

# Representa a configuração de patrulha de um Hunter dentro de uma StageArea.
@dataclass(frozen=True)
class HunterPatrol:
    hunter_id: str
    axis: HunterPatrolAxis
    minimum_position: float
    maximum_position: float
    movement_speed: float