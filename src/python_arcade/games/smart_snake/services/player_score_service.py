from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.domain.score_event import ScoreEvent


class PlayerScoreService:

    # Resumo: adiciona ao jogador os pontos correspondentes a um evento do gameplay.
    # Parâmetros: player_state contém a pontuação atual; score_event define os pontos conquistados.
    def process_score_event(
        self,
        player_state: PlayerState,
        score_event: ScoreEvent,
    ) -> None:
        player_state.add_score(
            points=score_event.value,
        )