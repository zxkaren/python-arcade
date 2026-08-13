from pathlib import Path

import pygame

from python_arcade.games.smart_snake.world.scenery_object import (
    SceneryObject,
)


# Responsável pela representação visual dos objetos estáticos de um cenário.
class SceneryRenderer:

    # Resumo: configura o diretório de assets e os caches de superfícies.
    # Parâmetros: assets_directory representa o diretório dos assets do cenário.
    # Retorno: nenhum.
    def __init__(
        self,
        assets_directory: Path,
    ) -> None:
        self.assets_directory = assets_directory
        self.asset_surfaces: dict[str, pygame.Surface] = {}
        self.scaled_asset_surfaces: dict[
            tuple[str, int],
            pygame.Surface,
        ] = {}

    # Resumo: carrega um asset apenas quando ele ainda não estiver em memória.
    # Parâmetros: asset_name identifica o arquivo de imagem do objeto.
    # Retorno: superfície original correspondente ao asset solicitado.
    def get_asset_surface(
        self,
        asset_name: str,
    ) -> pygame.Surface:
        if asset_name not in self.asset_surfaces:
            asset_path = self.assets_directory / asset_name

            self.asset_surfaces[asset_name] = pygame.image.load(
                asset_path
            )

        return self.asset_surfaces[asset_name]

    # Resumo: obtém a superfície no tamanho configurado preservando sua proporção.
    # Parâmetros: scenery_object contém o asset e a largura de renderização.
    # Retorno: superfície pronta para ser renderizada.
    def get_render_surface(
        self,
        scenery_object: SceneryObject,
    ) -> pygame.Surface:
        asset_surface = self.get_asset_surface(
            scenery_object.asset_name
        )

        if scenery_object.render_width is None:
            return asset_surface

        scaled_surface_key = (
            scenery_object.asset_name,
            scenery_object.render_width,
        )

        if scaled_surface_key not in self.scaled_asset_surfaces:
            original_width, original_height = asset_surface.get_size()

            scale_ratio = (
                scenery_object.render_width
                / original_width
            )

            render_height = round(
                original_height * scale_ratio
            )

            self.scaled_asset_surfaces[scaled_surface_key] = (
                pygame.transform.scale(
                    asset_surface,
                    (
                        scenery_object.render_width,
                        render_height,
                    ),
                )
            )

        return self.scaled_asset_surfaces[scaled_surface_key]

    # Resumo: renderiza os objetos do cenário nas posições configuradas.
    # Parâmetros: screen representa a tela e scenery_objects contém os objetos renderizados.
    # Retorno: nenhum.
    def render(
        self,
        screen: pygame.Surface,
        scenery_objects: tuple[SceneryObject, ...],
    ) -> None:
        for scenery_object in scenery_objects:
            object_surface = self.get_render_surface(
                scenery_object
            )

            object_rectangle = object_surface.get_rect(
                center=(
                    round(scenery_object.position_x),
                    round(scenery_object.position_y),
                ),
            )

            screen.blit(
                object_surface,
                object_rectangle,
            )