import pygame

from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_INITIAL_AREA_ID,
    RIVERBANK_STAGE_AREAS,
)
from python_arcade.games.smart_snake.content.smart_snake_collision import (
    SMART_SNAKE_COLLISION_BOX,
)
from python_arcade.games.smart_snake.controllers.player_movement_controller import (
    PlayerMovementController,
)
from python_arcade.games.smart_snake.controllers.smart_snake_animation_controller import (
    SmartSnakeAnimationController,
)
from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake
from python_arcade.games.smart_snake.scenes.base_scene import BaseScene
from python_arcade.games.smart_snake.ui.riverbank_environment_renderer import (
    RIVERBANK_ASSETS_DIRECTORY,
    RiverbankEnvironmentRenderer,
)
from python_arcade.games.smart_snake.ui.scenery_renderer import (
    SceneryRenderer,
)
from python_arcade.games.smart_snake.ui.smart_snake_renderer import (
    SmartSnakeRenderer,
)
from python_arcade.games.smart_snake.world.scenery_collision_constraint import (
    SceneryCollisionConstraint,
)
from python_arcade.games.smart_snake.world.stage_area_manager import (
    StageAreaManager,
)
from python_arcade.games.smart_snake.world.walkable_area_constraint import (
    WalkableAreaConstraint,
)
from python_arcade.games.smart_snake.domain.mouse import Mouse
from python_arcade.games.smart_snake.ui.mouse_renderer import (
    MouseRenderer,
)
from python_arcade.games.smart_snake.controllers.mouse_movement_controller import (
    MouseMovementController,
)
from python_arcade.games.smart_snake.controllers.mouse_route_controller import (
    MouseRouteController,
)
from python_arcade.games.smart_snake.services.mouse_spawner import (
    MouseSpawner,
)
from python_arcade.games.smart_snake.domain.mouse import Mouse
from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_INITIAL_AREA_ID,
    RIVERBANK_ROAD_MAXIMUM_Y,
    RIVERBANK_ROAD_MINIMUM_Y,
    RIVERBANK_STAGE_AREAS,
)
from python_arcade.games.smart_snake.services.mouse_consumption_service import (
    MouseConsumptionService,
)

SMART_SNAKE_MOVEMENT_SPEED = 250.0
SMART_SNAKE_ANIMATION_FRAME_DURATION = 0.2

MOUSE_MOVEMENT_SPEED = 100.0

RIVERBANK_ROAD_CENTER_Y = (
    RIVERBANK_ROAD_MINIMUM_Y
    + RIVERBANK_ROAD_MAXIMUM_Y
) / 2

# Representa a primeira área jogável da aventura.
class RiverbankScene(BaseScene):

    # Resumo: inicializa a área ativa, a Smart Snake e os recursos da Riverbank.
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

        self.mice = MouseSpawner().spawn_from_bushes(
            scenery_objects=active_area.scenery_objects,
            road_center_y=RIVERBANK_ROAD_CENTER_Y,
        )
        self.mouse_renderer = MouseRenderer()
        self.smart_snake_renderer = SmartSnakeRenderer()

        self.riverbank_environment_renderer = RiverbankEnvironmentRenderer(
            background_asset_name=active_area.background_asset_name,
        )

        self.scenery_renderer = SceneryRenderer(
            assets_directory=RIVERBANK_ASSETS_DIRECTORY,
        )

        self.player_movement_controller = PlayerMovementController()
        self.mouse_movement_controller = MouseMovementController()
        self.mouse_route_controller = MouseRouteController(
            movement_controller=self.mouse_movement_controller,
        )
        self.mouse_route_controller = MouseRouteController(
        movement_controller=self.mouse_movement_controller,
        )
        self.smart_snake_animation_controller = SmartSnakeAnimationController(
            frame_count=self.smart_snake_renderer.get_frame_count(),
            frame_duration=SMART_SNAKE_ANIMATION_FRAME_DURATION,
        )
        self.mouse_consumption_service = MouseConsumptionService()

        self.walkable_area_constraint = WalkableAreaConstraint()
        self.scenery_collision_constraint = SceneryCollisionConstraint()

        self.current_animation_frame_index = 0

    # Resumo: processa os eventos recebidos durante a fase.
    def handle_events(
        self,
        events: list[pygame.event.Event],
    ) -> None:
        return

    # Resumo: atualiza movimentação, restrições físicas e animação da Smart Snake.
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

        previous_position_x = self.smart_snake.position_x
        previous_position_y = self.smart_snake.position_y

        self.smart_snake.move(
            direction_x=direction_x,
            direction_y=direction_y,
            delta_time=delta_time,
        )

        self.constrain_smart_snake_to_walkable_area()

        self.constrain_smart_snake_to_scenery(
            previous_position_x=previous_position_x,
            previous_position_y=previous_position_y,
        )

        self.current_animation_frame_index = (
            self.smart_snake_animation_controller.update(
                delta_time=delta_time,
                is_moving=is_moving,
            )
        )
        self.update_mice_routes(
            delta_time=delta_time,
        )
        self.mouse_consumption_service.consume_colliding_mouse(
        smart_snake=self.smart_snake,
        mice=self.mice,
        )

    # Resumo: mantém todo o sprite da Smart Snake dentro da área caminhável ativa.
    def constrain_smart_snake_to_walkable_area(self) -> None:
        active_area = self.stage_area_manager.get_active_area()

        sprite_width, sprite_height = (
            self.smart_snake_renderer.get_sprite_size()
        )

        constrained_position_x, constrained_position_y = (
            self.walkable_area_constraint.constrain_position(
                position_x=self.smart_snake.position_x,
                position_y=self.smart_snake.position_y,
                sprite_width=float(sprite_width),
                sprite_height=float(sprite_height),
                walkable_area=active_area.walkable_area,
            )
        )

        self.smart_snake.position_x = constrained_position_x
        self.smart_snake.position_y = constrained_position_y

    # Resumo: impede que a Smart Snake ocupe o espaço de obstáculos do cenário.
    def constrain_smart_snake_to_scenery(
        self,
        previous_position_x: float,
        previous_position_y: float,
    ) -> None:
        active_area = self.stage_area_manager.get_active_area()

        constrained_position_x, constrained_position_y = (
            self.scenery_collision_constraint.constrain_position(
                previous_position_x=previous_position_x,
                previous_position_y=previous_position_y,
                target_position_x=self.smart_snake.position_x,
                target_position_y=self.smart_snake.position_y,
                collision_box=SMART_SNAKE_COLLISION_BOX,
                scenery_objects=active_area.scenery_objects,
            )
        )

        self.smart_snake.position_x = constrained_position_x
        self.smart_snake.position_y = constrained_position_y
    
    # Resumo: atualiza as trajetórias verticais de todos os ratos ativos na Riverbank.
    # Parâmetros: delta_time representa o tempo decorrido desde a última atualização.
    # Retorno: nenhum.
    def update_mice_routes(
        self,
        delta_time: float,
    ) -> None:
        for mouse in self.mice:
            if mouse.home_position_y < RIVERBANK_ROAD_CENTER_Y:
                away_target_y = RIVERBANK_ROAD_MAXIMUM_Y
            else:
                away_target_y = RIVERBANK_ROAD_MINIMUM_Y

            self.mouse_route_controller.update(
                mouse=mouse,
                away_target_y=away_target_y,
                movement_speed=MOUSE_MOVEMENT_SPEED,
                delta_time=delta_time,
            )

    # Resumo: renderiza o cenário Riverbank, seus objetos e a Smart Snake.
    def render(
        self,
        screen: pygame.Surface,
    ) -> None:
        self.riverbank_environment_renderer.render_background(
            screen=screen,
        )

        active_area = self.stage_area_manager.get_active_area()

        self.scenery_renderer.render(
            screen=screen,
            scenery_objects=active_area.scenery_objects,
        )

        for mouse in self.mice:
            self.mouse_renderer.render(
                screen=screen,
                position_x=mouse.position_x,
                position_y=mouse.position_y,
                direction=mouse.direction,
            )

        self.smart_snake_renderer.render(
            screen=screen,
            position_x=self.smart_snake.position_x,
            position_y=self.smart_snake.position_y,
            frame_index=self.current_animation_frame_index,
        )