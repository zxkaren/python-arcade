from python_arcade.games.smart_snake.domain.hunter import Hunter
from python_arcade.games.smart_snake.domain.hunter import HunterState

# Resumo: valida a identidade e a posição inicial armazenadas pelo Hunter.
def test_hunter_stores_identity_and_initial_position() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
    )

    assert hunter.hunter_id == "hunter_01"
    assert hunter.position_x == 900.0
    assert hunter.position_y == 500.0

# Resumo: garante que um Hunter seja criado inicialmente em patrulha.
def test_hunter_starts_patrolling() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
    )

    assert hunter.state == HunterState.PATROLLING

# Resumo: garante que um Hunter comum seja criado com dois pontos de vida.
def test_hunter_starts_with_two_hit_points() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
    )

    assert hunter.hit_points == 2

# Resumo: valida a redução dos pontos de vida quando o Hunter recebe dano.
def test_hunter_receives_damage() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
    )

    hunter.receive_damage()
    hunter.receive_damage()

    assert hunter.hit_points == 0

# Resumo: garante que somente o segundo acerto coloque o Hunter em estado de derrota.
def test_hunter_is_defeated_after_second_hit() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=900.0,
        position_y=500.0,
    )

    hunter.receive_damage()

    assert hunter.hit_points == 1
    assert hunter.state == HunterState.PATROLLING

    hunter.receive_damage()

    assert hunter.hit_points == 0
    assert hunter.state == HunterState.DEFEATED