from python_arcade.games.smart_snake.controllers.hunter_attack_range_checker import (
    HunterAttackRangeChecker,
)
from python_arcade.games.smart_snake.domain.hunter import (
    Hunter,
    HunterState,
)
from python_arcade.games.smart_snake.world.hunter_attack import HunterAttack


# Controla o ciclo de ataque de um Hunter.
class HunterAttackController:

    # Resumo: inicializa o controle de ataque e seus temporizadores.
    # Parâmetros: range_checker verifica se o alvo pode ser atacado.
    # Retorno: nenhum.
    def __init__(
        self,
        range_checker: HunterAttackRangeChecker,
    ) -> None:
        self.range_checker = range_checker
        self.attack_elapsed_times_by_hunter_id: dict[str, float] = {}
        self.cooldown_remaining_times_by_hunter_id: dict[str, float] = {}

    # Resumo: inicia o ataque quando o Hunter está disponível e o alvo está no alcance.
    # Parâmetros: Hunter, configuração de ataque e posição atual do alvo.
    # Retorno: True quando um novo ataque é iniciado; caso contrário, False.
    def try_start_attack(
        self,
        hunter: Hunter,
        hunter_attack: HunterAttack,
        target_position_x: float,
        target_position_y: float,
    ) -> bool:
        if hunter.state != HunterState.PATROLLING:
            return False

        cooldown_remaining = (
            self.cooldown_remaining_times_by_hunter_id.get(
                hunter.hunter_id,
                0.0,
            )
        )

        if cooldown_remaining > 0.0:
            return False

        is_target_within_range = self.range_checker.is_target_within_range(
            hunter=hunter,
            target_position_x=target_position_x,
            target_position_y=target_position_y,
            range_x=hunter_attack.range_x,
            range_y=hunter_attack.range_y,
        )

        if not is_target_within_range:
            return False

        hunter.state = HunterState.ATTACKING
        self.attack_elapsed_times_by_hunter_id[hunter.hunter_id] = 0.0

        return True

    # Resumo: atualiza a duração do ataque e o cooldown de um Hunter.
    # Parâmetros: Hunter, configuração de ataque e tempo decorrido.
    # Retorno: nenhum.
    def update(
        self,
        hunter: Hunter,
        hunter_attack: HunterAttack,
        delta_time: float,
    ) -> None:
        if hunter.state == HunterState.ATTACKING:
            self.update_active_attack(
                hunter=hunter,
                hunter_attack=hunter_attack,
                delta_time=delta_time,
            )
            return

        self.update_cooldown(
            hunter=hunter,
            delta_time=delta_time,
        )

    # Resumo: atualiza o tempo do golpe e encerra o ataque ao atingir sua duração.
    # Parâmetros: Hunter, configuração de ataque e tempo decorrido.
    # Retorno: nenhum.
    def update_active_attack(
        self,
        hunter: Hunter,
        hunter_attack: HunterAttack,
        delta_time: float,
    ) -> None:
        elapsed_time = self.attack_elapsed_times_by_hunter_id.get(
            hunter.hunter_id,
            0.0,
        )
        elapsed_time += delta_time

        if elapsed_time < hunter_attack.attack_duration:
            self.attack_elapsed_times_by_hunter_id[hunter.hunter_id] = (
                elapsed_time
            )
            return

        hunter.state = HunterState.PATROLLING
        self.attack_elapsed_times_by_hunter_id[hunter.hunter_id] = 0.0
        self.cooldown_remaining_times_by_hunter_id[hunter.hunter_id] = (
            hunter_attack.cooldown_duration
        )

    # Resumo: reduz o tempo restante de cooldown do Hunter.
    # Parâmetros: Hunter e tempo decorrido.
    # Retorno: nenhum.
    def update_cooldown(
        self,
        hunter: Hunter,
        delta_time: float,
    ) -> None:
        cooldown_remaining = (
            self.cooldown_remaining_times_by_hunter_id.get(
                hunter.hunter_id,
                0.0,
            )
        )

        if cooldown_remaining <= 0.0:
            return

        self.cooldown_remaining_times_by_hunter_id[hunter.hunter_id] = max(
            0.0,
            cooldown_remaining - delta_time,
        )