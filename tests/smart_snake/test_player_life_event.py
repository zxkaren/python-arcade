from python_arcade.games.smart_snake.domain.player_life_event import (
    PlayerLifeEvent,
)


# Resumo: valida o evento utilizado quando nenhuma alteração de vida acontece.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_life_event_defines_none_event() -> None:
    assert PlayerLifeEvent.NONE.value == "none"


# Resumo: valida o evento utilizado quando o jogador perde uma vida.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_life_event_defines_life_lost_event() -> None:
    assert PlayerLifeEvent.LIFE_LOST.value == "life_lost"


# Resumo: valida o evento utilizado quando todas as vidas terminam.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_life_event_defines_game_over_event() -> None:
    assert PlayerLifeEvent.GAME_OVER.value == "game_over"