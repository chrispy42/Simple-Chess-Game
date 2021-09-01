'''
This was one of my first pygame projects and is a simple game of chess. It is able to manage player turns and doesn't allow you to make illegal moves including
when you are in check. It is very long and repetative and I clearly did not have much of a grasp on how classes and inheritence could be used at the time but still cool
'''

import pygame
import random
pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 800
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

#load images
with open('pieces', 'r'):
    wpawnimage = pygame.image.load('whitePawn.png')
    wrookimage = pygame.image.load('whiteRook.png')
    wknightimage = pygame.image.load('whiteKnight.png')
    wbishopimage = pygame.image.load('whiteBishop.png')
    wkingimage = pygame.image.load('whiteKing.png')
    wqueenimage = pygame.image.load('whiteQueen.png')
    bpawnimage = pygame.image.load('blackPawn.png')
    brookimage = pygame.image.load('blackRook.png')
    bknightimage = pygame.image.load('blackKnight.png')
    bbishopimage = pygame.image.load('blackBishop.png')
    bkingimage = pygame.image.load('blackKing.png')
    bqueenimage = pygame.image.load('blackQueen.png')


playerturn = 0
pieces = [
        [0, 6, 'w', 'pawn', 0], [1, 6, 'w', 'pawn', 0], [2, 6, 'w', 'pawn', 0], [3, 6, 'w', 'pawn', 0], [4, 6, 'w', 'pawn', 0], [5, 6, 'w', 'pawn', 0], [6, 6, 'w', 'pawn', 0], [7, 6, 'w', 'pawn', 0],
        [0, 7, 'w', 'rook', 0], [1, 7, 'w', 'knight', 0], [2, 7, 'w', 'bishop', 0], [3, 7, 'w', 'queen', 0], [4, 7, 'w', 'king', 0], [5, 7, 'w', 'bishop', 0], [6, 7, 'w', 'knight', 0], [7, 7, 'w', 'rook', 0],
        [0, 1, 'b', 'pawn', 0], [1, 1, 'b', 'pawn', 0], [2, 1, 'b', 'pawn', 0], [3, 1, 'b', 'pawn', 0], [4, 1, 'b', 'pawn', 0], [5, 1, 'b', 'pawn', 0], [6, 1, 'b', 'pawn', 0], [7, 1, 'b', 'pawn', 0],
        [0, 0, 'b', 'rook', 0], [1, 0, 'b', 'knight', 0], [2, 0, 'b', 'bishop', 0], [3, 0, 'b', 'queen', 0], [4, 0, 'b', 'king', 0], [5, 0, 'b', 'bishop', 0], [6, 0, 'b', 'knight', 0], [7, 0, 'b', 'rook', 0],
    ]

class ChessPiece(object):
    def __init__(self, x, y, color, piece):
        self.x = x
        self.y = y
        self.piece = piece
        self.color = color
        self.firstmovepawns = True

    def drawpiece(self):
        if self.color == 'w':
            if self.piece == 'pawn':
                win.blit(wpawnimage, [50*self.x + 200, 50*self.y + 200,])
            elif self.piece == 'rook':
                win.blit(wrookimage, [50 * self.x + 200, 50 * self.y + 200, ])
            elif self.piece == 'knight':
                win.blit(wknightimage, [50 * self.x + 200, 50 * self.y + 200, ])
            elif self.piece == 'bishop':
                win.blit(wbishopimage, [50 * self.x + 200, 50 * self.y + 200, ])
            elif self.piece == 'queen':
                win.blit(wqueenimage, [50 * self.x + 200, 50 * self.y + 200, ])
            elif self.piece == 'king':
                win.blit(wkingimage, [50 * self.x + 200, 50 * self.y + 200, ])
        if self.color == 'b':
            if self.piece == 'pawn':
                win.blit(bpawnimage, [50*self.x + 200, 50*self.y + 200,])
            elif self.piece == 'rook':
                win.blit(brookimage, [50 * self.x + 200, 50 * self.y + 200, ])
            elif self.piece == 'knight':
                win.blit(bknightimage, [50 * self.x + 200, 50 * self.y + 200, ])
            elif self.piece == 'bishop':
                win.blit(bbishopimage, [50 * self.x + 200, 50 * self.y + 200, ])
            elif self.piece == 'queen':
                win.blit(bqueenimage, [50 * self.x + 200, 50 * self.y + 200, ])
            elif self.piece == 'king':
                win.blit(bkingimage, [50 * self.x + 200, 50 * self.y + 200, ])
        #pygame.draw.ellipse(win, piececolor, (50*self.x + 200, 50*self.y + 200, 50, 50))
    def showmoves(self, pieceposs, oppteampos):
        self.pieceposs = pieceposs
        self.oppteampos = oppteampos
        if self.piece == 'pawn':
            if self.color == 'w':
                forwardmove = True
                doubleforwardmove = True
                leftdiagmove = False
                rightdiagmove = False
                #change ability for dub jump on first move
                if self.firstmovepawns == False:
                    doubleforwardmove = False

                moves = []
                for i in range(len(self.pieceposs)):
                    if self.pieceposs[i][0] == self.x and self.pieceposs[i][1] == self.y-1:
                        forwardmove = False
                for i in range(len(self.pieceposs)):
                    if self.pieceposs[i][0] == self.x and self.pieceposs[i][1] == self.y-2:
                        doubleforwardmove = False
                for i in range(len(self.oppteampos)):
                    if self.oppteampos[i][0] == self.x-1 and self.oppteampos[i][1] == self.y-1:
                        leftdiagmove = True
                    if self.oppteampos[i][0] == self.x+1 and self.oppteampos[i][1] == self.y-1:
                        rightdiagmove = True
                if forwardmove and self.y >0:
                    moves.append((self.x, self.y-1))
                if doubleforwardmove and self.y > 1:
                    moves.append((self.x, self.y-2))
                if leftdiagmove and self.y >0 and self.x >0:
                    moves.append((self.x-1, self.y-1))
                if rightdiagmove and self.y >0 and self.x <7:
                    moves.append((self.x+1, self.y-1))
                for i in range(len(moves)):
                    pygame.draw.ellipse(win, (50, 50, 150), (50 * moves[i][0] + 210, 50 * moves[i][1] + 210, 30, 30))
                return moves
            if self.color == 'b':
                forwardmove = True
                doubleforwardmove = True
                leftdiagmove = False
                rightdiagmove = False
                if self.firstmovepawns == False:
                    doubleforwardmove = False
                moves = []
                for i in range(len(self.pieceposs)):
                    if self.pieceposs[i][0] == self.x and self.pieceposs[i][1] == self.y + 1:
                        forwardmove = False
                for i in range(len(self.pieceposs)):
                    if self.pieceposs[i][0] == self.x and self.pieceposs[i][1] == self.y+2:
                        doubleforwardmove = False
                for i in range(len(self.oppteampos)):
                    if self.oppteampos[i][0] == self.x - 1 and self.oppteampos[i][1] == self.y + 1:
                        leftdiagmove = True
                    if self.oppteampos[i][0] == self.x + 1 and self.oppteampos[i][1] == self.y + 1:
                        rightdiagmove = True
                if forwardmove and self.y <7:
                    moves.append((self.x, self.y + 1))
                if doubleforwardmove and self.y < 6:
                    moves.append((self.x, self.y+2))
                if leftdiagmove and self.y <8 and self.x >0:
                    moves.append((self.x - 1, self.y + 1))
                if rightdiagmove and self.y <8 and self.x <7:
                    moves.append((self.x + 1, self.y + 1))
                for i in range(len(moves)):
                    pygame.draw.ellipse(win, (50, 50, 150), (50 * moves[i][0] + 210, 50 * moves[i][1] + 210, 30, 30))
                return moves
        if self.piece == 'rook':
            moves = []

            #check for open spaces forward
            breakcheckforward = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckforward == False:
                        if (self.pieceposs[j][0] == self.x and self.pieceposs[j][1] == self.y-i) or self.y-i < 0:
                            forwardmoves = i
                            #check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][0] == self.x and self.oppteampos[l][1] == self.y-i:
                                    forwardmoves = i+1
                            breakcheckforward = True
            for i in range(1, forwardmoves):
                moves.append((self.x, self.y-i))

            #check for open spaces backward
            breakcheckbackward = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckbackward == False:
                        if (self.pieceposs[j][0] == self.x and self.pieceposs[j][1] == self.y + i) or self.y + i > 7:
                            backmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][0] == self.x and self.oppteampos[l][1] == self.y + i:
                                    backmoves = i+1
                            breakcheckbackward = True
            for i in range(1, backmoves):
                moves.append((self.x, self.y + i))

            #check for open spaces right
            breakcheckright = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckright == False:
                        if (self.pieceposs[j][1] == self.y and self.pieceposs[j][0] == self.x + i) or self.x + i > 7:
                            rightmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][1] == self.y and self.oppteampos[l][0] == self.x + i:
                                    rightmoves = i+1
                            breakcheckright = True
            for i in range(1, rightmoves):
                moves.append((self.x + i, self.y))

            #check for open spaces left
            breakcheckleft = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckleft == False:
                        if (self.pieceposs[j][1] == self.y and self.pieceposs[j][0] == self.x - i) or self.x - i < 0:
                            leftmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][1] == self.y and self.oppteampos[l][0] == self.x - i:
                                    leftmoves = i+1
                            breakcheckleft = True
            for i in range(1, leftmoves):
                moves.append((self.x - i, self.y))


            for i in range(len(moves)):
                pygame.draw.ellipse(win, (50, 50, 150), (50 * moves[i][0] + 210, 50 * moves[i][1] + 210, 30, 30))
            return moves
        if self.piece == 'knight':
            moves = []
            # topright
            piececheck = False
            for i in range(len(self.pieceposs)):
                if self.pieceposs[i][0] == self.x+1 and self.pieceposs[i][1] == self.y-2:
                    piececheck = True
                    for j in range(len(self.oppteampos)):
                        if self.oppteampos[j][0] == self.x + 1 and self.oppteampos[j][1] == self.y - 2:
                            moves.append((self.x+1, self.y-2))
            if piececheck == False and self.x+1<8 and self.y-2>=0:
                moves.append((self.x + 1, self.y - 2))

            #topleft
            piececheck = False
            for i in range(len(self.pieceposs)):
                if self.pieceposs[i][0] == self.x - 1 and self.pieceposs[i][1] == self.y - 2:
                    piececheck = True
                    for j in range(len(self.oppteampos)):
                        if self.oppteampos[j][0] == self.x - 1 and self.oppteampos[j][1] == self.y - 2:
                            moves.append((self.x - 1, self.y - 2))
            if piececheck == False and self.x - 1 >= 0 and self.y - 2 >= 0:
                moves.append((self.x - 1, self.y - 2))

            #righttop
            piececheck = False
            for i in range(len(self.pieceposs)):
                if self.pieceposs[i][0] == self.x + 2 and self.pieceposs[i][1] == self.y - 1:
                    piececheck = True
                    for j in range(len(self.oppteampos)):
                        if self.oppteampos[j][0] == self.x + 2 and self.oppteampos[j][1] == self.y - 1:
                            moves.append((self.x + 2, self.y - 1))
            if piececheck == False and self.x + 2 < 8 and self.y - 1 >= 0:
                moves.append((self.x + 2, self.y - 1))
            #rightdown
            piececheck = False
            for i in range(len(self.pieceposs)):
                if self.pieceposs[i][0] == self.x + 2 and self.pieceposs[i][1] == self.y + 1:
                    piececheck = True
                    for j in range(len(self.oppteampos)):
                        if self.oppteampos[j][0] == self.x + 2 and self.oppteampos[j][1] == self.y + 1:
                            moves.append((self.x + 2, self.y + 1))
            if piececheck == False and self.x + 2 < 8 and self.y + 1 < 8:
                moves.append((self.x + 2, self.y + 1))
            #downright
            piececheck = False
            for i in range(len(self.pieceposs)):
                if self.pieceposs[i][0] == self.x + 1 and self.pieceposs[i][1] == self.y + 2:
                    piececheck = True
                    for j in range(len(self.oppteampos)):
                        if self.oppteampos[j][0] == self.x + 1 and self.oppteampos[j][1] == self.y + 2:
                            moves.append((self.x + 1, self.y + 2))
            if piececheck == False and self.x + 1 < 8 and self.y + 2 < 8:
                moves.append((self.x + 1, self.y + 2))
            #downleft
            piececheck = False
            for i in range(len(self.pieceposs)):
                if self.pieceposs[i][0] == self.x - 1 and self.pieceposs[i][1] == self.y + 2:
                    piececheck = True
                    for j in range(len(self.oppteampos)):
                        if self.oppteampos[j][0] == self.x - 1 and self.oppteampos[j][1] == self.y + 2:
                            moves.append((self.x - 1, self.y + 2))
            if piececheck == False and self.x - 1 >= 0 and self.y + 2 < 8:
                moves.append((self.x - 1, self.y + 2))
            #lefttop
            piececheck = False
            for i in range(len(self.pieceposs)):
                if self.pieceposs[i][0] == self.x - 2 and self.pieceposs[i][1] == self.y - 1:
                    piececheck = True
                    for j in range(len(self.oppteampos)):
                        if self.oppteampos[j][0] == self.x - 2 and self.oppteampos[j][1] == self.y - 1:
                            moves.append((self.x - 2, self.y - 1))
            if piececheck == False and self.x - 2 >= 0 and self.y - 1 >= 0:
                moves.append((self.x - 2, self.y - 1))
            #leftdown
            piececheck = False
            for i in range(len(self.pieceposs)):
                if self.pieceposs[i][0] == self.x - 2 and self.pieceposs[i][1] == self.y + 1:
                    piececheck = True
                    for j in range(len(self.oppteampos)):
                        if self.oppteampos[j][0] == self.x - 2 and self.oppteampos[j][1] == self.y + 1:
                            moves.append((self.x - 2, self.y + 1))
            if piececheck == False and self.x - 2 >= 0 and self.y + 1 < 8:
                moves.append((self.x - 2, self.y + 1))

            for i in range(len(moves)):
                pygame.draw.ellipse(win, (50, 50, 150), (50 * moves[i][0] + 210, 50 * moves[i][1] + 210, 30, 30))
            return moves
        if self.piece == 'bishop':
            moves = []

            # check for open spaces forward
            breakcheckforward = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckforward == False:
                        if (self.pieceposs[j][0] == self.x + i and self.pieceposs[j][1] == self.y - i) or self.y - i < 0 or self.x + i > 7:
                            forwardmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][0] == self.x + i and self.oppteampos[l][1] == self.y - i:
                                    forwardmoves = i + 1
                            breakcheckforward = True
            for i in range(1, forwardmoves):
                moves.append((self.x + i, self.y - i))

            # check for open spaces backward
            breakcheckbackward = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckbackward == False:
                        if (self.pieceposs[j][0] == self.x - i and self.pieceposs[j][1] == self.y + i) or self.y + i > 7 or self.x - i < 0:
                            backmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][0] == self.x - i and self.oppteampos[l][1] == self.y + i:
                                    backmoves = i + 1
                            breakcheckbackward = True
            for i in range(1, backmoves):
                moves.append((self.x - i, self.y + i))

            # check for open spaces right
            breakcheckright = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckright == False:
                        if (self.pieceposs[j][1] == self.y + i and self.pieceposs[j][0] == self.x + i) or self.x + i > 7 or self.y + i > 7:
                            rightmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][1] == self.y + i and self.oppteampos[l][0] == self.x + i:
                                    rightmoves = i + 1
                            breakcheckright = True
            for i in range(1, rightmoves):
                moves.append((self.x + i, self.y + i))

            # check for open spaces left
            breakcheckleft = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckleft == False:
                        if (self.pieceposs[j][1] == self.y - i and self.pieceposs[j][0] == self.x - i) or self.x - i < 0 or self.y - i < 0:
                            leftmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][1] == self.y - i and self.oppteampos[l][0] == self.x - i:
                                    leftmoves = i + 1
                            breakcheckleft = True
            for i in range(1, leftmoves):
                moves.append((self.x - i, self.y - i))

            for i in range(len(moves)):
                pygame.draw.ellipse(win, (50, 50, 150), (50 * moves[i][0] + 210, 50 * moves[i][1] + 210, 30, 30))
            return moves
        if self.piece == 'queen':
            moves = []

            # check for open spaces forward
            breakcheckforward = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckforward == False:
                        if (self.pieceposs[j][0] == self.x and self.pieceposs[j][1] == self.y - i) or self.y - i < 0:
                            forwardmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][0] == self.x and self.oppteampos[l][1] == self.y - i:
                                    forwardmoves = i + 1
                            breakcheckforward = True
            for i in range(1, forwardmoves):
                moves.append((self.x, self.y - i))

            # check for open spaces backward
            breakcheckbackward = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckbackward == False:
                        if (self.pieceposs[j][0] == self.x and self.pieceposs[j][1] == self.y + i) or self.y + i > 7:
                            backmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][0] == self.x and self.oppteampos[l][1] == self.y + i:
                                    backmoves = i + 1
                            breakcheckbackward = True
            for i in range(1, backmoves):
                moves.append((self.x, self.y + i))

            # check for open spaces right
            breakcheckright = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckright == False:
                        if (self.pieceposs[j][1] == self.y and self.pieceposs[j][0] == self.x + i) or self.x + i > 7:
                            rightmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][1] == self.y and self.oppteampos[l][0] == self.x + i:
                                    rightmoves = i + 1
                            breakcheckright = True
            for i in range(1, rightmoves):
                moves.append((self.x + i, self.y))

            # check for open spaces left
            breakcheckleft = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckleft == False:
                        if (self.pieceposs[j][1] == self.y and self.pieceposs[j][0] == self.x - i) or self.x - i < 0:
                            leftmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][1] == self.y and self.oppteampos[l][0] == self.x - i:
                                    leftmoves = i + 1
                            breakcheckleft = True
            for i in range(1, leftmoves):
                moves.append((self.x - i, self.y))
            # check for open spaces forward
            breakcheckforward = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckforward == False:
                        if (self.pieceposs[j][0] == self.x + i and self.pieceposs[j][1] == self.y - i) or self.y - i < 0 or self.x + i > 7:
                            forwardmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][0] == self.x + i and self.oppteampos[l][1] == self.y - i:
                                    forwardmoves = i + 1
                            breakcheckforward = True
            for i in range(1, forwardmoves):
                moves.append((self.x + i, self.y - i))

            # check for open spaces backward
            breakcheckbackward = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckbackward == False:
                        if (self.pieceposs[j][0] == self.x - i and self.pieceposs[j][1] == self.y + i) or self.y + i > 7 or self.x - i < 0:
                            backmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][0] == self.x - i and self.oppteampos[l][1] == self.y + i:
                                    backmoves = i + 1
                            breakcheckbackward = True
            for i in range(1, backmoves):
                moves.append((self.x - i, self.y + i))

            # check for open spaces right
            breakcheckright = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckright == False:
                        if (self.pieceposs[j][1] == self.y + i and self.pieceposs[j][0] == self.x + i) or self.x + i > 7 or self.y + i > 7:
                            rightmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][1] == self.y + i and self.oppteampos[l][0] == self.x + i:
                                    rightmoves = i + 1
                            breakcheckright = True
            for i in range(1, rightmoves):
                moves.append((self.x + i, self.y + i))

            # check for open spaces left
            breakcheckleft = False
            for i in range(1, 9):
                for j in range(len(self.pieceposs)):
                    if breakcheckleft == False:
                        if (self.pieceposs[j][1] == self.y - i and self.pieceposs[j][0] == self.x - i) or self.x - i < 0 or self.y - i < 0:
                            leftmoves = i
                            # check if edgepiece is opp team
                            for l in range(len(self.oppteampos)):
                                if self.oppteampos[l][1] == self.y - i and self.oppteampos[l][0] == self.x - i:
                                    leftmoves = i + 1
                            breakcheckleft = True
            for i in range(1, leftmoves):
                moves.append((self.x - i, self.y - i))

            for i in range(len(moves)):
                pygame.draw.ellipse(win, (50, 50, 150), (50 * moves[i][0] + 210, 50 * moves[i][1] + 210, 30, 30))
            return moves
        if self.piece == 'king':
            moves = []
            forwardmove = True
            for i in range(len(self.pieceposs)):
                if self.x == self.pieceposs[i][0] and self.y - 1 == self.pieceposs[i][1]:
                    forwardmove = False
                    for j in range(len(self.oppteampos)):
                        if self.x == self.oppteampos[j][0] and self.y - 1 == self.oppteampos[j][1]:
                            moves.append((self.x, self.y - 1))
            if forwardmove:
                if self.y - 1 >= 0:
                    moves.append((self.x, self.y - 1))


            topright = True
            for i in range(len(self.pieceposs)):
                if self.x + 1 == self.pieceposs[i][0] and self.y - 1 == self.pieceposs[i][1]:
                    topright = False
                    for j in range(len(self.oppteampos)):
                        if self.x + 1 == self.oppteampos[j][0] and self.y - 1 == self.oppteampos[j][1]:
                            moves.append((self.x + 1, self.y - 1))
            if topright:
                if self.y - 1 >= 0 and self.x + 1 < 8:
                    moves.append((self.x + 1, self.y - 1))

            right = True
            for i in range(len(self.pieceposs)):
                if self.x + 1 == self.pieceposs[i][0] and self.y == self.pieceposs[i][1]:
                    right = False
                    for j in range(len(self.oppteampos)):
                        if self.x + 1 == self.oppteampos[j][0] and self.y == self.oppteampos[j][1]:
                            moves.append((self.x + 1, self.y))
            if right:
                if self.x + 1 < 8:
                    moves.append((self.x + 1, self.y))

            downright = True
            for i in range(len(self.pieceposs)):
                if self.x + 1 == self.pieceposs[i][0] and self.y + 1 == self.pieceposs[i][1]:
                    downright = False
                    for j in range(len(self.oppteampos)):
                        if self.x + 1 == self.oppteampos[j][0] and self.y + 1 == self.oppteampos[j][1]:
                            moves.append((self.x + 1, self.y + 1))
            if downright:
                if self.y + 1 < 8 and self.x + 1 < 8:
                    moves.append((self.x + 1, self.y + 1))

            down = True
            for i in range(len(self.pieceposs)):
                if self.x == self.pieceposs[i][0] and self.y + 1 == self.pieceposs[i][1]:
                    down = False
                    for j in range(len(self.oppteampos)):
                        if self.x == self.oppteampos[j][0] and self.y + 1 == self.oppteampos[j][1]:
                            moves.append((self.x, self.y + 1))
            if down:
                if self.y + 1 < 8:
                    moves.append((self.x, self.y + 1))

            downleft = True
            for i in range(len(self.pieceposs)):
                if self.x - 1 == self.pieceposs[i][0] and self.y + 1 == self.pieceposs[i][1]:
                    downleft = False
                    for j in range(len(self.oppteampos)):
                        if self.x - 1 == self.oppteampos[j][0] and self.y + 1 == self.oppteampos[j][1]:
                            moves.append((self.x - 1, self.y + 1))
            if downleft:
                if self.y + 1 < 8 and self.x - 1 >= 0:
                    moves.append((self.x - 1, self.y + 1))

            left = True
            for i in range(len(self.pieceposs)):
                if self.x - 1 == self.pieceposs[i][0] and self.y == self.pieceposs[i][1]:
                    left = False
                    for j in range(len(self.oppteampos)):
                        if self.x - 1 == self.oppteampos[j][0] and self.y == self.oppteampos[j][1]:
                            moves.append((self.x - 1, self.y))
            if left:
                if self.x - 1 >= 0:
                    moves.append((self.x - 1, self.y))

            topleft = True
            for i in range(len(self.pieceposs)):
                if self.x - 1 == self.pieceposs[i][0] and self.y - 1 == self.pieceposs[i][1]:
                    topleft = False
                    for j in range(len(self.oppteampos)):
                        if self.x - 1 == self.oppteampos[j][0] and self.y - 1 == self.oppteampos[j][1]:
                            moves.append((self.x - 1, self.y - 1))
            if topleft:
                if self.y - 1 >= 0 and self.x - 1 >= 0:
                    moves.append((self.x - 1, self.y - 1))


            #castle moves
            castleright = True
            castleLeft = True
            if self.firstmovepawns:
                pass

            for i in range(len(moves)):
                pygame.draw.ellipse(win, (50, 50, 150), (50 * moves[i][0] + 210, 50 * moves[i][1] + 210, 30, 30))
            return moves



def movepieces(win):
    global pieces
    global listofpieces
    global playerturn
    currentmousepos = (20, 20)
    clickedopenmoves = []
    currentmovingpiece = []
    stopshowingmoves = True
    for i in range(8):
        for j in range(8):
            if pygame.mouse.get_pos()[0] > ((50 * j) + 200) and pygame.mouse.get_pos()[0] < ((50 * j) + 200 + 50):
                if pygame.mouse.get_pos()[1] > ((50 * i) + 200) and pygame.mouse.get_pos()[1] < ((50 * i) + 200 + 50):
                    currentmousepos = (j, i)
    for i in range(len(pieces)):
        if pieces[i][0] == currentmousepos[0] and pieces[i][1] == currentmousepos[1]:
            if pygame.mouse.get_pressed()[0]:
                #check to make sure only the right color can move for that turn
                if i < 16 and playerturn == 0:
                    pieces[i][4] = 1
                    for j in range(len(pieces)):
                        if j != i:
                            pieces[j][4] = 0
                if i > 15 and playerturn == 1:
                    pieces[i][4] = 1
                    for j in range(len(pieces)):
                        if j != i:
                            pieces[j][4] = 0
    pieceposs = []
    blackpieceposs = []
    whitepieceposs = []
    for piece in pieces:
        pieceposs.append((piece[0], piece[1]))
        if piece[2] == 'b':
            blackpieceposs.append((piece[0], piece[1]))
        else:
            whitepieceposs.append((piece[0], piece[1]))
    # draw all pieces
    for piece in listofpieces:
        piece.drawpiece()
    # show moves for active pieces
    for i in range(len(listofpieces)):
        if pieces[i][4] == 1:
            if i < 16 and playerturn == 0:
                clickedopenmoves = listofpieces[i].showmoves(pieceposs, blackpieceposs)
                currentmovingpiece = (listofpieces[i], pieces[i])
            elif i > 15 and playerturn == 1:
                clickedopenmoves = listofpieces[i].showmoves(pieceposs, whitepieceposs)
                currentmovingpiece = (listofpieces[i], pieces[i])
    #checkfor clicked option to move on current piece
    for move in clickedopenmoves:
        if move == currentmousepos:
            if pygame.mouse.get_pressed()[0]:
                #check for piece in position and delete piece if there
                for piece in pieces:
                    if piece[0] == currentmousepos[0] and piece[1] == currentmousepos[1]:
                        #move piece off board to prevent problems with list
                        piece[0] = 20
                        piece[1] = 20
                #move piece
                currentmovingpiece[1][0] = currentmousepos[0]
                currentmovingpiece[1][1] = currentmousepos[1]
                #mark first turn for piece as done (for pawns)
                currentmovingpiece[0].firstmovepawns = False
                #switch turn
                if playerturn == 0:
                    playerturn = 1
                else:
                    playerturn = 0


    # change instance positions to match pieces variable
    for i in range(len(listofpieces)):
        listofpieces[i].x = pieces[i][0]
        listofpieces[i].y = pieces[i][1]
def drawboard(win):
    #draw checker pattern
    board = [[(0, 0) for _ in range(8)] for _ in range(8)]
    color = (0, 0, 0)
    currentmousepos = (1000, 1000, color)
    for i in range(len(board)):
        if color == (200, 200, 200):
            color = (133, 94, 66)
        else:
            color = (200, 200, 200)
        for j in range(len(board[i])):
            if pygame.mouse.get_pos()[0] > ((50*j)+200) and pygame.mouse.get_pos()[0] < ((50*j)+200+50):
                if pygame.mouse.get_pos()[1] > ((50*i)+200) and pygame.mouse.get_pos()[1] < ((50*i)+200+50):
                    currentmousepos = (i, j, color)
            pygame.draw.rect(win, color, ((50*j)+200, (50*i)+200, 50, 50))
            if color == (200, 200, 200):
                color = (133, 94, 66)
            else:
                color = (200, 200, 200)
    #draw boarder around board
    boardcolor = (60, 44, 30)
    pygame.draw.rect(win, boardcolor, (180, 180, 20, 440)); pygame.draw.rect(win, boardcolor, (600, 180, 20, 440)); pygame.draw.rect(win, boardcolor, (180, 180, 440, 20)); pygame.draw.rect(win, boardcolor, (180, 600, 440, 20))
    # draw mouse rect last so it overlaps
    pygame.draw.rect(win, currentmousepos[2], ((50 * currentmousepos[1]) + 190, (50 * currentmousepos[0]) + 190, 70, 70))
    currentmousepos = (1000, 1000, color)


def main(win):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawboard(win)
        movepieces(win)
        pygame.display.update()
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('chess')
#create class instance for each piece with starting positions
wpawn1 = ChessPiece(pieces[0][0], pieces[0][1], pieces[0][2], pieces[0][3])
wpawn2 = ChessPiece(pieces[1][0], pieces[1][1], pieces[1][2], pieces[1][3])
wpawn3 = ChessPiece(pieces[2][0], pieces[2][1], pieces[2][2], pieces[2][3])
wpawn4 = ChessPiece(pieces[3][0], pieces[3][1], pieces[3][2], pieces[3][3])
wpawn5 = ChessPiece(pieces[4][0], pieces[4][1], pieces[4][2], pieces[4][3])
wpawn6 = ChessPiece(pieces[5][0], pieces[5][1], pieces[5][2], pieces[5][3])
wpawn7 = ChessPiece(pieces[6][0], pieces[6][1], pieces[6][2], pieces[6][3])
wpawn8 = ChessPiece(pieces[7][0], pieces[7][1], pieces[7][2], pieces[7][3])
wrook1 = ChessPiece(pieces[8][0], pieces[8][1], pieces[8][2], pieces[8][3])
wknight1 = ChessPiece(pieces[9][0], pieces[9][1], pieces[9][2], pieces[9][3])
wbishop1 = ChessPiece(pieces[10][0], pieces[10][1], pieces[10][2], pieces[10][3])
wqueen1 = ChessPiece(pieces[11][0], pieces[11][1], pieces[11][2], pieces[11][3])
wking1 = ChessPiece(pieces[12][0], pieces[12][1], pieces[12][2], pieces[12][3])
wbishop2 = ChessPiece(pieces[13][0], pieces[13][1], pieces[13][2], pieces[13][3])
wknight2 = ChessPiece(pieces[14][0], pieces[14][1], pieces[14][2], pieces[14][3])
wrook2 = ChessPiece(pieces[15][0], pieces[15][1], pieces[15][2], pieces[15][3])
bpawn1 = ChessPiece(pieces[16][0], pieces[16][1], pieces[16][2], pieces[16][3])
bpawn2 = ChessPiece(pieces[17][0], pieces[17][1], pieces[17][2], pieces[17][3])
bpawn3 = ChessPiece(pieces[18][0], pieces[18][1], pieces[18][2], pieces[18][3])
bpawn4 = ChessPiece(pieces[19][0], pieces[19][1], pieces[19][2], pieces[19][3])
bpawn5 = ChessPiece(pieces[20][0], pieces[20][1], pieces[20][2], pieces[20][3])
bpawn6 = ChessPiece(pieces[21][0], pieces[21][1], pieces[21][2], pieces[21][3])
bpawn7 = ChessPiece(pieces[22][0], pieces[22][1], pieces[22][2], pieces[22][3])
bpawn8 = ChessPiece(pieces[23][0], pieces[23][1], pieces[23][2], pieces[23][3])
brook1 = ChessPiece(pieces[24][0], pieces[24][1], pieces[24][2], pieces[24][3])
bknight1 = ChessPiece(pieces[25][0], pieces[25][1], pieces[25][2], pieces[25][3])
bbishop1 = ChessPiece(pieces[26][0], pieces[26][1], pieces[26][2], pieces[26][3])
bqueen1 = ChessPiece(pieces[27][0], pieces[27][1], pieces[27][2], pieces[27][3])
bking1 = ChessPiece(pieces[28][0], pieces[28][1], pieces[28][2], pieces[28][3])
bbishop2 = ChessPiece(pieces[29][0], pieces[29][1], pieces[29][2], pieces[29][3])
bknight2 = ChessPiece(pieces[30][0], pieces[30][1], pieces[30][2], pieces[30][3])
brook2 = ChessPiece(pieces[31][0], pieces[31][1], pieces[31][2], pieces[31][3])
listofpieces = [wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8, wrook1, wknight1, wbishop1, wqueen1, wking1, wbishop2, wknight2, wrook2, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8, brook1, bknight1, bbishop1, bqueen1, bking1, bbishop2, bknight2, brook2]
main(win)  # start game
