#
# This program is the main program to initialise the board and display the pygame interface.
#

import pygame
from board import ChessBoard
from userInterface import UserInterface
if __name__ == "__main__":
    pygame.init()  # Pygame Initialisation
    surface = pygame.display.set_mode([600, 600], 0, 0)  # Adjust Game Window Size
    # Set Window Title
    pygame.display.set_caption('Final Project 1907978')
    # Initialize Board
    Board = ChessBoard()
    UI = UserInterface(surface, Board)
    UI.playGame()
    pygame.quit()  # Close program
