import pygame

from python_arcade.games.smart_snake.config.game_settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake
from python_arcade.games.smart_snake.scenes.base_scene import BaseScene
from python_arcade.games.smart_snake.ui.smart_snake_renderer import (
    SmartSnakeRenderer,
)
from python_arcade.games.smart_snake.controllers.player_movement_controller import (
    PlayerMovementController,
)
from python_arcade.games.smart_snake.controllers.smart_snake_animation_controller import (
    SmartSnakeAnimationController,
)
from python_arcade.games.smart_snake.ui.riverbank_environment_renderer import (
    RiverbankEnvironmentRenderer,
)
from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_INITIAL_AREA_ID,
    RIVERBANK_STAGE_AREAS,
)
from python_arcade.games.smart_snake.world.stage_area_manager import (
    StageAreaManager,
)

SMART_SNAKE_MOVEMENT_SPEED = 250.0
SMART_SNAKE_ANIMATION_FRAME_DURATION = 0.2


# Representa a primeira área jogável da aventura.
class RiverbankScene(BaseScene):

    # Inicializa a Smart Snake e os recursos visuais da fase.
    # Resumo: inicializa a área ativa, a Smart Snake e os recursos da Riverbank.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def __init__(self) -> None:
        self.stage_area_manager = StageAreaManager(
            stage_areas=RIVERBANK_STAGE_AREAS,
            initial_area_id=RIVERBANK_INITIAL_AREA_ID,
        )

        active_area = self.stage_area_manager.get_active_area()

        self.smart_snake = SmartSnake(
            position_x=active_area.player_spawn_x,
            position_y=active_area.player_spawn_y,
            movement_speed=SMART_SNAKE_MOVEMENT_SPEED,
        )

        self.smart_snake_renderer = SmartSnakeRenderer()

        self.riverbank_environment_renderer = RiverbankEnvironmentRenderer(
            background_asset_name=active_area.background_asset_name,
        )

        self.player_movement_controller = PlayerMovementController()

        self.smart_snake_animation_controller = SmartSnakeAnimationController(
            frame_count=self.smart_snake_renderer.get_frame_count(),
            frame_duration=SMART_SNAKE_ANIMATION_FRAME_DURATION,
        )

        self.current_animation_frame_index = 0
    # Processa os eventos recebidos durante a fase.
    def handle_events(
        self,
        events: list[pygame.event.Event],
    ) -> None:
        return

    # Resumo: atualiza a movimentação e a animação da Smart Snake.
    # Parâmetros: delta_time representa o tempo transcorrido desde o último frame.
    # Retorno: nenhum.
    def update(
        self,
        delta_time: float,
    ) -> None:
        pressed_keys = pygame.key.get_pressed()

        direction_x, direction_y = (
            self.player_movement_controller.get_movement_direction(
                pressed_keys
            )
        )

        is_moving = direction_x != 0.0 or direction_y != 0.0

        self.smart_snake.move(
            direction_x=direction_x,
            direction_y=direction_y,
            delta_time=delta_time,
        )

        self.constrain_smart_snake_to_screen()

        self.current_animation_frame_index = (
            self.smart_snake_animation_controller.update(
                delta_time=delta_time,
                is_moving=is_moving,
            )
        )

        self.constrain_smart_snake_to_screen()

    # Resumo: mantém todo o sprite da Smart Snake dentro da área visível do jogo.
    def constrain_smart_snake_to_screen(self) -> None:
        sprite_width, sprite_height = (
            self.smart_snake_renderer.get_sprite_size()
        )

        horizontal_margin = sprite_width / 2
        vertical_margin = sprite_height / 2

        minimum_position_x = horizontal_margin
        maximum_position_x = SCREEN_WIDTH - horizontal_margin

        minimum_position_y = vertical_margin
        maximum_position_y = SCREEN_HEIGHT - vertical_margin

        self.smart_snake.position_x = max(
            minimum_position_x,
            min(
                self.smart_snake.position_x,
                maximum_position_x,
            ),
        )

        self.smart_snake.position_y = max(
            minimum_position_y,
            min(
                self.smart_snake.position_y,
                maximum_position_y,
            ),
        )

    # Resumo: renderiza o cenário Riverbank e a Smart Snake.
    # Parâmetros: screen representa a superfície principal do jogo.
    # Retorno: nenhum.
    def render(
        self,
        screen: pygame.Surface,
    ) -> None:
        self.riverbank_environment_renderer.render_background(
            screen=screen,
        )

        self.smart_snake_renderer.render(
            screen=screen,
            position_x=self.smart_snake.position_x,
            position_y=self.smart_snake.position_y,
            frame_index=self.current_animation_frame_index,
        )