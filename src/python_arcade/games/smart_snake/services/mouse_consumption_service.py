from python_arcade.games.smart_snake.content.mouse_collision import (
    MOUSE_COLLISION_BOX,
)
from python_arcade.games.smart_snake.content.smart_snake_collision import (
    SMART_SNAKE_COLLISION_BOX,
)
from python_arcade.games.smart_snake.domain.mouse import Mouse
from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake
from python_arcade.games.smart_snake.world.collision_detector import (
    CollisionDetector,
)


class MouseConsumptionService:
    def __init__(self) -> None:
        self.collision_detector = CollisionDetector()

    # Resumo: consome o primeiro rato que estiver colidindo com a Smart Snake.
    # Parâmetros: smart_snake representa o jogador e mice contém os ratos ativos.
    # Retorno: rato consumido ou None quando não existe colisão.
    def consume_colliding_mouse(
        self,
        smart_snake: SmartSnake,
        mice: list[Mouse],
    ) -> Mouse | None:
        for mouse in mice.copy():
            is_colliding = self.collision_detector.are_colliding(
                first_collision_box=SMART_SNAKE_COLLISION_BOX,
                first_position_x=smart_snake.position_x,
                first_position_y=smart_snake.position_y,
                second_collision_box=MOUSE_COLLISION_BOX,
                second_position_x=mouse.position_x,
                second_position_y=mouse.position_y,
            )

            if is_colliding:
                mice.remove(mouse)
                return mouse

        return None