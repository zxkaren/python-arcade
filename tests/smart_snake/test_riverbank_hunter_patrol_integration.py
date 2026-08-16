from unittest.mock import Mock

from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    RiverbankScene,
)


# Resumo: garante que a Riverbank encaminhe os Hunters e suas patrulhas
# para o controlador responsável durante a atualização da cena.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_update_hunter_patrols_uses_active_area_configuration() -> None:
    active_area = Mock()
    active_area.hunters = ("hunter_01",)
    active_area.hunter_patrols = ("hunter_01_patrol",)

    stage_area_manager = Mock()
    stage_area_manager.get_active_area.return_value = active_area

    hunter_patrol_controller = Mock()

    riverbank_scene = RiverbankScene.__new__(RiverbankScene)
    riverbank_scene.stage_area_manager = stage_area_manager
    riverbank_scene.hunter_patrol_controller = hunter_patrol_controller

    riverbank_scene.update_hunter_patrols(
        delta_time=0.1,
    )

    hunter_patrol_controller.update.assert_called_once_with(
        hunters=active_area.hunters,
        hunter_patrols=active_area.hunter_patrols,
        delta_time=0.1,
    )