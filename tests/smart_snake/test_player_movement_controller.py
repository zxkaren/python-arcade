import pytest

from collections import defaultdict

import pygame

from python_arcade.games.smart_snake.controllers.player_movement_controller import (
    PlayerMovementController,
)


# Valida se a seta para a esquerda gera movimento horizontal negativo.
def test_player_movement_controller_moves_left() -> None:
    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_LEFT] = True

    controller = PlayerMovementController()

    direction_x, direction_y = controller.get_movement_direction(pressed_keys)

    assert direction_x == -1.0
    assert direction_y == 0.0


# Valida se a tecla D gera movimento horizontal positivo.
def test_player_movement_controller_moves_right_with_d() -> None:
    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_d] = True

    controller = PlayerMovementController()

    direction_x, direction_y = controller.get_movement_direction(pressed_keys)

    assert direction_x == 1.0
    assert direction_y == 0.0


# Valida se a seta para cima gera movimento vertical negativo.
def test_player_movement_controller_moves_up() -> None:
    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_UP] = True

    controller = PlayerMovementController()

    direction_x, direction_y = controller.get_movement_direction(pressed_keys)

    assert direction_x == 0.0
    assert direction_y == -1.0


# Valida se a tecla S gera movimento vertical positivo.
def test_player_movement_controller_moves_down_with_s() -> None:
    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_s] = True

    controller = PlayerMovementController()

    direction_x, direction_y = controller.get_movement_direction(pressed_keys)

    assert direction_x == 0.0
    assert direction_y == 1.0


# Valida se nenhuma tecla pressionada mantém a personagem parada.
def test_player_movement_controller_stays_still_without_input() -> None:
    pressed_keys = defaultdict(bool)

    controller = PlayerMovementController()

    direction_x, direction_y = controller.get_movement_direction(pressed_keys)

    assert direction_x == 0.0
    assert direction_y == 0.0

# Valida se o movimento diagonal mantém magnitude normalizada.
def test_player_movement_controller_normalizes_diagonal_movement() -> None:
    pressed_keys = defaultdict(bool)
    pressed_keys[pygame.K_w] = True
    pressed_keys[pygame.K_d] = True

    controller = PlayerMovementController()

    direction_x, direction_y = controller.get_movement_direction(pressed_keys)

    assert direction_x == pytest.approx(0.70710678)
    assert direction_y == pytest.approx(-0.70710678)