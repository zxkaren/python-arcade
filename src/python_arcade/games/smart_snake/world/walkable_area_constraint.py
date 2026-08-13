from python_arcade.games.smart_snake.world.walkable_area import (
    WalkableArea,
    WalkableRegion,
)


# Responsável por manter personagens dentro das regiões caminháveis da área.
class WalkableAreaConstraint:

    # Resumo: encontra a posição válida mais próxima dentro da área caminhável.
    # Parâmetros: posição desejada, dimensões do sprite e área caminhável atual.
    # Retorno: posição X e Y ajustada para manter todo o sprite em uma região válida.
    def constrain_position(
        self,
        position_x: float,
        position_y: float,
        sprite_width: float,
        sprite_height: float,
        walkable_area: WalkableArea,
    ) -> tuple[float, float]:
        valid_positions = [
            self.calculate_valid_position_for_region(
                position_x=position_x,
                position_y=position_y,
                sprite_width=sprite_width,
                sprite_height=sprite_height,
                walkable_region=walkable_region,
            )
            for walkable_region in walkable_area.regions
            if self.region_supports_sprite(
                sprite_width=sprite_width,
                sprite_height=sprite_height,
                walkable_region=walkable_region,
            )
        ]

        if not valid_positions:
            raise ValueError(
                "Walkable area does not contain a region large enough "
                "for the sprite."
            )

        return min(
            valid_positions,
            key=lambda valid_position: self.calculate_distance_squared(
                source_x=position_x,
                source_y=position_y,
                target_x=valid_position[0],
                target_y=valid_position[1],
            ),
        )

    # Resumo: verifica se uma região comporta completamente o sprite.
    # Parâmetros: dimensões do sprite e região caminhável analisada.
    # Retorno: verdadeiro quando o sprite cabe dentro da região.
    def region_supports_sprite(
        self,
        sprite_width: float,
        sprite_height: float,
        walkable_region: WalkableRegion,
    ) -> bool:
        region_width = (
            walkable_region.maximum_x
            - walkable_region.minimum_x
        )
        region_height = (
            walkable_region.maximum_y
            - walkable_region.minimum_y
        )

        return (
            region_width >= sprite_width
            and region_height >= sprite_height
        )

    # Resumo: limita uma posição para que o sprite permaneça dentro de uma região.
    # Parâmetros: posição desejada, dimensões do sprite e região caminhável.
    # Retorno: posição X e Y ajustada para a região informada.
    def calculate_valid_position_for_region(
        self,
        position_x: float,
        position_y: float,
        sprite_width: float,
        sprite_height: float,
        walkable_region: WalkableRegion,
    ) -> tuple[float, float]:
        horizontal_margin = sprite_width / 2
        vertical_margin = sprite_height / 2

        minimum_position_x = (
            walkable_region.minimum_x
            + horizontal_margin
        )
        maximum_position_x = (
            walkable_region.maximum_x
            - horizontal_margin
        )

        minimum_position_y = (
            walkable_region.minimum_y
            + vertical_margin
        )
        maximum_position_y = (
            walkable_region.maximum_y
            - vertical_margin
        )

        constrained_position_x = max(
            minimum_position_x,
            min(position_x, maximum_position_x),
        )

        constrained_position_y = max(
            minimum_position_y,
            min(position_y, maximum_position_y),
        )

        return (
            constrained_position_x,
            constrained_position_y,
        )

    # Resumo: calcula a distância ao quadrado entre duas posições.
    # Parâmetros: coordenadas de origem e destino utilizadas na comparação.
    # Retorno: distância ao quadrado entre os dois pontos.
    def calculate_distance_squared(
        self,
        source_x: float,
        source_y: float,
        target_x: float,
        target_y: float,
    ) -> float:
        difference_x = target_x - source_x
        difference_y = target_y - source_y

        return (
            difference_x ** 2
            + difference_y ** 2
        )