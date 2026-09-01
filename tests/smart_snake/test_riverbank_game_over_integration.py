from unittest.mock import Mock

from python_arcade.games.smart_snake.controllers.player_defeat_controller import (
    PlayerDefeatController,
)
from python_arcade.games.smart_snake.domain.player_life_event import (
    PlayerLifeEvent,
)
from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    PLAYER_DEFEAT_DURATION,
    RiverbankScene,
)
from python_arcade.games.smart_snake.services.player_life_service import (
    PlayerLifeService,
)


# Resumo: valida se a Riverbank comunica o Game Over após a última vida.
def test_riverbank_calls_game_over_after_final_defeat() -> None:
    on_game_over = Mock()

    riverbank_scene = RiverbankScene.__new__(
        RiverbankScene,
    )

    riverbank_scene.player_state = PlayerState(
        current_health=0,
        lives=1,
    )
    riverbank_scene.player_life_service = PlayerLifeService()
    riverbank_scene.player_defeat_controller = PlayerDefeatController(
        defeat_duration=PLAYER_DEFEAT_DURATION,
        blink_count=2,
    )
    riverbank_scene.player_life_event_this_update = PlayerLifeEvent.NONE
    riverbank_scene.is_game_over = False
    riverbank_scene.on_game_over = on_game_over

    riverbank_scene.update_player_defeat(
        delta_time=0.0,
    )

    on_game_over.assert_not_called()

    riverbank_scene.update_player_defeat(
        delta_time=PLAYER_DEFEAT_DURATION,
    )

    assert riverbank_scene.player_state.lives == 0
    assert riverbank_scene.player_life_event_this_update == (
        PlayerLifeEvent.GAME_OVER
    )
    assert riverbank_scene.is_game_over is True

    on_game_over.assert_called_once_with()