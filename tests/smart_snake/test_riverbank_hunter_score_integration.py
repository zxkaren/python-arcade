from unittest.mock import Mock

from python_arcade.games.smart_snake.controllers.hunter_defeat_controller import (
    HunterDefeatController,
)
from python_arcade.games.smart_snake.domain.hunter import (
    Hunter,
    HunterState,
)
from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.domain.score_event import ScoreEvent
from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    HUNTER_DEFEAT_DURATION,
    RiverbankScene,
)
from python_arcade.games.smart_snake.services.player_life_service import (
    PlayerLifeService,
)
from python_arcade.games.smart_snake.services.player_score_service import (
    PlayerScoreService,
)


# Resumo: garante que a derrota de um Hunter conceda pontos somente uma vez.
def test_riverbank_scores_hunter_defeat_only_once() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
        state=HunterState.DEFEATED,
        hit_points=0,
    )

    active_area = Mock()
    active_area.hunters = (hunter,)

    stage_area_manager = Mock()
    stage_area_manager.get_active_area.return_value = active_area

    riverbank_scene = RiverbankScene.__new__(RiverbankScene)
    riverbank_scene.stage_area_manager = stage_area_manager
    riverbank_scene.hunter_defeat_controller = HunterDefeatController(
        defeat_duration=HUNTER_DEFEAT_DURATION,
        blink_count=2,
    )
    riverbank_scene.removed_hunter_ids = set()
    riverbank_scene.player_state = PlayerState()
    riverbank_scene.player_score_service = PlayerScoreService()
    riverbank_scene.player_life_service = PlayerLifeService()
    riverbank_scene.extra_lives_granted_this_update = 0

    riverbank_scene.update_hunter_defeats(
        delta_time=HUNTER_DEFEAT_DURATION,
    )

    assert (
        riverbank_scene.player_state.score
        == ScoreEvent.HUNTER_DEFEATED.value
    )

    assert hunter.hunter_id in riverbank_scene.removed_hunter_ids

    riverbank_scene.update_hunter_defeats(
        delta_time=HUNTER_DEFEAT_DURATION,
    )

    assert (
        riverbank_scene.player_state.score
        == ScoreEvent.HUNTER_DEFEATED.value
    )