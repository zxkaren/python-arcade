# Controla o ciclo visual de derrota da Smart Snake.
class PlayerDefeatController:

    # Resumo: inicializa o ciclo de derrota com duração e quantidade de piscadas.
    # Parâmetros: defeat_duration define o tempo total; blink_count define quantas vezes a Smart Snake pisca.
    def __init__(
        self,
        defeat_duration: float,
        blink_count: int,
    ) -> None:
        self.defeat_duration = defeat_duration
        self.blink_count = blink_count
        self.elapsed_time = 0.0
        self.is_active = False

    # Resumo: inicia um novo ciclo visual de derrota.
    def start(self) -> None:
        self.elapsed_time = 0.0
        self.is_active = True

    # Resumo: avança o tempo do ciclo de derrota ativo.
    # Parâmetros: delta_time informa o tempo decorrido desde o último frame.
    # Retorno: True quando o ciclo de derrota terminou.
    def update(
        self,
        delta_time: float,
    ) -> bool:
        if not self.is_active:
            return False

        self.elapsed_time = min(
            self.defeat_duration,
            self.elapsed_time + delta_time,
        )

        return self.elapsed_time >= self.defeat_duration

    # Resumo: informa se a Smart Snake deve ser desenhada durante a piscada.
    # Retorno: True quando a Smart Snake deve permanecer visível.
    def is_visible(self) -> bool:
        if not self.is_active:
            return True

        if self.elapsed_time >= self.defeat_duration:
            return False

        blink_phase_count = self.blink_count * 2
        blink_phase_duration = (
            self.defeat_duration / blink_phase_count
        )

        current_phase = int(
            self.elapsed_time / blink_phase_duration
        )

        return current_phase % 2 == 0

    # Resumo: encerra o ciclo atual e prepara o controller para uma nova derrota.
    def reset(self) -> None:
        self.elapsed_time = 0.0
        self.is_active = False