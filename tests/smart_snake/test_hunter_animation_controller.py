from python_arcade.games.smart_snake.controllers.hunter_animation_controller import (
    HunterAnimationController,
)


# Resumo: garante que os frames avancem conforme a duração padrão.
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


# Resumo: garante que uma animação possa utilizar duração de frame específica.
def test_hunter_animation_uses_custom_frame_duration() -> None:
    animation_controller = HunterAnimationController(
        frame_count=2,
        frame_duration=0.2,
    )

    first_frame_index = animation_controller.update(
        hunter_id="hunter_01",
        delta_time=0.2,
        is_moving=True,
        frame_duration=0.3,
    )

    second_frame_index = animation_controller.update(
        hunter_id="hunter_01",
        delta_time=0.1,
        is_moving=True,
        frame_duration=0.3,
    )

    assert first_frame_index == 0
    assert second_frame_index == 1


# Resumo: garante que o reset retorne a animação ao primeiro frame.
def test_hunter_animation_resets_to_first_frame() -> None:
    animation_controller = HunterAnimationController(
        frame_count=2,
        frame_duration=0.2,
    )

    animation_controller.update(
        hunter_id="hunter_01",
        delta_time=0.2,
        is_moving=True,
    )

    assert animation_controller.frame_indices_by_hunter_id["hunter_01"] == 1

    animation_controller.reset(
        hunter_id="hunter_01",
    )

    assert animation_controller.frame_indices_by_hunter_id["hunter_01"] == 0
    assert animation_controller.elapsed_times_by_hunter_id["hunter_01"] == 0.0