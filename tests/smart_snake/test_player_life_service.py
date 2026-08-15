from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.services.player_life_service import (
    PlayerLifeService,
)
from python_arcade.games.smart_snake.domain.player_life_event import (
    PlayerLifeEvent,
)


# Resumo: valida se pontuação abaixo de 3000 não concede vida adicional.
def test_player_life_service_does_not_grant_life_before_score_milestone() -> None:
    player_state = PlayerState(
        score=2999,
    )
    player_life_service = PlayerLifeService()

    extra_lives_granted = (
        player_life_service.process_score_milestones(
            player_state=player_state,
        )
    )

    assert extra_lives_granted == 0
    assert player_state.lives == 3


# Resumo: valida se alcançar 3000 pontos concede uma vida adicional.
def test_player_life_service_grants_life_at_score_milestone() -> None:
    player_state = PlayerState(
        score=3000,
    )
    player_life_service = PlayerLifeService()

    extra_lives_granted = (
        player_life_service.process_score_milestones(
            player_state=player_state,
        )
    )

    assert extra_lives_granted == 1
    assert player_state.lives == 4
    assert player_state.score_life_milestones_reached == 1


# Resumo: valida se um marco de score já premiado não concede a mesma vida novamente.
def test_player_life_service_does_not_repeat_score_milestone_reward() -> None:
    player_state = PlayerState(
        score=3000,
    )
    player_life_service = PlayerLifeService()

    player_life_service.process_score_milestones(
        player_state=player_state,
    )

    extra_lives_granted = (
        player_life_service.process_score_milestones(
            player_state=player_state,
        )
    )

    assert extra_lives_granted == 0
    assert player_state.lives == 4


# Resumo: valida se cada intervalo de 3000 pontos concede uma nova vida.
def test_player_life_service_grants_life_for_each_score_interval() -> None:
    player_state = PlayerState(
        score=6000,
    )
    player_life_service = PlayerLifeService()

    extra_lives_granted = (
        player_life_service.process_score_milestones(
            player_state=player_state,
        )
    )

    assert extra_lives_granted == 2
    assert player_state.lives == 5
    assert player_state.score_life_milestones_reached == 2

# Resumo: valida se HP disponível não altera vidas nem produz evento.
def test_player_life_service_does_nothing_when_health_remains() -> None:
    player_state = PlayerState(
        current_health=50,
        lives=3,
    )
    player_life_service = PlayerLifeService()

    life_event = player_life_service.process_health_depletion(
        player_state=player_state,
    )

    assert life_event == PlayerLifeEvent.NONE
    assert player_state.lives == 3
    assert player_state.current_health == 50


# Resumo: valida se HP esgotado consome uma vida e restaura a vida máxima.
def test_player_life_service_restores_health_after_life_is_lost() -> None:
    player_state = PlayerState(
        current_health=0,
        lives=3,
    )
    player_life_service = PlayerLifeService()

    life_event = player_life_service.process_health_depletion(
        player_state=player_state,
    )

    assert life_event == PlayerLifeEvent.LIFE_LOST
    assert player_state.lives == 2
    assert player_state.current_health == player_state.maximum_health


# Resumo: valida se perder a última vida produz o evento de Game Over.
def test_player_life_service_returns_game_over_after_last_life() -> None:
    player_state = PlayerState(
        current_health=0,
        lives=1,
    )
    player_life_service = PlayerLifeService()

    life_event = player_life_service.process_health_depletion(
        player_state=player_state,
    )

    assert life_event == PlayerLifeEvent.GAME_OVER
    assert player_state.lives == 0
    assert player_state.current_health == 0