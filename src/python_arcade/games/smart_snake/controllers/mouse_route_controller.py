from python_arcade.games.smart_snake.controllers.mouse_movement_controller import (
    MouseMovementController,
)
from python_arcade.games.smart_snake.domain.mouse import (
    Mouse,
    MouseDirection,
    MouseRouteState,
)


# Controla a trajetória vertical executada por um rato durante o gameplay.
class MouseRouteController:

    # Resumo: inicializa o controle de rota utilizando o movimento do rato.
    # Parâmetros: movement_controller executa os deslocamentos da entidade.
    # Retorno: nenhum.
    def __init__(
        self,
        movement_controller: MouseMovementController,
    ) -> None:
        self.movement_controller = movement_controller

    # Resumo: atualiza o movimento vertical do rato conforme seu estado de rota.
    # Parâmetros: mouse, destino oposto ao arbusto, velocidade e tempo decorrido.
    # Retorno: nenhum.
    def update(
        self,
        mouse: Mouse,
        away_target_y: float,
        movement_speed: float,
        delta_time: float,
    ) -> None:
        if mouse.route_state == MouseRouteState.MOVING_AWAY_FROM_BUSH:
            self.move_away_from_bush(
                mouse=mouse,
                away_target_y=away_target_y,
                movement_speed=movement_speed,
                delta_time=delta_time,
            )
            return

        self.return_to_bush(
            mouse=mouse,
            away_target_y=away_target_y,
            movement_speed=movement_speed,
            delta_time=delta_time,
        )

    # Resumo: movimenta o rato para longe do arbusto e inicia o retorno no limite.
    # Parâmetros: mouse, destino oposto ao arbusto, velocidade e tempo decorrido.
    # Retorno: nenhum.
    def move_away_from_bush(
        self,
        mouse: Mouse,
        away_target_y: float,
        movement_speed: float,
        delta_time: float,
    ) -> None:
        direction_y = self.get_vertical_movement_direction(
            direction=mouse.direction,
        )

        self.movement_controller.move(
            mouse=mouse,
            direction_x=0.0,
            direction_y=direction_y,
            movement_speed=movement_speed,
            delta_time=delta_time,
        )

        if not self.has_reached_position(
            current_position_y=mouse.position_y,
            target_position_y=away_target_y,
            direction=mouse.direction,
        ):
            return

        mouse.position_y = away_target_y
        mouse.direction = self.get_opposite_direction(
            direction=mouse.direction,
        )
        mouse.route_state = MouseRouteState.RETURNING_TO_BUSH

    # Resumo: movimenta o rato de volta ao arbusto e reinicia o ciclo ao chegar.
    # Parâmetros: mouse, destino usado para determinar a direção inicial, velocidade e tempo.
    # Retorno: nenhum.
    def return_to_bush(
        self,
        mouse: Mouse,
        away_target_y: float,
        movement_speed: float,
        delta_time: float,
    ) -> None:
        direction_y = self.get_vertical_movement_direction(
            direction=mouse.direction,
        )

        self.movement_controller.move(
            mouse=mouse,
            direction_x=0.0,
            direction_y=direction_y,
            movement_speed=movement_speed,
            delta_time=delta_time,
        )

        if not self.has_reached_position(
            current_position_y=mouse.position_y,
            target_position_y=mouse.home_position_y,
            direction=mouse.direction,
        ):
            return

        mouse.position_y = mouse.home_position_y
        mouse.direction = self.get_away_direction(
            home_position_y=mouse.home_position_y,
            away_target_y=away_target_y,
        )
        mouse.route_state = MouseRouteState.MOVING_AWAY_FROM_BUSH

    # Resumo: converte a direção do rato para o valor utilizado no eixo vertical.
    # Parâmetros: direction representa a orientação atual do rato.
    # Retorno: direção numérica para movimentação no eixo Y.
    def get_vertical_movement_direction(
        self,
        direction: MouseDirection,
    ) -> float:
        if direction == MouseDirection.DOWN:
            return 1.0

        return -1.0

    # Resumo: informa se o rato alcançou ou ultrapassou seu destino vertical.
    # Parâmetros: posição atual, posição alvo e direção utilizada no movimento.
    # Retorno: verdadeiro quando o destino foi alcançado.
    def has_reached_position(
        self,
        current_position_y: float,
        target_position_y: float,
        direction: MouseDirection,
    ) -> bool:
        if direction == MouseDirection.DOWN:
            return current_position_y >= target_position_y

        return current_position_y <= target_position_y

    # Resumo: retorna a direção vertical oposta à direção recebida.
    # Parâmetros: direction representa a orientação atual.
    # Retorno: direção vertical oposta.
    def get_opposite_direction(
        self,
        direction: MouseDirection,
    ) -> MouseDirection:
        if direction == MouseDirection.DOWN:
            return MouseDirection.UP

        return MouseDirection.DOWN

    # Resumo: identifica a direção que afasta o rato de seu arbusto.
    # Parâmetros: posição do arbusto e destino oposto da trajetória.
    # Retorno: direção inicial da rota.
    def get_away_direction(
        self,
        home_position_y: float,
        away_target_y: float,
    ) -> MouseDirection:
        if away_target_y > home_position_y:
            return MouseDirection.DOWN

        return MouseDirection.UP