from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_AREA_01,
)
from python_arcade.games.smart_snake.world.hunter_patrol import (
    HunterPatrolAxis,
)


# Resumo: garante que o Hunter da Riverbank tenha uma patrulha vertical válida.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_riverbank_hunter_has_vertical_patrol_configuration() -> None:
    hunter = RIVERBANK_AREA_01.hunters[0]
    hunter_patrol = RIVERBANK_AREA_01.hunter_patrols[0]

    assert hunter_patrol.hunter_id == hunter.hunter_id
    assert hunter_patrol.axis == HunterPatrolAxis.VERTICAL
    assert hunter_patrol.minimum_position < hunter.position_y
    assert hunter.position_y < hunter_patrol.maximum_position
    assert hunter_patrol.movement_speed > 0.0