# Controla a progressão dos frames de animação dos Hunters ativos.
class HunterAnimationController:

    # Resumo: inicializa o controle de animação dos Hunters.
    # Parâmetros: frame_count e duração de cada frame em segundos.
    # Retorno: nenhum.
    def __init__(
        self,
        frame_count: int,
        frame_duration: float,
    ) -> None:
        self.frame_count = frame_count
        self.frame_duration = frame_duration
        self.frame_indices_by_hunter_id: dict[str, int] = {}
        self.elapsed_times_by_hunter_id: dict[str, float] = {}

    # Resumo: atualiza e retorna o frame atual de um Hunter.
    # Parâmetros: hunter_id, tempo decorrido e indicador de movimentação.
    # Retorno: índice do frame atual da animação.
    def update(
        self,
        hunter_id: str,
        delta_time: float,
        is_moving: bool,
    ) -> int:
        if not is_moving:
            self.frame_indices_by_hunter_id[hunter_id] = 0
            self.elapsed_times_by_hunter_id[hunter_id] = 0.0
            return 0

        current_frame_index = self.frame_indices_by_hunter_id.get(
            hunter_id,
            0,
        )
        elapsed_time = self.elapsed_times_by_hunter_id.get(
            hunter_id,
            0.0,
        )

        elapsed_time += delta_time

        while elapsed_time >= self.frame_duration:
            elapsed_time -= self.frame_duration
            current_frame_index = (
                current_frame_index + 1
            ) % self.frame_count

        self.frame_indices_by_hunter_id[hunter_id] = current_frame_index
        self.elapsed_times_by_hunter_id[hunter_id] = elapsed_time

        return current_frame_index