from copy import deepcopy

from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_INITIAL_AREA_ID,
    RIVERBANK_STAGE_AREAS,
)
from python_arcade.games.smart_snake.domain.hunter import (
    HunterState,
)
from python_arcade.games.smart_snake.world.stage_area_manager import (
    StageAreaManager,
)


# Resumo: valida que uma nova instância da Riverbank recebe Hunters em estado inicial.
def test_new_riverbank_state_starts_with_fresh_hunter() -> None:
    first_stage_area_manager = StageAreaManager(
        stage_areas=deepcopy(RIVERBANK_STAGE_AREAS),
        initial_area_id=RIVERBANK_INITIAL_AREA_ID,
    )

    first_hunter = (
        first_stage_area_manager
        .get_active_area()
        .hunters[0]
    )

    first_hunter.state = HunterState.ATTACKING
    first_hunter.hit_points = 1

    second_stage_area_manager = StageAreaManager(
        stage_areas=deepcopy(RIVERBANK_STAGE_AREAS),
        initial_area_id=RIVERBANK_INITIAL_AREA_ID,
    )

    second_hunter = (
        second_stage_area_manager
        .get_active_area()
        .hunters[0]
    )

    assert second_hunter is not first_hunter
    assert second_hunter.state == HunterState.PATROLLING
    assert second_hunter.hit_points == 2