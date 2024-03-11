import pygame
import random

class gameLoop:
    def __init__(self, level):
        self.level = level
        display_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((display_info.current_w, display_info.current_h))
        self.colors = [(255, 255, 0), (0, 0, 255), (255, 0, 0)]  # RGB values for yellow, blue, and red colors
        self.game_board_start, self.game_board_solution = self.load_level(1)
        self.running = True

    def generate_board(self, board):
        if board == 1:
            # 4x4 square board
            game_board_solution = [[random.choice(self.colors) for _ in range(4)] for _ in range(4)]
            game_board_start = [[random.choice(self.colors) for _ in range(4)] for _ in range(4)]  # Different color for each square
        elif board == 2:
            # 5x5 square without (1,3), (3,1), (5,3), (3,5) squares
            pass
        elif board == 3:
            pass
        elif board == 4:
            # 6x6 square board
            game_board_solution = [[random.choice(self.colors) for _ in range(6)] for _ in range(6)]
            game_board_start = [[random.choice(self.colors) for _ in range(6)] for _ in range(6)]  # Different color for each square
        return game_board_start, game_board_solution

    def load_level(self, board):
        game_board_start, game_board_solution = self.generate_board(board)
        return game_board_start, game_board_solution

    def draw_board(self, game_board, position, square_size):
        x, y = position
        for i, row in enumerate(game_board):
            for j, color in enumerate(row):
                pygame.draw.rect(self.screen, color, pygame.Rect(x + j * square_size, y + i * square_size, square_size, square_size))


    def update(self, events):
        # Update the game state here
        display_info = pygame.display.Info()

        # Draw the game boards
        self.draw_board(self.game_board_start, (50, 50), 50)
        self.draw_board(self.game_board_solution, (display_info.current_w - 200, 50), 20)

        pygame.display.flip()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Handle up arrow key event
                    continue
                elif event.key == pygame.K_DOWN:
                    # Handle down arrow key event
                    continue
                elif event.key == pygame.K_LEFT:
                    # Handle left arrow key event
                    continue
                elif event.key == pygame.K_RIGHT:
                    # Handle right arrow key event
                    continue

        return True