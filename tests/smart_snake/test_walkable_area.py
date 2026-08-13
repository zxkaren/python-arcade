from python_arcade.games.smart_snake.world.walkable_area import (
    WalkableArea,
    WalkableRegion,
)


# Resumo: valida se uma região caminhável preserva seus limites.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_walkable_region_stores_boundaries() -> None:
    walkable_region = WalkableRegion(
        minimum_x=0.0,
        maximum_x=1280.0,
        minimum_y=430.0,
        maximum_y=650.0,
    )

    assert walkable_region.minimum_x == 0.0
    assert walkable_region.maximum_x == 1280.0
    assert walkable_region.minimum_y == 430.0
    assert walkable_region.maximum_y == 650.0


# Resumo: valida se uma área caminhável pode possuir múltiplas regiões.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_walkable_area_stores_multiple_regions() -> None:
    horizontal_region = WalkableRegion(
        minimum_x=0.0,
        maximum_x=1280.0,
        minimum_y=430.0,
        maximum_y=650.0,
    )

    vertical_region = WalkableRegion(
        minimum_x=600.0,
        maximum_x=780.0,
        minimum_y=250.0,
        maximum_y=650.0,
    )

    walkable_area = WalkableArea(
        regions=(
            horizontal_region,
            vertical_region,
        ),
    )

    assert walkable_area.regions == (
        horizontal_region,
        vertical_region,
    )