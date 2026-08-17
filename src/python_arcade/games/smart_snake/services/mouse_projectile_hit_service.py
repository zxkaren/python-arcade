from typing import Protocol

from python_arcade.games.smart_snake.content.mouse_collision import (
    MOUSE_COLLISION_BOX,
)
from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)
from python_arcade.games.smart_snake.world.collision_box import CollisionBox
from python_arcade.games.smart_snake.world.collision_detector import (
    CollisionDetector,
)


# Representa qualquer alvo capaz de receber dano de um projétil.
class DamageableTarget(Protocol):
    position_x: float
    position_y: float

    def receive_damage(
        self,
        damage_points: int = 1,
    ) -> None:
        ...


# Processa impactos dos projéteis de rato contra alvos que recebem dano.
class MouseProjectileHitService:

    # Resumo: inicializa o serviço utilizando o detector de colisões do jogo.
    def __init__(self) -> None:
        self.collision_detector = CollisionDetector()

    # Resumo: aplica dano ao alvo atingido e consome o primeiro projétil em colisão.
    # Parâmetros: alvo, sua área de colisão e coleção de projéteis ativos.
    # Retorno: projétil que atingiu o alvo ou None quando não houve impacto.
    def hit_target(
        self,
        target: DamageableTarget,
        target_collision_box: CollisionBox,
        mouse_projectiles: list[MouseProjectile],
    ) -> MouseProjectile | None:
        for mouse_projectile in mouse_projectiles.copy():
            is_colliding = self.collision_detector.are_colliding(
                first_collision_box=MOUSE_COLLISION_BOX,
                first_position_x=mouse_projectile.position_x,
                first_position_y=mouse_projectile.position_y,
                second_collision_box=target_collision_box,
                second_position_x=target.position_x,
                second_position_y=target.position_y,
            )

            if not is_colliding:
                continue

            target.receive_damage()
            mouse_projectiles.remove(mouse_projectile)

            return mouse_projectile

        return None