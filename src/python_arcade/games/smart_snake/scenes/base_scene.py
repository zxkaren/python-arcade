from abc import ABC, abstractmethod

import pygame


# Define o comportamento obrigatório de todas as cenas da Smart Snake.
class BaseScene(ABC):

    # Processa os eventos recebidos durante a cena.
    @abstractmethod
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        pass

    # Atualiza o estado interno da cena.
    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

    # Renderiza os elementos visuais da cena.
    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        pass