from asyncio import constants
from textwrap import fill
from tkinter import Scale
import pygame as py
import sys

tile = 50
piecesize = 25
scale = 100
screen = py.display.set_mode((600,600))
py.display.set_caption("chess")

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
    ["horse", [1,1]]
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
        py.draw.circle(screen, (255,0,0),(p[1][0]*piecesize+scale, p[1][1]*piecesize+scale), 10)
        print(p[1])


while True:
    py.display.update()
    drawBaord()
    drawPieces()
    
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit
            sys.exit()
    