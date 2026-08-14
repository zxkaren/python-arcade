from python_arcade.games.smart_snake.controllers.mouse_projectile_movement_controller import (
    MouseProjectileMovementController,
)
from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)
from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake
from python_arcade.games.smart_snake.services.mouse_projectile_launcher import (
    MouseProjectileLauncher,
)


class MouseProjectileController:

    # Resumo: inicializa o controle dos projéteis lançados durante o gameplay.
    # Parâmetros: projectile_launcher cria projéteis; movement_controller movimenta os projéteis ativos.
    # Retorno: nenhum.
    def __init__(
        self,
        projectile_launcher: MouseProjectileLauncher,
        movement_controller: MouseProjectileMovementController,
    ) -> None:
        self.projectile_launcher = projectile_launcher
        self.movement_controller = movement_controller
        self.active_projectiles: list[MouseProjectile] = []

    # Resumo: tenta lançar um rato e adiciona o projétil criado à coleção ativa.
    # Parâmetros: smart_snake fornece posição e direção; player_state fornece a munição.
    # Retorno: MouseProjectile criado ou None quando o lançamento não é possível.
    def launch_projectile(
        self,
        smart_snake: SmartSnake,
        player_state: PlayerState,
    ) -> MouseProjectile | None:
        mouse_projectile = self.projectile_launcher.launch(
            smart_snake=smart_snake,
            player_state=player_state,
        )

        if mouse_projectile is None:
            return None

        self.active_projectiles.append(mouse_projectile)

        return mouse_projectile

    # Resumo: atualiza a posição de todos os projéteis ativos.
    # Parâmetros: movement_speed define a velocidade; delta_time representa o tempo entre frames.
    # Retorno: nenhum.
    def update_projectiles(
        self,
        movement_speed: float,
        delta_time: float,
    ) -> None:
        for mouse_projectile in self.active_projectiles:
            self.movement_controller.move(
                mouse_projectile=mouse_projectile,
                movement_speed=movement_speed,
                delta_time=delta_time,
            )

    # Resumo: remove projéteis que ultrapassaram os limites permitidos.
    # Parâmetros: minimum_x, maximum_x, minimum_y e maximum_y definem os limites válidos.
    # Retorno: nenhum.
    def remove_projectiles_outside_bounds(
        self,
        minimum_x: float,
        maximum_x: float,
        minimum_y: float,
        maximum_y: float,
    ) -> None:
        self.active_projectiles = [
            mouse_projectile
            for mouse_projectile in self.active_projectiles
            if (
                minimum_x <= mouse_projectile.position_x <= maximum_x
                and minimum_y <= mouse_projectile.position_y <= maximum_y
            )
        ]