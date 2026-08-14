from dataclasses import dataclass


# Representa o estado da Smart Snake durante o gameplay.
@dataclass
class SmartSnake:
    position_x: float
    position_y: float
    movement_speed: float
    last_direction_x: float = 0.0
    last_direction_y: float = 0.0

    # Resumo: atualiza a posição e memoriza a última direção válida de movimento.
    # Parâmetros: direction_x e direction_y representam a direção; delta_time representa o tempo entre frames.
    # Retorno: nenhum.
    def move(
        self,
        direction_x: float,
        direction_y: float,
        delta_time: float,
    ) -> None:
        movement_distance = self.movement_speed * delta_time

        self.position_x += direction_x * movement_distance
        self.position_y += direction_y * movement_distance

        is_moving = direction_x != 0.0 or direction_y != 0.0

        if is_moving:
            self.last_direction_x = direction_x
            self.last_direction_y = direction_y