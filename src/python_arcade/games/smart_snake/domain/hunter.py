from dataclasses import dataclass
from enum import Enum

class HunterDirection(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

class HunterState(Enum):
    PATROLLING = "patrolling"
    ATTACKING = "attacking"
    DEFEATED = "defeated"

# Representa o estado de um Hunter comum durante o gameplay.
@dataclass
class Hunter:
    hunter_id: str
    position_x: float
    position_y: float
    direction: HunterDirection = HunterDirection.UP
    state: HunterState = HunterState.PATROLLING
    hit_points: int = 2

    # Resumo: reduz os pontos de vida e marca o Hunter como derrotado ao chegar a zero.
    # Parâmetros: damage_points representa a quantidade de dano recebido.
    def receive_damage(self, damage_points: int = 1) -> None:
        self.hit_points = max(0, self.hit_points - damage_points)

        if self.hit_points == 0:
            self.state = HunterState.DEFEATED