from python_arcade.games.smart_snake.controllers.hunter_movement_controller import (
    HunterMovementController,
)
from python_arcade.games.smart_snake.domain.hunter import (
    Hunter,
    HunterDirection,
)


# Controla as trajetórias de patrulha de um Hunter comum.
class HunterRouteController:

    # Resumo: inicializa o controle de rota utilizando o movimento do Hunter.
    # Parâmetros: movement_controller executa os deslocamentos da entidade.
    # Retorno: nenhum.
    def __init__(
        self,
        movement_controller: HunterMovementController,
    ) -> None:
        self.movement_controller = movement_controller

    # Resumo: atualiza a patrulha vertical e inverte a direção nos limites.
    # Parâmetros: Hunter, limites verticais, velocidade e tempo decorrido.
    # Retorno: nenhum.
    def update_vertical(
        self,
        hunter: Hunter,
        minimum_position_y: float,
        maximum_position_y: float,
        movement_speed: float,
        delta_time: float,
    ) -> None:
        direction_y = self.get_vertical_movement_direction(
            direction=hunter.direction,
        )

        self.movement_controller.move(
            hunter=hunter,
            direction_x=0.0,
            direction_y=direction_y,
            movement_speed=movement_speed,
            delta_time=delta_time,
        )

        if hunter.direction == HunterDirection.UP:
            if hunter.position_y > minimum_position_y:
                return

            hunter.position_y = minimum_position_y
            hunter.direction = HunterDirection.DOWN
            return

        if hunter.position_y < maximum_position_y:
            return

        hunter.position_y = maximum_position_y
        hunter.direction = HunterDirection.UP

    # Resumo: atualiza a patrulha horizontal e inverte a direção nos limites.
    # Parâmetros: Hunter, limites horizontais, velocidade e tempo decorrido.
    # Retorno: nenhum.
    def update_horizontal(
        self,
        hunter: Hunter,
        minimum_position_x: float,
        maximum_position_x: float,
        movement_speed: float,
        delta_time: float,
    ) -> None:
        direction_x = self.get_horizontal_movement_direction(
            direction=hunter.direction,
        )

        self.movement_controller.move(
            hunter=hunter,
            direction_x=direction_x,
            direction_y=0.0,
            movement_speed=movement_speed,
            delta_time=delta_time,
        )

        if hunter.direction == HunterDirection.LEFT:
            if hunter.position_x > minimum_position_x:
                return

            hunter.position_x = minimum_position_x
            hunter.direction = HunterDirection.RIGHT
            return

        if hunter.position_x < maximum_position_x:
            return

        hunter.position_x = maximum_position_x
        hunter.direction = HunterDirection.LEFT

    # Resumo: converte a direção do Hunter para o valor usado no eixo vertical.
    # Parâmetros: direction representa a orientação atual do Hunter.
    # Retorno: direção numérica utilizada no eixo Y.
    def get_vertical_movement_direction(
        self,
        direction: HunterDirection,
    ) -> float:
        if direction == HunterDirection.DOWN:
            return 1.0

        return -1.0

    # Resumo: converte a direção do Hunter para o valor usado no eixo horizontal.
    # Parâmetros: direction representa a orientação atual do Hunter.
    # Retorno: direção numérica utilizada no eixo X.
    def get_horizontal_movement_direction(
        self,
        direction: HunterDirection,
    ) -> float:
        if direction == HunterDirection.RIGHT:
            return 1.0

        return -1.0