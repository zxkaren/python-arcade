from collections.abc import Callable

import pygame

from python_arcade.games.smart_snake.scenes.base_scene import BaseScene
from python_arcade.games.smart_snake.ui.game_over_renderer import (
    GameOverRenderer,
)


# Representa a tela exibida após o jogador perder todas as vidas.
class GameOverScene(BaseScene):

    # Resumo: inicializa a tela de Game Over e a ação de reinício da partida.
    # Parâmetros: on_try_again representa a ação executada ao pressionar Enter.
    def __init__(
        self,
        on_try_again: Callable[[], None],
    ) -> None:
        self.on_try_again = on_try_again
        self.game_over_renderer = GameOverRenderer()

    # Resumo: processa o comando para iniciar uma nova tentativa.
    # Parâmetros: events contém os eventos capturados pelo Pygame.
    def handle_events(
        self,
        events: list[pygame.event.Event],
    ) -> None:
        for game_event in events:
            if (
                game_event.type == pygame.KEYDOWN
                and game_event.key == pygame.K_RETURN
            ):
                self.on_try_again()

    # Resumo: mantém a tela de Game Over sem atualizações de gameplay.
    def update(
        self,
        delta_time: float,
    ) -> None:
        return

    # Resumo: renderiza a arte de Game Over preenchendo toda a tela.
    # Parâmetros: screen representa a superfície principal do jogo.
    def render(
        self,
        screen: pygame.Surface,
    ) -> None:
        self.game_over_renderer.render(
            screen=screen,
        )