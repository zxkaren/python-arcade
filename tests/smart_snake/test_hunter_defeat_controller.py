from python_arcade.games.smart_snake.controllers.hunter_defeat_controller import (
    HunterDefeatController,
)


# Resumo: valida as duas piscadas e a conclusão do ciclo de derrota.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_hunter_defeat_controller_blinks_twice_before_finishing() -> None:
    defeat_controller = HunterDefeatController(
        defeat_duration=2.0,
        blink_count=2,
    )

    assert defeat_controller.is_visible(
        hunter_id="hunter_01",
    ) is True

    defeat_finished = defeat_controller.update(
        hunter_id="hunter_01",
        delta_time=0.5,
    )

    assert defeat_controller.is_visible(
        hunter_id="hunter_01",
    ) is False
    assert defeat_finished is False

    defeat_controller.update(
        hunter_id="hunter_01",
        delta_time=0.5,
    )

    assert defeat_controller.is_visible(
        hunter_id="hunter_01",
    ) is True

    defeat_controller.update(
        hunter_id="hunter_01",
        delta_time=0.5,
    )

    assert defeat_controller.is_visible(
        hunter_id="hunter_01",
    ) is False

    defeat_finished = defeat_controller.update(
        hunter_id="hunter_01",
        delta_time=0.5,
    )

    assert defeat_finished is True
    assert defeat_controller.is_visible(
        hunter_id="hunter_01",
    ) is False