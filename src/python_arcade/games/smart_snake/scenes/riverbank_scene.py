import pygame

from python_arcade.games.smart_snake.config.game_settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from python_arcade.games.smart_snake.content.hunter_collision import (
    HUNTER_COLLISION_BOX,
)
from python_arcade.games.smart_snake.content.riverbank_areas import (
    RIVERBANK_INITIAL_AREA_ID,
    RIVERBANK_ROAD_MAXIMUM_Y,
    RIVERBANK_ROAD_MINIMUM_Y,
    RIVERBANK_STAGE_AREAS,
)
from python_arcade.games.smart_snake.content.smart_snake_collision import (
    SMART_SNAKE_COLLISION_BOX,
)
from python_arcade.games.smart_snake.controllers.hunter_animation_controller import (
    HunterAnimationController,
)
from python_arcade.games.smart_snake.controllers.hunter_attack_controller import (
    HunterAttackController,
)
from python_arcade.games.smart_snake.controllers.hunter_attack_range_checker import (
    HunterAttackRangeChecker,
)
from python_arcade.games.smart_snake.controllers.hunter_defeat_controller import (
    HunterDefeatController,
)
from python_arcade.games.smart_snake.controllers.hunter_movement_controller import (
    HunterMovementController,
)
from python_arcade.games.smart_snake.controllers.hunter_patrol_controller import (
    HunterPatrolController,
)
from python_arcade.games.smart_snake.controllers.hunter_route_controller import (
    HunterRouteController,
)
from python_arcade.games.smart_snake.controllers.mouse_movement_controller import (
    MouseMovementController,
)
from python_arcade.games.smart_snake.controllers.mouse_projectile_controller import (
    MouseProjectileController,
)
from python_arcade.games.smart_snake.controllers.mouse_projectile_movement_controller import (
    MouseProjectileMovementController,
)
from python_arcade.games.smart_snake.controllers.mouse_route_controller import (
    MouseRouteController,
)
from python_arcade.games.smart_snake.controllers.player_movement_controller import (
    PlayerMovementController,
)
from python_arcade.games.smart_snake.controllers.smart_snake_animation_controller import (
    SmartSnakeAnimationController,
)
from python_arcade.games.smart_snake.domain.hunter import HunterState
from python_arcade.games.smart_snake.domain.player_life_event import (
    PlayerLifeEvent,
)
from python_arcade.games.smart_snake.domain.player_state import PlayerState
from python_arcade.games.smart_snake.domain.score_event import ScoreEvent
from python_arcade.games.smart_snake.domain.smart_snake import SmartSnake
from python_arcade.games.smart_snake.scenes.base_scene import BaseScene
from python_arcade.games.smart_snake.services.mouse_consumption_service import (
    MouseConsumptionService,
)
from python_arcade.games.smart_snake.services.mouse_projectile_hit_service import (
    MouseProjectileHitService,
)
from python_arcade.games.smart_snake.services.mouse_projectile_launcher import (
    MouseProjectileLauncher,
)
from python_arcade.games.smart_snake.services.mouse_spawner import (
    MouseSpawner,
)
from python_arcade.games.smart_snake.services.player_life_service import (
    PlayerLifeService,
)
from python_arcade.games.smart_snake.services.player_score_service import (
    PlayerScoreService,
)
from python_arcade.games.smart_snake.ui.hunter_renderer import (
    HunterRenderer,
)
from python_arcade.games.smart_snake.ui.mouse_projectile_renderer import (
    MouseProjectileRenderer,
)
from python_arcade.games.smart_snake.ui.mouse_renderer import (
    MouseRenderer,
)
from python_arcade.games.smart_snake.ui.player_hud_renderer import (
    PlayerHudRenderer,
)
from python_arcade.games.smart_snake.ui.player_lives_renderer import (
    PlayerLivesRenderer,
)
from python_arcade.games.smart_snake.ui.player_score_renderer import (
    PlayerScoreRenderer,
)
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

SMART_SNAKE_MOVEMENT_SPEED = 250.0
SMART_SNAKE_ANIMATION_FRAME_DURATION = 0.2

MOUSE_MOVEMENT_SPEED = 100.0
MOUSE_PROJECTILE_MOVEMENT_SPEED = 500.0
MOUSE_PROJECTILE_CLEANUP_MARGIN = 100.0

HUNTER_ANIMATION_FRAME_COUNT = 2
HUNTER_ANIMATION_FRAME_DURATION = 0.4

HUNTER_DEFEAT_DURATION = 1.2
HUNTER_DEFEAT_BLINK_COUNT = 2

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

        self.hunter_attack_controller = HunterAttackController(
            range_checker=HunterAttackRangeChecker(),
        )

        self.mouse_renderer = MouseRenderer()
        self.hunter_renderer = HunterRenderer()
        self.mouse_projectile_renderer = MouseProjectileRenderer()
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

        self.hunter_movement_controller = HunterMovementController()
        self.hunter_route_controller = HunterRouteController(
            movement_controller=self.hunter_movement_controller,
        )
        self.hunter_patrol_controller = HunterPatrolController(
            route_controller=self.hunter_route_controller,
        )
        self.hunter_animation_controller = HunterAnimationController(
            frame_count=HUNTER_ANIMATION_FRAME_COUNT,
            frame_duration=HUNTER_ANIMATION_FRAME_DURATION,
        )
        self.hunter_defeat_controller = HunterDefeatController(
            defeat_duration=HUNTER_DEFEAT_DURATION,
            blink_count=HUNTER_DEFEAT_BLINK_COUNT,
        )

        self.hunter_animation_frame_indices: dict[str, int] = {}
        self.removed_hunter_ids: set[str] = set()

        self.smart_snake_animation_controller = (
            SmartSnakeAnimationController(
                frame_count=self.smart_snake_renderer.get_frame_count(),
                frame_duration=SMART_SNAKE_ANIMATION_FRAME_DURATION,
            )
        )

        self.player_state = PlayerState()
        self.player_score_service = PlayerScoreService()

        self.mouse_projectile_controller = MouseProjectileController(
            projectile_launcher=MouseProjectileLauncher(),
            movement_controller=MouseProjectileMovementController(),
        )
        self.mouse_projectile_hit_service = MouseProjectileHitService()

        self.player_life_service = PlayerLifeService()

        self.extra_lives_granted_this_update = 0
        self.player_life_event_this_update = PlayerLifeEvent.NONE
        self.is_game_over = False

        self.mouse_consumption_service = MouseConsumptionService()

        self.player_hud_renderer = PlayerHudRenderer()
        self.player_score_renderer = PlayerScoreRenderer()
        self.player_lives_renderer = PlayerLivesRenderer()

        self.walkable_area_constraint = WalkableAreaConstraint()
        self.scenery_collision_constraint = SceneryCollisionConstraint()

        self.current_animation_frame_index = 0

    # Resumo: processa os eventos recebidos durante a fase.
    # Parâmetros: events contém os eventos capturados pelo Pygame.
    # Retorno: nenhum.
    def handle_events(
        self,
        events: list[pygame.event.Event],
    ) -> None:
        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_SPACE:
                self.mouse_projectile_controller.launch_projectile(
                    smart_snake=self.smart_snake,
                    player_state=self.player_state,
                )

    # Resumo: atualiza movimentação, restrições físicas e animação da Smart Snake.
    def update(
        self,
        delta_time: float,
    ) -> None:
        self.extra_lives_granted_this_update = 0
        self.player_life_event_this_update = PlayerLifeEvent.NONE

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

        self.update_hunter_attacks(
            delta_time=delta_time,
        )

        self.update_hunter_patrols(
            delta_time=delta_time,
        )

        self.update_hunter_animations(
            delta_time=delta_time,
        )

        self.mouse_projectile_controller.update_projectiles(
            movement_speed=MOUSE_PROJECTILE_MOVEMENT_SPEED,
            delta_time=delta_time,
        )

        self.process_mouse_projectile_hits()

        self.update_hunter_defeats(
            delta_time=delta_time,
        )

        self.mouse_projectile_controller.remove_projectiles_outside_bounds(
            minimum_x=-MOUSE_PROJECTILE_CLEANUP_MARGIN,
            maximum_x=SCREEN_WIDTH + MOUSE_PROJECTILE_CLEANUP_MARGIN,
            minimum_y=-MOUSE_PROJECTILE_CLEANUP_MARGIN,
            maximum_y=SCREEN_HEIGHT + MOUSE_PROJECTILE_CLEANUP_MARGIN,
        )

        consumed_mouse = (
            self.mouse_consumption_service.consume_colliding_mouse(
                smart_snake=self.smart_snake,
                mice=self.mice,
            )
        )

        if consumed_mouse is not None:
            self.player_state.process_consumed_mouse()

            self.extra_lives_granted_this_update += (
                self.process_score_event(
                    score_event=ScoreEvent.MOUSE_CONSUMED,
                )
            )

        if not self.is_game_over:
            self.player_life_event_this_update = (
                self.player_life_service.process_health_depletion(
                    player_state=self.player_state,
                )
            )

        if (
            self.player_life_event_this_update
            == PlayerLifeEvent.GAME_OVER
        ):
            self.is_game_over = True

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

    # Resumo: atualiza os ciclos de ataque dos Hunters configurados na área ativa.
    # Parâmetros: delta_time representa o tempo decorrido desde a última atualização.
    def update_hunter_attacks(
        self,
        delta_time: float,
    ) -> None:
        active_area = self.stage_area_manager.get_active_area()

        hunters_by_id = {
            hunter.hunter_id: hunter
            for hunter in active_area.hunters
        }

        for hunter_attack in active_area.hunter_attacks:
            hunter = hunters_by_id.get(
                hunter_attack.hunter_id
            )

            if hunter is None:
                continue

            self.hunter_attack_controller.update(
                hunter=hunter,
                hunter_attack=hunter_attack,
                delta_time=delta_time,
            )

            attack_started = (
                self.hunter_attack_controller.try_start_attack(
                    hunter=hunter,
                    hunter_attack=hunter_attack,
                    target_position_x=self.smart_snake.position_x,
                    target_position_y=self.smart_snake.position_y,
                )
            )

            if not attack_started:
                continue

            self.hunter_animation_controller.reset(
                hunter_id=hunter.hunter_id,
            )

            self.hunter_animation_frame_indices[hunter.hunter_id] = 0

    # Resumo: atualiza as patrulhas configuradas para os Hunters da área ativa.
    def update_hunter_patrols(
        self,
        delta_time: float,
    ) -> None:
        active_area = self.stage_area_manager.get_active_area()

        self.hunter_patrol_controller.update(
            hunters=active_area.hunters,
            hunter_patrols=active_area.hunter_patrols,
            delta_time=delta_time,
        )

    # Resumo: atualiza os frames de animação dos Hunters da área ativa.
    # Parâmetros: delta_time representa o tempo decorrido desde o último frame.
    def update_hunter_animations(
        self,
        delta_time: float,
    ) -> None:
        active_area = self.stage_area_manager.get_active_area()

        patrolling_hunter_ids = {
            hunter_patrol.hunter_id
            for hunter_patrol in active_area.hunter_patrols
        }

        hunter_attacks_by_id = {
            hunter_attack.hunter_id: hunter_attack
            for hunter_attack in active_area.hunter_attacks
        }

        for hunter in active_area.hunters:
            is_animating = (
                hunter.hunter_id in patrolling_hunter_ids
                or hunter.state == HunterState.ATTACKING
            )

            hunter_attack = hunter_attacks_by_id.get(
                hunter.hunter_id
            )

            if (
                hunter.state == HunterState.ATTACKING
                and hunter_attack is not None
            ):
                frame_index = (
                    self.hunter_animation_controller.update(
                        hunter_id=hunter.hunter_id,
                        delta_time=delta_time,
                        is_moving=is_animating,
                        frame_duration=(
                            hunter_attack.animation_frame_duration
                        ),
                    )
                )
            else:
                frame_index = (
                    self.hunter_animation_controller.update(
                        hunter_id=hunter.hunter_id,
                        delta_time=delta_time,
                        is_moving=is_animating,
                    )
                )

            self.hunter_animation_frame_indices[hunter.hunter_id] = (
                frame_index
            )

    # Resumo: processa impactos dos projéteis ativos contra os Hunters da área.
    # Parâmetros: nenhum.
    # Retorno: nenhum.
    def process_mouse_projectile_hits(self) -> None:
        active_area = self.stage_area_manager.get_active_area()

        for hunter in active_area.hunters:
            if hunter.state == HunterState.DEFEATED:
                continue

            self.mouse_projectile_hit_service.hit_target(
                target=hunter,
                target_collision_box=HUNTER_COLLISION_BOX,
                mouse_projectiles=(
                    self.mouse_projectile_controller.active_projectiles
                ),
            )

    # Resumo: finaliza derrotas, remove Hunters do gameplay e concede sua pontuação.
    # Parâmetros: delta_time representa o tempo decorrido desde o último frame.
    def update_hunter_defeats(
        self,
        delta_time: float,
    ) -> None:
        active_area = self.stage_area_manager.get_active_area()

        for hunter in active_area.hunters:
            if hunter.hunter_id in self.removed_hunter_ids:
                continue

            if hunter.state != HunterState.DEFEATED:
                continue

            defeat_finished = self.hunter_defeat_controller.update(
                hunter_id=hunter.hunter_id,
                delta_time=delta_time,
            )

            if not defeat_finished:
                continue

            self.removed_hunter_ids.add(
                hunter.hunter_id,
            )

            self.extra_lives_granted_this_update += (
                self.process_score_event(
                    score_event=ScoreEvent.HUNTER_DEFEATED,
                )
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

        for hunter in active_area.hunters:
            if hunter.hunter_id in self.removed_hunter_ids:
                continue

            if (
                hunter.state == HunterState.DEFEATED
                and not self.hunter_defeat_controller.is_visible(
                    hunter_id=hunter.hunter_id,
                )
            ):
                continue

            self.hunter_renderer.render(
                screen=screen,
                position_x=hunter.position_x,
                position_y=hunter.position_y,
                direction=hunter.direction,
                frame_index=self.hunter_animation_frame_indices.get(
                    hunter.hunter_id,
                    0,
                ),
                state=hunter.state,
            )

        for mouse_projectile in (
            self.mouse_projectile_controller.active_projectiles
        ):
            self.mouse_projectile_renderer.render(
                screen=screen,
                position_x=mouse_projectile.position_x,
                position_y=mouse_projectile.position_y,
                direction_x=mouse_projectile.direction_x,
                direction_y=mouse_projectile.direction_y,
            )

        self.smart_snake_renderer.render(
            screen=screen,
            position_x=self.smart_snake.position_x,
            position_y=self.smart_snake.position_y,
            frame_index=self.current_animation_frame_index,
        )

        self.player_hud_renderer.render_health_bar(
            screen=screen,
            current_health=self.player_state.current_health,
            maximum_health=self.player_state.maximum_health,
        )

        self.player_lives_renderer.render(
            screen=screen,
            lives=self.player_state.lives,
        )

        self.player_hud_renderer.render_mouse_inventory(
            screen=screen,
            stored_mice=self.player_state.stored_mice,
        )

        self.player_score_renderer.render(
            screen=screen,
            score=self.player_state.score,
        )

    # Resumo: processa um evento de pontuação e verifica novos marcos de vida extra.
    # Parâmetros: score_event representa a ação do gameplay que concedeu pontos.
    # Retorno: quantidade de vidas extras concedidas após a atualização do score.
    def process_score_event(
        self,
        score_event: ScoreEvent,
    ) -> int:
        self.player_score_service.process_score_event(
            player_state=self.player_state,
            score_event=score_event,
        )

        return self.player_life_service.process_score_milestones(
            player_state=self.player_state,
        )