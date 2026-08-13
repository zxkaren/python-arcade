import pygame

from python_arcade.games.smart_snake.ui.dialogue_box import DialogueBox


# Valida se o retrato da Smart Snake é localizado e carregado corretamente.
def test_dialogue_box_loads_smart_snake_portrait(
    monkeypatch,
) -> None:
    monkeypatch.setenv("SDL_VIDEODRIVER", "dummy")

    pygame.init()
    pygame.display.set_mode((1, 1))

    try:
        dialogue_box = DialogueBox()

        portrait_surface = dialogue_box.get_portrait_surface(
            "smart_snake"
        )

        assert portrait_surface is not None
        assert portrait_surface.get_width() > 0
        assert portrait_surface.get_height() > 0
    finally:
        pygame.quit()