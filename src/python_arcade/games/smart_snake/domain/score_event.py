from enum import Enum

# Representa os eventos do gameplay que concedem pontos ao jogador.
class ScoreEvent(Enum):
    MOUSE_CONSUMED = 50
    HUNTER_DEFEATED = 100
    CHIEF_HUNTER_DEFEATED = 500