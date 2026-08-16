from python_arcade.games.smart_snake.domain.hunter import Hunter


class HunterMovementController:

    # Resumo: movimenta um Hunter de acordo com direção, velocidade e tempo decorrido.
    # Parâmetros: hunter, direction_x, direction_y, movement_speed e delta_time.
    # Retorno: nenhum.
    def move(
        self,
        hunter: Hunter,
        direction_x: float,
        direction_y: float,
        movement_speed: float,
        delta_time: float,
    ) -> None:
        hunter.position_x += direction_x * movement_speed * delta_time
        hunter.position_y += direction_y * movement_speed * delta_time