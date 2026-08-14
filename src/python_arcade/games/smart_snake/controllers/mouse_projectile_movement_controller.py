from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)


class MouseProjectileMovementController:

    # Resumo: movimenta um rato lançado conforme sua direção, velocidade e tempo.
    # Parâmetros: mouse_projectile, movement_speed e delta_time.
    # Retorno: nenhum.
    def move(
        self,
        mouse_projectile: MouseProjectile,
        movement_speed: float,
        delta_time: float,
    ) -> None:
        mouse_projectile.position_x += (
            mouse_projectile.direction_x
            * movement_speed
            * delta_time
        )

        mouse_projectile.position_y += (
            mouse_projectile.direction_y
            * movement_speed
            * delta_time
        )