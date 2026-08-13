from dataclasses import dataclass


# Representa uma área navegável pertencente a uma fase do jogo.
@dataclass(frozen=True)
class StageArea:
    area_id: str
    background_asset_name: str
    player_spawn_x: float
    player_spawn_y: float