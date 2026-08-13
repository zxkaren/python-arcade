import pygame


# Interpreta os comandos do teclado utilizados para movimentar a Smart Snake.
class PlayerMovementController:

    # Resumo: identifica a direção de movimento a partir das teclas pressionadas.
    # Parâmetros: pressed_keys representa o estado atual das teclas do teclado.
    # Retorno: tupla contendo as direções horizontal e vertical.
    def get_movement_direction(
        self,
        pressed_keys: pygame.key.ScancodeWrapper,
    ) -> tuple[float, float]:
        direction_x = 0.0
        direction_y = 0.0

        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            direction_x -= 1.0

        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            direction_x += 1.0

        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            direction_y -= 1.0

        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            direction_y += 1.0

        movement_magnitude = (
            direction_x**2 + direction_y**2
        ) ** 0.5

        if movement_magnitude > 0:
            direction_x /= movement_magnitude
            direction_y /= movement_magnitude

        return direction_x, direction_y