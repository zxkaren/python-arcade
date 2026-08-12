import pygame

from python_arcade.games.smart_snake.config.game_settings import (
    GAME_TITLE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TARGET_FPS,
)
from python_arcade.games.smart_snake.core.scene_manager import SceneManager
from python_arcade.games.smart_snake.scenes.intro_scene import IntroScene
from python_arcade.games.smart_snake.scenes.main_menu_scene import MainMenuScene
from python_arcade.games.smart_snake.scenes.stage_scene import StageScene

# Controla o ciclo principal de execução da Smart Snake.
class SmartSnakeGame:

    # Inicializa os recursos básicos necessários para executar o jogo.
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.is_running = True

        intro_scene = IntroScene(self.show_main_menu)
        self.scene_manager = SceneManager(intro_scene)

    # Mantém o game loop ativo até o jogador encerrar a janela.
    def run(self) -> None:
        try:
            while self.is_running:
                self.handle_events()

                delta_time = self.clock.tick(TARGET_FPS) / 1000.0

                self.scene_manager.update(delta_time)
                self.scene_manager.render(self.screen)

                pygame.display.flip()
        finally:
            pygame.quit()

    # Processa os eventos globais da aplicação.
    def handle_events(self) -> None:
        frame_events = pygame.event.get()

        for game_event in frame_events:
            if game_event.type == pygame.QUIT:
                self.is_running = False

        self.scene_manager.handle_events(frame_events)

    # Exibe o menu principal da Smart Snake.
    def show_main_menu(self) -> None:
        main_menu_scene = MainMenuScene(self.show_stage_one)
        self.scene_manager.change_scene(main_menu_scene)

    # Exibe a primeira fase da aventura.
    def show_stage_one(self) -> None:
        stage_one_scene = StageScene(
            stage_number=1,
            stage_name="RIVERBANK",
        )
        self.scene_manager.change_scene(stage_one_scene)