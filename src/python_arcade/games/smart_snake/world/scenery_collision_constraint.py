from python_arcade.games.smart_snake.world.collision_box import CollisionBox
from python_arcade.games.smart_snake.world.scenery_collision_checker import (
    SceneryCollisionChecker,
)
from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)


# Responsável por impedir posições ocupadas por obstáculos do cenário.
class SceneryCollisionConstraint:

    # Resumo: inicializa a restrição de movimento contra objetos do cenário.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        self.scenery_collision_checker = SceneryCollisionChecker()

    # Resumo: mantém a posição anterior quando a posição alvo está bloqueada.
    # Parâmetros: posições anterior e alvo, hitbox e objetos da área atual.
    # Retorno: posição permitida para a entidade.
    def constrain_position(
        self,
        previous_position_x: float,
        previous_position_y: float,
        target_position_x: float,
        target_position_y: float,
        collision_box: CollisionBox,
        scenery_objects: tuple[SceneryObject, ...],
    ) -> tuple[float, float]:
        is_target_position_blocked = (
            self.scenery_collision_checker.is_position_blocked(
                collision_box=collision_box,
                position_x=target_position_x,
                position_y=target_position_y,
                scenery_objects=scenery_objects,
            )
        )

        if is_target_position_blocked:
            return (
                previous_position_x,
                previous_position_y,
            )

        return (
            target_position_x,
            target_position_y,
        )