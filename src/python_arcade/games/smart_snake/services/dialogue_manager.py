from python_arcade.games.smart_snake.content.dialogue import DialogueLine


# Controla a progressão das falas durante um diálogo.
class DialogueManager:

    # Inicializa o diálogo com as falas recebidas.
    def __init__(self, dialogue_lines: list[DialogueLine]) -> None:
        self.dialogue_lines = list(dialogue_lines)
        self.current_line_index = 0

    # Retorna a fala atualmente exibida.
    def get_current_line(self) -> DialogueLine | None:
        if self.is_finished():
            return None

        return self.dialogue_lines[self.current_line_index]

    # Avança para a próxima fala disponível.
    def advance_dialogue(self) -> None:
        if not self.is_finished():
            self.current_line_index += 1

    # Informa se todas as falas já foram exibidas.
    def is_finished(self) -> bool:
        return self.current_line_index >= len(self.dialogue_lines)