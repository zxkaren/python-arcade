from dataclasses import dataclass

MOUSE_HEALTH_RECOVERY = 25

@dataclass
class PlayerState:
    maximum_health: int = 100
    current_health: int = 100
    stored_mice: int = 0

    # adiciona um rato ao estoque disponível para uso pelo jogador.
    def store_mouse(self) -> None:
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