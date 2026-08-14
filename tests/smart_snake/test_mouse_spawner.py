from python_arcade.games.smart_snake.domain.mouse import MouseDirection
from python_arcade.games.smart_snake.services.mouse_spawner import (
    MouseSpawner,
)
from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)


# Resumo: valida se o spawner cria ratos nos arbustos orientados para o centro da estrada.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_mouse_spawner_creates_mice_from_bushes() -> None:
    scenery_objects = (
        SceneryObject(
            object_id="test_upper_bush",
            asset_name="bush_01.png",
            position_x=300.0,
            position_y=400.0,
            render_width=110,
        ),
        SceneryObject(
            object_id="test_rock",
            asset_name="rock_01.png",
            position_x=700.0,
            position_y=500.0,
            render_width=170,
        ),
        SceneryObject(
            object_id="test_lower_bush",
            asset_name="bush_01.png",
            position_x=900.0,
            position_y=620.0,
            render_width=110,
        ),
    )

    mouse_spawner = MouseSpawner()

    mice = mouse_spawner.spawn_from_bushes(
        scenery_objects=scenery_objects,
        road_center_y=510.0,
    )

    assert len(mice) == 2

    assert mice[0].position_x == 300.0
    assert mice[0].position_y == 400.0
    assert mice[0].home_position_y == 400.0
    assert mice[0].direction == MouseDirection.DOWN

    assert mice[1].position_x == 900.0
    assert mice[1].position_y == 620.0
    assert mice[1].home_position_y == 620.0
    assert mice[1].direction == MouseDirection.UP