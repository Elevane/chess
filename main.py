from asyncio import constants
from textwrap import fill
from tkinter import Scale
import pygame as py
import sys

tile = 60
piecesize = 60
scale = 100
screen = py.display.set_mode((800,800))
py.display.set_caption("chess")
horseimg = py.image.load("horse.png").convert_alpha()

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

pieces = [
    ["horse", [1,1], (255,0,0)],
    ["tower", [8,1], (0,255,0)]
]


def drawBaord():
    for y, row in enumerate(board):
            for x, col in enumerate(row):
                if col == 0:
                    py.draw.rect(screen, (255,255,255),(y*tile+scale,x*tile+scale, tile, tile))
                else:
                    py.draw.rect(screen, (111,111,111), (y*tile+scale, x*tile+scale, tile, tile))


def drawPieces():
    for p in pieces:
        x = p[1][0] - 1 
        y = p[1][1] - 1 
        piecerect = py.Rect(x*tile+scale, y*tile+scale, piecesize, piecesize)
        screen.blit(horseimg, piecerect)
        

def OnMouseOnPiece():
    pos = py.mouse.get_pos()
    for p in pieces:
        x = p[1][0] - 1 
        y = p[1][1] - 1
        collidepiece = py.Rect((x*tile+scale, y*tile+scale,piecesize, piecesize ))
        py.draw.rect(screen,(0,125,125), collidepiece, width=2)
        if(collidepiece.collidepoint(pos)):
            print(p[0])
            ##clickable

while True:
    py.display.update()
    drawBaord()
    drawPieces()
    OnMouseOnPiece()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit
            sys.exit()
        