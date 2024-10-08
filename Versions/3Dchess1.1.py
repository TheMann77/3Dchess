#version notes:

#First working game
#No UI
#No check, en passant, castling, checkmate


import numpy as np
import pygame
import chess
import io

class Pawn:
    def __init__(self, location, colour):
        self.name = 'P'
        self.location = location
        self.colour = colour

    def find_moves(self):
        moves = []
        if self.colour == 'W':
            if board[self.location[0], self.location[1] - 1, self.location[2]] == '  ':
                moves.append([self.location[0], self.location[1] - 1, self.location[2]])
                if board[self.location[0], self.location[1] - 2, self.location[2]] == '  ':
                    moves.append([self.location[0], self.location[1] - 2, self.location[2]])
            if board[self.location[0] - 1, self.location[1], self.location[2]] == '  ':
                moves.append([self.location[0] - 1, self.location[1], self.location[2]])
                if board[self.location[0] - 2, self.location[1], self.location[2]] == '  ':
                    moves.append([self.location[0] - 2, self.location[1], self.location[2]])
            for i in [-1,1]:
                if board[self.location[0], self.location[1] - 1, self.location[2] + i] != '  ':
                    moves.append([self.location[0], self.location[1] - 1, self.location[2] + i])
                if board[self.location[0] - 1, self.location[1], self.location[2] + i] != '  ':
                    moves.append([self.location[0] - 1, self.location[1], self.location[2] + i])
        if self.colour == 'B':
            if board[self.location[0], self.location[1] + 1, self.location[2]] == '  ':
                moves.append([self.location[0], self.location[1] + 1, self.location[2]])
                if board[self.location[0], self.location[1] + 2, self.location[2]] == '  ':
                    moves.append([self.location[0], self.location[1] + 2, self.location[2]])
            if board[self.location[0] + 1, self.location[1], self.location[2]] == '  ':
                moves.append([self.location[0] + 1, self.location[1], self.location[2]])
                if board[self.location[0] + 2, self.location[1], self.location[2]] == '  ':
                    moves.append([self.location[0] + 2, self.location[1], self.location[2]])
            for i in [-1,1]:
                if board[self.location[0], self.location[1] + 1, self.location[2] + i] != '  ':
                    moves.append([self.location[0], self.location[1] + 1, self.location[2] + i])
                if board[self.location[0] + 1, self.location[1], self.location[2] + i] != '  ':
                    moves.append([self.location[0] + 1, self.location[1], self.location[2] + i])
        return moves

        

class Rook:
    def __init__(self, location, colour):
        self.name = 'R'
        self.location = location
        self.colour = colour

    def find_moves(self):
        moves = []
        for i in [-1,1]:
            flag = False
            e = 1
            while flag == False:
                try:
                    if all(x>=0 for x in [self.location[0]+i*e, self.location[1], self.location[2]]):
                        if board[self.location[0]+i*e, self.location[1], self.location[2]] == '  ':
                            moves.append([self.location[0]+i*e, self.location[1], self.location[2]])
                            e += 1
                        elif board[self.location[0]+i*e, self.location[1], self.location[2]].colour != self.colour:
                            moves.append([self.location[0]+i*e, self.location[1], self.location[2]])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        for i in [-1,1]:
            flag = False
            e = 1
            while flag == False:
                try:
                    if all(x>=0 for x in [self.location[0], self.location[1]+i*e, self.location[2]]):
                        if board[self.location[0], self.location[1]+i*e, self.location[2]] == '  ':
                            moves.append([self.location[0], self.location[1]+i*e, self.location[2]])
                            e += 1
                        elif board[self.location[0], self.location[1]+i*e, self.location[2]].colour != self.colour:
                            moves.append([self.location[0], self.location[1]+i*e, self.location[2]])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        for i in [-1,1]:
            flag = False
            e = 1
            while flag == False:
                try:
                    if all(x>=0 for x in [self.location[0], self.location[1], self.location[2]+i*e]):
                        if board[self.location[0], self.location[1], self.location[2]+i*e] == '  ':
                            moves.append([self.location[0], self.location[1], self.location[2]+i*e])
                            e += 1
                        elif board[self.location[0], self.location[1], self.location[2]+i*e].colour != self.colour:
                            moves.append([self.location[0], self.location[1], self.location[2]+i*e])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        return moves
                
    
class Bishop:
    def __init__(self, location, colour):
        self.name = 'B'
        self.location = location
        self.colour = colour

    def find_moves(self):
        moves = []
        for i in [-1,1]:
            for a in [-1,1]:
                flag = False
                e = 1
                while flag == False:
                    try:
                        if all(x>=0 for x in [self.location[0]+i*e, self.location[1]+a*e, self.location[2]]):
                            if board[self.location[0]+i*e, self.location[1]+a*e, self.location[2]] == '  ':
                                moves.append([self.location[0]+i*e, self.location[1]+a*e, self.location[2]])
                                e += 1
                            elif board[self.location[0]+i*e, self.location[1]+a*e, self.location[2]].colour != self.colour:
                                moves.append([self.location[0]+i*e, self.location[1]+a*e, self.location[2]])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1,1]:
            for a in [-1,1]:
                flag = False
                e = 1
                while flag == False:
                    try:
                        if all(x>=0 for x in [self.location[0], self.location[1]+i*e, self.location[2]+a*e]):
                            if board[self.location[0], self.location[1]+i*e, self.location[2]+a*e] == '  ':
                                moves.append([self.location[0], self.location[1]+i*e, self.location[2]+a*e])
                                e += 1
                            elif board[self.location[0], self.location[1]+i*e, self.location[2]+a*e].colour != self.colour:
                                moves.append([self.location[0], self.location[1]+i*e, self.location[2]+a*e])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1,1]:
            for a in [-1,1]:
                flag = False
                e = 1
                while flag == False:
                    try:
                        if all(x>=0 for x in [self.location[0]+i*e, self.location[1], self.location[2]+a*e]):
                            if board[self.location[0]+i*e, self.location[1], self.location[2]+a*e] == '  ':
                                moves.append([self.location[0]+i*e, self.location[1], self.location[2]+a*e])
                                e += 1
                            elif board[self.location[0]+i*e, self.location[1], self.location[2]+a*e].colour != self.colour:
                                moves.append([self.location[0]+i*e, self.location[1], self.location[2]+a*e])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        return moves
        
class Knight:
    def __init__(self, location, colour):
        self.name = 'N'
        self.location = location
        self.colour = colour

    def find_moves(self):
        moves = []
        for a in range(3):
            for x in [-1,1]:
                for b in range(3):
                    for y in[-1,1]:
                        if a!=b:
                            vector = [0,0,0]
                            vector[a] = 2*x
                            vector[b] = y
                            try:
                                if all(x>=0 for x in [self.location[0]+vector[0], self.location[1]+vector[1], self.location[2]+vector[2]]):
                                    if board[self.location[0]+vector[0], self.location[1]+vector[1], self.location[2]+vector[2]] ==  '  ':
                                        moves.append([self.location[0]+vector[0], self.location[1]+vector[1], self.location[2]+vector[2]])
                                    elif board[self.location[0]+vector[0], self.location[1]+vector[1], self.location[2]+vector[2]].colour != self.colour:
                                        moves.append([self.location[0]+vector[0], self.location[1]+vector[1], self.location[2]+vector[2]])
                            except IndexError:
                                pass
        return moves

class King:
    def __init__(self, location, colour):
        self.name = 'K'
        self.location = location
        self.colour = colour

    def find_moves(self):
        moves = []
        for a in [-1,0,1]:
            for b in [-1,0,1]:
                for c in [-1,0,1]:
                    if [a,b,c].count(0) in [1,2]:
                        try:
                            if board[self.location[0]+a, self.location[1]+b, self.location[2]+c] == '  ':
                                moves.append([self.location[0]+a, self.location[1]+b, self.location[2]+c])
                            elif board[self.location[0]+a, self.location[1]+b, self.location[2]+c].colour != self.colour:
                                moves.append([self.location[0]+a, self.location[1]+b, self.location[2]+c])
                        except IndexError:
                            pass                   

class Queen:
    def __init__(self, location, colour):
        self.name = 'Q'
        self.location = location
        self.colour = colour

    def find_moves(self):
        moves = []
        for i in [-1,1]:
            for a in [-1,1]:
                flag = False
                e = 1
                while flag == False:
                    try:
                        if all(x>=0 for x in [self.location[0]+i*e, self.location[1]+a*e, self.location[2]]):
                            if board[self.location[0]+i*e, self.location[1]+a*e, self.location[2]] == '  ':
                                moves.append([self.location[0]+i*e, self.location[1]+a*e, self.location[2]])
                                e += 1
                            elif board[self.location[0]+i*e, self.location[1]+a*e, self.location[2]].colour != self.colour:
                                moves.append([self.location[0]+i*e, self.location[1]+a*e, self.location[2]])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1,1]:
            for a in [-1,1]:
                flag = False
                e = 1
                while flag == False:
                    try:
                        if all(x>=0 for x in [self.location[0], self.location[1]+i*e, self.location[2]+a*e]):
                            if board[self.location[0], self.location[1]+i*e, self.location[2]+a*e] == '  ':
                                moves.append([self.location[0], self.location[1]+i*e, self.location[2]+a*e])
                                e += 1
                            elif board[self.location[0], self.location[1]+i*e, self.location[2]+a*e].colour != self.colour:
                                moves.append([self.location[0], self.location[1]+i*e, self.location[2]+a*e])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1,1]:
            for a in [-1,1]:
                flag = False
                e = 1
                while flag == False:
                    try:
                        if all(x>=0 for x in [self.location[0]+i*e, self.location[1], self.location[2]+a*e]):
                            if board[self.location[0]+i*e, self.location[1], self.location[2]+a*e] == '  ':
                                moves.append([self.location[0]+i*e, self.location[1], self.location[2]+a*e])
                                e += 1
                            elif board[self.location[0]+i*e, self.location[1], self.location[2]+a*e].colour != self.colour:
                                moves.append([self.location[0]+i*e, self.location[1], self.location[2]+a*e])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1,1]:
            flag = False
            e = 1
            while flag == False:
                try:
                    if all(x>=0 for x in [self.location[0]+i*e, self.location[1], self.location[2]]):
                        if board[self.location[0]+i*e, self.location[1], self.location[2]] == '  ':
                            moves.append([self.location[0]+i*e, self.location[1], self.location[2]])
                            e += 1
                        elif board[self.location[0]+i*e, self.location[1], self.location[2]].colour != self.colour:
                            moves.append([self.location[0]+i*e, self.location[1], self.location[2]])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        for i in [-1,1]:
            flag = False
            e = 1
            while flag == False:
                try:
                    if all(x>=0 for x in [self.location[0], self.location[1]+i*e, self.location[2]]):
                        if board[self.location[0], self.location[1]+i*e, self.location[2]] == '  ':
                            moves.append([self.location[0], self.location[1]+i*e, self.location[2]])
                            e += 1
                        elif board[self.location[0], self.location[1]+i*e, self.location[2]].colour != self.colour:
                            moves.append([self.location[0], self.location[1]+i*e, self.location[2]])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        for i in [-1,1]:
            flag = False
            e = 1
            while flag == False:
                try:
                    if all(x>=0 for x in [self.location[0], self.location[1], self.location[2]+i*e]):
                        if board[self.location[0], self.location[1], self.location[2]+i*e] == '  ':
                            moves.append([self.location[0], self.location[1], self.location[2]+i*e])
                            e += 1
                        elif board[self.location[0], self.location[1], self.location[2]+i*e].colour != self.colour:
                            moves.append([self.location[0], self.location[1], self.location[2]+i*e])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        return moves
        
def board_to_fen(layer):
    # Use StringIO to build string more efficiently than concatenating
    with io.StringIO() as s:
        for row in layer:
            empty = 0
            for cell in row:

                if cell == '  ':
                    empty += 1
                
                else:
                    c = str.lower(cell.colour)
                    if empty > 0:
                        s.write(str(empty))
                        empty = 0
                    s.write(cell.name.upper() if c == 'w' else cell.name.lower())
                    
            if empty > 0:
                s.write(str(empty))
            s.write('/')
        # Move one position back to overwrite last '/'
        s.seek(s.tell() - 1)
        # If you do not have the additional information choose what to put
        s.write(' w KQkq - 0 1')
        return s.getvalue()


def output_board():
    
    for x in board:
        for y in x:
            print([a if a == '  ' else a.colour + a.name for a in y])
        print()
        


#create board
rows = 8
columns = 8
boards = 3
board = []
for a in range(boards):
    board.append([])
    for b in range(columns):
        board[-1].append([])
        for x in range(rows):
            board[-1][-1].append('  ')
board = np.array(board, dtype=object)

#Setup board
setup = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
colours = ['W', 'B']
for i in range(2):
    for e in range(len(setup)):
        board[-i*2+2, -i*7+7, e] = setup[e]([-i*2+2, -i*7+7, e], colours[i])
        board[-i*2+2, -i*5+6, e] = Pawn([-i*2+2, -i*5+6, e], colours[i])




castling = [True, True]
enpassant = [False, False]
check = [False, False]
checkmate = [False, False]
stalemate = False
turn = 'W'
backpieces = {'Q':Queen, 'R':Rook, 'B':Bishop, 'K':Knight}

while checkmate == [False, False] and stalemate == False:
    output_board()
    movefrom = [int(input("board")), int(input("row")), int(input("column"))]
    valid = False
    if board[movefrom[0],movefrom[1],movefrom[2]] != '  ':
        if board[movefrom[0],movefrom[1],movefrom[2]].colour == turn:
            valid = True
    while valid == False:
        print("invalid")
        movefrom = [int(input("board")), int(input("row")), int(input("column"))]
        if board[movefrom[0],movefrom[1],movefrom[2]] != '  ':
            if board[movefrom[0],movefrom[1],movefrom[2]].colour == turn:
                 valid = True
    print()
    moveto = [int(input("board")), int(input("row")), int(input("column"))]
    while moveto not in board[movefrom[0],movefrom[1],movefrom[2]].find_moves():
        print("invalid")
        moveto = [int(input("board")), int(input("row")), int(input("column"))]
        
    board[moveto[0],moveto[1],moveto[2]] = board[movefrom[0],movefrom[1],movefrom[2]]
    board[movefrom[0],movefrom[1],movefrom[2]] = '  '
    board[moveto[0],moveto[1],moveto[2]].location = moveto

    if (moveto[0] == 0 and moveto[1] == 0 and turn == 'W') or (moveto[0] == 2 and moveto[1] == 2 and turn == 'B'):
        if board[moveto[0],moveto[1],moveto[2]].name == 'P':
            board[moveto[0],moveto[1],moveto[2]] = backpieces[input("Queen(Q), Rook(R), Bishop(B) or Knight(N)")](board[moveto[0],moveto[1],moveto[2]].location, board[moveto[0],moveto[1],moveto[2]].colour)
        


    if turn == 'W':
        turn = 'B'
    else:
        turn = 'W'
