from dataclasses import dataclass


# Representa o estado de um Hunter comum durante o gameplay.
@dataclass
class Hunter:
    hunter_id: str
    position_x: float
    position_y: float