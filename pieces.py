

class Pieces:
    
#
# This class defines each possible piece in chess and describes their "moveset" or possible moves they can legally make.
#

    def __init__(self, Board):
        self.chessboard = Board  # Store the instance of the board to the piece

    def findMoveSet(self, index):
        pass

#=================================================================================================================================================
class Rook(Pieces):
    
# This is the Rook Piece, It can move Horizontally and Vertically up to 8 squares and has the castling special move.

    def testCastling(self, row, column, i, board_roamer):
    
    # Castling Special Move, Checks if Castling is Legal


        castling = ""  # Initialize castle move (would return nothing if we can't perform)
        # If we are on the last row
        if row == 7:
            # If we are evaluate the rook's initial positions
            if column == 0 or column == 7:
                # If we can reach king with now pieces in between
                if self.chessboard.boardArray[row][column+board_roamer*i] == "A":
                    previousPosition = self.chessboard.boardArray[row][column+board_roamer*i]  # define previousPosition as potential piece
                    self.chessboard.boardArray[row][column] = "A"  # Set current position of piece to blank
                    self.chessboard.boardArray[row][column+board_roamer*i] = "R"  # Set potential piece to promotion piece
                    # If move is a safe move, and no negative indexing is occuring
                    if self.chessboard.kingissafe() and (column+board_roamer*i) >= 0:
                        # Format: column rook, column king, Rook, king,C
                        # Compute move as it is valid
                        if column == 0:
                            castling += str(column)+str(column+board_roamer*i-1) + str(column+board_roamer*i)+"R"+"C"
                        elif column == 7:
                                castling += str(column)+ str(column+board_roamer*i+1) + str(column+board_roamer*i)+"R"+"C"
                    self.chessboard.boardArray[row][column] = "R"  # Set current piece back to Rook
                    self.chessboard.boardArray[row][column+board_roamer*i] = previousPosition

        return castling

    def testHorizontal(self, row, column, i, movelist):
        board_roamer = 1  # set board_roamer back to start
        # Go through infinite loop to evaluate all horizontal moves
        try:
            # Keep looping until we reach a non blank space
            while(self.chessboard.boardArray[row][column+board_roamer*i] == " "):
                previousPosition = self.chessboard.boardArray[row][column+board_roamer*i]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row][column+board_roamer*i] = "R"  # Set potential piece to current piece
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and column+board_roamer*i >= 0:
                    movelist += str(row) + str(column) + str(row) +str(column + board_roamer*i) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "R"  # Set current piece back to rook
                self.chessboard.boardArray[row][column+board_roamer*i] = previousPosition  # Set potential piece back to it's previousPosition
                board_roamer += 1  # Increment board roamer

            if self.chessboard.boardArray[row][column+board_roamer*i].islower():
                previousPosition = self.chessboard.boardArray[row][column+board_roamer*i]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row][column+board_roamer*i] = "R"  # Set potential piece to current piece
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and column+board_roamer*i >= 0:
                    movelist += str(row) + str(column) + str(row) +str(column + board_roamer*i)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "R"  # Set current piece back to Rook
                self.chessboard.boardArray[row][column+board_roamer*i] = previousPosition  # Set potential piece back to it's previousPosition

            movelist += self.testCastling(row, column, i, board_roamer)

        except IndexError:
            pass

        return movelist

    def testVertical(self, row, column, i, movelist):
        board_roamer = 1  # set board_roamer back to start
        # We now have to do the same thing for vertical moves
        try:
            # Keep looping until we reach a non blank space
            while(self.chessboard.boardArray[row+board_roamer*i][column] == " "):
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row+board_roamer*i][column] = "R"  # Set potential piece to current piece
                # If move is a safe move
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0:
                    movelist += str(row) + str(column) + str(row+board_roamer*i) + str(column) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "R"  # Set current piece back to Rook
                self.chessboard.boardArray[row+board_roamer*i][column] = previousPosition  # Set potential piece back to it's previousPosition
                board_roamer += 1  # Increment board roamer

            if self.chessboard.boardArray[row+board_roamer*i][column].islower():
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row+board_roamer*i][column] = "R"  # Set potential piece to current piece
                # If move is a safe move
                if self.chessboard.kingissafe() and (row+board_roamer*i) >= 0:
                    movelist += str(row) + str(column) + str(row+board_roamer*i) + str(column) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "R"  # Set current piece back to
                self.chessboard.boardArray[row+board_roamer*i][column] = previousPosition  # Set potential piece back to it's previousPosition
        except IndexError:
            pass

        return movelist

    def findMoveSet(self, index):

        movelist = ""  # declare a list that will store all potential moves.
        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8

        for i in range(-1, 2, 2):
            movelist = self.testVertical(row, column, i, movelist)
            movelist = self.testHorizontal(row, column, i, movelist)

        return movelist  # Return list of moves possible

#=================================================================================================================================================
class Knight(Pieces):

# This is the Knight Piece, It can move in L shapes and over other pieces.

    def findMoveSet(self, index):
    # Goes through all legal knight moves.
    
        movelist = ""  # declare a list that will store all potential moves.

        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8
        # For loop to cover particular moves a knight can make
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                # Covers moves where knight moves two columns and one row
                try:
                    if self.chessboard.boardArray[row+i][column+j*2] == " " or self.chessboard.boardArray[row+i][column+j*2].islower():
                        previousPosition = self.chessboard.boardArray[row+i][column+j*2]  # define previousPosition as potential piece
                        self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                        self.chessboard.boardArray[row+i][column+j*2] = "K"  # Set potential piece to current piece
                        # If move is a safe move, and no negative indexing is occuring
                        if self.chessboard.kingissafe()and row+i >= 0 and column+j*2 >= 0:
                            movelist += str(row)+str(column) + str(row+i) + str(column+j*2) + str(previousPosition)  # Add tested move to our movelist
                        self.chessboard.boardArray[row][column] = "K"  # Set current piece back to knight
                        self.chessboard.boardArray[row+i][column+j*2] = previousPosition  # Set potential piece back to it's previousPosition
                except IndexError:
                    pass
                # Covers moves where knight moves two rows and one column
                try:
                    if self.chessboard.boardArray[row+i*2][column+j] == " " or self.chessboard.boardArray[row+i*2][column+j].islower():
                        previousPosition =self.chessboard.boardArray[row+i*2][column+j]  # define previousPosition as potential piece
                        self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                        self.chessboard.boardArray[row+i*2][column+j] = "K"  # Set potential piece to current piece
                        # If move is a safe move, and no negative indexing is occuring
                        if self.chessboard.kingissafe() and row+i*2 >= 0 and column+j >=0:
                            movelist += str(row)+str(column) + str(row+i*2) + str(column+j) + str(previousPosition)  # Add tested move to our movelist
                        self.chessboard.boardArray[row][column] = "K"  # Set current piece back to knight
                        self.chessboard.boardArray[row+i*2][column+j] = previousPosition  # Set potential piece back to it's previousPosition
                except IndexError:
                    pass

        return movelist  # Return list of moves possible

#=================================================================================================================================================
class Bishop(Pieces):
        # This is the Bishop Piece, It can move Diagonally.
        
    def checkDiagonal(self, movelist, row, column, i, j):
         # Goes through all legal Bishop moves.
        board_roamer = 1  # temporary variable to increment through board
        try:
            while(self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] == " "):
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = "B"  # Set potential piece to current piece
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0 and (column+board_roamer*j) >= 0:
                    movelist += str(row)+str(column)+str(row+board_roamer*i)+str(column+board_roamer*j)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "B"  # Set current piece back to Bishop
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = previousPosition  # Set potential piece back to it's previousPosition
                board_roamer +=1  # Increment board_roamer
            if self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j].islower() :
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = "B"  # Set potential piece to current piece
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0 and (column+board_roamer*j) >= 0:
                    movelist += str(row)+str(column)+str(row+board_roamer*i)+str(column+board_roamer*j)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "B"  # Set current piece back to
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = previousPosition  # Set potential piece back to it's previousPosition
        except IndexError:
            pass
        return movelist


    def findMoveSet(self, index):
        # This Moveset is described as all the moves the bishop can make
        movelist = ""  # declare a list that will store all potential moves.
        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8
        # For loop that covers all diagonal moves
        for i in range(-1, 2, 2):
            for j in range(-1, 2,2):
                movelist = self.checkDiagonal(movelist, row, column, i, j) # Check if bishop can move


        return movelist  # Return list of moves possible

#=================================================================================================================================================
class Queen(Pieces):
    # This is the Queen Piece, It has the moveset of a Castle + Bishop.
    
    def testMovement(self, row, column, i, j, movelist):
        board_roamer = 1  # temporary variable to increment through board
        try:
            while(self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] == " "):
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = "Q"  # Set potential piece to current piece
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0 and (column+board_roamer*j) >= 0:
                    movelist += str(row)+str(column)+str(row+board_roamer*i)+str(column+board_roamer*j)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "Q"  # Set current piece back to queen
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = previousPosition  # Set potential piece back to it's previousPosition
                board_roamer += 1  # increment board_roamer
            # If we can capture a piece
            if self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j].islower():
                previousPosition = self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = "Q"  # Set potential piece to current piece
                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and (row+board_roamer*i) >=0 and (column+board_roamer*j) >= 0:
                    movelist += str(row)+str(column)+str(row+board_roamer*i)+str(column+board_roamer*j)+str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "Q"  # Set current piece back to queen
                self.chessboard.boardArray[row+board_roamer*i][column+board_roamer*j] = previousPosition  # Set potential piece back to it's previousPosition
        except IndexError:
            pass
        return movelist

    def findMoveSet(self, index):
    # Goes through all legal Queen moves.
        movelist = ""  # declare a list that will store all potential moves.
        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8
        # For loop that covers all possible moves Queen can make
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    movelist = self.testMovement(row, column, i, j, movelist)


        return movelist  # Return list of moves possible

#=================================================================================================================================================
class King(Pieces):
    # This is the King Piece, It can move any direction 1 space.
    def testMove(self, index, row, column, i, movelist):
        try:
            # If potential position is blank or has an enemy piece
            if self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3].islower() or self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3] == " ":
                previousPosition = self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3] = "A"  # Set potential piece to current piece
                kingTemp = self.chessboard.kingPosition_White  # Store current kingPosition_in temporary variable
                self.chessboard.kingPosition_White = index+(i//3)*8 +i%3-9  # Set new potential king position

                # If move is a safe move, and no negative indexing is occuring
                if self.chessboard.kingissafe() and row-1+i//3 >=0 and column-1+ i%3>=0:
                        movelist += str(row)+ str(column)+ str(row-1+i//3)+ str(column-1+i%3)+ str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "A"  # Set current piece back to king
                self.chessboard.boardArray[row - 1 + i//3][column-1+ i%3] = previousPosition  # Set potential piece back to it's previousPosition
                self.chessboard.kingPosition_White = kingTemp  # Set king position back to current
        except IndexError:
            pass
        return movelist

    def findMoveSet(self, index):
    # Check King Legal Moves
        movelist = ""  # declare a list that will store all potential moves.
        # define row and column variables with respect to index

        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8

        for i in range(9):
            # if king makes a move (essentially index 4 is the kings current position and we do not want to check that spot)
            if i != 4:
                movelist = self.testMove(index, row, column, i, movelist)

        return movelist  # Return list of moves possible

#=================================================================================================================================================
class Pawn(Pieces):
    
      # This is the Pawn Piece, It can move any direction 1 space. Unless It is it's first move, then it can move upto 2, It can attack diagonally forwards one space.
      
    def testMovement(self, row, column, index, movelist):
        # Can pawn move one up
        try:
            # If potential space is blank and index is below promotion level
            if self.chessboard.boardArray[row-1][column] == " " and index >= 16:
                previousPosition = self.chessboard.boardArray[row-1][column]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row-1][column] = "P"  # Set potential piece to current piece
                # If move is a safe move
                if self.chessboard.kingissafe() and (row-1) >= 0:
                    movelist += str(row) + str(column) + str(row-1) + str(column) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "P"  # Set current piece back to pawn
                self.chessboard.boardArray[row-1][column] = previousPosition  # Set potential piece back to it's previousPosition
        except IndexError:
            pass

        # Can pawn move two up
        try:
            # If potential space is blank and index is below promotion level
            if self.chessboard.boardArray[row-1][column] == " " and self.chessboard.boardArray[row-2][column] == " " and index >= 48:
                previousPosition = self.chessboard.boardArray[row-2][column]  # define previousPosition as potential piece
                self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                self.chessboard.boardArray[row-2][column] = "P"  # Set potential piece to current piece
                # If move is a safe move,
                if self.chessboard.kingissafe() and row-2 >=0:
                    movelist += str(row) + str(column) + str(row-2) + str(column) + str(previousPosition)  # Add tested move to our movelist
                self.chessboard.boardArray[row][column] = "P"  # Set current piece back to pawn
                self.chessboard.boardArray[row-2][column] = previousPosition  # Set potential piece back to it's previousPosition

        except IndexError:
            pass

        # If pawn able to perform Promotion without capturing
        try:
            # If potential space is blank and index is above promotion level
            if self.chessboard.boardArray[row-1][column] == " " and index < 16:
                promotionList = ["Q", "R", "B", "K"]  # Define a list of pieces pawn can be Promoted to

                # loop through promotion pieces in promotionList to generate potential move sets
                for promPiece in promotionList:
                    previousPosition = self.chessboard.boardArray[row-1][column]  # define previousPosition as potential piece
                    self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                    self.chessboard.boardArray[row-1][column] = promPiece  # Set potential piece to current piece
                    # If move is a safe move
                    if self.chessboard.kingissafe():
                        # Format: column 1, column 2, captured-piece, new-piece, P
                        movelist += str(column) + str(column) + str(previousPosition) + str(promPiece) + "P"  # Add tested move to our movelist
                    self.chessboard.boardArray[row][column] = "P"  # Set current piece back to pawn
                    self.chessboard.boardArray[row-1][column] = previousPosition  # Set potential piece back to it's previousPosition
        except IndexError:
            pass

        return movelist

    def testCapture(self, index, row, column, movelist):
        for i in range(-1, 2, 2):
            try:
                # Check if we encounter a piece
                if self.chessboard.boardArray[row-1][column+i].islower():
                    if index < 16:
                        promotionList = ["Q", "R", "B", "K"]  # Define a list of pieces pawn can be Promoted to
                        # Loop through promotionList pieces to evaluate different potential moves with different pieces
                        for promPiece in promotionList:
                            previousPosition = self.chessboard.boardArray[row-1][column+i]  # define previousPosition as potential piece
                            self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                            self.chessboard.boardArray[row-1][column+i] = promPiece  # Set potential piece to promotion piece

                            # If move is a safe move, and no negative indexing is occuring
                            if self.chessboard.kingissafe() and (column+i) >= 0:
                                # Format: column 1, column 2, captured-piece, new-piece,P
                                movelist += str(column) + str(column+i)+str(previousPosition)+str(promPiece)+"P"
                            self.chessboard.boardArray[row][column] = "P"  # Set current piece back to pawn
                            self.chessboard.boardArray[row-1][column+i] = previousPosition  # Set potential piece back to it's previousPosition

                    # If we have a promotion and capture case
                    else:
                        previousPosition = self.chessboard.boardArray[row-1][column+i]  # define previousPosition as potential piece
                        self.chessboard.boardArray[row][column] = " "  # Set current position of piece to blank
                        self.chessboard.boardArray[row-1][column+i] = "P"  # Set potential piece to current piece
                        # If move is a safe move, and no negative indexing is occuring
                        if self.chessboard.kingissafe() and (row-1) >= 0 and (column+i) >= 0:
                            movelist += str(row) + str(column) + str(row-1)+str(column+i) + str(previousPosition)  # Add tested move to our movelist
                        self.chessboard.boardArray[row][column] = "P"  # Set current piece back to pawn
                        self.chessboard.boardArray[row-1][column+i] = previousPosition  # Set potential piece back to it's previousPosition

            except IndexError:
                pass

        return movelist

    def findMoveSet(self, index):
        
    # Check for Legal Pawn Moves.

        movelist = ""  # declare a list that will store all potential moves.

        # Define Row and Columns for referencing the chessBoard
        row = index//8
        column = index % 8

        # Loop through potential moves pawn can make for capturing

        movelist = self.testCapture(index, row, column, movelist)

        movelist = self.testMovement(row, column, index, movelist)


        return movelist  # Return list of moves possible
