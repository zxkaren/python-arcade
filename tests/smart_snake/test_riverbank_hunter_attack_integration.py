from unittest.mock import Mock

from python_arcade.games.smart_snake.scenes.riverbank_scene import (
    RiverbankScene,
)


# Resumo: valida se a cena utiliza a configuração de ataque da área ativa.
def test_update_hunter_attacks_uses_active_area_configuration() -> None:
    hunter = Mock()
    hunter.hunter_id = "hunter_01"

    hunter_attack = Mock()
    hunter_attack.hunter_id = "hunter_01"

    active_area = Mock()
    active_area.hunters = (hunter,)
    active_area.hunter_attacks = (hunter_attack,)

    stage_area_manager = Mock()
    stage_area_manager.get_active_area.return_value = active_area

    smart_snake = Mock()
    smart_snake.position_x = 900.0
    smart_snake.position_y = 450.0

    hunter_attack_controller = Mock()
    hunter_attack_controller.try_start_attack.return_value = False

    riverbank_scene = RiverbankScene.__new__(RiverbankScene)
    riverbank_scene.stage_area_manager = stage_area_manager
    riverbank_scene.smart_snake = smart_snake
    riverbank_scene.hunter_attack_controller = hunter_attack_controller

    riverbank_scene.update_hunter_attacks(
        delta_time=0.1,
    )

    hunter_attack_controller.update.assert_called_once_with(
        hunter=hunter,
        hunter_attack=hunter_attack,
        delta_time=0.1,
    )

    hunter_attack_controller.try_start_attack.assert_called_once_with(
        hunter=hunter,
        hunter_attack=hunter_attack,
        target_position_x=900.0,
        target_position_y=450.0,
    )


# Resumo: valida se um novo ataque reinicia a animação no primeiro frame.
def test_update_hunter_attacks_resets_animation_when_attack_starts() -> None:
    hunter = Mock()
    hunter.hunter_id = "hunter_01"

    hunter_attack = Mock()
    hunter_attack.hunter_id = "hunter_01"

    active_area = Mock()
    active_area.hunters = (hunter,)
    active_area.hunter_attacks = (hunter_attack,)

    stage_area_manager = Mock()
    stage_area_manager.get_active_area.return_value = active_area

    smart_snake = Mock()
    smart_snake.position_x = 900.0
    smart_snake.position_y = 450.0

    hunter_attack_controller = Mock()
    hunter_attack_controller.try_start_attack.return_value = True

    hunter_animation_controller = Mock()

    riverbank_scene = RiverbankScene.__new__(RiverbankScene)
    riverbank_scene.stage_area_manager = stage_area_manager
    riverbank_scene.smart_snake = smart_snake
    riverbank_scene.hunter_attack_controller = hunter_attack_controller
    riverbank_scene.hunter_animation_controller = (
        hunter_animation_controller
    )
    riverbank_scene.hunter_animation_frame_indices = {
        "hunter_01": 1,
    }

    riverbank_scene.update_hunter_attacks(
        delta_time=0.1,
    )

    hunter_animation_controller.reset.assert_called_once_with(
        hunter_id="hunter_01",
    )

    assert (
        riverbank_scene.hunter_animation_frame_indices["hunter_01"]
        == 0
    )