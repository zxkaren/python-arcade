from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake


# Valida o deslocamento horizontal da Smart Snake para a direita.
def test_smart_snake_moves_right() -> None:
    smart_snake = SmartSnake(
        position_x=100,
        position_y=200,
        movement_speed=250,
    )

    smart_snake.move(
        direction_x=1,
        direction_y=0,
        delta_time=0.5,
    )

    assert smart_snake.position_x == 225
    assert smart_snake.position_y == 200


# Valida o deslocamento vertical da Smart Snake para cima.
def test_smart_snake_moves_up() -> None:
    smart_snake = SmartSnake(
        position_x=100,
        position_y=200,
        movement_speed=250,
    )

    smart_snake.move(
        direction_x=0,
        direction_y=-1,
        delta_time=0.5,
    )

    assert smart_snake.position_x == 100
    assert smart_snake.position_y == 75


# Valida o deslocamento vertical da Smart Snake para baixo.
def test_smart_snake_moves_down() -> None:
    smart_snake = SmartSnake(
        position_x=100,
        position_y=200,
        movement_speed=250,
    )

    smart_snake.move(
        direction_x=0,
        direction_y=1,
        delta_time=0.5,
    )

    assert smart_snake.position_x == 100
    assert smart_snake.position_y == 325