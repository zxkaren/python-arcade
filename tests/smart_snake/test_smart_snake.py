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

# Resumo: valida se a Smart Snake memoriza sua última direção de movimento.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_smart_snake_stores_last_movement_direction() -> None:
    smart_snake = SmartSnake(
        position_x=100,
        position_y=200,
        movement_speed=250,
    )

    smart_snake.move(
        direction_x=-1.0,
        direction_y=0.0,
        delta_time=0.5,
    )

    assert smart_snake.last_direction_x == -1.0
    assert smart_snake.last_direction_y == 0.0


# Resumo: valida se parar não apaga a última direção válida da Smart Snake.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_smart_snake_keeps_last_direction_when_stopped() -> None:
    smart_snake = SmartSnake(
        position_x=100,
        position_y=200,
        movement_speed=250,
    )

    smart_snake.move(
        direction_x=0.0,
        direction_y=-1.0,
        delta_time=0.5,
    )

    smart_snake.move(
        direction_x=0.0,
        direction_y=0.0,
        delta_time=0.5,
    )

    assert smart_snake.last_direction_x == 0.0
    assert smart_snake.last_direction_y == -1.0