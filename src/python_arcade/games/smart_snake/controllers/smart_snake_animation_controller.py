# Controla a alternância dos frames de animação da Smart Snake.
class SmartSnakeAnimationController:

    # Resumo: inicializa o controle temporal da animação.
    # Parâmetros: frame_count define a quantidade de frames e frame_duration
    # representa por quanto tempo cada frame permanece visível.
    # Retorno: nenhum.
    def __init__(
        self,
        frame_count: int,
        frame_duration: float,
    ) -> None:
        self.frame_count = frame_count
        self.frame_duration = frame_duration

        self.current_frame_index = 0
        self.elapsed_time = 0.0

    # Resumo: atualiza o frame atual conforme o tempo e o estado de movimento.
    # Parâmetros: delta_time representa o tempo desde o último frame e
    # is_moving informa se a Smart Snake está se movimentando.
    # Retorno: índice do frame que deve ser exibido.
    def update(
        self,
        delta_time: float,
        is_moving: bool,
    ) -> int:
        if not is_moving:
            self.current_frame_index = 0
            self.elapsed_time = 0.0

            return self.current_frame_index

        self.elapsed_time += delta_time

        while self.elapsed_time >= self.frame_duration:
            self.elapsed_time -= self.frame_duration

            self.current_frame_index = (
                self.current_frame_index + 1
            ) % self.frame_count

        return self.current_frame_index