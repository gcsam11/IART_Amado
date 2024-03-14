import pygame

class LevelMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 72)  # Larger font for the title
        self.options = ["Level 1", "Level 2", "Level 3", "Back"]
        self.selected_option = 0
        self.title = "AMADO"
        self.update_fonts()

    def draw(self):
        # Draw the title
        title = self.title_font.render(self.title, True, (255, 255, 255))
        title_position = ((self.screen.get_width() - title.get_width()) // 2, 50)
        self.screen.blit(title, title_position)

        # Draw the menu options
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                color = (255, 0, 0)  # Red color for selected option
            else:
                color = (255, 255, 255)  # White color for other options
            text = self.option_font.render(option, True, color)
            self.screen.blit(text, (50, 150 + i * 50))  # Adjust the position to avoid overlapping with the title
        
    def update_screen(self, screen):
        self.screen = screen
        self.update_fonts()

    def update_fonts(self):
        # Adjust the font size based on the screen size
        title_font_size = self.screen.get_height() // 10
        option_font_size = self.screen.get_height() // 20

        self.title_font = pygame.font.Font(None, title_font_size)
        self.option_font = pygame.font.Font(None, option_font_size)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                selected_option = self.options[self.selected_option]
                if selected_option == "Back":
                    return "Back"
                else:
                    return self.options[self.selected_option]