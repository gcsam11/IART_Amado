import pygame
from menu import Menu
from settings import SettingsMenu

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    menu = Menu(screen)
    settingsMenu = SettingsMenu(screen)
    current_menu = "main"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif current_menu == "main":
                result = menu.handle_input(event)
                if result == "Play":
                    # Call the game loop here
                    continue
                elif result == "Settings":
                    # Call the settings screen here
                    current_menu = "settings"
                    continue
                elif result == "Quit":
                    pygame.quit()
            elif current_menu == "settings":
                result = settingsMenu.handle_input(event)
                if result == "Back":
                    current_menu = "main"


        screen.fill((0, 0, 0))  # Fill the screen with black color

        if current_menu == "main":
            menu.draw()
        elif current_menu == "settings":
            settingsMenu.draw()

        pygame.display.update()

if __name__ == "__main__":
    main()