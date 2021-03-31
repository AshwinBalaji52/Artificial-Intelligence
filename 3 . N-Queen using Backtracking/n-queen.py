# -*- coding: utf-8 -*-
"""
Created on Thu Mar 1 00:42:23 2021
@author: Ashwin Balaji
"""


class chessBoard:
    def __init__(self, dimension):
        # board has dimensions dimension x dimension
        self.dimension = dimension
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
                    print('-', end=' ')
            print()
 
 
def displaySolutions(dimension):
    board = chessBoard(dimension)
    possibleSolutions = solutionBacktracker(board)
    print('Solutions :', possibleSolutions)
 
def solutionBacktracker(board):
    
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
 
print("\t\t\t\n N-QUEEN : BACKTRACKING \n")
size = int(input('Dimensions : '))
displaySolutions(size)