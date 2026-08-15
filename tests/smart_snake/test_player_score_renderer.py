from collections.abc import Generator

import pygame
import pytest

from python_arcade.games.smart_snake.ui.player_score_renderer import (
    PlayerScoreRenderer,
)


# Resumo: prepara o Pygame para os testes do renderer sem abrir uma janela real.
# Parâmetros: monkeypatch configura temporariamente o driver de vídeo.
# Retorno: ambiente temporário do Pygame durante os testes.
@pytest.fixture
def pygame_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> Generator[None, None, None]:
    monkeypatch.setenv(
        "SDL_VIDEODRIVER",
        "dummy",
    )

    pygame.init()
    pygame.display.set_mode((1, 1))

    try:
        yield
    finally:
        pygame.quit()


# Resumo: valida se a pontuação é formatada com seis dígitos.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_player_score_renderer_formats_score_with_leading_zeroes() -> None:
    player_score_renderer = PlayerScoreRenderer()

    formatted_score = player_score_renderer.format_score(
        score=50,
    )

    assert formatted_score == "000050"


# Resumo: valida se pontuações maiores preservam corretamente seus dígitos.
# Parâmetros: nenhum.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_player_score_renderer_formats_larger_score() -> None:
    player_score_renderer = PlayerScoreRenderer()

    formatted_score = player_score_renderer.format_score(
        score=1250,
    )

    assert formatted_score == "001250"

# Resumo: valida se o renderer exibe o título e a pontuação formatada.
# Parâmetros: pygame_environment prepara o ambiente e monkeypatch intercepta os textos.
# Retorno: nenhum.
@pytest.mark.usefixtures("pygame_environment")
def test_player_score_renderer_renders_label_and_formatted_score(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    player_score_renderer = PlayerScoreRenderer()
    screen = pygame.Surface((1280, 720))

    rendered_texts: list[str] = []

    def capture_outlined_text(
        screen: pygame.Surface,
        text: str,
        position: tuple[int, int],
    ) -> None:
        rendered_texts.append(text)

    monkeypatch.setattr(
        player_score_renderer,
        "render_outlined_text",
        capture_outlined_text,
    )

    player_score_renderer.render(
        screen=screen,
        score=150,
    )

    assert rendered_texts == [
        "SCORE",
        "000150",
    ]