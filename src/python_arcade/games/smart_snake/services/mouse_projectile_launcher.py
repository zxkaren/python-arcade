from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)
from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake


class MouseProjectileLauncher:

    # Resumo: cria um projétil utilizando um rato armazenado pelo jogador.
    # Parâmetros: smart_snake contém posição e direção; player_state contém o estoque de ratos.
    # Retorno: MouseProjectile quando o lançamento é possível ou None caso contrário.
    def launch(
        self,
        smart_snake: SmartSnake,
        player_state: PlayerState,
    ) -> MouseProjectile | None:
        has_launch_direction = (
            smart_snake.last_direction_x != 0.0
            or smart_snake.last_direction_y != 0.0
        )

        if not has_launch_direction:
            return None

        mouse_was_used = player_state.use_stored_mouse()

        if not mouse_was_used:
            return None

        return MouseProjectile(
            position_x=smart_snake.position_x,
            position_y=smart_snake.position_y,
            direction_x=smart_snake.last_direction_x,
            direction_y=smart_snake.last_direction_y,
        )