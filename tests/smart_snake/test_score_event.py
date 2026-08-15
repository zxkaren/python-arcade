from python_arcade.games.smart_snake.domain.score_event import ScoreEvent


# Resumo: valida a pontuação concedida ao consumir um rato.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_score_event_defines_mouse_consumed_score() -> None:
    assert ScoreEvent.MOUSE_CONSUMED.value == 50


# Resumo: valida a pontuação concedida ao derrotar um Hunter comum.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_score_event_defines_hunter_defeated_score() -> None:
    assert ScoreEvent.HUNTER_DEFEATED.value == 100


# Resumo: valida a pontuação concedida ao derrotar o Chief Hunter.
# Parâmetros: nenhum.
# Retorno: nenhum.
def test_score_event_defines_chief_hunter_defeated_score() -> None:
    assert ScoreEvent.CHIEF_HUNTER_DEFEATED.value == 500