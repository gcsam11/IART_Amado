import pygame
import random

class gameLoop:
    def __init__(self, level):
        self.level = level
        display_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((display_info.current_w, display_info.current_h))
        self.colors = [(255, 255, 0), (0, 0, 255), (255, 0, 0)]  # RGB values for yellow, blue, and red colors
        self.color_dict = {(255, 255, 0):0, (0, 0, 255):1, (255, 0, 0):2}
        self.game_board_start, self.game_board_solution = self.load_level(1)
        self.running = True
        self.cursor_position = (0, 0)

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
        offset = 10
        for i, row in enumerate(game_board):
            for j, color in enumerate(row):
                if (j,i)==self.cursor_position:
                    pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(x + j * square_size + offset*j - 7.5, y + i * square_size + offset*i - 7.5, square_size+15, square_size+15))
                pygame.draw.rect(self.screen, color, pygame.Rect(offset*j + x + j * square_size, offset*i + y + i * square_size, square_size, square_size))


    def is_valid_position(self, position):
        x, y = position
        if x < 0 or x >= len(self.game_board_start[0]) or y < 0 or y >= len(self.game_board_start):
            return False
        return True
    
    def move_cursor(self, next_position):
        x,y = self.cursor_position
        next_x, next_y = next_position
        if self.is_valid_position(next_position):
            self.cursor_position = next_position
        else: 
            return False
        if self.game_board_start[next_y][next_x] != self.game_board_start[y][x]:
            first_color_num = self.color_dict[self.game_board_start[y][x]]
            second_color_num = self.color_dict[self.game_board_start[next_y][next_x]]
            remaining_color_num = 3 - first_color_num - second_color_num
            final_color = self.colors[remaining_color_num]
            self.game_board_start[next_y][next_x]=final_color
        return True


    def update(self, events):
        # Update the game state here
        display_info = pygame.display.Info()

        # Draw the game boards
        self.draw_board(self.game_board_start, (50, 50), 50)
        self.draw_board(self.game_board_solution, (display_info.current_w - 200, 50), 20)

        # Debug print current board
        print("Current Board:")
        for row in self.game_board_start:
            print(row)        

        pygame.display.flip()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Handle up arrow key event
                    current_position = self.cursor_position
                    next_position = (current_position[0], current_position[1] - 1)
                    self.move_cursor(next_position)
                elif event.key == pygame.K_DOWN:
                    # Handle down arrow key event
                    current_position = self.cursor_position
                    next_position = (current_position[0], current_position[1] + 1)
                    self.move_cursor(next_position)
                elif event.key == pygame.K_LEFT:
                    # Handle left arrow key event
                    current_position = self.cursor_position
                    next_position = (current_position[0] - 1, current_position[1])
                    self.move_cursor(next_position)
                elif event.key == pygame.K_RIGHT:
                    # Handle right arrow key event
                    current_position = self.cursor_position
                    next_position = (current_position[0] + 1, current_position[1])
                    self.move_cursor(next_position)

        return True