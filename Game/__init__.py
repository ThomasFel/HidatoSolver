# to perform a deep copy of the board, for the need to add a number each time
from copy import copy, deepcopy

class HidatoRepresentation:

    def __init__(self, board, currNum, row, col):
        self.board = board
        self.currNum = currNum
        self.row = row
        self.col = col

    def isAdmissible(self):
        isFree = False  # assume the space is taken
        isAdj = True    # because not always there will be a next number placed on the board
        # if the given rows and cols are in range of the board
        if (self.row >= 0) and (self.row < len(self.board)) and (self.col >= 0) and (self.col < len(self.board)):
            # if the space is empty - then can be placed there
            if self.board[self.row][self.col] == 0:
                isFree = True
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                # if the next number exists - i want to check if it is adjacent to currNum
                if self.board[i][j] == (self.currNum + 1):
                    if(i - 1 <= self.row <= i + 1) and (j - 1 <= self.col <= j + 1):
                        isAdj = True
                    else:
                        isAdj = False
        # if the space is free and close to an existing higher number, then is admissible
        return isAdj and isFree

class HidatoState:

    def __init__(self, parent, board, currNum, row, col, heuristic):
        self.parent = parent
        self.H = heuristic
        self.representation = HidatoRepresentation(board, currNum, row, col)

    # this function checks if the next number we want to put on the board is a new one, or has it already been placed
    def nextNum(self, currNum):
        for i in range(0, len(self.representation.board)):
            for j in range(0, len(self.representation.board)):
                # if the number already exists, move up one and keep searching for the next, and update it's placement
                if self.representation.board[i][j] == (currNum + 1):
                    self.representation.currNum += 1
                    currNum += 1
                    self.representation.row = i
                    self.representation.col = j

class Game:

    def __init__(self, initialState=None, heuristic=None):
        self.state = initialState
        self.heuristic = heuristic

    def neighbors(self, state):
        out = set([])
        return out

    def getState(self):
        return self.state

    def solution(self, state):
        return True

class HidatoGame(Game):

    def __init__(self, board, currNum, row, col, heuristic):
        self.state = HidatoState(None, board, currNum, row, col, heuristic)
        self.heuristic = heuristic

    def neighbors(self, state):
        out = []
        rep = state.representation
        # check what is the next number and where do you start
        state.nextNum(rep.currNum)
        # numbers of possible moves to traverse in loops
        possibleRows = [-1, 0, 1]
        possibleCols = [-1, 0, 1]
        # create a state for each admissible direction
        for i in range(0, 3):
            for j in range(0, 3):
                # (parent, board, currNum, row, col, heuristic):
                n = HidatoState(state, rep.board, rep.currNum + 1, rep.row + possibleRows[i], rep.col + possibleCols[j], state.H)
                if n.representation.isAdmissible():
                    newBoard = deepcopy(n.representation.board)
                    newBoard[n.representation.row][n.representation.col] = n.representation.currNum
                    n.representation.board = deepcopy(newBoard)
                    out.append(n)
        return out

    def solution(self, state):
        # if there are no more blank spaces on the board - a solution was found
        for i in range(0, len(state.representation.board)):
            for j in range(0, len(state.representation.board)):
                if state.representation.board[i][j] == 0:
                    return False
        return True
