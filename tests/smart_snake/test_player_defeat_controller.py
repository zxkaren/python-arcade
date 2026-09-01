from python_arcade.games.smart_snake.controllers.player_defeat_controller import (
    PlayerDefeatController,
)


# Resumo: valida o ciclo completo de piscada da derrota da Smart Snake.
def test_player_defeat_controller_blinks_until_cycle_finishes() -> None:
    defeat_controller = PlayerDefeatController(
        defeat_duration=1.2,
        blink_count=2,
    )

    defeat_controller.start()

    assert defeat_controller.is_visible() is True

    defeat_finished = defeat_controller.update(
        delta_time=0.3,
    )

    assert defeat_finished is False
    assert defeat_controller.is_visible() is False

    defeat_controller.update(
        delta_time=0.3,
    )

    assert defeat_controller.is_visible() is True

    defeat_controller.update(
        delta_time=0.3,
    )

    assert defeat_controller.is_visible() is False

    defeat_finished = defeat_controller.update(
        delta_time=0.3,
    )

    assert defeat_finished is True
    assert defeat_controller.is_visible() is False