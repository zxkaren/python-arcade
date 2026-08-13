from python_arcade.games.smart_snake.content.dialogue import DialogueLine
from python_arcade.games.smart_snake.services.dialogue_manager import (
    DialogueManager,
)


# Valida se o diálogo inicia exibindo a primeira fala.
def test_dialogue_manager_starts_with_first_line() -> None:
    dialogue_lines = [
        DialogueLine("Smart Snake", "Primeira fala."),
        DialogueLine("Smart Snake", "Segunda fala."),
    ]

    dialogue_manager = DialogueManager(dialogue_lines)

    current_line = dialogue_manager.get_current_line()

    assert current_line is dialogue_lines[0]


# Valida se o diálogo avança para a próxima fala.
def test_dialogue_manager_advances_to_next_line() -> None:
    dialogue_lines = [
        DialogueLine("Smart Snake", "Primeira fala."),
        DialogueLine("Smart Snake", "Segunda fala."),
    ]

    dialogue_manager = DialogueManager(dialogue_lines)
    dialogue_manager.advance_dialogue()

    current_line = dialogue_manager.get_current_line()

    assert current_line is dialogue_lines[1]


# Valida se o diálogo informa corretamente quando todas as falas terminaram.
def test_dialogue_manager_finishes_after_last_line() -> None:
    dialogue_lines = [
        DialogueLine("Smart Snake", "Última fala."),
    ]

    dialogue_manager = DialogueManager(dialogue_lines)
    dialogue_manager.advance_dialogue()

    assert dialogue_manager.is_finished() is True
    assert dialogue_manager.get_current_line() is None


# Valida o comportamento de um diálogo sem falas.
def test_dialogue_manager_handles_empty_dialogue() -> None:
    dialogue_manager = DialogueManager([])

    assert dialogue_manager.is_finished() is True
    assert dialogue_manager.get_current_line() is None