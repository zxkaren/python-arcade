import pygame

from python_arcade.games.smart_snake.config.game_settings import (
    GAME_TITLE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TARGET_FPS,
)

# Controla o ciclo principal de execução da Smart Snake.
class SmartSnakeGame:
    # Resumo: inicializa os recursos básicos necessários para executar o jogo.
    def __init__(self) -> None:

        pygame.init()

        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.is_running = True

    # Resumo: mantém o game loop ativo até o jogador encerrar a janela.
    def run(self) -> None:
        try:
            while self.is_running:
                self.handle_events()
                self.screen.fill((0, 0, 0))

                pygame.display.flip()
                self.clock.tick(TARGET_FPS)
        finally:
            pygame.quit()

    # Resumo: processa os eventos gerados durante a execução do jogo.
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False