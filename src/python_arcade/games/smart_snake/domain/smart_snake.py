from dataclasses import dataclass


# Representa o estado da Smart Snake durante o gameplay.
@dataclass
class SmartSnake:
    position_x: float
    position_y: float
    movement_speed: float

    # Resumo: atualiza a posição da Smart Snake conforme a direção e o tempo decorrido.
    # Parâmetros: direction_x e direction_y representam a direção; delta_time representa o tempo entre frames.
    def move(
        self,
        direction_x: float,
        direction_y: float,
        delta_time: float,
    ) -> None:
        movement_distance = self.movement_speed * delta_time

        self.position_x += direction_x * movement_distance
        self.position_y += direction_y * movement_distance