from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.domain.player_state import (
    MAX_STORED_MICE,
    PlayerState,
)

# Resumo: valida o estado inicial do jogador.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_state_starts_with_full_health_and_no_stored_mice() -> None:
    player_state = PlayerState()

    assert player_state.maximum_health == 100
    assert player_state.current_health == 100
    assert player_state.stored_mice == 0


# Resumo: valida se um rato consumido pode ser armazenado pelo jogador.
def test_player_state_stores_mouse() -> None:
    player_state = PlayerState()

    player_state.store_mouse()

    assert player_state.stored_mice == 1

# Resumo: valida se o jogador perde vida ao receber dano.
def test_player_state_receives_damage() -> None:
    player_state = PlayerState()

    player_state.receive_damage(damage_amount=30)

    assert player_state.current_health == 70


# Resumo: valida se a vida do jogador nunca fica abaixo de zero.
def test_player_state_health_does_not_go_below_zero() -> None:
    player_state = PlayerState()

    player_state.receive_damage(damage_amount=150)

    assert player_state.current_health == 0

# Resumo: valida se o jogador recupera vida.
def test_player_state_restores_health() -> None:
    player_state = PlayerState(
        current_health=50,
    )

    player_state.restore_health(health_amount=30)

    assert player_state.current_health == 80


# Resumo: valida se a recuperação não ultrapassa a vida máxima.
def test_player_state_health_does_not_exceed_maximum() -> None:
    player_state = PlayerState(
        current_health=80,
    )

    player_state.restore_health(health_amount=50)

    assert player_state.current_health == 100

# Resumo: valida se um rato armazenado pode ser utilizado.
def test_player_state_uses_stored_mouse() -> None:
    player_state = PlayerState(
        stored_mice=2,
    )

    mouse_was_used = player_state.use_stored_mouse()

    assert mouse_was_used is True
    assert player_state.stored_mice == 1


# Resumo: valida se o estoque permanece em zero quando não há rato disponível.
def test_player_state_does_not_use_mouse_when_storage_is_empty() -> None:
    player_state = PlayerState()

    mouse_was_used = player_state.use_stored_mouse()

    assert mouse_was_used is False
    assert player_state.stored_mice == 0

# Resumo: valida se um rato consumido recupera vida quando o jogador está ferido.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_state_consumed_mouse_restores_health_when_injured() -> None:
    player_state = PlayerState(
        current_health=50,
    )

    player_state.process_consumed_mouse()

    assert player_state.current_health == 75
    assert player_state.stored_mice == 0


# Resumo: valida se um rato consumido vira estoque quando a vida está cheia.
def test_player_state_consumed_mouse_is_stored_when_health_is_full() -> None:
    player_state = PlayerState()

    player_state.process_consumed_mouse()

    assert player_state.current_health == 100
    assert player_state.stored_mice == 1

# Resumo: valida se o estoque de ratos respeita a capacidade máxima.
def test_player_state_does_not_store_more_than_maximum_mice() -> None:
    player_state = PlayerState(
        stored_mice=MAX_STORED_MICE,
    )

    player_state.store_mouse()

    assert player_state.stored_mice == MAX_STORED_MICE

# Resumo: valida se um rato consumido com vida cheia não ultrapassa o estoque máximo.
def test_player_state_consumed_mouse_respects_maximum_storage() -> None:
    player_state = PlayerState(
        current_health=100,
        stored_mice=MAX_STORED_MICE,
    )

    player_state.process_consumed_mouse()

    assert player_state.stored_mice == MAX_STORED_MICE

# Resumo: valida se o jogador inicia a partida com pontuação zerada.
def test_player_state_starts_with_zero_score() -> None:
    player_state = PlayerState()

    assert player_state.score == 0

# Resumo: valida se pontos conquistados são acumulados na pontuação do jogador.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_state_accumulates_score() -> None:
    player_state = PlayerState()

    player_state.add_score(
        points=50,
    )
    player_state.add_score(
        points=100,
    )

    assert player_state.score == 150

# Resumo: valida se o jogador inicia a partida com três vidas.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_state_starts_with_three_lives() -> None:
    player_state = PlayerState()

    assert player_state.lives == 3

# Resumo: valida se o jogador pode receber uma vida adicional.
def test_player_state_gains_life() -> None:
    player_state = PlayerState()

    player_state.gain_life()

    assert player_state.lives == 4

# Resumo: valida se o jogador perde uma vida quando ainda possui vidas disponíveis.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_player_state_loses_life() -> None:
    player_state = PlayerState()

    life_was_lost = player_state.lose_life()

    assert life_was_lost is True
    assert player_state.lives == 2


# Resumo: valida se a quantidade de vidas nunca fica negativa.
def test_player_state_does_not_lose_life_below_zero() -> None:
    player_state = PlayerState(
        lives=0,
    )

    life_was_lost = player_state.lose_life()

    assert life_was_lost is False
    assert player_state.lives == 0