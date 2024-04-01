import pygame

class TutorialMenu:
    def __init__(self, screen):
        self.screen = screen
        self.title = "AMADO"
        self.ai_options = ["0 -> BFS",
        "1 -> DFS", 
        "2 -> Simple Greedy", 
        "3 -> Color Cluster Greedy",
        "4 -> A* Simple", 
        "5 -> A* Color Cluster",
        "6 -> Depth Limited", 
        "7 -> Iterative Deepening"]
        self.selected_option = 0
        self.update_fonts()

    # Update the screen and adjust the font sizes accordingly
    def update_screen(self, screen):
        self.screen = screen
        self.update_fonts()

    # Adjust the font size based on the screen size
    def update_fonts(self):
        # Adjust the font size based on the screen size
        title_font_size = self.screen.get_height() // 10
        option_font_size = self.screen.get_height() // 20

        self.title_font = pygame.font.Font(None, title_font_size)
        self.option_font = pygame.font.Font(None, option_font_size)

    # Draw the tutorial menu
    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black color

        # Draw the title
        title = self.title_font.render(self.title, True, (255, 255, 255))
        title_position = ((self.screen.get_width() - title.get_width()) // 2, self.screen.get_height() // 10)  # Position the title at 1/10th of the screen height
        self.screen.blit(title, title_position)

        # Draw the tutorial keys
        text = self.option_font.render("Use the arrow keys to move the player", True, (255, 255, 255))
        text_position = ((self.screen.get_width() - text.get_width()) // 2, self.screen.get_height() // 4)  # Position the options at 1/4th of the screen height
        self.screen.blit(text, text_position)

        text = self.option_font.render("When entering the game, you can play it yourself", True, (255, 255, 255))
        text_position = ((self.screen.get_width() - text.get_width()) // 2, self.screen.get_height() // 4 + 30)  # Position the options at 1/4th of the screen height, with 30 pixels between each option
        self.screen.blit(text, text_position)

        text = self.option_font.render("Or choose to enable the AI:", True, (255, 255, 255))
        text_position = ((self.screen.get_width() - text.get_width()) // 2, self.screen.get_height() // 4 + 60)  # Position the options at 1/4th of the screen height, with 60 pixels between each option
        self.screen.blit(text, text_position)

        # Loop through the ai_options array and print each option
        for i, option in enumerate(self.ai_options):
            text = self.option_font.render(option, True, (255, 255, 255))
            text_position = ((self.screen.get_width() - text.get_width()) // 2, self.screen.get_height() // 4 + 80 + i * 20)  # Position the options at 1/4th of the screen height, with 20 pixels between each option
            self.screen.blit(text, text_position)

        pygame.display.flip()

    # Tutorial Menu Input Handler
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.ai_options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.ai_options)
            elif event.key == pygame.K_ESCAPE:
                return "Back"