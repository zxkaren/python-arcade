from dataclasses import dataclass


# Representa uma área retangular de colisão relativa à posição de uma entidade.
@dataclass(frozen=True)
class CollisionBox:
    width: float
    height: float
    offset_x: float = 0.0
    offset_y: float = 0.0

    # Resumo: calcula os limites absolutos da área de colisão.
    # Parâmetros: position_x e position_y representam o centro da entidade.
    # Retorno: limites mínimo e máximo dos eixos X e Y.
    def calculate_bounds(
        self,
        position_x: float,
        position_y: float,
    ) -> tuple[float, float, float, float]:
        collision_center_x = position_x + self.offset_x
        collision_center_y = position_y + self.offset_y

        horizontal_margin = self.width / 2
        vertical_margin = self.height / 2

        minimum_x = collision_center_x - horizontal_margin
        maximum_x = collision_center_x + horizontal_margin
        minimum_y = collision_center_y - vertical_margin
        maximum_y = collision_center_y + vertical_margin

        return (
            minimum_x,
            maximum_x,
            minimum_y,
            maximum_y,
        )