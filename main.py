import pygame
from menu import Menu
from settings import SettingsMenu
from levelMenu import LevelMenu
from gameLoop import gameLoop

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE )
    menu = Menu(screen)
    settingsMenu = SettingsMenu(screen)
    levelMenu = LevelMenu(screen)
    current_menu = "main"
    game = None

    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(30)
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
                    break
                elif result == "Settings":
                    current_menu = "settings"
                    break
                elif result == "Quit":
                    pygame.quit()
            elif current_menu == "settings":
                result = settingsMenu.handle_input(event)
                if result == "Back":
                    current_menu = "main"   
                    break
                elif result != None:
                    result = result.split("x")
                    screen = pygame.display.set_mode((int(result[0]), int(result[1])), pygame.RESIZABLE)
                    menu.update_screen(screen)
                    settingsMenu.update_screen(screen)
                    levelMenu.update_screen(screen)
                    if game is not None:
                        game.update_screen(screen)
            elif current_menu == "levelselection":
                result = levelMenu.handle_input(event)
                if result == "Back":
                    current_menu = "main"
                    break
                if result == "Level 1":
                    current_menu = "gameLoop"
                    game = gameLoop(1, 1)  
                    break
                elif result == "Level 2":
                    current_menu = "gameLoop"
                    game = gameLoop(2, 1) 
                    break
                elif result == "Level 3":
                    current_menu = "gameLoop"
                    game = gameLoop(3, 1)
                    break
            elif current_menu == "gameLoop":
                if game is not None:
                    # Check if the game board and the solution board are equal
                    if game.board_is_solved():
                        if game.board < game.totalBoards:
                            # There is a next board, load it
                            game = gameLoop(game.level, game.board + 1)
                        else:
                            # There is no next board, the game is finished
                            print("Game finished!")
                            game = None
                            current_menu = "main"
                    if game is not None and not game.update(events):
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