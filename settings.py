import pygame

class SettingsMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.options = ["800x600", "1024x768", "1280x720", "1920x1080", "Back"]
        self.back_font = pygame.font.Font(None, 72)
        self.selected_option = 0
        info = pygame.display.Info()  # Get current screen info
        self.selected_resolution = f"{info.current_w}x{info.current_h}"  # Initialize selected_resolution with current resolution

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
                selected_option = self.options[self.selected_option]
                if selected_option == "Back":
                    return "Back"
                else:
                    width, height = map(int, selected_option.split('x'))
                    self.screen = pygame.display.set_mode((width, height))
                    