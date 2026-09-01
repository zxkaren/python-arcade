from unittest.mock import Mock

import pygame

from python_arcade.games.smart_snake.scenes.game_over_scene import (
    GameOverScene,
)


# Resumo: valida se Enter executa a ação de tentar novamente.
def test_game_over_scene_calls_try_again_when_enter_is_pressed() -> None:
    on_try_again = Mock()

    game_over_scene = GameOverScene.__new__(
        GameOverScene,
    )
    game_over_scene.on_try_again = on_try_again

    enter_event = Mock()
    enter_event.type = pygame.KEYDOWN
    enter_event.key = pygame.K_RETURN

    game_over_scene.handle_events(
        events=[enter_event],
    )

    on_try_again.assert_called_once_with()


# Resumo: valida se a cena delega a renderização para o GameOverRenderer.
def test_game_over_scene_renders_game_over_screen() -> None:
    game_over_renderer = Mock()
    screen = Mock()

    game_over_scene = GameOverScene.__new__(
        GameOverScene,
    )
    game_over_scene.game_over_renderer = game_over_renderer

    game_over_scene.render(
        screen=screen,
    )

    game_over_renderer.render.assert_called_once_with(
        screen=screen,
    )