import pygame
from menu import Menu
from settings import SettingsMenu
from levelMenu import LevelMenu
from gameLoop import gameLoop

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    menu = Menu(screen)
    settingsMenu = SettingsMenu(screen)
    levelMenu = LevelMenu(screen)
    current_menu = "main"
    game = None

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game is not None:
                        game = None
                    current_menu = "main"
            screen.fill((0, 0, 0))  # Fill the screen with black color
            if current_menu == "main":
                result = menu.handle_input(event)
                if result == "Play":
                    current_menu = "levelselection"
                    continue
                elif result == "Settings":
                    current_menu = "settings"
                    continue
                elif result == "Quit":
                    pygame.quit()
            elif current_menu == "settings":
                result = settingsMenu.handle_input(event)
                if result == "Back":
                    current_menu = "main"
            elif current_menu == "levelselection":
                result = levelMenu.handle_input(event)
                if result == "Back":
                    current_menu = "main"
                if result == "Level 1":
                    current_menu = "gameLoop"
                    game = gameLoop(1)  
                elif result == "Level 2":
                    current_menu = "gameLoop"
                    game = gameLoop(2) 
                elif result == "Level 3":
                    current_menu = "gameLoop"
                    game = gameLoop(3)
            elif current_menu == "gameLoop":
                if game is not None:
                    if not game.update(events):
                        current_menu = "main"

        if current_menu == "main":
            menu.draw()
        elif current_menu == "settings":
            settingsMenu.draw()
        elif current_menu == "levelselection":
            levelMenu.draw()          
          
        pygame.display.flip()

if __name__ == "__main__":
    main()