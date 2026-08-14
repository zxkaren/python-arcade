from python_arcade.games.smart_snake.domain.mouse import (
    Mouse,
    MouseDirection,
)
from python_arcade.games.smart_snake.world.scenery_object import SceneryObject


MOUSE_SPAWN_SCENERY_ASSET_NAME = "bush_01.png"


# Responsável por criar ratos utilizando objetos do cenário como pontos de origem.
class MouseSpawner:

    # Resumo: cria ratos posicionados nos arbustos e orientados para o centro da estrada.
    # Parâmetros: scenery_objects contém o cenário e road_center_y define o centro vertical da estrada.
    # Retorno: lista de ratos criados nos pontos de spawn encontrados.
    def spawn_from_bushes(
        self,
        scenery_objects: tuple[SceneryObject, ...],
        road_center_y: float,
    ) -> list[Mouse]:
        mice = []

        for scenery_object in scenery_objects:
            if scenery_object.asset_name != MOUSE_SPAWN_SCENERY_ASSET_NAME:
                continue

            mouse_direction = self.get_initial_direction(
                bush_position_y=scenery_object.position_y,
                road_center_y=road_center_y,
            )

            mice.append(
                Mouse(
                    position_x=scenery_object.position_x,
                    position_y=scenery_object.position_y,
                    home_position_y=scenery_object.position_y,
                    direction=mouse_direction,
                )
            )

        return mice

    # Resumo: define a direção inicial do rato conforme a posição vertical do arbusto.
    # Parâmetros: bush_position_y representa o arbusto e road_center_y o centro da estrada.
    # Retorno: direção vertical inicial do rato.
    def get_initial_direction(
        self,
        bush_position_y: float,
        road_center_y: float,
    ) -> MouseDirection:
        if bush_position_y < road_center_y:
            return MouseDirection.DOWN

        return MouseDirection.UP