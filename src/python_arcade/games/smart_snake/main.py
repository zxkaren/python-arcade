from python_arcade.games.smart_snake.core.game import SmartSnakeGame

# Inicia a execução principal da Smart Snake.
def start_game() -> None:
    smart_snake_game = SmartSnakeGame()
    smart_snake_game.run()

if __name__ == "__main__":
    start_game()