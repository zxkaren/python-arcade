from python_arcade.games.smart_snake.controllers.smart_snake_animation_controller import (
    SmartSnakeAnimationController,
)


# Resumo: valida se a animação começa utilizando o primeiro frame.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_smart_snake_animation_starts_on_first_frame() -> None:
    animation_controller = SmartSnakeAnimationController(
        frame_count=2,
        frame_duration=0.2,
    )

    assert animation_controller.current_frame_index == 0


# Resumo: valida se o frame permanece igual antes do intervalo da animação.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_smart_snake_animation_keeps_frame_before_interval() -> None:
    animation_controller = SmartSnakeAnimationController(
        frame_count=2,
        frame_duration=0.2,
    )

    frame_index = animation_controller.update(
        delta_time=0.1,
        is_moving=True,
    )

    assert frame_index == 0


# Resumo: valida se a animação avança após completar o intervalo definido.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_smart_snake_animation_advances_frame() -> None:
    animation_controller = SmartSnakeAnimationController(
        frame_count=2,
        frame_duration=0.2,
    )

    frame_index = animation_controller.update(
        delta_time=0.2,
        is_moving=True,
    )

    assert frame_index == 1


# Resumo: valida se os frames alternam continuamente durante o movimento.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_smart_snake_animation_cycles_frames() -> None:
    animation_controller = SmartSnakeAnimationController(
        frame_count=2,
        frame_duration=0.2,
    )

    animation_controller.update(
        delta_time=0.2,
        is_moving=True,
    )

    frame_index = animation_controller.update(
        delta_time=0.2,
        is_moving=True,
    )

    assert frame_index == 0


# Resumo: valida se a animação retorna ao primeiro frame quando o movimento para.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_smart_snake_animation_resets_when_stopped() -> None:
    animation_controller = SmartSnakeAnimationController(
        frame_count=2,
        frame_duration=0.2,
    )

    animation_controller.update(
        delta_time=0.2,
        is_moving=True,
    )

    frame_index = animation_controller.update(
        delta_time=0.1,
        is_moving=False,
    )

    assert frame_index == 0
    assert animation_controller.elapsed_time == 0.0