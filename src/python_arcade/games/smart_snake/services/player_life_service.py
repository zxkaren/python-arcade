from python_arcade.games.smart_snake.domain.player_state import PlayerState

from python_arcade.games.smart_snake.domain.player_life_event import (
    PlayerLifeEvent,
)

EXTRA_LIFE_SCORE_INTERVAL = 3000


class PlayerLifeService:

    # Resumo: concede vidas extras correspondentes aos novos marcos de score alcançados.
    # Parâmetros: player_state contém score, vidas e marcos já premiados.
    # Retorno: quantidade de novas vidas concedidas nesta verificação.
    def process_score_milestones(
        self,
        player_state: PlayerState,
    ) -> int:
        reached_milestones = (
            player_state.score
            // EXTRA_LIFE_SCORE_INTERVAL
        )

        pending_extra_lives = (
            reached_milestones
            - player_state.score_life_milestones_reached
        )

        if pending_extra_lives <= 0:
            return 0

        remaining_extra_lives = pending_extra_lives

        while remaining_extra_lives > 0:
            player_state.gain_life()
            remaining_extra_lives -= 1

        player_state.score_life_milestones_reached = (
            reached_milestones
        )

        return pending_extra_lives

    # Resumo: processa o esgotamento do HP e identifica perda de vida ou Game Over.
    def process_health_depletion(
        self,
        player_state: PlayerState,
    ) -> PlayerLifeEvent:
        if player_state.current_health > 0:
            return PlayerLifeEvent.NONE

        life_was_lost = player_state.lose_life()

        if not life_was_lost:
            return PlayerLifeEvent.GAME_OVER

        if player_state.lives == 0:
            return PlayerLifeEvent.GAME_OVER

        player_state.current_health = player_state.maximum_health

        return PlayerLifeEvent.LIFE_LOST