from dataclasses import dataclass

MOUSE_HEALTH_RECOVERY = 25
MAX_STORED_MICE = 5

@dataclass
class PlayerState:
    maximum_health: int = 100
    current_health: int = 100
    stored_mice: int = 0
    score: int = 0
    lives: int = 3
    score_life_milestones_reached: int = 0

    # Resumo: armazena um rato respeitando a capacidade máxima do jogador.
    def store_mouse(self) -> None:
        if self.stored_mice >= MAX_STORED_MICE:
            return

        self.stored_mice += 1

    # Reduz a vida atual do jogador sem permitir valores abaixo de zero.
    def receive_damage(self, damage_amount: int) -> None:
        self.current_health = max(
            0,
            self.current_health - damage_amount,
        )

    # Recupera a vida do jogador sem ultrapassar a vida máxima.
    def restore_health(self, health_amount: int) -> None:
        self.current_health = min(
            self.maximum_health,
            self.current_health + health_amount,
        )

    # Resumo: utiliza um rato armazenado quando houver estoque disponível.
    # Parâmetros: nenhum.
    # Retorno: True quando um rato foi utilizado ou False quando o estoque está vazio.
    def use_stored_mouse(self) -> bool:
        if self.stored_mice == 0:
            return False

        self.stored_mice -= 1
        return True

    # Resumo: aplica a consequência de um rato consumido conforme o estado atual.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def process_consumed_mouse(self) -> None:
        if self.current_health < self.maximum_health:
            self.restore_health(
                health_amount=MOUSE_HEALTH_RECOVERY,
            )
            return

        self.store_mouse()
    # Resumo: adiciona pontos à pontuação do jogador.
    def add_score(
        self,
        points: int,
    ) -> None:
        self.score += points

    # Resumo: adiciona uma vida ao jogador.
    def gain_life(self) -> None:
        self.lives += 1

    # Resumo: remove uma vida do jogador quando ainda existem vidas disponíveis.
    def lose_life(self) -> bool:
        if self.lives <= 0:
            return False

        self.lives -= 1

        return True