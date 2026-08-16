from unittest.mock import Mock

from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    RiverbankScene,
)


# Resumo: garante que a Riverbank atualize a animação dos Hunters em patrulha.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_update_hunter_animations_uses_patrolling_hunters() -> None:
    hunter = Mock()
    hunter.hunter_id = "hunter_01"

    hunter_patrol = Mock()
    hunter_patrol.hunter_id = "hunter_01"

    active_area = Mock()
    active_area.hunters = (hunter,)
    active_area.hunter_patrols = (hunter_patrol,)

    stage_area_manager = Mock()
    stage_area_manager.get_active_area.return_value = active_area

    hunter_animation_controller = Mock()
    hunter_animation_controller.update.return_value = 1

    riverbank_scene = RiverbankScene.__new__(RiverbankScene)
    riverbank_scene.stage_area_manager = stage_area_manager
    riverbank_scene.hunter_animation_controller = (
        hunter_animation_controller
    )
    riverbank_scene.hunter_animation_frame_indices = {}

    riverbank_scene.update_hunter_animations(
        delta_time=0.2,
    )

    hunter_animation_controller.update.assert_called_once_with(
        hunter_id="hunter_01",
        delta_time=0.2,
        is_moving=True,
    )

    assert (
        riverbank_scene.hunter_animation_frame_indices["hunter_01"]
        == 1
    )