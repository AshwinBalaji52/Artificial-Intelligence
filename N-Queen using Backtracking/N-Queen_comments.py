# -*- coding: utf-8 -*-
"""
Created on Thu Mar 1 00:42:23 2021
@author: Ashwin Balaji
"""


class chessBoard:
    def __init__(self, dimension):
        # board has dimensions dimension x dimension
        self.dimension = dimension
        # columns[r] is a number c if a queen is placed at row r and column c.
        # columns[r] is out of range if no queen is place in row r.
        # Thus after all queens are placed, they will be at positions
        # (columns[0], 0), (columns[1], 1), ... (columns[dimension - 1], dimension - 1)
        self.columns = []
 
    def matrixdimension(self):
        return self.dimension
 
    def evaluateQueens(self):
        return len(self.columns)
 
    def backtrackNextRow(self, column):
        self.columns.append(column)
 
    def popQueen(self):
        return self.columns.pop()
 
    def isSafe(self, column):
        # index of next row
        row = len(self.columns)
 
        # check column
        for queeninColumn in self.columns:
            if column == queeninColumn:
                return False
 
        # check diagonal
        for queeninRow, queeninColumn in enumerate(self.columns):
            if queeninColumn - queeninRow == column - row:
                return False
 
        # check other diagonal
        for queeninRow, queeninColumn in enumerate(self.columns):
            if ((self.dimension - queeninColumn) - queeninRow
                == (self.dimension - column) - row):
                return False
 
        return True
 
    def display(self):
        for row in range(self.dimension):
            for column in range(self.dimension):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
 
 
def displaySolutions(dimension):
    """Display a chessboard for each possible configuration of placing n queens
    on an n x n chessboard where n = dimension and print the number of such
    configurations."""
    board = chessBoard(dimension)
    possibleSolutions = solutionBacktracker(board)
    print('Number of solutions:', possibleSolutions)
 
def solutionBacktracker(board):
    """Display a chessboard for each possible configuration of filling the given
    board with queens and return the number of such configurations."""
    dimension = board.matrixdimension()
 
    # if board is full, display solution
    if dimension == board.evaluateQueens():
        board.display()
        print()
        return 1
 
    possibleSolutions = 0
    
    for column in range(dimension):
        if board.isSafe(column):
            
            board.backtrackNextRow(column)
            possibleSolutions += solutionBacktracker(board)
            board.popQueen()
 
    return possibleSolutions
 
 
size = int(input('Dimensions : '))
displaySolutions(size)