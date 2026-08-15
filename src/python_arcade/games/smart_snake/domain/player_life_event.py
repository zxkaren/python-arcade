from enum import Enum


# Representa os eventos produzidos pelo sistema de vidas do jogador.
class PlayerLifeEvent(Enum):
    NONE = "none"
    LIFE_LOST = "life_lost"
    GAME_OVER = "game_over"