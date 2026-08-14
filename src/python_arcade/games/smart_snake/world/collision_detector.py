from python_arcade.games.smart_snake.world.collision_box import CollisionBox


# Responsável por identificar sobreposição entre áreas retangulares de colisão.
class CollisionDetector:

    # Resumo: verifica se duas áreas de colisão estão sobrepostas.
    # Parâmetros: collision boxes e posições centrais dos dois elementos comparados.
    # Retorno: True quando existe sobreposição entre as áreas; caso contrário, False.
    def are_colliding(
        self,
        first_collision_box: CollisionBox,
        first_position_x: float,
        first_position_y: float,
        second_collision_box: CollisionBox,
        second_position_x: float,
        second_position_y: float,
    ) -> bool:
        (
            first_minimum_x,
            first_maximum_x,
            first_minimum_y,
            first_maximum_y,
        ) = first_collision_box.calculate_bounds(
            position_x=first_position_x,
            position_y=first_position_y,
        )

        (
            second_minimum_x,
            second_maximum_x,
            second_minimum_y,
            second_maximum_y,
        ) = second_collision_box.calculate_bounds(
            position_x=second_position_x,
            position_y=second_position_y,
        )

        overlaps_horizontally = (
            first_minimum_x < second_maximum_x
            and first_maximum_x > second_minimum_x
        )

        overlaps_vertically = (
            first_minimum_y < second_maximum_y
            and first_maximum_y > second_minimum_y
        )

        return overlaps_horizontally and overlaps_vertically