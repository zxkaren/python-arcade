from unittest.mock import Mock

from python_arcade.games.smart_snake.core.scene_manager import SceneManager


# Valida se o SceneManager inicia com a cena informada.
def test_scene_manager_starts_with_initial_scene() -> None:
    initial_scene = Mock()

    scene_manager = SceneManager(initial_scene)

    assert scene_manager.current_scene is initial_scene


# Valida se o SceneManager substitui corretamente a cena ativa.
def test_scene_manager_changes_current_scene() -> None:
    initial_scene = Mock()
    next_scene = Mock()

    scene_manager = SceneManager(initial_scene)
    scene_manager.change_scene(next_scene)

    assert scene_manager.current_scene is next_scene

# Valida se os eventos são encaminhados para a cena ativa.
def test_scene_manager_forwards_events_to_current_scene() -> None:
    current_scene = Mock()
    frame_events = []

    scene_manager = SceneManager(current_scene)
    scene_manager.handle_events(frame_events)

    current_scene.handle_events.assert_called_once_with(frame_events)


# Valida se a atualização é encaminhada para a cena ativa.
def test_scene_manager_updates_current_scene() -> None:
    current_scene = Mock()
    delta_time = 0.016

    scene_manager = SceneManager(current_scene)
    scene_manager.update(delta_time)

    current_scene.update.assert_called_once_with(delta_time)


# Valida se a renderização é encaminhada para a cena ativa.
def test_scene_manager_renders_current_scene() -> None:
    current_scene = Mock()
    screen = Mock()

    scene_manager = SceneManager(current_scene)
    scene_manager.render(screen)

    current_scene.render.assert_called_once_with(screen)