from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)


# Resumo: valida se um objeto de cenário mantém sua configuração de posicionamento.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_object_stores_configuration() -> None:
    scenery_object = SceneryObject(
        object_id="rock_01",
        asset_name="rock_01.png",
        position_x=320.0,
        position_y=480.0,
    )

    assert scenery_object.object_id == "rock_01"
    assert scenery_object.asset_name == "rock_01.png"
    assert scenery_object.position_x == 320.0
    assert scenery_object.position_y == 480.0

# Resumo: valida se um objeto do cenário preserva sua largura de renderização.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_scenery_object_stores_render_width() -> None:
    scenery_object = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=550.0,
        position_y=520.0,
        render_width=80,
    )

    assert scenery_object.render_width == 80