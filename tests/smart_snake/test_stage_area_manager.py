import pytest

from python_arcade.games.smart_snake.world.stage_area import StageArea
from python_arcade.games.smart_snake.world.stage_area_manager import (
    StageAreaManager,
)
from python_arcade.games.smart_snake.world.walkable_area import (
    WalkableArea,
    WalkableRegion,
)

# Resumo: cria uma área caminhável genérica reutilizável nos testes.
# Parâmetros: nenhum.
# Retorno: WalkableArea utilizada pelas StageAreas de teste.
def create_test_walkable_area() -> WalkableArea:
    return WalkableArea(
        regions=(
            WalkableRegion(
                minimum_x=0.0,
                maximum_x=1280.0,
                minimum_y=400.0,
                maximum_y=650.0,
            ),
        ),
    )

# Resumo: cria uma área de Riverbank reutilizável nos testes do manager.
# Parâmetros: nenhum.
# Retorno: StageArea configurada como primeira área da Riverbank.
def create_riverbank_area() -> StageArea:
    return StageArea(
        area_id="riverbank_area_01",
        background_asset_name="riverbank_background.png",
        player_spawn_x=65.0,
        player_spawn_y=490.0,
        walkable_area=create_test_walkable_area(),
    )


# Resumo: valida se o manager inicia utilizando a área configurada como ativa.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_stage_area_manager_starts_with_initial_area() -> None:
    riverbank_area = create_riverbank_area()

    stage_area_manager = StageAreaManager(
        stage_areas=[riverbank_area],
        initial_area_id="riverbank_area_01",
    )

    active_area = stage_area_manager.get_active_area()

    assert active_area == riverbank_area


# Resumo: valida se o manager consegue alterar a área ativa.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_stage_area_manager_changes_active_area() -> None:
    first_area = StageArea(
        area_id="forest_area_01",
        background_asset_name="forest_01.png",
        player_spawn_x=60.0,
        player_spawn_y=450.0,
        walkable_area=create_test_walkable_area(),
    )

    second_area = StageArea(
        area_id="forest_area_02",
        background_asset_name="forest_02.png",
        player_spawn_x=70.0,
        player_spawn_y=460.0,
        walkable_area=create_test_walkable_area(),
    )

    stage_area_manager = StageAreaManager(
        stage_areas=[
            first_area,
            second_area,
        ],
        initial_area_id="forest_area_01",
    )

    stage_area_manager.change_area("forest_area_02")

    assert stage_area_manager.get_active_area() == second_area


# Resumo: valida se o manager rejeita a ativação de uma área inexistente.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_stage_area_manager_rejects_unknown_area() -> None:
    riverbank_area = create_riverbank_area()

    stage_area_manager = StageAreaManager(
        stage_areas=[riverbank_area],
        initial_area_id="riverbank_area_01",
    )

    with pytest.raises(
        ValueError,
        match="Stage area not found: unknown_area",
    ):
        stage_area_manager.change_area("unknown_area")