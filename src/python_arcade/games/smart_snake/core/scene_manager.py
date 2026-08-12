import pygame

from python_arcade.games.smart_snake.scenes.base_scene import BaseScene


# Controla a cena atualmente exibida pela Smart Snake.
class SceneManager:

    # Inicializa o gerenciador com a primeira cena do jogo.
    # Parâmetros: initial_scene representa a cena que será exibida inicialmente.
    def __init__(self, initial_scene: BaseScene) -> None:
        self.current_scene = initial_scene

    # Substitui a cena atual por uma nova cena.
    # Parâmetros: next_scene representa a próxima cena que será exibida.
    def change_scene(self, next_scene: BaseScene) -> None:
        self.current_scene = next_scene

    # Encaminha os eventos para a cena atualmente ativa.
    # Parâmetros: events contém os eventos capturados pelo Pygame.
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        self.current_scene.handle_events(events)

    # Atualiza a lógica da cena atualmente ativa.
    # Parâmetros: delta_time representa o tempo transcorrido desde o último frame.
    def update(self, delta_time: float) -> None:
        self.current_scene.update(delta_time)

    # Renderiza a cena atualmente ativa.
    # Parâmetros: screen representa a superfície principal do jogo.
    def render(self, screen: pygame.Surface) -> None:
        self.current_scene.render(screen)