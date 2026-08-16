from dataclasses import dataclass

# Representa a configuração de ataque de um Hunter dentro de uma StageArea.
@dataclass(frozen=True)
class HunterAttack:
    hunter_id: str
    range_x: float
    range_y: float
    attack_duration: float
    animation_frame_duration: float
    cooldown_duration: float