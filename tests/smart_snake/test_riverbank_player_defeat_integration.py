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


# Resumo: garante que a vida seja perdida somente após o ciclo de derrota.
def test_riverbank_processes_life_loss_after_player_defeat_cycle() -> None:
    riverbank_scene = RiverbankScene.__new__(RiverbankScene)

    riverbank_scene.player_state = PlayerState(
        current_health=0,
        lives=3,
    )
    riverbank_scene.player_life_service = PlayerLifeService()
    riverbank_scene.player_defeat_controller = PlayerDefeatController(
        defeat_duration=PLAYER_DEFEAT_DURATION,
        blink_count=2,
    )
    riverbank_scene.player_life_event_this_update = PlayerLifeEvent.NONE
    riverbank_scene.is_game_over = False

    gameplay_blocked = riverbank_scene.update_player_defeat(
        delta_time=0.0,
    )

    assert gameplay_blocked is True
    assert riverbank_scene.player_defeat_controller.is_active is True
    assert riverbank_scene.player_state.lives == 3
    assert riverbank_scene.player_state.current_health == 0

    gameplay_blocked = riverbank_scene.update_player_defeat(
        delta_time=PLAYER_DEFEAT_DURATION,
    )

    assert gameplay_blocked is True
    assert riverbank_scene.player_life_event_this_update == (
        PlayerLifeEvent.LIFE_LOST
    )
    assert riverbank_scene.player_state.lives == 2
    assert riverbank_scene.player_state.current_health == 100
    assert riverbank_scene.player_defeat_controller.is_active is False
    assert riverbank_scene.is_game_over is False