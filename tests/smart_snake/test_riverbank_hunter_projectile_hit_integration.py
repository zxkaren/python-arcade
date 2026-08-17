from unittest.mock import Mock

from python_arcade.games.smart_snake.domain.hunter import Hunter
from python_arcade.games.smart_snake.domain.mouse_projectile import (
    MouseProjectile,
)
from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    RiverbankScene,
)
from python_arcade.games.smart_snake.services.mouse_projectile_hit_service import (
    MouseProjectileHitService,
)


# Resumo: valida se a Riverbank aplica o impacto de um projétil ao Hunter ativo.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_riverbank_processes_mouse_projectile_hit_against_hunter() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
    )

    active_area = Mock()
    active_area.hunters = (hunter,)

    stage_area_manager = Mock()
    stage_area_manager.get_active_area.return_value = active_area

    mouse_projectile = MouseProjectile(
        position_x=900.0,
        position_y=500.0,
        direction_x=1.0,
        direction_y=0.0,
    )

    mouse_projectile_controller = Mock()
    mouse_projectile_controller.active_projectiles = [
        mouse_projectile,
    ]

    riverbank_scene = RiverbankScene.__new__(RiverbankScene)
    riverbank_scene.stage_area_manager = stage_area_manager
    riverbank_scene.mouse_projectile_controller = (
        mouse_projectile_controller
    )
    riverbank_scene.mouse_projectile_hit_service = (
        MouseProjectileHitService()
    )

    riverbank_scene.process_mouse_projectile_hits()

    assert hunter.hit_points == 1
    assert (
        mouse_projectile_controller.active_projectiles
        == []
    )