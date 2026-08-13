from pathlib import Path

import pygame

from python_arcade.games.smart_snake.content.dialogue import DialogueLine


DIALOGUE_BOX_MARGIN = 40
DIALOGUE_BOX_HEIGHT = 220
DIALOGUE_BOX_PADDING = 24
PORTRAIT_AREA_WIDTH = 170
DIALOGUE_CONTENT_GAP = 24

BACKGROUND_COLOR = (20, 24, 22)
BORDER_COLOR = (190, 220, 190)
SPEAKER_COLOR = (150, 210, 150)
TEXT_COLOR = (245, 245, 245)

PORTRAITS_DIRECTORY = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "portraits"
)

# Renderiza as falas narrativas em uma caixa de diálogo.
class DialogueBox:

    # Inicializa os recursos visuais utilizados pela caixa de diálogo.
    def __init__(self) -> None:
        self.speaker_font = pygame.font.Font(None, 32)
        self.text_font = pygame.font.Font(None, 28)
        self.continue_font = pygame.font.Font(None, 26)
        self.portrait_surface_cache: dict[str, pygame.Surface] = {}

    # Carrega o retrato solicitado e mantém a imagem disponível em memória.
    def get_portrait_surface(
        self,
        portrait_asset_name: str | None,
    ) -> pygame.Surface | None:
        if portrait_asset_name is None:
            return None

        if portrait_asset_name in self.portrait_surface_cache:
            return self.portrait_surface_cache[portrait_asset_name]

        portrait_path = PORTRAITS_DIRECTORY / f"{portrait_asset_name}.png"

        if not portrait_path.exists():
            return None

        portrait_surface = pygame.image.load(portrait_path).convert_alpha()

        self.portrait_surface_cache[portrait_asset_name] = portrait_surface

        return portrait_surface
    # Renderiza uma fala na região inferior da tela.
    def render(
        self,
        screen: pygame.Surface,
        dialogue_line: DialogueLine,
    ) -> None:
        dialogue_box_rectangle = pygame.Rect(
            DIALOGUE_BOX_MARGIN,
            screen.get_height() - DIALOGUE_BOX_HEIGHT - DIALOGUE_BOX_MARGIN,
            screen.get_width() - (DIALOGUE_BOX_MARGIN * 2),
            DIALOGUE_BOX_HEIGHT,
        )

        pygame.draw.rect(
            screen,
            BACKGROUND_COLOR,
            dialogue_box_rectangle,
            border_radius=12,
        )

        pygame.draw.rect(
            screen,
            BORDER_COLOR,
            dialogue_box_rectangle,
            width=2,
            border_radius=12,
        )

        self.render_portrait_area(
            screen,
            dialogue_box_rectangle,
            dialogue_line.portrait_asset_name,
)

        self.render_speaker_name(
            screen,
            dialogue_box_rectangle,
            dialogue_line.speaker_name,
        )

        self.render_dialogue_text(
            screen,
            dialogue_box_rectangle,
            dialogue_line.text,
        )

        self.render_continue_indicator(
            screen,
            dialogue_box_rectangle,
        )

    # Renderiza o retrato da personagem dentro da área reservada.
    def render_portrait_area(
        self,
        screen: pygame.Surface,
        dialogue_box_rectangle: pygame.Rect,
        portrait_asset_name: str | None,
    ) -> None:
        portrait_rectangle = pygame.Rect(
            dialogue_box_rectangle.left + DIALOGUE_BOX_PADDING,
            dialogue_box_rectangle.top + DIALOGUE_BOX_PADDING,
            PORTRAIT_AREA_WIDTH - DIALOGUE_BOX_PADDING,
            dialogue_box_rectangle.height - (DIALOGUE_BOX_PADDING * 2),
        )

        pygame.draw.rect(
            screen,
            BORDER_COLOR,
            portrait_rectangle,
            width=1,
            border_radius=8,
        )

        portrait_surface = self.get_portrait_surface(portrait_asset_name)

        if portrait_surface is None:
            return

        portrait_width = portrait_surface.get_width()
        portrait_height = portrait_surface.get_height()

        width_scale = portrait_rectangle.width / portrait_width
        height_scale = portrait_rectangle.height / portrait_height
        portrait_scale = min(width_scale, height_scale)

        scaled_width = int(portrait_width * portrait_scale)
        scaled_height = int(portrait_height * portrait_scale)

        scaled_portrait_surface = pygame.transform.smoothscale(
            portrait_surface,
            (scaled_width, scaled_height),
        )

        portrait_position = scaled_portrait_surface.get_rect(
            center=portrait_rectangle.center
        )

        screen.blit(
            scaled_portrait_surface,
            portrait_position,
        )

    # Renderiza o nome da personagem responsável pela fala.
    def render_speaker_name(
        self,
        screen: pygame.Surface,
        dialogue_box_rectangle: pygame.Rect,
        speaker_name: str,
    ) -> None:
        speaker_surface = self.speaker_font.render(
            speaker_name,
            True,
            SPEAKER_COLOR,
        )

        speaker_position = (
            dialogue_box_rectangle.left
            + PORTRAIT_AREA_WIDTH
            + DIALOGUE_CONTENT_GAP,
            dialogue_box_rectangle.top + DIALOGUE_BOX_PADDING,
        )

        screen.blit(
            speaker_surface,
            speaker_position,
        )

    # Renderiza o texto da fala com quebra automática de linha.
    def render_dialogue_text(
        self,
        screen: pygame.Surface,
        dialogue_box_rectangle: pygame.Rect,
        dialogue_text: str,
    ) -> None:
        text_start_x = (
    dialogue_box_rectangle.left
    + PORTRAIT_AREA_WIDTH
    + DIALOGUE_CONTENT_GAP
)
        text_start_y = dialogue_box_rectangle.top + 65

        maximum_text_width = (
            dialogue_box_rectangle.right
            - text_start_x
            - DIALOGUE_BOX_PADDING
        )

        wrapped_lines = self.wrap_text(
            dialogue_text,
            maximum_text_width,
        )

        line_height = self.text_font.get_linesize()

        for line_index, wrapped_line in enumerate(wrapped_lines):
            text_surface = self.text_font.render(
                wrapped_line,
                True,
                TEXT_COLOR,
            )

            text_position = (
                text_start_x,
                text_start_y + (line_index * line_height),
            )

            screen.blit(
                text_surface,
                text_position,
            )

    # Divide um texto em linhas compatíveis com a largura disponível.
    def wrap_text(
        self,
        dialogue_text: str,
        maximum_width: int,
    ) -> list[str]:
        words = dialogue_text.split()
        wrapped_lines = []
        current_line = ""

        for word in words:
            candidate_line = (
                f"{current_line} {word}".strip()
            )

            candidate_width = self.text_font.size(candidate_line)[0]

            if candidate_width <= maximum_width:
                current_line = candidate_line
                continue

            if current_line:
                wrapped_lines.append(current_line)

            current_line = word

        if current_line:
            wrapped_lines.append(current_line)

        return wrapped_lines

    # Renderiza o indicador utilizado para avançar o diálogo.
    def render_continue_indicator(
        self,
        screen: pygame.Surface,
        dialogue_box_rectangle: pygame.Rect,
    ) -> None:
        continue_surface = self.continue_font.render(
            "[>]",
            True,
            BORDER_COLOR,
        )

        continue_position = continue_surface.get_rect(
            bottomright=(
                dialogue_box_rectangle.right - DIALOGUE_BOX_PADDING,
                dialogue_box_rectangle.bottom - DIALOGUE_BOX_PADDING,
            )
        )

        screen.blit(
            continue_surface,
            continue_position,
        )