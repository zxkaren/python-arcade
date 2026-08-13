from collections.abc import Callable

import pygame

from python_arcade.games.smart_snake.content.intro_dialogue import (
    INTRO_DIALOGUE_LINES,
)
from python_arcade.games.smart_snake.scenes.base_scene import BaseScene
from python_arcade.games.smart_snake.services.dialogue_manager import (
    DialogueManager,
)
from python_arcade.games.smart_snake.ui.dialogue_box import DialogueBox


BACKGROUND_COLOR = (10, 18, 13)


# Representa a introdução narrativa da aventura da Smart Snake.
class IntroScene(BaseScene):

    # Inicializa o diálogo do prólogo e a ação executada ao final.
    def __init__(self, on_continue: Callable[[], None]) -> None:
        self.on_continue = on_continue
        self.dialogue_manager = DialogueManager(INTRO_DIALOGUE_LINES)
        self.dialogue_box = DialogueBox()

    # Processa os comandos utilizados para controlar o diálogo.
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        for game_event in events:
            if game_event.type != pygame.KEYDOWN:
                continue

            if game_event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.advance_dialogue()
                continue

            if game_event.key == pygame.K_ESCAPE:
                self.on_continue()

    # Avança a conversa ou encerra a introdução.
    def advance_dialogue(self) -> None:
        self.dialogue_manager.advance_dialogue()

        if self.dialogue_manager.is_finished():
            self.on_continue()

    # Atualiza o estado da introdução.
    def update(self, delta_time: float) -> None:
        return

    # Renderiza o prólogo e a fala atualmente ativa.
    def render(self, screen: pygame.Surface) -> None:
        screen.fill(BACKGROUND_COLOR)

        current_dialogue_line = self.dialogue_manager.get_current_line()

        if current_dialogue_line is None:
            return

        self.dialogue_box.render(
            screen,
            current_dialogue_line,
        )