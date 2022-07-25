import pygame
from pieces import *
from ratings import Ratings
import time

class UserInterface:
    
#
# This Class is responsible for the UI element of the project, This includes drawing the game in pygame and using the pre-saved assets in the assets folder.
#

    def __init__(self, surface, Board):
        self.surface = surface  # Holds the surface variable defined for pygame
        self.inPlay = True  # Inplay variable to check if we are still playing the game
        self.squareSize = 75  # Size of square; used as a scale for pieces and board squares (Re adjust this variable if you want to change size of game)
        self.pieces = 64
        # mouseInitial Stores the inital X and y coordinates user makes when clicking mouse on board
        self.mouseInitialX = 0
        self.mouseInitialY = 0

        # mouseFinal Stores the finale X and y coordinates user makes when releasing mouse on board
        self.mouseFinalX = 0
        self.mouseFinalY = 0

        self.chessboard = Board  # Initialize given board onto interface
        self.playerMove = ""  # stores players move they make
        self.computerMove = "" # Stores computers move they make
        self.playerColor = "" # Color of player
        self.computerColor = "" # Color of computer


#=====================================================================================================================================================================

    def drawComponent(self):
        '''
        Draw component draws elements including the game board, chess chessPieces
        and text cues and indications
        '''
        # Creates visual representation of board by Making Checkered square pattern
        for i in range(0, self.pieces, 2):
            pygame.draw.rect(self.surface, (120, 60, 30), [(i % 8+(i//8) % 2)*self.squareSize, (i//8)*self.squareSize, self.squareSize, self.squareSize])  # Draws brown squares
            pygame.draw.rect(self.surface, (245, 245, 220), [((i+1) % 8-((i+1)//8) % 2)*self.squareSize, ((i+1)//8)*self.squareSize, self.squareSize, self.squareSize])  # Draws beige squares
        #  Loop through every piece
        for index in range(self.pieces):
            currentPosition = self.chessboard.boardArray[index//8][index % 8]  # looking at current piece in board
            # If White Pawn Found
            if currentPosition == "P":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_pl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_pd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If Black Pawn Found
            elif currentPosition == "p":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_pd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_pl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board

            # If White Knight Found
            elif currentPosition == "K":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_nl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_nd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image

            # If Black Knight Found 
            elif currentPosition == "k":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_nd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_nl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image

            # If White Bishop Found
            elif currentPosition == "B":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_bl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_bd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image

            # If Black Bishop Found
            elif currentPosition == "b":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_bd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_bl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image

            # If White Rook Found
            elif currentPosition == "R":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_rl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_rd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image

            # If Black Rook Found
            elif currentPosition == "r":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_rd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_rl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image

            # If Black Knight Found 
            elif currentPosition == "Q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_ql.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_qd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image

            # If Black Queen Found 
            elif currentPosition == "q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_qd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_ql.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image

            # If White King Found
            elif currentPosition == "A":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_kl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto boardArray
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_kd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image
            # If Black King Found
            
            elif currentPosition == "a":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_kd.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw image onto board
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_kl.png")  # Load piece image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))  # Resize piece image with respect to the board
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))  # Draw Image

        pygame.display.update()  # Update the display board when complete

#=====================================================================================================================================================================
        
    def eventHandler(self):

#
# This Function "Listens" for user inputs such as mouse clicks, when a mouse click is detected,
# it stores the mouse position, used for checking what moves user wants to make
#

        # Read pygame events
        for event in pygame.event.get():
            # If user Tries To Exit
            if event.type == pygame.QUIT:
                self.inPlay = False  # Set exit variable to false and exit loop
                break

            # If we press the mouse down (Click Mouse)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If we are currently inside the board
                if pygame.mouse.get_pos()[0] < 8*self.squareSize and pygame.mouse.get_pos()[1] < 8*self.squareSize:
                    self.mouseInitialX = pygame.mouse.get_pos()[0]  # Store Mouse X Position
                    self.mouseInitialY = pygame.mouse.get_pos()[1]  # Store Mouse Y Position

            # If Unclick
            if event.type == pygame.MOUSEBUTTONUP:
                # If we are currently inside the board
                if pygame.mouse.get_pos()[0] < 8*self.squareSize and pygame.mouse.get_pos()[1] < 8*self.squareSize:
                    self.mouseFinalX = pygame.mouse.get_pos()[0]  # Store released X position 
                    self.mouseFinalY = pygame.mouse.get_pos()[1]  # Store released Y position
                    self.computeMove()  

#=====================================================================================================================================================================
                    
    def computeMove(self):

#
# This Function allows for users to make moves with their mouse. It first checks for special moves such as pawn promotion or castling
#
        # We now have to translate the coordinates in a way the board will understand
        # If we have a pawn promotion
        rowInitial = self.mouseInitialY//self.squareSize
        columnInitial = self.mouseInitialX//self.squareSize
        rowFinal = self.mouseFinalY//self.squareSize
        columnFinal = self.mouseFinalX//self.squareSize

        if rowFinal == 0 and rowInitial == 1 and self.chessboard.boardArray[rowInitial][columnInitial] == "P":
            # Allow player to choose which piece to promote to
            promotionPiece = input("Promotion Available! Select promotion [Q,R,B,K]: ")
            # Send move to promote piece
            self.playerMove += str(columnInitial) + str(columnFinal) + str(self.chessboard.boardArray[rowFinal][columnFinal])+ promotionPiece + "P"

        # If player is performing a castling move
        elif rowFinal == 7 and (columnInitial == 0 or columnInitial == 7) and self.chessboard.boardArray[rowInitial][columnInitial] == "R" and self.chessboard.boardArray[rowFinal][columnFinal] == "A":
            # Set current move as the current move player has made

            if columnInitial == 0:
                self.playerMove += str(columnInitial) + str(columnFinal-1) + str(columnFinal) + "R" + "C"
            elif columnInitial == 7:
                self.playerMove += str(columnInitial) + str(columnFinal+1) + str(columnFinal) + "R" + "C"

        # Otherwise we have a regular Move
        else:
            # Set current move as the current move player has made
            self.playerMove += str(rowInitial) + str(columnInitial) + str(rowFinal) + str(columnFinal) + str(self.chessboard.boardArray[rowFinal][(columnFinal)])

        # If the move we make is a valid move
        if self.playerMove in self.chessboard.generateMoveList():
            self.chessboard.computeMove(self.playerMove)  # Make the move on the board
            self.drawComponent()  # Visually update board
            # It's now the computer's turn to make a move. Call computerMoves
            self.computerMoves()
        else:
            print("Invalid Move, Please Try Again")
        # Set current move back to empty to generate next move
        self.playerMove = ""
        self.computerMove = ""
#=====================================================================================================================================================================
        
    def computerMoves(self):
#
# This functions allows the computer to move, It does this through the alphaBeta Function
#
        # Display that it is the computers turn
        if self.computerColor == "W":
            print("White's Turn")
        else:
            print("Black's Turn")

        self.chessboard.changePerspective()  # change to the computer's perspective
        self.computerMove = self.chessboard.alphaBeta(self.chessboard.MAXDEPTH, float("inf"), -float("inf"), "", 0)
        # If computer cannot make a move
        # Player wins
        if self.computerMove is None:
            print("CHECKMATE!")
            time.sleep(15)
            self.inPlay = False
        # Otherwise compute move
        else:
            self.chessboard.computeMove(self.computerMove)  # Allow computer to make move using alphaBeta

        self.chessboard.changePerspective()  # Change back to the player's persepctive
        self.drawComponent()  # Visually update board

        # If we have hit a checkmate or a stalemate
        # If checkmate
        if len(self.chessboard.generateMoveList()) == 0:
            if self.chessboard.kingissafe() is False:
                print("CHECKMATE!")
                time.sleep(15)  # 15 Second delay (usually to verify if checkmate is legitimate)
                self.inPlay = False
            # Otherwise if stalemate
            else:
                print("STALEMATE!")
                time.sleep(15)  # 15 Second delay (usually to verify if checkmate is legitimate)
                self.inPlay = False

        # Print check message if player is in check
        if self.chessboard.kingissafe() is False:
            print("Check!")

        # Display that it is the players turn
        if self.playerColor == "W":
            print("White's Turn")
        else:
            print("Black's Turn")

#=====================================================================================================================================================================
            
    def playGame(self):
#        
# Basic Game Function, will loop a game until either the computer or player cannot move.
#

        self.surface.fill((255, 255, 255))  # initially Fill screen with white
        # Prompt user to select what colour they want to play as
        while(self.playerColor != "W" and self.playerColor != "B"):
            self.playerColor = input("Would You Like To Play As White or Black? (W/B): ")

        self.drawComponent()  # Call drawComponent to initially draw the board

        # Set computerColor based on color user selects
        if self.playerColor == "W":
            self.computerColor = "B"
        else:
            self.computerColor = "W"

        # If Player Selects White, They Start First
        if self.playerColor == "W":
            print("White's Turn")

        else:
            # If Player Selectes White, Computer Starts First
            print("White's Turn")
            self.computerMoves() # Computer makes first move
            print("Black's Turn")
        # Call the event handler until user chooses to exit game
        while self.inPlay:
            self.eventHandler()  # Check For Player Input with Mouse (Event Handler)
