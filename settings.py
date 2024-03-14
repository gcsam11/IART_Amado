import pygame

class SettingsMenu:
    def __init__(self, screen):
        self.screen = screen
        self.options = ["640x480", "800x600", "1024x768", "1280x960", "Back"]
        self.selected_option = 0
        self.info = pygame.display.Info()  # Get current screen info
        self.selected_resolution = f"{self.info.current_w}x{self.info.current_h}"  # Initialize selected_resolution with current resolution
        self.font = pygame.font.Font(None, self.screen.get_height() // 20)

    def update_screen(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, self.screen.get_height() // 20)  # Update the font size based on the new screen size

    def draw(self):
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                color = (255, 0, 0)  # White color for selected option
            else:
                color = (255, 255, 255)  # Grey color for other options

            text = self.font.render(option, True, color)
            rect = text.get_rect()
            rect.center = (self.screen.get_width() / 2, 200 + i * 60)
            self.screen.blit(text, rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_option]
        return None
                    