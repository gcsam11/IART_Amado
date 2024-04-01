import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.options = ["Play", "Settings", "Tutorial", "Quit"]
        self.selected_option = 0
        self.title = "AMADO"
        self.update_fonts()

    # Update the screen and adjust the font sizes accordingly
    def update_screen(self, screen):
        self.screen = screen
        self.update_fonts()

    # Adjust the font size based on the screen size
    def update_fonts(self):
        title_font_size = self.screen.get_height() // 10
        option_font_size = self.screen.get_height() // 20

        self.title_font = pygame.font.Font(None, title_font_size)
        self.option_font = pygame.font.Font(None, option_font_size)

    # Drawing Menu Function
    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black color
        # Draw the title
        title = self.title_font.render(self.title, True, (255, 255, 255))
        title_position = ((self.screen.get_width() - title.get_width()) // 2, self.screen.get_height() // 10)
        self.screen.blit(title, title_position)

        # Draw the menu options
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                color = (255, 0, 0)  # Red color for selected option
            else:
                color = (255, 255, 255)  # White color for other options
            text = self.option_font.render(option, True, color)
            text_position = ((self.screen.get_width() - text.get_width()) // 2, self.screen.get_height() // 2 + i * 50)
            self.screen.blit(text, text_position)

    # Menu Input Handler
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_option]