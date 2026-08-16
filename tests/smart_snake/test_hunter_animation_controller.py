from python_arcade.games.smart_snake.controllers.hunter_animation_controller import (
    HunterAnimationController,
)


# Resumo: garante que os frames avancem conforme a duração configurada.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_hunter_animation_advances_frames_while_moving() -> None:
    animation_controller = HunterAnimationController(
        frame_count=2,
        frame_duration=0.2,
    )

    first_frame_index = animation_controller.update(
        hunter_id="hunter_01",
        delta_time=0.1,
        is_moving=True,
    )

    second_frame_index = animation_controller.update(
        hunter_id="hunter_01",
        delta_time=0.1,
        is_moving=True,
    )

    third_frame_index = animation_controller.update(
        hunter_id="hunter_01",
        delta_time=0.2,
        is_moving=True,
    )

    assert first_frame_index == 0
    assert second_frame_index == 1
    assert third_frame_index == 0