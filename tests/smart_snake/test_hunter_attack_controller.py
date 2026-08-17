from python_arcade.games.smart_snake.controllers.hunter_attack_controller import (
    HunterAttackController,
)
from python_arcade.games.smart_snake.controllers.hunter_attack_range_checker import (
    HunterAttackRangeChecker,
)
from python_arcade.games.smart_snake.domain.hunter import (
    Hunter,
    HunterState,
)
from python_arcade.games.smart_snake.world.hunter_attack import HunterAttack


def create_hunter_attack() -> HunterAttack:
    return HunterAttack(
        hunter_id="hunter_01",
        range_x=220.0,
        range_y=100.0,
        attack_duration=0.6,
        animation_frame_duration=0.3,
        cooldown_duration=1.0,
    )


# Resumo: garante que o Hunter inicie o ataque quando o alvo estiver no alcance.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_hunter_starts_attack_when_target_is_within_range() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
    )

    attack_controller = HunterAttackController(
        range_checker=HunterAttackRangeChecker(),
    )

    attack_started = attack_controller.try_start_attack(
        hunter=hunter,
        hunter_attack=create_hunter_attack(),
        target_position_x=900.0,
        target_position_y=450.0,
    )

    assert attack_started is True
    assert hunter.state == HunterState.ATTACKING


# Resumo: garante que o Hunter permaneça patrulhando quando o alvo estiver fora do alcance.
def test_hunter_does_not_attack_when_target_is_outside_range() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
    )

    attack_controller = HunterAttackController(
        range_checker=HunterAttackRangeChecker(),
    )

    attack_started = attack_controller.try_start_attack(
        hunter=hunter,
        hunter_attack=create_hunter_attack(),
        target_position_x=700.0,
        target_position_y=450.0,
    )

    assert attack_started is False
    assert hunter.state == HunterState.PATROLLING


# Resumo: valida se o Hunter retorna à patrulha ao concluir a duração do ataque.
def test_hunter_returns_to_patrol_after_attack_duration() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
        state=HunterState.ATTACKING,
    )

    hunter_attack = create_hunter_attack()

    attack_controller = HunterAttackController(
        range_checker=HunterAttackRangeChecker(),
    )

    attack_controller.update(
        hunter=hunter,
        hunter_attack=hunter_attack,
        delta_time=hunter_attack.attack_duration,
    )

    assert hunter.state == HunterState.PATROLLING


# Resumo: valida se o Hunter não inicia outro ataque durante o cooldown.
def test_hunter_does_not_attack_during_cooldown() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
        state=HunterState.ATTACKING,
    )

    hunter_attack = create_hunter_attack()

    attack_controller = HunterAttackController(
        range_checker=HunterAttackRangeChecker(),
    )

    attack_controller.update(
        hunter=hunter,
        hunter_attack=hunter_attack,
        delta_time=hunter_attack.attack_duration,
    )

    attack_started = attack_controller.try_start_attack(
        hunter=hunter,
        hunter_attack=hunter_attack,
        target_position_x=900.0,
        target_position_y=450.0,
    )

    assert hunter.state == HunterState.PATROLLING
    assert attack_started is False

# Resumo: garante que um Hunter derrotado não possa iniciar um novo ataque.
def test_defeated_hunter_does_not_start_attack() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
        state=HunterState.DEFEATED,
    )

    attack_controller = HunterAttackController(
        range_checker=HunterAttackRangeChecker(),
    )

    attack_started = attack_controller.try_start_attack(
        hunter=hunter,
        hunter_attack=create_hunter_attack(),
        target_position_x=900.0,
        target_position_y=450.0,
    )

    assert attack_started is False
    assert hunter.state == HunterState.DEFEATED