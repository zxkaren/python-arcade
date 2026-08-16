from python_arcade.games.smart_snake.domain.hunter import Hunter

# Verifica se um alvo está dentro da área de alcance de ataque de um Hunter.
class HunterAttackRangeChecker:

    # Resumo: verifica se a posição informada está dentro do alcance do Hunter.
    # Parâmetros: Hunter, posição do alvo e alcances horizontal e vertical.
    # Retorno: True quando o alvo está dentro do alcance; caso contrário, False.
    def is_target_within_range(
        self,
        hunter: Hunter,
        target_position_x: float,
        target_position_y: float,
        range_x: float,
        range_y: float,
    ) -> bool:
        horizontal_distance = abs(
            target_position_x - hunter.position_x
        )
        vertical_distance = abs(
            target_position_y - hunter.position_y
        )

        return (
            horizontal_distance <= range_x
            and vertical_distance <= range_y
        )