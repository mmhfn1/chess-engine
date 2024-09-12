##the main driver file responsible for handling user input and displaying current GameState object

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 
SQ_SIZE = HEIGHT// DIMENSION
MAX_FPS = 30
IMAGES = {}

#initialize gloabl dict of images. will be called later to main. we can use the dict to access images
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(SQ_SIZE, SQ_SIZE))

#main driver for code
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages() #only run once before while loop
    running = True
    sqSelected = () #no square is selected keeps track of the last square selected by the user. tuple(row, col)
    playerClicks = [] #keeps track of player clicks. two tuples [(row, col), (row, col)]. eg: [(6, 4), (4, 4)]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #location of the mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): #select if square has already been selected
                    sqSelected = () #deselect
                    playerClicks = [] #reset player moves
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #append for first and second clicks
                if len(playerClicks) == 2: #after second click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.Board)
                    print(move.getChessNotation())
                    gs.makeMove(move) #reset clicks
                    sqSelected = () #reset moves made by player
                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

#responsible for all graphics within current game state
def drawGameState(screen, gs):
    drawBoard(screen) #draws squares on board
    drawPieces(screen, gs.Board) #draws pieces on top of squares

#draw squares on the board. top left is always white
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
#draws pieces on the board as present in GameState.Board
def drawPieces(screen, Board):
    for row in range(DIMENSION):
        for col in range (DIMENSION):
            piece = Board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
