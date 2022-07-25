import pieces
from ratings import Ratings


class ChessBoard:
    
#
# I have decided to represent my chess board as a 2d array with lowercase and uppercase letters representing different sides.
#

    def __init__(self):
    
        self.boardArray = [
        ["r", "k", "b", "q", "a", "b", "k", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "K", "B", "Q", "A", "B", "K", "R"]
        ]
        self.TOTALPIECES = 64  # Total number of pieces/squares that exist in a board game
        self.kingPosition_White = 60  # Current position of white king
        self.kingPosition_Black = 4  # Current position of black king
        self.MAXDEPTH = 3  # Maximum depth alphaBeta pruning will occur in, This can be changed but the higher the number is, the turn takes exponentially more time.

#==================================================================================================================================================================
    def generateMoveList(self):

#
# This function applies the movelist to all availble pieces, effectively gathering information on all possible moves that can be made.
#

        # declare a list that will store all potential moves. It starts empty
        # In the case that there are no moves available
        movelist = ""  # declare a list that will store all potential moves.

        # loop through each element in board array (evaluates position [0][0], [0][1], etc.)
        rook = pieces.Rook(self)
        knight = pieces.Knight(self)
        bishop = pieces.Bishop(self)
        queen = pieces.Queen(self)
        king = pieces.King(self)
        pawn = pieces.Pawn(self)

        for index in range(self.TOTALPIECES):
            currentPosition = self.boardArray[index//8][index%8]  # look at current position in board by referencing it from our chessBoard array

            # If current position is a rook
            if currentPosition == 'R':
                movelist += rook.findMoveSet(index)  # return possible moves rook can make

            # If current position is a pawn
            elif currentPosition == 'K':
                movelist += knight.findMoveSet(index)  # return possible moves knight can make

            # If current position is a pawn
            elif currentPosition == 'B':
                movelist += bishop.findMoveSet(index)  # return possible moves bishop can make

            # If current position is a pawn
            elif currentPosition == 'Q':
                movelist += queen.findMoveSet(index)  # return possible moves queen can make

            # If current position is a pawn
            elif currentPosition == 'A':
                movelist += king.findMoveSet(index)  # return possible moves king can make

            # If current position is a pawn
            elif currentPosition == 'P':
                movelist += pawn.findMoveSet(index)  # return possible moves pawn can make

        return movelist  # Return list of moves possible  # Once we have generated all possible moves, we can return our movelist
#==================================================================================================================================================================
    
    def kingissafe(self):
        
#
# This function checks if the king is safe or not, as this move takes priority over all moves, If the move is not safe it is considered invalid.
#

        # Initialize row and column king is currently on
        kingRow = self.kingPosition_White//8
        kingColumn = self.kingPosition_White % 8
        # For evaluating knight
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                try:
                    # If position contains a knight
                    if self.boardArray[kingRow + i][kingColumn + 2*j] == "k" and kingRow + i >= 0 and kingColumn + 2*j >=0:
                        return False  # Move is not safe!
                except IndexError:
                    pass
                try:
                    # If position contains a knight
                    if self.boardArray[kingRow + 2*i][kingColumn +j] == "k" and kingRow + 2*i >= 0 and kingColumn + j >=0:
                        return False  # Move is not safe!
                except IndexError:
                    pass

        board_roamer = 1  # board_roamer variable used to increment through board

        # For evaluating King Moves
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if i != 0 or j != 0:
                    try:
                        # If encountered move is a king
                        if self.boardArray[kingRow + i][kingColumn + j] == "a" and kingRow + i >= 0 and kingColumn + j >=0:
                            return False  # Move is not safe!
                    except IndexError:
                        pass

        # For evaluating Pawn
        # This is saying as long as the king is not in the top two rows (saves a bit of running time)
        if self.kingPosition_White >= 16:
            try:
                # If diagonal position contains a pawn
                if self.boardArray[kingRow -1][kingColumn -1] == "p" and kingRow - 1 >= 0 and kingColumn -1 >=0:
                    return False  # Move is not safe!
            except IndexError:
                pass
            try:
                # If diagonal position contains a pawn
                if self.boardArray[kingRow -1][kingColumn +1] == "p" and kingRow - 1 >= 0:
                    return False  # Move is not safe!
            except IndexError:
                pass

        # For evaluating multiple straight moving maxPlayers like the queen or rook
        for i in range(-1, 2, 2):
            try:
                # Infinite loop for traversing down horizontal until we hit a non-blank position
                while self.boardArray[kingRow][kingColumn + board_roamer*i] == " ":
                    board_roamer += 1  # Increment board roamer
                # If current detected piece is a queen or rook
                if self.boardArray[kingRow][kingColumn + board_roamer*i] == "r" or self.boardArray[kingRow][kingColumn + board_roamer*i] == "q" and kingColumn + board_roamer*i >= 0:
                    return False  # Move is not safe!
            except IndexError:
                pass
            board_roamer = 1  # set board_roamer back to start
            try:
                # Infinite loop for traversing down vertical until we hit a non-blank position
                while self.boardArray[kingRow + board_roamer*i][kingColumn] == " ":
                    board_roamer += 1  # Increment board roamer

                # If current postion we are looking at contains a rook or a queen
                if self.boardArray[kingRow + board_roamer*i][kingColumn] == "r" or self.boardArray[kingRow + board_roamer*i][kingColumn] == "q" and kingRow + board_roamer*i >= 0:
                    return False  # Move is not safe!
            except IndexError:
                pass
            board_roamer = 1  # set board_roamer back to start

        # For multiple diagonal moving maxPlayers like the queen or bishop
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                try:
                    # Infinite loop for traversing down diagonal until we hit a non-blank position
                    while self.boardArray[kingRow + board_roamer*i][kingColumn + board_roamer*j] == " ":
                        board_roamer += 1  # Increment board roamer until we hit a piece or an edge
                    # If current detected piece is a queen or bishop
                    if self.boardArray[kingRow + board_roamer*i][kingColumn + board_roamer*j] == "b" or self.boardArray[kingRow + board_roamer*i][kingColumn + board_roamer*j] == "q" and kingRow + board_roamer*i >= 0 and kingColumn + board_roamer*j >= 0:
                        return False  # Move is not safe!

                except IndexError:
                    pass
                board_roamer = 1  # set board_roamer back to start

        # Return true if King passes all the tests!
        return True
#==================================================================================================================================================================
    def computeMove(self, givenMove):
#
# Once a move has been detected as valid and is in the moveSet list, A function then once evaluates the best move, must compute the move.
# First it checks for special moves such as moving king, castling or promoting, in which case extra steps are needed.
#

        # If move is NOT regular move
        if givenMove[4] == "P" or givenMove[4] == "C":
            # Check If Promoting
            if givenMove[4] == "P":
                self.boardArray[1][int(givenMove[0])] = " "  # Set current position to blank
                self.boardArray[0][int(givenMove[1])] = givenMove[3]  # set position to Given promotion piece
            # Check If Castling
            elif givenMove[4] == "C":
                # Move King (as part of castling)
                self.boardArray[7][int(givenMove[0])] = " " # Set position rook sits in to blank
                self.boardArray[7][int(givenMove[1])] = "A" # Set new king position
                self.boardArray[7][int(givenMove[2])] = givenMove[3]  # set new rook position

        else:
            # Set previous position to blank and currentPosition to Piece
            self.boardArray[int(givenMove[2])][int(givenMove[3])] = self.boardArray[int(givenMove[0])][int(givenMove[1])]  # Set position to piece we are moving
            self.boardArray[int(givenMove[0])][int(givenMove[1])] = " "  # Set previous position piece was in to blank
            #  If new position is the human king
            if self.boardArray[int(givenMove[2])][int(givenMove[3])] == "A":
                self.kingPosition_White = 8*int(givenMove[2])+int(givenMove[3])  # Re adjust global king position
                # This is done so that our global position of king is properly adjusted



    def uncomputeMove(self, givenMove):
#
# Undo Function if needs to go back
#
        # Otherwise if it is a pawn promotion

        # If move is NOT a pawn promotion
        if givenMove[4] == "P" or givenMove[4] == "C":
            if givenMove[4] == "P":
                self.boardArray[1][int(givenMove[0])] = "P"  # Set square before promotion back to pawn
                self.boardArray[0][int(givenMove[1])] = givenMove[2]  # Set promotion position back to captured piece
            elif givenMove[4] == "C":
                # Moving the King
                self.boardArray[7][int(givenMove[1])] = " "
                self.boardArray[7][int(givenMove[2])] = "A"
                # Moving the Rook
                self.boardArray[7][int(givenMove[0])] = givenMove[3]

        else:
            # Set previous position to blank and currentPosition to piece
            self.boardArray[int(givenMove[0])][int(givenMove[1])] = self.boardArray[int(givenMove[2])][int(givenMove[3])]  # Set position back to previous piece
            self.boardArray[int(givenMove[2])][int(givenMove[3])] = givenMove[4]  # Set potential postion back to captured piece
            #  If position we undid was a king
            if self.boardArray[int(givenMove[0])][int(givenMove[1])] == "A":
                self.kingPosition_White = 8*int(givenMove[0])+int(givenMove[1])  # Undo global king position adjustment


#==================================================================================================================================================================

    def alphaBeta(self, depth, beta, alpha, givenMove, maxPlayer):

# Algorithm (https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning.
# This alogithm is an existing chess algorithm known as alphaBeta pruning.
# Values and the algorithm were copied from the public domain.

        moveslist = self.generateMoveList()  # Start by finding all current moves possible
        ratingE = Ratings(self)

        # If we hit the deepest possible depth or no moves are available
        if depth == 0 or len(moveslist) == 0:
            if givenMove == "":
                return None
            else:
                return givenMove + str(ratingE.evaluateRating(len(moveslist), depth)*(maxPlayer*2-1))  # Return move with negated rating

        maxPlayer = 1 - maxPlayer  # Set maxPlayer to opposite of current value

        # This loop will evaluate every single move in moveselist
        for i in range(0, len(moveslist), 5):
            # Make the move on the board
            self.computeMove(moveslist[i:(i+5)])
            # Change the perspective
            self.changePerspective()
            # Recursively calls alphaBeta with a depth 1 less than it's current
            # As well as evaluates the move we are currently on
            nextNode = self.alphaBeta(depth-1, beta, alpha, moveslist[i:(i+5)], maxPlayer)

            value = int(nextNode[5:])  # Store the value returned from next node
            #  We must change the perspective right side up again
            self.changePerspective()
            self.uncomputeMove(moveslist[i:(i+5)])  # Undo current move
            #  If we are currently looking at maxPlayer 0
            if maxPlayer == 0:
                # If our value is less than or equal to the current value of beta
                if value <= beta:
                    beta = value  # Set new beta to be current value
                    #  If we are at our global depth
                    if depth == self.MAXDEPTH:
                        givenMove = nextNode[0:5]  # Our current move is currently the optimal move that can be made
            else:
                # If our value is greater than the current value of alpha
                if value > alpha:
                    alpha = value  # Set new alpha to current value
                    # If we have reached our global depth
                    if depth == self.MAXDEPTH:
                        givenMove = nextNode[0:5]  # Our current move is currently the optimal move tha can be made
                # If we have broken out of our bound
                if alpha >= beta:
                    # If we are currently maxPlayer 0
                    if maxPlayer == 0:
                        return givenMove + str(beta)  # Return move plus our value (in this case beta)
                    # Otherwise if we are currently maxPlayer 1
                    else:

                        return givenMove + str(alpha)  # Return move plus our value (in this case alpha)
        # In the case where every move we have evaluated is not better than our current value
        # If we are currently maxPlayer 0
        if maxPlayer == 0:

            return givenMove + str(beta)  # Return move plus our value (in this case beta)
        # Otherwise if we are currently maxPlayer 1
        else:

            return givenMove + str(alpha)  # Return move plus our value (in this case alpha)
        
#==================================================================================================================================================================
    def changePerspective(self):
#
# This function changes the perspective of the board, It is used to evaluate enemy moves and used for the alphaBeta pruning algorithm.
#

        # We only need to loop through the 'top' of the board
        for index in range(32):
            # Set our current row and column with respect to index
            row = index//8
            column = index % 8
            # If we are currently on one of our pieces
            if self.boardArray[row][column].isupper():
                flipPiece = self.boardArray[row][column].lower()  # Set it as an enemy piece
            else:
                flipPiece = self.boardArray[row][column].upper()  # Set enemy piece as friendly otherwise

            # We compute the same evaluations as above but for the piece at the opposite corner
            # If currently one of our pieces
            if self.boardArray[7-row][7-column].isupper():
                self.boardArray[row][column] = self.boardArray[7-row][7-column].lower() # Set current piece to enemy piece
            else:
                self.boardArray[row][column] = self.boardArray[7-row][7-column].upper()  # Set enemy piece as friendly otherwise

            self.boardArray[7-row][7-column] = flipPiece  # Set piece to flipped piece

        kingFlipped = self.kingPosition_White  # Set temporary kingFlipped variable for white position
        # Set new white and black king positions
        self.kingPosition_White = 63 - self.kingPosition_Black
        self.kingPosition_Black = 63 - kingFlipped
