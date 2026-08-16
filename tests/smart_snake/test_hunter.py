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