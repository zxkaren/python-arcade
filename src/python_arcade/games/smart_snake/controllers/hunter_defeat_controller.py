# Controla a duração e a alternância visual da derrota de um Hunter.
class HunterDefeatController:

    # Resumo: inicializa o ciclo de derrota com duração e quantidade de piscadas.
    # Parâmetros: defeat_duration define o tempo total; blink_count define quantas vezes o Hunter pisca.
    # Retorno: nenhum.
    def __init__(
        self,
        defeat_duration: float,
        blink_count: int,
    ) -> None:
        self.defeat_duration = defeat_duration
        self.blink_count = blink_count
        self.elapsed_times_by_hunter_id: dict[str, float] = {}

    # Resumo: avança o tempo de derrota de um Hunter.
    # Parâmetros: hunter_id identifica o Hunter e delta_time informa o tempo decorrido.
    # Retorno: True quando o ciclo de derrota terminou.
    def update(
        self,
        hunter_id: str,
        delta_time: float,
    ) -> bool:
        elapsed_time = self.elapsed_times_by_hunter_id.get(
            hunter_id,
            0.0,
        )

        elapsed_time = min(
            self.defeat_duration,
            elapsed_time + delta_time,
        )

        self.elapsed_times_by_hunter_id[hunter_id] = elapsed_time

        return elapsed_time >= self.defeat_duration

    # Resumo: informa se o Hunter deve ser desenhado durante o efeito de piscada.
    # Parâmetros: hunter_id identifica o Hunter em estado de derrota.
    # Retorno: True quando o Hunter deve permanecer visível.
    def is_visible(
        self,
        hunter_id: str,
    ) -> bool:
        elapsed_time = self.elapsed_times_by_hunter_id.get(
            hunter_id,
            0.0,
        )

        if elapsed_time >= self.defeat_duration:
            return False

        blink_phase_count = self.blink_count * 2
        blink_phase_duration = (
            self.defeat_duration / blink_phase_count
        )

        current_phase = int(
            elapsed_time / blink_phase_duration
        )

        return current_phase % 2 == 0