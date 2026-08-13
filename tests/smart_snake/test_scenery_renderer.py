from pathlib import Path

import pygame
import pytest

from python_arcade.games.smart_snake.ui.scenery_renderer import (
    SceneryRenderer,
)
from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)


# Resumo: valida se um objeto do cenário é renderizado pela posição central configurada.
# Parâmetros: monkeypatch substitui o carregamento do asset por uma superfície de teste.
# Retorno: nenhum.
def test_scenery_renderer_renders_object_at_configured_position(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    object_surface = pygame.Surface((100, 60))
    object_surface.fill((255, 255, 255))

    monkeypatch.setattr(
        pygame.image,
        "load",
        lambda asset_path: object_surface,
    )

    renderer = SceneryRenderer(
        assets_directory=Path("fake_assets"),
    )

    scenery_object = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=500.0,
        position_y=400.0,
    )

    screen = pygame.Surface((1280, 720))
    screen.fill((0, 0, 0))

    renderer.render(
        screen=screen,
        scenery_objects=(scenery_object,),
    )

    expected_rectangle = object_surface.get_rect(
        center=(500, 400),
    )

    assert screen.get_at(expected_rectangle.center) == (
        255,
        255,
        255,
        255,
    )

# Resumo: valida se objetos com o mesmo asset reutilizam a superfície carregada.
# Parâmetros: monkeypatch intercepta o carregamento dos assets.
# Retorno: nenhum.
def test_scenery_renderer_reuses_loaded_asset_surface(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    object_surface = pygame.Surface((100, 60))
    asset_load_count = 0

    def load_asset(
        asset_path: Path,
    ) -> pygame.Surface:
        nonlocal asset_load_count
        asset_load_count += 1

        return object_surface

    monkeypatch.setattr(
        pygame.image,
        "load",
        load_asset,
    )

    renderer = SceneryRenderer(
        assets_directory=Path("fake_assets"),
    )

    first_rock = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=300.0,
        position_y=400.0,
    )

    second_rock = SceneryObject(
        object_id="rock_01_instance_02",
        asset_name="rock_01.png",
        position_x=700.0,
        position_y=500.0,
    )

    screen = pygame.Surface((1280, 720))

    renderer.render(
        screen=screen,
        scenery_objects=(
            first_rock,
            second_rock,
        ),
    )

    assert asset_load_count == 1

# Resumo: valida se o renderer redimensiona o objeto mantendo sua proporção original.
# Parâmetros: monkeypatch intercepta o carregamento e o redimensionamento do asset.
# Retorno: nenhum.
def test_scenery_renderer_scales_object_to_render_width(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original_surface = pygame.Surface((200, 100))
    captured_scaled_size = None

    def load_asset(
        asset_path: Path,
    ) -> pygame.Surface:
        return original_surface

    def capture_scale(
        surface: pygame.Surface,
        size: tuple[int, int],
    ) -> pygame.Surface:
        nonlocal captured_scaled_size
        captured_scaled_size = size

        return pygame.Surface(size)

    monkeypatch.setattr(
        pygame.image,
        "load",
        load_asset,
    )

    monkeypatch.setattr(
        pygame.transform,
        "scale",
        capture_scale,
    )

    renderer = SceneryRenderer(
        assets_directory=Path("fake_assets"),
    )

    scenery_object = SceneryObject(
        object_id="rock_01_instance_01",
        asset_name="rock_01.png",
        position_x=500.0,
        position_y=400.0,
        render_width=80,
    )

    screen = pygame.Surface((1280, 720))

    renderer.render(
        screen=screen,
        scenery_objects=(scenery_object,),
    )

    assert captured_scaled_size == (80, 40)