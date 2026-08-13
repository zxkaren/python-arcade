from dataclasses import dataclass


# Representa uma fala exibida durante os eventos narrativos do jogo.
@dataclass(frozen=True)
class DialogueLine:
    speaker_name: str
    text: str
    portrait_asset_name: str | None = None