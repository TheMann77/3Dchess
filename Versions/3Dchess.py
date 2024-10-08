import numpy as np

class Pawn:
    def __init__(self, location, colour):
        self.name = 'P'
        self.location = location
        self.colour = colour

    def check_move(self, to, board):
        can_move = False
        
        if self.colour == 'W':
            if board[to[0], to[1], to[2]] == '  ':
                if board[to[0], to[1], to[2]].colour != self.colour:
                    if self.location[0] == 2 and self.location[1] == 6:
                        if to[0] == self.location[0] and to[1] == self.location[1] - 2 and to[2] == self.location[2]:
                            if board[self.location[0], self.location[1] - 1, self.location[2]] == '  ':
                                can_move = True
                        elif to[0] == self.location[0] - 2 and to[1] == self.location[1] and to[2] == self.location[2]:
                            if board[self.location[0] - 1, self.location[1], self.location[2]] == '  ':
                                can_move = True
                    elif to[0] == self.location[0] and to[1] == self.location[1] - 1 and to[2] == self.location[2]:
                        can_move = True
                    elif to[0] == self.location[0] - 1 and to[1] == self.location[1] and to[2] == self.location[2]:
                        can_move = True
            else:
                if (to[0] == self.location[0] and to[1] == self.location[1] - 1) or (to[0] == self.location[0] - 1 and to[1] == self.location[1]):
                    if abs(to[2] - self.location[2]) == 1:
                        can_move == True

        if self.colour == 'B':
            if board[to[0], to[1], to[2]] != '  ':
                if board[to[0], to[1], to[2]].colour != self.colour:
                    if self.location[0] == 0 and self.location[1] == 1:
                        if to[0] == self.location[0] and to[1] == self.location[1] + 2 and to[2] == self.location[2]:
                            if board[self.location[0], self.location[1] + 1, self.location[2]] == '  ':
                                can_move = True
                        elif to[0] == self.location[0] + 2 and to[1] == self.location[1] and to[2] == self.location[2]:
                            if board[self.location[0] + 1, self.location[1], self.location[2]] == '  ':
                                can_move = True
                    elif to[0] == self.location[0] and to[1] == self.location[1] + 1 and to[2] == self.location[2]:
                        can_move = True
                    elif to[0] == self.location[0] + 1 and to[1] == self.location[1] and to[2] == self.location[2]:
                        can_move = True
            else:
                if (to[0] == self.location[0] and to[1] == self.location[1] + 1) or (to[0] == self.location[0] + 1 and to[1] == self.location[1]):
                    if abs(to[2] - self.location[2]) == 1:
                        can_move == True
            
        
        return can_move

class Rook:
    def __init__(self, location, colour):
        self.name = 'R'
        self.location = location
        self.colour = colour

    def check_move(self, to, board):
        can_move = False
        if to[0] != self.location[0] and to[1] == self.location[1] and to[2] == self.location[2]:
            can_move = True
            for i in range(self.location[0] + int((to[0]-self.location[0])/abs(to[0]-self.location[0])), to[0], int((to[0]-self.location[0])/abs(to[0]-self.location[0]))):
                if board[i,self.location[1], self.location[2]] != '  ':
                    can_move = False
        elif to[0] == self.location[0] and to[1] != self.location[1] and to[2] == self.location[2]:
            can_move = True
            for i in range(self.location[1] + int((to[1]-self.location[1])/abs(to[1]-self.location[1])), to[1], int((to[1]-self.location[1])/abs(to[1]-self.location[1]))):
                if board[self.location[0],i, self.location[2]] != '  ':
                    can_move = False
        elif to[0] == self.location[0] and to[1] == self.location[1] and to[2] != self.location[2]:
            can_move = True
            for i in range(self.location[2] + int((to[2]-self.location[2])/abs(to[2]-self.location[2])), to[2], int((to[2]-self.location[2])/abs(to[2]-self.location[2]))):
                if board[self.location[0],self.location[1], i] != '  ':
                    can_move = False
        if board[to[0],to[1],to[2]] != '  ':
            if board[to[0],to[1],to[2]].colour == self.colour:
                can_move = False
        return can_move
    
class Bishop:
    def __init__(self, location, colour):
        self.name = 'B'
        self.location = location
        self.colour = colour
"""
    def check_move(self, to, board):
        can_move = False
        if to[0] == self.location[0] and abs(to[1] - self.location[1]) == abs(to[2] - self.location[2]):
            can_move = True
            for i in range(self.location[1] + (to[1]-self.location[1])/abs(to[1]-self.location[1]), to[1], (to[1]-self.location[1])/abs(to[1]-self.location[1]))
                if board[self.location[0],i, *******enter how y value changes with x******] != '  ':
                    can_move = False
"""
class Knight:
    def __init__(self, location, colour):
        self.name = 'N'
        self.location = location
        self.colour = colour

class King:
    def __init__(self, location, colour):
        self.name = 'K'
        self.location = location
        self.colour = colour

class Queen:
    def __init__(self, location, colour):
        self.name = 'Q'
        self.location = location
        self.colour = colour

def output_board(board):
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
