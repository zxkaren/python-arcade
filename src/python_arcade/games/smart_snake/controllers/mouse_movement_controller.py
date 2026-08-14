from python_arcade.games.smart_snake.domain.mouse import Mouse


class MouseMovementController:
    # Resumo: movimenta um rato de acordo com direção, velocidade e tempo decorrido.
    # Parâmetros: mouse, direction_x, direction_y, movement_speed e delta_time.
    # Retorno: nenhum.
    def move(
        self,
        mouse: Mouse,
        direction_x: float,
        direction_y: float,
        movement_speed: float,
        delta_time: float,
    ) -> None:
        mouse.position_x += direction_x * movement_speed * delta_time
        mouse.position_y += direction_y * movement_speed * delta_time