
#
# This program stores the material value for each piece, These values are then used to evaluate potential moves. 
# Details of how the computer makes these decisions is found in the literature review.
#

from pieces import*

class Ratings:

    def __init__(self, Board):
        self.rating = 0  # Set Rating to 0
        self.material = 0  # Set Material to 0
        self.chessboard = Board  

#=======================================================================================================================================
        
    def evaluateRating(self, moveCount, depth):

#
# This is the function which rates how many possible moves the computer can make, It takes in arguments such as moveCount,
# This checks for flexibility and is a factor in rating how strong a move is in the alphaBeta algorithm.
#
# Also stores how "deep" or how many moves ahead the algorithm is.

# With these factors it returns the score of the current move which is later compared with other move ratings to return the best move.
#



        # Evalurate Move Rating
        self.material = self.rateMaterial()  # Evaluate Board Material
        self.rating += self.material  # Increase "move score" based on Material gain of move
        self.rating += self.rateAttack()  # Evaluate Attack "How many enemy pieces are attacking this postition?"
        self.rating += self.rateMoveability(moveCount, depth, self.material)  # Evaluate Move Rating

        # By Making A good move, this means the enemy cannot make a good move in return.
        self.chessboard.changePerspective()  # Change Perspective to Enemy

        self.material = self.rateMaterial()# Evaluate Board Material
        self.rating -= self.material    # Increase "move score" based on Material gain of move

        self.rating -= self.rateAttack()  # Evaluate Attack "How many enemy pieces are attacking this postition?"
        self.rating -= self.rateMoveability(moveCount, depth, self.material)  # Evaluate Move Rating

        self.chessboard.changePerspective() 
        # Once material is evaluated return a negated version of our rating
        # (Works with algorithm) and add score based on how deep we currently are in the search tree
        return -(self.rating + depth*60)

#=======================================================================================================================================
    
    def rateMaterial(self):
   
# This Function Simply Adds Up The Board Material

        
        materialRating = 0  # Start Counter at 0
        bishopCounter = 0  # Bishop Counter = 0 This is because Bishops value changes based on how many there are.
        # Loop through all positions on the board to see how many pieces we have
        for index in range(self.chessboard.TOTALPIECES):
            CaseTest = self.chessboard.boardArray[index//8][index % 8]
            # If Pawn Found
            if CaseTest == "P":
                materialRating += 100  # Increase Material
            # If Rook Found
            elif CaseTest == "R":
                materialRating += 600  # Increase Material
            # If King Found
            elif CaseTest == "K":
                materialRating += 400  # Increase Material
            # If Bishop Found
            elif CaseTest == "B":
                bishopCounter += 1  # Increment bishop counter
            # If Queen Found
            elif CaseTest == "Q":
                materialRating += 1200  # Increase Material

        # Calculate Bishop Value Based on number of Bishops on Board.
        if bishopCounter >= 2:
            materialRating += 200*bishopCounter  # Increase Material
        # Worth Less With 1 Bishop
        elif bishopCounter == 1:
            materialRating += 150  # Increase Material

        return materialRating  # Return Material Output
    
#=======================================================================================================================================
    
    def rateAttack(self):
        
# This function evaluates the attack rating of positions used by the alphaBeta algorithm.
# If you move a piece into a position, Is it attacked and does it put the king in check?

        attackRating = 0

        temporyKingPosition = self.chessboard.kingPosition_White
        # Go through Each Piece
        for i in range(self.chessboard.TOTALPIECES):
            CaseTest = self.chessboard.boardArray[i//8][i%8]
            # If Piece is a Pawn
            if CaseTest == "P":
                self.kingPosition_White = i  # Move king to current position
                # Check if move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 30
            # If Piece is a Rook
            elif CaseTest == "R":
                self.kingPosition_White = i  # Move king to current position
                # Check if move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 250
            # If Piece is a Knight
            elif CaseTest == "K":
                self.kingPosition_White = i  # Move king to current position
                # Check if move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 150
              # If Piece is a Bishop
            elif CaseTest == "B":
                self.kingPosition_White = i  # Move king to current position
                # Check if move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 150
            # Evalutate if current piece is a Queen
            elif CaseTest == "Q":
                self.kingPosition_White = i  # Move king to current position
                # Check if move is unsafe
                if self.chessboard.kingissafe() is False:
                    attackRating -= 450

        self.chessboard.kingPosition_White = temporyKingPosition
                # Check if move is unsafe
        if (self.chessboard.kingissafe() is False):
            attackRating -= 500
        return attackRating
    
#=======================================================================================================================================
    
    def rateMoveability(self, moveCount, depth, material):


# This function evaluates the move rating of positions used by the alphaBeta algorithm.
# If you move a piece into a position, how movable is it? How flexible does it leave your board.
# alphaBeta pruning favours movable moves.

        moveabilityRating = moveCount  # Move Score Inreases for a highly movable move


        # Check for Checkmate
        if moveCount == 0:
            # If there are no available moves, We are in checkmate
            if self.chessboard.kingissafe() is False:
                moveabilityRating += -(150000*depth)  # Very Heavily Negative Impact on Score

            # Otherwise if stalemate
            else:
                moveabilityRating += -(100000*depth)  # Heavily Negative Impack on Score


        return moveabilityRating # Return How Movable a move is.
