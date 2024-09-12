##responsible for storing the current state of the chess game
##used to determine valid moves at the current state
#keeps a move log

class GameState():
    def __init__(self):
        #8x8 2d lst and each element of the list has 2 characters. first characted represents the color of the piece (b/w). 
        #second represents the type of the piece (R, N, B, Q, K, p)
        #"--" represents and empty  space with no piece
        self.Board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp" , "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp" , "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.WhiteToMove = True
        self.moveLog = []