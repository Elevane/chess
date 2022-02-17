
import pygame as py
import sys

tile = 60
piecesize = 60
scale = 100
WIDTH, HEIGHT = 800,800
screen = py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("chess")
knightw = py.image.load("images/knightw.png").convert_alpha()
knightb = py.image.load("images/knightb.png").convert_alpha()
rookb = py.image.load("images/rookb.png").convert_alpha()
rookw = py.image.load("images/rookw.png").convert_alpha()
bishopw =  py.image.load("images/bishopw.png").convert_alpha()
bishopb =  py.image.load("images/bishopb.png").convert_alpha()
queenw=   py.image.load("images/queenw.png").convert_alpha()
queenb=   py.image.load("images/queenb.png").convert_alpha()
kingw =   py.image.load("images/kingw.png").convert_alpha()
kingb =   py.image.load("images/kingb.png").convert_alpha()
pawnw =   py.image.load("images/pawnw.png").convert_alpha()
pawnb =   py.image.load("images/pawnb.png").convert_alpha()


board = [
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0]
]


imgtowers = {
    "knightw" : knightw,
    "knightb": knightb,
    "rookw": rookw,
    "rookb": rookb,
    "bishopw": bishopw,
    "bishopb": bishopb,
    "queenw": queenw,
    "queenb": queenb,
    "kingw": kingw,
    "kingb": kingb,
    "pawnw1":pawnw,
    "pawnb1":pawnb,
    "pawnb2":pawnb,
    "pawnb3":pawnb,
    "pawnb4":pawnb,
    "pawnb5":pawnb,
    "pawnb6":pawnb,
    "pawnb7":pawnb,
    "pawnb8":pawnb,
    "pawnw2":pawnw,
    "pawnw3":pawnw,
    "pawnw4":pawnw,
    "pawnw5":pawnw,
    "pawnw6":pawnw,
    "pawnw7":pawnw,
    "pawnw8":pawnw,
}

pieces = [
    ##black
    ["knightb", [2,1], True],
    ["knightb", [7,1], True],
    ["rookb", [8,1], True],
    ["rookb", [1,1], True],
    ["bishopb", [6,1], True],
    ["bishopb", [3,1], True],
    ["kingb", [5,1], True],
    ["queenb", [4,1], True],
    ["pawnb1", [1,2], True],
    ["pawnb2", [2,2], True],
    ["pawnb3", [3,2], True],
    ["pawnb4", [4,2], True],
    ["pawnb5", [5,2], True],
    ["pawnb6", [6,2], True],
    ["pawnb7", [7,2], True],
    ["pawnb8", [8,2], True],


    ##white
    ["knightw", [2,8], True],
    ["knightw", [7,8], True],
    ["rookw", [8,8], True],
    ["rookw", [1,8], True],
    ["bishopw", [6,8], True],
    ["bishopw", [3,8], True],
    ["kingw", [5,8], True],
    ["queenw", [4,8], True],
    ["pawnw1", [1,7], True],
    ["pawnw2", [2,7], True],
    ["pawnw3", [3,7], True],
    ["pawnw4", [4,7], True],
    ["pawnw5", [5,7], True],
    ["pawnw6", [6,7], True],
    ["pawnw7", [7,7], True],
    ["pawnw8", [8,7], True],
]

class Chess:

    def __init__(self):
        self.isDragingPiece = False
        self.draggablepiece = []


    def drawBaord(self):
        for y, row in enumerate(board):
                for x, col in enumerate(row):
                    if col == 0:
                        py.draw.rect(screen, (255,255,255),(y*tile+scale,x*tile+scale, tile, tile))
                    else:
                        py.draw.rect(screen, (111,111,111), (y*tile+scale, x*tile+scale, tile, tile))

    def GetPieceByChoords(self,pos):
        for p in pieces:
            x = p[1][0] - 1 
            y = p[1][1] - 1 
            piecerect = py.Rect(x*tile+scale, y*tile+scale, piecesize, piecesize)
            if(piecerect.collidepoint(pos)):
                return p

    def drawOnePiece(self, pos, piece):
        x = pos[0]
        y = pos[1] 
        piecerect = py.Rect(x - piecesize/2, y-piecesize/2, piecesize, piecesize)
        screen.blit(imgtowers[piece[0]], piecerect)
       


    def drawPieces(self):
        for p in pieces:
            x = p[1][0] - 1 
            y = p[1][1] - 1 
            if(p[2]):
                piecerect = py.Rect(x*tile+scale, y*tile+scale, piecesize, piecesize)
                screen.blit(imgtowers[p[0]], piecerect)
            if len(p) == 4:
                collidepiece = py.Rect((x*tile+scale, y*tile+scale,piecesize, piecesize))
                py.draw.rect(screen,(255,0,0), collidepiece, width=3)

    def DrawDraggedPiece(self):
        if len(self.draggablepiece) > 0 and self.isDragingPiece:
            self.drawOnePiece(py.mouse.get_pos(), self.draggablepiece)

    def PlacePieceOnBoard(self, piece, pos):
        for p in pieces:
            if p == piece:
                ## calculer les coords dans le board
                coords = [4,4]
                p[1] = coords


    def hoverDraggable(self, piece):
        for p in pieces:
            if p == piece:
                p.append(True)


    def RemoveHoverDraggable(self, piece):
        for p in pieces:
            if p == piece:
                if len(p) == 4:
                    p[3] == False

    def getBoardsPosFromMousePos(pos):
        #TODO : calculer les coords d'une case de type board [0,1] a partir de la pos de la souris
        pass

    def onClick(self, event):      
        piece = self.GetPieceByChoords(event.pos)
        if not self.isDragingPiece:
                if piece :
                    self.isDragingPiece = True
                    self.draggablepiece = piece
                    self.hoverDraggable(piece)
        else:
            print("relache")
            self.PlacePieceOnBoard(self.draggablepiece, event.pos)
            self.isDragingPiece = False
            self.RemoveHoverDraggable(self.draggablepiece)


    def onHover(self):
        mousepos = py.mouse.get_pos()
        for p in pieces:
            x = p[1][0] - 1 
            y = p[1][1] - 1 
            collidepiece = py.Rect((x*tile+scale, y*tile+scale,piecesize, piecesize ))
            if(collidepiece.collidepoint(mousepos)):
                py.draw.rect(screen,(255,0,0), collidepiece, width=3)
                ##clickable


    def drawBG(self):
        bg = py.Rect(0,0, WIDTH, HEIGHT)
        py.draw.rect(screen, (0,0,0), bg)

    def run(self):
        while True:
           
            py.display.update()
            self.drawBG()
            self.drawBaord()
            self.drawPieces()
            ##self.onHover()
            self.DrawDraggedPiece()
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()
                elif event.type == py.MOUSEBUTTONDOWN:
                    self.onClick(event)
                 

if "__main__" == __name__:
    app = Chess()
    app.run()