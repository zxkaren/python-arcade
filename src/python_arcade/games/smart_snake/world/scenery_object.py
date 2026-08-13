from dataclasses import dataclass

# Representa um objeto estático posicionado em uma área do cenário.
@dataclass(frozen=True)
class SceneryObject:
    object_id: str
    asset_name: str
    position_x: float
    position_y: float
    render_width: int | None = None