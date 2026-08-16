from python_arcade.games.smart_snake.controllers.hunter_attack_range_checker import (
    HunterAttackRangeChecker,
)
from python_arcade.games.smart_snake.domain.hunter import Hunter


# Resumo: garante que um alvo dentro dos dois eixos esteja no alcance do Hunter.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_target_is_within_hunter_attack_range() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
    )

    range_checker = HunterAttackRangeChecker()

    is_within_range = range_checker.is_target_within_range(
        hunter=hunter,
        target_position_x=900.0,
        target_position_y=450.0,
        range_x=220.0,
        range_y=100.0,
    )

    assert is_within_range is True


# Resumo: garante que um alvo fora do eixo horizontal não esteja no alcance.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_target_is_outside_hunter_attack_range() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
    )

    range_checker = HunterAttackRangeChecker()

    is_within_range = range_checker.is_target_within_range(
        hunter=hunter,
        target_position_x=700.0,
        target_position_y=450.0,
        range_x=220.0,
        range_y=100.0,
    )

    assert is_within_range is False