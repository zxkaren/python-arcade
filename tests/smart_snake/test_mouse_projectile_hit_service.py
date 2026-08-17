from python_arcade.games.smart_snake.content.hunter_collision import (
    HUNTER_COLLISION_BOX,
)
from python_arcade.games.smart_snake.domain.hunter import (
    Hunter,
    HunterState,
)
from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)
from python_arcade.games.smart_snake.services.mouse_projectile_hit_service import (
    MouseProjectileHitService,
)


# Resumo: valida se um projétil colidindo causa dano e é removido após o impacto.
def test_mouse_projectile_hit_service_damages_hunter_and_consumes_projectile() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
    )

    colliding_projectile = MouseProjectile(
        position_x=900.0,
        position_y=500.0,
        direction_x=1.0,
        direction_y=0.0,
    )

    distant_projectile = MouseProjectile(
        position_x=300.0,
        position_y=500.0,
        direction_x=1.0,
        direction_y=0.0,
    )

    mouse_projectiles = [
        colliding_projectile,
        distant_projectile,
    ]

    hit_service = MouseProjectileHitService()

    hit_projectile = hit_service.hit_target(
        target=hunter,
        target_collision_box=HUNTER_COLLISION_BOX,
        mouse_projectiles=mouse_projectiles,
    )

    assert hit_projectile is colliding_projectile
    assert hunter.hit_points == 1
    assert hunter.state == HunterState.PATROLLING
    assert mouse_projectiles == [distant_projectile]