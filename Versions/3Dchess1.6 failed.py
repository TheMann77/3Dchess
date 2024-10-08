#version notes:

#working UI
#removed check for ai preperation
#No checkmate, castling, en passant, but I think castling and en passant lose their purpose in 3 dimensions
import numpy as np
import pygame, sys
import random


class Pawn:
    def __init__(self, location, colour):
        self.name = 'P'
        self.location = location
        self.colour = colour
        self.symbol = '♙'
        self.value = 100

    def find_moves(self):

        
        moves = []
        if self.colour == 'W':
            try:
                if board[self.location[0], self.location[1] - 1, self.location[2]] == '  ':
                    moves.append([self.location[0], self.location[1] - 1, self.location[2]])
                    if board[self.location[0], self.location[1] - 2, self.location[2]] == '  ' and self.location[0] == 2 and self.location[1] == 6:
                        moves.append([self.location[0], self.location[1] - 2, self.location[2]])
            except IndexError:
                pass
            try:
                if board[self.location[0] - 1, self.location[1], self.location[2]] == '  ':
                    moves.append([self.location[0] - 1, self.location[1], self.location[2]])
                    if board[self.location[0] - 2, self.location[1], self.location[2]] == '  ' and self.location[0] == 2 and self.location[1] == 6:
                        moves.append([self.location[0] - 2, self.location[1], self.location[2]])
            except IndexError:
                pass
            for i in [-1,1]:
                try:
                    if board[self.location[0], self.location[1] - 1, self.location[2] + i] != '  ':
                        moves.append([self.location[0], self.location[1] - 1, self.location[2] + i])
                except IndexError:
                    pass
                try:
                    if board[self.location[0] - 1, self.location[1], self.location[2] + i] != '  ':
                        moves.append([self.location[0] - 1, self.location[1], self.location[2] + i])
                except IndexError:
                    pass
        if self.colour == 'B':
            try:
                if board[self.location[0], self.location[1] + 1, self.location[2]] == '  ':
                    moves.append([self.location[0], self.location[1] + 1, self.location[2]])
                    if board[self.location[0], self.location[1] + 2, self.location[2]] == '  ' and self.location[0] == 0 and self.location[1] == 1:
                        moves.append([self.location[0], self.location[1] + 2, self.location[2]])
            except IndexError:
                pass
            try:
                if board[self.location[0] + 1, self.location[1], self.location[2]] == '  ':
                    moves.append([self.location[0] + 1, self.location[1], self.location[2]])
                    if board[self.location[0] + 2, self.location[1], self.location[2]] == '  ' and self.location[0] == 0 and self.location[1] == 1:
                        moves.append([self.location[0] + 2, self.location[1], self.location[2]])
            except IndexError:
                pass
            for i in [-1,1]:
                try:
                    if board[self.location[0], self.location[1] + 1, self.location[2] + i] != '  ':
                        moves.append([self.location[0], self.location[1] + 1, self.location[2] + i])
                except IndexError:
                    pass
                try:
                    if board[self.location[0] + 1, self.location[1], self.location[2] + i] != '  ':
                        moves.append([self.location[0] + 1, self.location[1], self.location[2] + i])
                except IndexError:
                    pass

        return moves

        

class Rook:
    def __init__(self, location, colour):
        self.name = 'R'
        self.location = location
        self.colour = colour
        self.symbol = '♖'
        self.value = 525

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
        self.symbol = '♗'
        self.value = 350

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
        self.symbol = '♘'
        self.value = 350

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
        self.symbol = '♔'
        self.value = 10000

    def find_moves(self):
        moves = []
        for a in [-1,0,1]:
            for b in [-1,0,1]:
                for c in [-1,0,1]:
                    if [a,b,c].count(0) in [1,2]:
                        try:
                            if all(x>=0 for x in [self.location[0]+a, self.location[1]+b, self.location[2]+c]):
                                if board[self.location[0]+a, self.location[1]+b, self.location[2]+c] == '  ':
                                    moves.append([self.location[0]+a, self.location[1]+b, self.location[2]+c])
                                elif board[self.location[0]+a, self.location[1]+b, self.location[2]+c].colour != self.colour:
                                    moves.append([self.location[0]+a, self.location[1]+b, self.location[2]+c])
                        except IndexError:
                            pass     
        return moves

class Queen:
    def __init__(self, location, colour):
        self.name = 'Q'
        self.location = location
        self.colour = colour
        self.symbol = '♕'
        self.value = 1000

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



def str_board(board):
    for x in board:
        for y in x:
            print([a if a == '  ' else a.colour + a.name for a in y])
        print()

def output_board():
    
    for a in range(boards):
        for b in range(rows):
            for c in range(columns):
                if (a + b + c) % 2 == 0:
                    pygame.draw.rect(screen, (245,245,200), (30*c,30*b+270*a,30,30))
                else:
                    pygame.draw.rect(screen, (225,198,153), (30*c,30*b+270*a,30,30))
                if board[a,b,c] != '  ':
                    screen.blit(font.render(board[a,b,c].name, True, (255,255,255) if board[a,b,c].colour == 'W' else (0,0,0)), (30*c+5,30*b+270*a+5))
    
def output_moves(moves):
    surface = pygame.Surface((240,780), pygame.SRCALPHA)
    for move in moves:
        pygame.draw.circle(surface, (0,0,0,50), (30*move[2]+15, 30*move[1]+270*move[0]+15), 10)
    screen.blit(surface, (0,0))


def evaluate(board, colour):
    score = 0
    for a in range(boards):
        for b in range(columns):
            for c in range(rows):
                if board[a,b,c] != '  ':
                    if board[a,b,c].colour == colour:
                        score += board[a,b,c].value
                    else:
                        score -= board[a,b,c].value
    return score

def move_piece(movefrom, moveto, board):
    board[moveto[0],moveto[1],moveto[2]] = board[movefrom[0],movefrom[1],movefrom[2]]
    board[movefrom[0],movefrom[1],movefrom[2]] = '  '
    board[moveto[0],moveto[1],moveto[2]].location = moveto

#create board
global rows
rows = 8
global columns
columns = 8
global boards
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
setup = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
colours = ['W', 'B']
for i in range(2):
    for e in range(len(setup)):
        board[-i*2+2, -i*7+7, e] = setup[e]([-i*2+2, -i*7+7, e], colours[i])
        board[-i*2+2, -i*5+6, e] = Pawn([-i*2+2, -i*5+6, e], colours[i])


pygame.init()

screen = pygame.display.set_mode((240, 780))
surface = pygame.Surface((240,780), pygame.SRCALPHA)

font = pygame.font.SysFont(None, 35)


castling = [True, True]
enpassant = [False, False]
check = [False, False]
checkmate = [False, False]
stalemate = False
kings = [[2,7,4],[0,0,4]]
turn = 'W'
backpieces = {'Q':Queen, 'R':Rook, 'B':Bishop, 'K':Knight}
mode = 'input_from'
while checkmate == [False, False] and stalemate == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    screen.fill((255,255,255))
    output_board()
    if turn == 'W':
        if mode == 'input_from':
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if not((y > 240 and y < 270) or (y > 510 and y < 540)):
                    a = y//280
                    b = ((y-30*a)%240)//30
                    c = x // 30
                    if board[a,b,c] != '  ':
                        if board[a,b,c].colour == turn:
                            movefrom = [a,b,c]
                            mode = 'input_to'
    
        if mode == 'input_to':
            output_moves(board[movefrom[0], movefrom[1], movefrom[2]].find_moves())
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if not((y > 240 and y < 270) or (y > 510 and y < 540)):
                    a = y//280
                    b = ((y-30*a)%240)//30
                    c = x // 30
                    if [a,b,c] in board[movefrom[0], movefrom[1], movefrom[2]].find_moves():
                        moveto = [a,b,c]
                        move_piece(movefrom, moveto, board)
    
                        if (moveto[0] == 0 and moveto[1] == 0 and turn == 'W') or (moveto[0] == 2 and moveto[1] == 2 and turn == 'B'):
                            if board[moveto[0],moveto[1],moveto[2]].name == 'P':
                                board[moveto[0],moveto[1],moveto[2]] = backpieces['Q'](board[moveto[0],moveto[1],moveto[2]].location, board[moveto[0],moveto[1],moveto[2]].colour)

                            
    
    
                        if turn == 'W':
                            turn = 'B'
                        else:
                            turn = 'W'
                                    
                        mode = 'input_from'
                        
                    elif board[a,b,c] != '  ':
                        if board[a,b,c].colour == turn:
                            movefrom = [a,b,c]
        
    else:
        posmoves = []
        for a in range(boards):
            for b in range(rows):
                for c in range(columns):
                    if board[a,b,c] != '  ':
                        if board[a,b,c].colour == turn:
                            try:
                                for move in board[a,b,c].find_moves():
                                    posmoves.append([[a,b,c], move])
                            except TypeError:
                                pass
        if len(posmoves) >= 1:
            #move = random.choice(posmoves)
            maxscore = -100000
            maxmove = []
            for posmove in posmoves:
                tempboard = np.copy(board)
                move_piece(posmove[0], posmove[1], tempboard)
                score = evaluate(tempboard, turn)
                if score > maxscore:
                    maxscore = score
                    maxmove = [posmove]
                elif score == maxscore:
                    maxmove.append(posmove)
            move = random.choice(maxmove)
                
        else:
            print('checkmate')
        
        movefrom, moveto = move[0], move[1]
        move_piece(movefrom, moveto, board)

        if (moveto[0] == 0 and moveto[1] == 0 and turn == 'W') or (moveto[0] == 2 and moveto[1] == 2 and turn == 'B'):
            if board[moveto[0],moveto[1],moveto[2]].name == 'P':
                board[moveto[0],moveto[1],moveto[2]] = backpieces['Q'](board[moveto[0],moveto[1],moveto[2]].location, board[moveto[0],moveto[1],moveto[2]].colour)
        if board[moveto[0],moveto[1],moveto[2]].name == 'K':
            if board[moveto[0],moveto[1],moveto[2]].colour == 'W':
                kings[0] = [moveto[0],moveto[1],moveto[2]]
            else:
                kings[1] = [moveto[0],moveto[1],moveto[2]]
        turn = 'W'
        
        
    pygame.display.flip()
