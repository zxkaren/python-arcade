from unittest.mock import Mock

from python_arcade.games.smart_snake.controllers.hunter_attack_controller import (
    HunterAttackController,
)
from python_arcade.games.smart_snake.controllers.hunter_attack_range_checker import (
    HunterAttackRangeChecker,
)
from python_arcade.games.smart_snake.domain.hunter import Hunter
from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    RiverbankScene,
)
from python_arcade.games.smart_snake.world.hunter_attack import HunterAttack


# Resumo: garante que o impacto do Hunter cause dano uma única vez no ataque.
def test_riverbank_applies_hunter_attack_damage_once() -> None:
    hunter = Hunter(
        hunter_id="hunter_01",
        position_x=1050.0,
        position_y=500.0,
    )

    hunter_attack = HunterAttack(
        hunter_id="hunter_01",
        range_x=220.0,
        range_y=100.0,
        damage_points=50,
        attack_duration=0.6,
        animation_frame_duration=0.3,
        cooldown_duration=1.0,
    )

    active_area = Mock()
    active_area.hunters = (hunter,)
    active_area.hunter_attacks = (hunter_attack,)

    stage_area_manager = Mock()
    stage_area_manager.get_active_area.return_value = active_area

    smart_snake = Mock()
    smart_snake.position_x = 900.0
    smart_snake.position_y = 500.0

    riverbank_scene = RiverbankScene.__new__(RiverbankScene)
    riverbank_scene.stage_area_manager = stage_area_manager
    riverbank_scene.smart_snake = smart_snake
    riverbank_scene.player_state = PlayerState()
    riverbank_scene.hunter_attack_controller = HunterAttackController(
        range_checker=HunterAttackRangeChecker(),
    )
    riverbank_scene.hunter_animation_controller = Mock()
    riverbank_scene.hunter_animation_frame_indices = {}

    riverbank_scene.update_hunter_attacks(
        delta_time=0.0,
    )

    assert riverbank_scene.player_state.current_health == 100

    riverbank_scene.update_hunter_attacks(
        delta_time=0.3,
    )

    assert riverbank_scene.player_state.current_health == 50

    riverbank_scene.update_hunter_attacks(
        delta_time=0.1,
    )

    assert riverbank_scene.player_state.current_health == 50