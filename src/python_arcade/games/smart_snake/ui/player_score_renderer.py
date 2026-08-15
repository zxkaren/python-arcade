import pygame


SCORE_FONT_NAME = "msgothic"
SCORE_FONT_SIZE = 20

SCORE_TEXT_COLOR = (255, 220, 0)
SCORE_OUTLINE_COLOR = (0, 0, 0)

SCORE_OUTLINE_SIZE = 2
SCORE_DIGITS = 6

SCORE_MARGIN_RIGHT = 24
SCORE_POSITION_Y = 20
SCORE_LINE_GAP = 4
SCORE_LABEL = "SCORE"


class PlayerScoreRenderer:

    # Resumo: inicializa a fonte utilizada para exibir a pontuação.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        self.font = pygame.font.SysFont(
            SCORE_FONT_NAME,
            SCORE_FONT_SIZE,
            bold=True,
        )

    # Resumo: formata a pontuação com zeros à esquerda.
    # Parâmetros: score representa a pontuação atual do jogador.
    # Retorno: texto formatado com quantidade fixa de dígitos.
    def format_score(
        self,
        score: int,
    ) -> str:
        return f"{score:0{SCORE_DIGITS}d}"

    # Resumo: renderiza um texto amarelo com contorno preto.
    # Parâmetros: screen recebe o desenho; text é o conteúdo; position define a posição.
    # Retorno: nenhum.
    def render_outlined_text(
        self,
        screen: pygame.Surface,
        text: str,
        position: tuple[int, int],
    ) -> None:
        position_x, position_y = position

        outline_surface = self.font.render(
            text,
            False,
            SCORE_OUTLINE_COLOR,
        )

        outline_offsets = (
            (-SCORE_OUTLINE_SIZE, 0),
            (SCORE_OUTLINE_SIZE, 0),
            (0, -SCORE_OUTLINE_SIZE),
            (0, SCORE_OUTLINE_SIZE),
            (-SCORE_OUTLINE_SIZE, -SCORE_OUTLINE_SIZE),
            (-SCORE_OUTLINE_SIZE, SCORE_OUTLINE_SIZE),
            (SCORE_OUTLINE_SIZE, -SCORE_OUTLINE_SIZE),
            (SCORE_OUTLINE_SIZE, SCORE_OUTLINE_SIZE),
        )

        for offset_x, offset_y in outline_offsets:
            screen.blit(
                outline_surface,
                (
                    position_x + offset_x,
                    position_y + offset_y,
                ),
            )

        score_surface = self.font.render(
            text,
            False,
            SCORE_TEXT_COLOR,
        )

        screen.blit(
            score_surface,
            position,
        )
    # Resumo: renderiza o título e a pontuação atual no canto superior direito.
    # Parâmetros: screen recebe o desenho; score representa a pontuação atual.
    # Retorno: nenhum.
    def render(
        self,
        screen: pygame.Surface,
        score: int,
    ) -> None:
        formatted_score = self.format_score(
            score=score,
        )

        score_width, score_height = self.font.size(
            formatted_score,
        )
        label_width, _ = self.font.size(
            SCORE_LABEL,
        )

        score_block_width = max(
            score_width,
            label_width,
        )

        score_block_position_x = (
            screen.get_width()
            - SCORE_MARGIN_RIGHT
            - score_block_width
        )

        label_position_x = (
            score_block_position_x
            + (score_block_width - label_width) // 2
        )
        score_position_x = (
            score_block_position_x
            + (score_block_width - score_width) // 2
        )

        self.render_outlined_text(
            screen=screen,
            text=SCORE_LABEL,
            position=(
                label_position_x,
                SCORE_POSITION_Y,
            ),
        )

        self.render_outlined_text(
            screen=screen,
            text=formatted_score,
            position=(
                score_position_x,
                SCORE_POSITION_Y
                + score_height
                + SCORE_LINE_GAP,
            ),
        )