import pygame
from menu import Menu
from settings import SettingsMenu
from levelMenu import LevelMenu
from gameLoop import gameLoop
from tutorialMenu import tutorialMenu

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE )
    menu = Menu(screen)
    settingsMenu = SettingsMenu(screen)
    levelMenu = LevelMenu(screen)
    tutorialMenu = tutorialMenu(screen)
    current_menu = "main"
    game = None

    win = pygame.mixer.Sound("sounds/win.mp3")
    lose = pygame.mixer.Sound("sounds/gameover.mp3")

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
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
                elif result == "Tutorial":
                    current_menu = "tutorial"
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
                    tutorialMenu.update_screen(screen)
                    if game is not None:
                        game.update_screen(screen)
            elif current_menu == "levelselection":
                result = levelMenu.handle_input(event)
                if result == len(levelMenu.options)-1:
                    current_menu = "main"
                    break
                elif result != None:
                    current_menu = "gameLoop"
                    game = gameLoop(result+1, 1)  
                    break
            elif current_menu == "tutorial":
                result = tutorialMenu.handle_input(event)
                if result == "Back":
                    current_menu = "main"
                    break
            elif current_menu == "gameLoop":
                if game is not None:
                    # Game has been lost
                    if not game.update(event):
                        lose.play()
                        pygame.time.delay(5000)
                        # Out of lives, back to main menu
                        if game.lives <= 0:
                            game = None
                            current_menu = "main"
                        # Restart the current board with one less life
                        else:
                            newgame = gameLoop(game.level, game.board, 0, game.lives)
                            game = None
                            game = newgame
                            pygame.event.clear()
                    # Check if the game board and the solution board are equal
                    if game.board_is_solved():
                        win.play()
                        pygame.time.delay(4000)
                        if game.board < game.totalBoards:
                            # There is a next board, load it
                            newgame = gameLoop(game.level, game.board + 1, game.timer, game.lives)
                            game = None
                            game = newgame
                            pygame.event.clear()
                        else:
                            # There is no next board, the game is finished
                            print("Game finished!")
                            game = None
                            current_menu = "main"

        if current_menu == "main":
            menu.draw()
        elif current_menu == "settings":
            settingsMenu.draw()
        elif current_menu == "levelselection":
            levelMenu.draw()         
        elif current_menu == "Tutorial":
            tutorialMenu.draw()
          
        pygame.display.flip()

if __name__ == "__main__":
    main()