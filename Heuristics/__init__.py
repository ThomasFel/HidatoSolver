class Heuristic:

    def __init__(self):
        pass

    def H(self, state):
        return 1

class HidatoHeuristic(Heuristic):

    # This heuristic function counts how many taken spaces are around the current number in the given state
    def H(self, state):
        countTaken = 0
        sr = state.representation
        if sr.row > 0:
            if sr.col > 0:
                if sr.board[sr.row - 1][sr.col - 1] != 0:
                    countTaken += 1
            if sr.board[sr.row - 1][sr.col] != 0:
                countTaken += 1
            if sr.col < len(sr.board) - 1:
                if sr.board[sr.row - 1][sr.col + 1] != 0:
                    countTaken += 1

        if sr.col > 0:
            if sr.board[sr.row][sr.col - 1] != 0:
                countTaken += 1

        if sr.col < len(sr.board) - 1:
            if sr.board[sr.row][sr.col + 1] != 0:
                countTaken += 1

        if sr.row < len(sr.board) - 1:
            if sr.col > 0:
                if sr.board[sr.row + 1][sr.col - 1] != 0:
                    countTaken += 1
            if sr.board[sr.row + 1][sr.col] != 0:
                countTaken += 1
            if sr.col < len(sr.board) - 1:
                if sr.board[sr.row + 1][sr.col + 1] != 0:
                    countTaken += 1
        return countTaken