from python_arcade.games.smart_snake.world.collision_box import CollisionBox
from python_arcade.games.smart_snake.world.collision_detector import (
    CollisionDetector,
)
from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)


# Responsável por verificar colisões contra objetos bloqueantes do cenário.
class SceneryCollisionChecker:

    # Resumo: inicializa o verificador com o detector geométrico de colisões.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        self.collision_detector = CollisionDetector()

    # Resumo: verifica se uma posição está bloqueada por algum objeto do cenário.
    # Parâmetros: hitbox, posição analisada e objetos existentes na área atual.
    # Retorno: True quando a posição colide com um objeto bloqueante.
    def is_position_blocked(
        self,
        collision_box: CollisionBox,
        position_x: float,
        position_y: float,
        scenery_objects: tuple[SceneryObject, ...],
    ) -> bool:
        for scenery_object in scenery_objects:
            if not scenery_object.blocks_movement:
                continue

            if scenery_object.collision_box is None:
                continue

            is_colliding = self.collision_detector.are_colliding(
                first_collision_box=collision_box,
                first_position_x=position_x,
                first_position_y=position_y,
                second_collision_box=scenery_object.collision_box,
                second_position_x=scenery_object.position_x,
                second_position_y=scenery_object.position_y,
            )

            if is_colliding:
                return True

        return False