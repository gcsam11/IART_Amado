import pygame
import random

class gameLoop:
    def __init__(self, level, board, remaining_time=0, lives=3):
        self.level = level
        self.totalBoards = 5
        self.move_count = 0
        self.board = board
        display_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((display_info.current_w, display_info.current_h))
        self.colors = [(255, 255, 0), (0, 0, 255), (255, 0, 0)]  # RGB values for yellow, blue, and red colors
        self.color_dict = {(255, 255, 0):0, (0, 0, 255):1, (255, 0, 0):2}
        self.cursor_position = (0, 0)
        self.game_board_start, self.game_board_solution = self.load_level(self.board)
        self.regression_algorithm(level)
        self.moved = False
        self.font = pygame.font.Font(None, 36)
        self.timer = 180 if (70+remaining_time) > 180 else 70+remaining_time
        self.timer_text = str(self.timer).rjust(3)
        self.timer_text_update = self.font.render(self.timer_text, True, (255, 255, 255))
        self.lives = lives
        self.running = True
    
    def regression_algorithm(self, difficulty):
        if difficulty == 1:
            steps = 5*len(self.game_board_start)
        elif difficulty == 2:
            steps = 10*len(self.game_board_start)
        elif difficulty == 3:
            steps = 20*len(self.game_board_start)
        original_cursor = self.cursor_position
        row = random.randint(0, len(self.game_board_start)-1)
        valid_list = [x for x in range(len(self.game_board_start[row])) if self.game_board_start[row][x] != (0,0,0)]
        col = random.choice(valid_list)
        self.cursor_position = (col, row)
        for _ in range(steps):
            direction = random.choice(["up", "down", "left", "right"])
            if direction == "up":
                if (not self.move_cursor((self.cursor_position[0], self.cursor_position[1]-1))):
                    steps+=1
            elif direction == "down":
                if (not self.move_cursor((self.cursor_position[0], self.cursor_position[1]+1))):
                    steps+=1
            elif direction == "left":
                if (not self.move_cursor((self.cursor_position[0]-1, self.cursor_position[1]))):
                    steps+=1
            elif direction == "right":
                if (not self.move_cursor((self.cursor_position[0]+1, self.cursor_position[1]))):
                    steps+=1
        self.cursor_position = original_cursor

    def update_screen(self, screen):
        self.screen = screen

    def generate_board(self, board):
        if board == 1:
            # 4x4 square board
            game_board_solution = [[random.choice(self.colors) for _ in range(4)] for _ in range(4)]
        elif board == 2:
            # 5x5 square without (1,3), (3,1), (5,3), (3,5) squares
            game_board_solution = [[random.choice(self.colors) for _ in range(5)] for _ in range(5)]
            game_board_solution[0][2] = (0,0,0)
            game_board_solution[2][0] = (0,0,0)
            game_board_solution[4][2] = (0,0,0)
            game_board_solution[2][4] = (0,0,0)
        elif board == 3:
            # 8x8 board without a few spots
            game_board_solution = [[random.choice(self.colors) for _ in range(8)] for _ in range(8)]
            for i in range(0, 8):
                for j in range(0, 8):
                    if i == 0 and j in [0, 4, 5, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 1 and j in [3, 4, 5, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 2 and j in [6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 3 and j in [1, 3, 5, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 4 and j in [0, 1]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 5 and j in [0, 1, 3, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 6 and j in [0, 1, 2, 3, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
                    elif i == 7 and j in [0, 1, 2, 3, 5, 6, 7]:
                        game_board_solution[i][j] = (0, 0, 0)
            self.cursor_position = (0, 1)
        elif board == 4:
            # 6x6 square board
            game_board_solution = [[random.choice(self.colors) for _ in range(6)] for _ in range(6)]
        elif board == 5:
            # 8x8 razor board
            game_board_solution = [[(0,0,0) for _ in range(8)] for _ in range(8)]
            for i in range(8):
                for j in range(8):
                    if not ((i == 0 and j in [0, 1, 2, 3, 5, 6, 7]) or \
                    (i == 1 and j in [0, 1, 2, 7]) or \
                    (i == 2 and j in [0, 1, 5, 7]) or \
                    (i == 3 and j in [0, 4]) or \
                    (i == 4 and j in [3, 7]) or \
                    (i == 5 and j in [0, 2, 6, 7]) or \
                    (i == 6 and j in [0, 1, 5, 6, 7]) or \
                    (i == 7 and j in [0, 1, 2, 4, 5, 6, 7])):
                        game_board_solution[i][j] = random.choice(self.colors)
            self.cursor_position = (4,0)
        game_board_start = []
        for list in game_board_solution:
            game_board_start.append(list.copy())
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
        if x < 0 or x >= len(self.game_board_start[0]) or y < 0 or y >= len(self.game_board_start) or self.game_board_start[y][x] == (0,0,0):
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
    
    def board_is_solved(self):
        return self.game_board_start == self.game_board_solution

    def update(self, event):
        if event.type == pygame.USEREVENT:
            if self.moved == True:
                self.timer -= 1
                if self.timer > 0:
                    self.timer_text = str(self.timer).rjust(3)
                elif self.lives == 1:
                    self.timer_text = 'Game Over!'
                    self.lives -= 1
                else:
                    self.timer_text = 'Time\'s up!'
                    self.lives -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_count += 1
                # Handle up arrow key event
                current_position = self.cursor_position
                next_position = (current_position[0], current_position[1] - 1)
                self.move_cursor(next_position)
                if (not self.moved):
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    self.moved = True
            elif event.key == pygame.K_DOWN:
                self.move_count += 1
                # Handle down arrow key event
                current_position = self.cursor_position
                next_position = (current_position[0], current_position[1] + 1)
                self.move_cursor(next_position)
                if (not self.moved):
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    self.moved = True
            elif event.key == pygame.K_LEFT:
                self.move_count += 1
                # Handle left arrow key event
                current_position = self.cursor_position
                next_position = (current_position[0] - 1, current_position[1])
                self.move_cursor(next_position)
                if (not self.moved):
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    self.moved = True
            elif event.key == pygame.K_RIGHT:
                self.move_count += 1
                # Handle right arrow key event
                current_position = self.cursor_position
                next_position = (current_position[0] + 1, current_position[1])
                self.move_cursor(next_position)
                if (not self.moved):
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    self.moved = True

        self.draw_aux()

        if self.timer <= 0:
            return False
        return True
    
    def draw_aux(self):
        # Update the game state here
        display_info = pygame.display.Info()

        square_size = int(display_info.current_w * (5 / 100))
        square_solution_size = int(display_info.current_w * (2.5 / 100))

        self.screen.fill((0, 0, 0))

        # Draw a line that separates the solution from the board
        pygame.draw.line(self.screen, (255, 0, 0), (display_info.current_w - (len(self.game_board_solution[0]) * square_solution_size) - 100, 10), (display_info.current_w - (len(self.game_board_solution[0]) * square_solution_size) - 100, display_info.current_h - 10), 5)

        # Calculate the coordinates for the game board based on the screen width and height
        game_board_x = (display_info.current_w - (len(self.game_board_solution[0]) * square_solution_size) - 100 - (len(self.game_board_start[0]) * square_size)) / 2
        game_board_y = display_info.current_h / 2 - (square_size * len(self.game_board_start) / 2)

        # Draw the game board with the calculated coordinates
        self.draw_board(self.game_board_start, (game_board_x, game_board_y), square_size)

        # Draw the solution board
        self.draw_board(self.game_board_solution, (display_info.current_w - (len(self.game_board_solution[0]) * square_solution_size) - 75, 50), square_solution_size)
        self.screen.blit(self.font.render("Move Count: " + str(self.move_count), True, (255, 255, 255)), (10, 10))
        self.screen.blit(self.font.render("Lives: " + str(self.lives), True, (255, 255, 255)), (250, 10))
        bar_width = 50
        bar_height = 10
        num_bars = self.timer // 5

        if self.timer % 5 == 0:
            self.timer_text_update = self.font.render(str(self.timer), True, (255, 255, 255))

        self.screen.blit(self.timer_text_update, (display_info.current_w - self.timer_text_update.get_width() - 10, display_info.current_h - self.timer_text_update.get_height() - 10))        

        for i in range(min(num_bars, 19)):
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(display_info.current_w - (10 + bar_width) - self.timer_text_update.get_width() - 10, display_info.current_h - (10 + (i+1) * (bar_height + 5)), bar_width, bar_height))

        pygame.display.flip()
    
    def ai_move(self, movelist):
        for move in movelist:
            self.move_cursor(move)
