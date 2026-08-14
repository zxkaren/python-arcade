from dataclasses import dataclass


# Representa o estado de um rato lançado como projétil durante o gameplay.
@dataclass
class MouseProjectile:
    position_x: float
    position_y: float
    direction_x: float
    direction_y: float