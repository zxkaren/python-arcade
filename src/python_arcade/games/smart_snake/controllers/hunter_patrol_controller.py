from python_arcade.games.smart_snake.controllers.hunter_route_controller import (
    HunterRouteController,
)
from python_arcade.games.smart_snake.domain.hunter import (
    Hunter,
    HunterState,
)
from python_arcade.games.smart_snake.world.hunter_patrol import (
    HunterPatrol,
    HunterPatrolAxis,
)


# Coordena as patrulhas configuradas para os Hunters de uma StageArea.
class HunterPatrolController:

    # Resumo: inicializa o controlador com o componente responsável pelas rotas.
    # Parâmetros: route_controller executa as trajetórias dos Hunters.
    # Retorno: nenhum.
    def __init__(
        self,
        route_controller: HunterRouteController,
    ) -> None:
        self.route_controller = route_controller

    # Resumo: atualiza as patrulhas dos Hunters que estão em estado de patrulha.
    # Parâmetros: hunters, hunter_patrols e tempo decorrido desde o último frame.
    # Retorno: nenhum.
    def update(
        self,
        hunters: tuple[Hunter, ...],
        hunter_patrols: tuple[HunterPatrol, ...],
        delta_time: float,
    ) -> None:
        hunters_by_id = {
            hunter.hunter_id: hunter
            for hunter in hunters
        }

        for hunter_patrol in hunter_patrols:
            hunter = hunters_by_id.get(hunter_patrol.hunter_id)

            if hunter is None:
                continue

            if hunter.state != HunterState.PATROLLING:
                continue

            if hunter_patrol.axis == HunterPatrolAxis.VERTICAL:
                self.route_controller.update_vertical(
                    hunter=hunter,
                    minimum_position_y=hunter_patrol.minimum_position,
                    maximum_position_y=hunter_patrol.maximum_position,
                    movement_speed=hunter_patrol.movement_speed,
                    delta_time=delta_time,
                )
                continue

            if hunter_patrol.axis == HunterPatrolAxis.HORIZONTAL:
                self.route_controller.update_horizontal(
                    hunter=hunter,
                    minimum_position_x=hunter_patrol.minimum_position,
                    maximum_position_x=hunter_patrol.maximum_position,
                    movement_speed=hunter_patrol.movement_speed,
                    delta_time=delta_time,
                )