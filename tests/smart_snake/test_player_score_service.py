from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.domain.score_event import ScoreEvent
from python_arcade.games.smart_snake.services.player_score_service import (
    PlayerScoreService,
)


# Resumo: valida se o serviço adiciona ao jogador a pontuação do evento recebido.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_score_service_adds_score_from_event() -> None:
    player_state = PlayerState()
    player_score_service = PlayerScoreService()

    player_score_service.process_score_event(
        player_state=player_state,
        score_event=ScoreEvent.MOUSE_CONSUMED,
    )

    assert player_state.score == 50


# Resumo: valida se pontuações de eventos diferentes são acumuladas.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_score_service_accumulates_different_score_events() -> None:
    player_state = PlayerState()
    player_score_service = PlayerScoreService()

    player_score_service.process_score_event(
        player_state=player_state,
        score_event=ScoreEvent.MOUSE_CONSUMED,
    )

    player_score_service.process_score_event(
        player_state=player_state,
        score_event=ScoreEvent.HUNTER_DEFEATED,
    )

    assert player_state.score == 150