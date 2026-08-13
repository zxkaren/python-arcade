from dataclasses import dataclass


# Representa uma região retangular em que personagens podem se movimentar.
@dataclass(frozen=True)
class WalkableRegion:
    minimum_x: float
    maximum_x: float
    minimum_y: float
    maximum_y: float


# Representa o conjunto de regiões caminháveis pertencentes a uma StageArea.
@dataclass(frozen=True)
class WalkableArea:
    regions: tuple[WalkableRegion, ...]