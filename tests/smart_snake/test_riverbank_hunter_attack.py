from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_AREA_01,
)

# Resumo: garante que o Hunter da Riverbank tenha configuração de ataque válida.
def test_riverbank_hunter_has_attack_configuration() -> None:
    hunter = RIVERBANK_AREA_01.hunters[0]
    hunter_attack = RIVERBANK_AREA_01.hunter_attacks[0]

    assert hunter_attack.hunter_id == hunter.hunter_id
    assert hunter_attack.range_x > 0.0
    assert hunter_attack.range_y > 0.0
    assert hunter_attack.cooldown_duration > 0.0
    assert hunter_attack.animation_frame_duration > 0.0