from unittest.mock import Mock

from python_arcade.games.smart_snake.controllers.hunter_defeat_controller import (
    HunterDefeatController,
)
from python_arcade.games.smart_snake.domain.hunter import (
    Hunter,
    HunterState,
)
from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    RiverbankScene,
)


# Resumo: valida se a Riverbank avança o ciclo visual de um Hunter derrotado.
def test_riverbank_updates_defeated_hunter_blink_cycle() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
        state=HunterState.DEFEATED,
    )

    active_area = Mock()
    active_area.hunters = (hunter,)

    stage_area_manager = Mock()
    stage_area_manager.get_active_area.return_value = active_area

    riverbank_scene = RiverbankScene.__new__(RiverbankScene)
    riverbank_scene.stage_area_manager = stage_area_manager
    riverbank_scene.hunter_defeat_controller = HunterDefeatController(
        defeat_duration=1.2,
        blink_count=2,
    )
    riverbank_scene.removed_hunter_ids = set()
    riverbank_scene.extra_lives_granted_this_update = 0
    riverbank_scene.process_score_event = Mock(return_value=0)

    riverbank_scene.update_hunter_defeats(
        delta_time=0.3,
    )

    assert riverbank_scene.hunter_defeat_controller.is_visible(
        hunter_id=hunter.hunter_id,
    ) is False

    assert hunter.hunter_id not in riverbank_scene.removed_hunter_ids

    riverbank_scene.process_score_event.assert_not_called()


# Resumo: valida se o Hunter é removido do gameplay ao concluir sua derrota.
def test_riverbank_removes_hunter_after_defeat_cycle() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
        state=HunterState.DEFEATED,
    )

    active_area = Mock()
    active_area.hunters = (hunter,)

    stage_area_manager = Mock()
    stage_area_manager.get_active_area.return_value = active_area

    riverbank_scene = RiverbankScene.__new__(RiverbankScene)
    riverbank_scene.stage_area_manager = stage_area_manager
    riverbank_scene.hunter_defeat_controller = HunterDefeatController(
        defeat_duration=1.2,
        blink_count=2,
    )
    riverbank_scene.removed_hunter_ids = set()
    riverbank_scene.extra_lives_granted_this_update = 0
    riverbank_scene.process_score_event = Mock(return_value=0)

    riverbank_scene.update_hunter_defeats(
        delta_time=1.2,
    )

    assert hunter.hunter_id in riverbank_scene.removed_hunter_ids
    assert riverbank_scene.extra_lives_granted_this_update == 0

    riverbank_scene.process_score_event.assert_called_once()