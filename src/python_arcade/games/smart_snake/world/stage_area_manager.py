from python_arcade.games.smart_snake.world.stage_area import StageArea


# Gerencia as áreas disponíveis dentro de uma fase e identifica a área ativa.
class StageAreaManager:

    # Resumo: registra as áreas da fase e define qual delas começa ativa.
    # Parâmetros: stage_areas contém as áreas disponíveis e initial_area_id identifica a área inicial.
    # Retorno: nenhum.
    def __init__(
        self,
        stage_areas: list[StageArea],
        initial_area_id: str,
    ) -> None:
        self.stage_areas = {
            stage_area.area_id: stage_area
            for stage_area in stage_areas
        }

        self.active_area_id = initial_area_id

        self.get_active_area()

    # Resumo: retorna a área atualmente ativa na fase.
    # Parâmetros: nenhum.
    # Retorno: StageArea correspondente à área ativa.
    def get_active_area(self) -> StageArea:
        if self.active_area_id not in self.stage_areas:
            raise ValueError(
                f"Stage area not found: {self.active_area_id}"
            )

        return self.stage_areas[self.active_area_id]

    # Resumo: altera a área ativa da fase.
    # Parâmetros: area_id identifica a nova área que deverá ficar ativa.
    # Retorno: nenhum.
    def change_area(
        self,
        area_id: str,
    ) -> None:
        if area_id not in self.stage_areas:
            raise ValueError(
                f"Stage area not found: {area_id}"
            )

        self.active_area_id = area_id