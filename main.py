import pygame as py
import sys

tile = 60
piecesize = 60
scale = 100
WIDTH, HEIGHT = 800, 800
screen = py.display.set_mode((WIDTH, HEIGHT))
py.font.init()
turn_text = py.font.SysFont('Comic Sans MS', 30)
score_text = py.font.SysFont('Comic Sans MS', 20)
py.mixer.init()
piece_sound = py.mixer.Sound("sounds/sound_piece.mp3")
py.display.set_caption("chess")
knightw = py.image.load("images/knightw.png").convert_alpha()
knightb = py.image.load("images/knightb.png").convert_alpha()
rookb = py.image.load("images/rookb.png").convert_alpha()
rookw = py.image.load("images/rookw.png").convert_alpha()
bishopw = py.image.load("images/bishopw.png").convert_alpha()
bishopb = py.image.load("images/bishopb.png").convert_alpha()
queenw = py.image.load("images/queenw.png").convert_alpha()
queenb = py.image.load("images/queenb.png").convert_alpha()
kingw = py.image.load("images/kingw.png").convert_alpha()
kingb = py.image.load("images/kingb.png").convert_alpha()
pawnw = py.image.load("images/pawnw.png").convert_alpha()
pawnb = py.image.load("images/pawnb.png").convert_alpha()

board = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]

imgtowers = {
    "knightw": knightw,
    "knightb": knightb,
    "rookw": rookw,
    "rookb": rookb,
    "bishopw": bishopw,
    "bishopb": bishopb,
    "queenw": queenw,
    "queenb": queenb,
    "kingw": kingw,
    "kingb": kingb,
    "pawn1w": pawnw,
    "pawn1b": pawnb,
    "pawn2b": pawnb,
    "pawn3b": pawnb,
    "pawn4b": pawnb,
    "pawn5b": pawnb,
    "pawn6b": pawnb,
    "pawn7b": pawnb,
    "pawn8b": pawnb,
    "pawn2w": pawnw,
    "pawn3w": pawnw,
    "pawn4w": pawnw,
    "pawn5w": pawnw,
    "pawn6w": pawnw,
    "pawn7w": pawnw,
    "pawn8w": pawnw,
}

pieces = [
    ##black
    ["knight", [2, 1], True, False, "black"],
    ["knight", [7, 1], True, False, "black"],
    ["rook", [8, 1], True, False, "black"],
    ["rook", [1, 1], True, False, "black"],
    ["bishop", [6, 1], True, False, "black"],
    ["bishop", [3, 1], True, False, "black"],
    ["king", [5, 1], True, False, "black"],
    ["queen", [4, 1], True, False, "black"],
    ["pawn1", [1, 2], True, False, "black"],
    ["pawn2", [2, 2], True, False, "black"],
    ["pawn3", [3, 2], True, False, "black"],
    ["pawn4", [4, 2], True, False, "black"],
    ["pawn5", [5, 2], True, False, "black"],
    ["pawn6", [6, 2], True, False, "black"],
    ["pawn7", [7, 2], True, False, "black"],
    ["pawn8", [8, 2], True, False, "black"],

    ##white
    ["knight", [2, 8], True, False, "white"],
    ["knight", [7, 8], True, False, "white"],
    ["rook", [8, 8], True, False, "white"],
    ["rook", [1, 8], True, False, "white"],
    ["bishop", [6, 8], True, False, "white"],
    ["bishop", [3, 8], True, False, "white"],
    ["king", [5, 8], True, False, "white"],
    ["queen", [4, 8], True, False, "white"],
    ["pawn1", [1, 7], True, False, "white"],
    ["pawn2", [2, 7], True, False, "white"],
    ["pawn3", [3, 7], True, False, "white"],
    ["pawn4", [4, 7], True, False, "white"],
    ["pawn5", [5, 7], True, False, "white"],
    ["pawn6", [6, 7], True, False, "white"],
    ["pawn7", [7, 7], True, False, "white"],
    ["pawn8", [8, 7], True, False, "white"],
]


class Chess:

    def __init__(self):
        self.isDragingPiece = False
        self.draggablepiece = []
        self.turn = "white"
        self.white_points = 0
        self.black_points = 0

    def draw_board(self):
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if col == 0:
                    py.draw.rect(screen, (255, 255, 255), (y * tile + scale, x * tile + scale, tile, tile))
                else:
                    py.draw.rect(screen, (111, 111, 111), (y * tile + scale, x * tile + scale, tile, tile))

    def get_piece_by_coords(self, pos):
        for p in pieces:
            x = p[1][0] - 1
            y = p[1][1] - 1
            piecerect = py.Rect(x * tile + scale, y * tile + scale, piecesize, piecesize)
            if (piecerect.collidepoint(pos)) and p[2] is not False:
                return p

    def drawOnePiece(self, pos, piece):
        x = pos[0]
        y = pos[1]
        piecerect = py.Rect(x - piecesize / 2, y - piecesize / 2, piecesize, piecesize)
        if piece[4] == "white":
            screen.blit(imgtowers[piece[0] + "w"], piecerect)
        else:
            screen.blit(imgtowers[piece[0] + "b"], piecerect)

    def draw_pieces(self):
        for p in pieces:
            x = p[1][0] - 1
            y = p[1][1] - 1
            if (p[2]):
                piecerect = py.Rect(x * tile + scale, y * tile + scale, piecesize, piecesize)
                if p[4] == "white":
                    screen.blit(imgtowers[p[0] + "w"], piecerect)
                else:
                    screen.blit(imgtowers[p[0] + "b"], piecerect)
            if p[3] is True:
                color = (255, 0, 0) if p[4] is "white" else (0, 0, 255)
                collidepiece = py.Rect((x * tile + scale, y * tile + scale, piecesize, piecesize))
                py.draw.rect(screen, color, collidepiece, width=3)

    def draw_draggable_piece(self):
        if len(self.draggablepiece) > 0 and self.isDragingPiece:
            self.drawOnePiece(py.mouse.get_pos(), self.draggablepiece)

    def place_piece_on_board(self, piece):
        for p in pieces:
            if p == piece and self.turn == p[4]:
                coords = self.get_board_pos_from_mouse_pos()
                p[1] = coords
                self.has_piece_ont_it(p)

    def has_piece_ont_it(self, pieceToCompare):
        for p in pieces:
            if p[1] == pieceToCompare[1] and p[4] is not pieceToCompare[4]:
                p[2] = False
                if p[4] is "white":
                    self.black_points += 1
                else:
                    self.white_points += 1

    def hover_draggable(self, piece):
        for p in pieces:
            if p == piece:
                p[3] = True

    def remove_hover_draggable(self, piece):
        for p in pieces:
            if p == piece:
                p[3] = False

    def get_board_pos_from_mouse_pos(self):
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                posx = x * tile + scale
                posy = y * tile + scale
                boardsquarecollider = py.Rect(posx, posy, tile, tile)
                if boardsquarecollider.collidepoint(py.mouse.get_pos()):
                    return [x + 1, y + 1]

    def on_click(self, event):
        piece = self.get_piece_by_coords(event.pos)
        if not self.isDragingPiece:
            if piece and piece[4] == self.turn:
                self.isDragingPiece = True
                self.draggablepiece = piece
                self.hover_draggable(piece)
        else:
            self.place_piece_on_board(self.draggablepiece)
            self.isDragingPiece = False
            self.remove_hover_draggable(self.draggablepiece)
            self.draggablepiece = []
            piece_sound.play()
            if self.turn == "white":
                self.turn = "black"
            else:
                self.turn = "white"
    def display_turn(self):
        textsurface = turn_text.render(self.turn, False, (255, 255, 255))
        screen.blit(textsurface, (600, 50))

    def display_score(self):
        blackscore = score_text.render(f" score noir : {self.black_points}", False, (255, 255, 255))
        whitescore = score_text.render(f" score blanc : {self.white_points}", False, (255, 255, 255))
        screen.blit(blackscore, (600, 80))
        screen.blit(whitescore, (600, 100))

    def on_hover(self):
        mousepos = py.mouse.get_pos()
        for p in pieces:
            x = p[1][0] - 1
            y = p[1][1] - 1
            collidepiece = py.Rect((x * tile + scale, y * tile + scale, piecesize, piecesize))
            if (collidepiece.collidepoint(mousepos)):
                py.draw.rect(screen, (255, 0, 0), collidepiece, width=3)
                ##clickable

    def draw_background(self):
        bg = py.Rect(0, 0, WIDTH, HEIGHT)
        py.draw.rect(screen, (0, 0, 0), bg)

    def run(self):
        while True:
            self.display_turn()
            self.display_score()
            py.display.update()
            self.draw_background()
            self.draw_board()
            self.draw_pieces()
            self.draw_draggable_piece()
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()
                elif event.type == py.MOUSEBUTTONDOWN:
                    self.on_click(event)


if "__main__" == __name__:
    app = Chess()
    app.run()
