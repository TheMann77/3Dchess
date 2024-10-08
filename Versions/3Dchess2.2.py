# version notes:

# working UI
# has working check
# No checkmate, castling, en passant, but I think castling and en passant lose their purpose in 3 dimensions
# Working multi-move minimax ai
# No position value

import numpy as np
import pygame
import sys
import random
import time

depth = 3




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
                    if board[self.location[0], self.location[1] - 2, self.location[2]] == '  ' and self.location[
                            0] == 2 and self.location[1] == 6:
                        moves.append([self.location[0], self.location[1] - 2, self.location[2]])
            except IndexError:
                pass
            try:
                if board[self.location[0] - 1, self.location[1], self.location[2]] == '  ':
                    moves.append([self.location[0] - 1, self.location[1], self.location[2]])
                    if board[self.location[0] - 2, self.location[1], self.location[2]] == '  ' and self.location[
                            0] == 2 and self.location[1] == 6:
                        moves.append([self.location[0] - 2, self.location[1], self.location[2]])
            except IndexError:
                pass
            for i in [-1, 1]:
                try:
                    if board[self.location[0], self.location[1] - 1, self.location[2] + i] != '  ':
                        if board[self.location[0], self.location[1] - 1, self.location[2] + i].colour != self.colour:
                            moves.append([self.location[0], self.location[1] - 1, self.location[2] + i])
                except IndexError:
                    pass
                try:
                    if board[self.location[0] - 1, self.location[1], self.location[2] + i] != '  ':
                        if board[self.location[0] - 1, self.location[1], self.location[2] + i].colour != self.colour:
                            moves.append([self.location[0] - 1, self.location[1], self.location[2] + i])
                except IndexError:
                    pass
        if self.colour == 'B':
            try:
                if board[self.location[0], self.location[1] + 1, self.location[2]] == '  ':
                    moves.append([self.location[0], self.location[1] + 1, self.location[2]])
                    if board[self.location[0], self.location[1] + 2, self.location[2]] == '  ' and self.location[
                            0] == 0 and self.location[1] == 1:
                        moves.append([self.location[0], self.location[1] + 2, self.location[2]])
            except IndexError:
                pass
            try:
                if board[self.location[0] + 1, self.location[1], self.location[2]] == '  ':
                    moves.append([self.location[0] + 1, self.location[1], self.location[2]])
                    if board[self.location[0] + 2, self.location[1], self.location[2]] == '  ' and self.location[
                            0] == 0 and self.location[1] == 1:
                        moves.append([self.location[0] + 2, self.location[1], self.location[2]])
            except IndexError:
                pass
            for i in [-1, 1]:
                try:
                    if board[self.location[0], self.location[1] + 1, self.location[2] + i] != '  ':
                        if board[self.location[0], self.location[1] + 1, self.location[2] + i].colour != self.colour:
                            moves.append([self.location[0], self.location[1] + 1, self.location[2] + i])
                except IndexError:
                    pass
                try:
                    if board[self.location[0] + 1, self.location[1], self.location[2] + i] != '  ':
                        if board[self.location[0] + 1, self.location[1], self.location[2] + i].colour != self.colour:
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
        for i in [-1, 1]:
            flag = False
            e = 1
            while not flag:
                try:
                    if all(x >= 0 for x in [self.location[0] + i * e, self.location[1], self.location[2]]):
                        if board[self.location[0] + i * e, self.location[1], self.location[2]] == '  ':
                            moves.append([self.location[0] + i * e, self.location[1], self.location[2]])
                            e += 1
                        elif board[self.location[0] + i * e, self.location[1], self.location[2]].colour != self.colour:
                            moves.append([self.location[0] + i * e, self.location[1], self.location[2]])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        for i in [-1, 1]:
            flag = False
            e = 1
            while not flag:
                try:
                    if all(x >= 0 for x in [self.location[0], self.location[1] + i * e, self.location[2]]):
                        if board[self.location[0], self.location[1] + i * e, self.location[2]] == '  ':
                            moves.append([self.location[0], self.location[1] + i * e, self.location[2]])
                            e += 1
                        elif board[self.location[0], self.location[1] + i * e, self.location[2]].colour != self.colour:
                            moves.append([self.location[0], self.location[1] + i * e, self.location[2]])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        for i in [-1, 1]:
            flag = False
            e = 1
            while not flag:
                try:
                    if all(x >= 0 for x in [self.location[0], self.location[1], self.location[2] + i * e]):
                        if board[self.location[0], self.location[1], self.location[2] + i * e] == '  ':
                            moves.append([self.location[0], self.location[1], self.location[2] + i * e])
                            e += 1
                        elif board[self.location[0], self.location[1], self.location[2] + i * e].colour != self.colour:
                            moves.append([self.location[0], self.location[1], self.location[2] + i * e])
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
        for i in [-1, 1]:
            for a in [-1, 1]:
                flag = False
                e = 1
                while not flag:
                    try:
                        if all(x >= 0 for x in [self.location[0] + i * e, self.location[1] + a * e, self.location[2]]):
                            if board[self.location[0] + i * e, self.location[1] + a * e, self.location[2]] == '  ':
                                moves.append([self.location[0] + i * e, self.location[1] + a * e, self.location[2]])
                                e += 1
                            elif board[self.location[0] + i * e, self.location[1] + a * e, self.location[
                                    2]].colour != self.colour:
                                moves.append([self.location[0] + i * e, self.location[1] + a * e, self.location[2]])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1, 1]:
            for a in [-1, 1]:
                flag = False
                e = 1
                while not flag:
                    try:
                        if all(x >= 0 for x in [self.location[0], self.location[1] + i * e, self.location[2] + a * e]):
                            if board[self.location[0], self.location[1] + i * e, self.location[2] + a * e] == '  ':
                                moves.append([self.location[0], self.location[1] + i * e, self.location[2] + a * e])
                                e += 1
                            elif board[self.location[0], self.location[1] + i * e, self.location[
                                    2] + a * e].colour != self.colour:
                                moves.append([self.location[0], self.location[1] + i * e, self.location[2] + a * e])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1, 1]:
            for a in [-1, 1]:
                flag = False
                e = 1
                while not flag:
                    try:
                        if all(x >= 0 for x in [self.location[0] + i * e, self.location[1], self.location[2] + a * e]):
                            if board[self.location[0] + i * e, self.location[1], self.location[2] + a * e] == '  ':
                                moves.append([self.location[0] + i * e, self.location[1], self.location[2] + a * e])
                                e += 1
                            elif board[self.location[0] + i * e, self.location[1], self.location[
                                    2] + a * e].colour != self.colour:
                                moves.append([self.location[0] + i * e, self.location[1], self.location[2] + a * e])
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
            for x in [-1, 1]:
                for b in range(3):
                    for y in [-1, 1]:
                        if a != b:
                            vector = [0, 0, 0]
                            vector[a] = 2 * x
                            vector[b] = y
                            try:
                                if all(x >= 0 for x in [self.location[0] + vector[0], self.location[1] + vector[1],
                                                        self.location[2] + vector[2]]):
                                    if board[self.location[0] + vector[0], self.location[1] + vector[1],
                                             self.location[2] + vector[2]] == '  ':
                                        moves.append([self.location[0] + vector[0], self.location[1] + vector[1],
                                                      self.location[2] + vector[2]])
                                    elif board[self.location[0] + vector[0], self.location[1] + vector[1],
                                               self.location[2] + vector[2]].colour != self.colour:
                                        moves.append([self.location[0] + vector[0], self.location[1] + vector[1],
                                                      self.location[2] + vector[2]])
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
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                for c in [-1, 0, 1]:
                    if [a, b, c].count(0) in [1, 2]:
                        try:
                            if all(x >= 0 for x in [self.location[0] + a, self.location[1] + b, self.location[2] + c]):
                                if board[self.location[0] + a, self.location[1] + b, self.location[2] + c] == '  ':
                                    moves.append([self.location[0] + a, self.location[1] + b, self.location[2] + c])
                                elif board[self.location[0] + a, self.location[1] + b, self.location[
                                                                                2] + c].colour != self.colour:
                                    moves.append([self.location[0] + a, self.location[1] + b, self.location[2] + c])
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
        for i in [-1, 1]:
            for a in [-1, 1]:
                flag = False
                e = 1
                while not flag:
                    try:
                        if all(x >= 0 for x in [self.location[0] + i * e, self.location[1] + a * e, self.location[2]]):
                            if board[self.location[0] + i * e, self.location[1] + a * e, self.location[2]] == '  ':
                                moves.append([self.location[0] + i * e, self.location[1] + a * e, self.location[2]])
                                e += 1
                            elif board[self.location[0] + i * e, self.location[1] + a * e, self.location[
                                                    2]].colour != self.colour:
                                moves.append([self.location[0] + i * e, self.location[1] + a * e, self.location[2]])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1, 1]:
            for a in [-1, 1]:
                flag = False
                e = 1
                while not flag:
                    try:
                        if all(x >= 0 for x in [self.location[0], self.location[1] + i * e, self.location[2] + a * e]):
                            if board[self.location[0], self.location[1] + i * e, self.location[2] + a * e] == '  ':
                                moves.append([self.location[0], self.location[1] + i * e, self.location[2] + a * e])
                                e += 1
                            elif board[self.location[0], self.location[1] + i * e, self.location[
                                                                                2] + a * e].colour != self.colour:
                                moves.append([self.location[0], self.location[1] + i * e, self.location[2] + a * e])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1, 1]:
            for a in [-1, 1]:
                flag = False
                e = 1
                while not flag:
                    try:
                        if all(x >= 0 for x in [self.location[0] + i * e, self.location[1], self.location[2] + a * e]):
                            if board[self.location[0] + i * e, self.location[1], self.location[2] + a * e] == '  ':
                                moves.append([self.location[0] + i * e, self.location[1], self.location[2] + a * e])
                                e += 1
                            elif board[self.location[0] + i * e, self.location[1], self.location[
                                                                                2] + a * e].colour != self.colour:
                                moves.append([self.location[0] + i * e, self.location[1], self.location[2] + a * e])
                                flag = True
                            else:
                                flag = True
                        else:
                            flag = True
                    except IndexError:
                        flag = True
        for i in [-1, 1]:
            flag = False
            e = 1
            while not flag:
                try:
                    if all(x >= 0 for x in [self.location[0] + i * e, self.location[1], self.location[2]]):
                        if board[self.location[0] + i * e, self.location[1], self.location[2]] == '  ':
                            moves.append([self.location[0] + i * e, self.location[1], self.location[2]])
                            e += 1
                        elif board[self.location[0] + i * e, self.location[1], self.location[2]].colour != self.colour:
                            moves.append([self.location[0] + i * e, self.location[1], self.location[2]])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        for i in [-1, 1]:
            flag = False
            e = 1
            while not flag:
                try:
                    if all(x >= 0 for x in [self.location[0], self.location[1] + i * e, self.location[2]]):
                        if board[self.location[0], self.location[1] + i * e, self.location[2]] == '  ':
                            moves.append([self.location[0], self.location[1] + i * e, self.location[2]])
                            e += 1
                        elif board[self.location[0], self.location[1] + i * e, self.location[2]].colour != self.colour:
                            moves.append([self.location[0], self.location[1] + i * e, self.location[2]])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True
        for i in [-1, 1]:
            flag = False
            e = 1
            while not flag:
                try:
                    if all(x >= 0 for x in [self.location[0], self.location[1], self.location[2] + i * e]):
                        if board[self.location[0], self.location[1], self.location[2] + i * e] == '  ':
                            moves.append([self.location[0], self.location[1], self.location[2] + i * e])
                            e += 1
                        elif board[self.location[0], self.location[1], self.location[2] + i * e].colour != self.colour:
                            moves.append([self.location[0], self.location[1], self.location[2] + i * e])
                            flag = True
                        else:
                            flag = True
                    else:
                        flag = True
                except IndexError:
                    flag = True

        return moves


def check_check(some_board):
    temp_check = [False, False]
    for a in range(boards):
        for b in range(rows):
            for c in range(columns):
                if some_board[a, b, c] != '  ':
                    if some_board[a, b, c].colour == 'W':
                        try:
                            if kings[1] in some_board[a, b, c].find_moves(some_board, checking_check=False):
                                temp_check[0] = True
                        except TypeError:
                            pass
                    else:
                        try:
                            if kings[0] in some_board[a, b, c].find_moves(some_board, checking_check=False):
                                temp_check[1] = True
                        except TypeError:
                            pass
    return temp_check


def str_board():
    for x in board:
        for y in x:
            print([a if a == '  ' else a.colour + a.name for a in y])
        print()


def output_board():
    for a in range(boards):
        for b in range(rows):
            for c in range(columns):
                if (a + b + c) % 2 == 0:
                    pygame.draw.rect(screen, (245, 245, 200), (30 * c, 30 * b + 270 * a, 30, 30))
                else:
                    pygame.draw.rect(screen, (225, 198, 153), (30 * c, 30 * b + 270 * a, 30, 30))
                if not board[a, b, c] == '  ':
                    screen.blit(font.render(board[a, b, c].name, True,
                                            (255, 0, 0) if board[a, b, c].colour == 'W' else (0, 0, 0)),
                                (30 * c + 5, 30 * b + 270 * a + 5))


def output_moves(moves):
    surface = pygame.Surface((240, 780), pygame.SRCALPHA)
    for move in moves:
        pygame.draw.circle(surface, (0, 0, 0, 50), (30 * move[2] + 15, 30 * move[1] + 270 * move[0] + 15), 10)
    screen.blit(surface, (0, 0))


def evaluate(colour):
    score = 0
    for a in range(boards):
        for b in range(columns):
            for c in range(rows):
                if board[a, b, c] != '  ':
                    if board[a, b, c].colour == colour:
                        score += board[a, b, c].value
                    else:
                        score -= board[a, b, c].value
    return score


def minimax(turn, overall_turn, depth, start_eval, maximising=True, alpha=-1000000, beta=1000000):
    if depth <= 0 or sum(isinstance(x, King) for layer in board for row in layer for x in row) < 2:
        if evaluate(overall_turn) <= start_eval:
            return [evaluate(overall_turn), None]
    best_move = None
    pos_moves = []
    for a in range(boards):
        for b in range(rows):
            for c in range(columns):
                if board[a, b, c] != '  ':
                    if board[a, b, c].colour == turn:
                        try:
                            for move in board[a, b, c].find_moves():
                                pos_moves.append([[a, b, c], move])
                        except TypeError:
                            pass
    random.shuffle(pos_moves)
    if maximising:
        bestValue = -1000000
    else:
        bestValue = 1000000
    for pos_move in pos_moves:
        to = board[pos_move[1][0], pos_move[1][1], pos_move[1][2]]
        board[pos_move[1][0], pos_move[1][1], pos_move[1][2]] = board[pos_move[0][0], pos_move[0][1], pos_move[0][2]]
        board[pos_move[0][0], pos_move[0][1], pos_move[0][2]] = '  '
        board[pos_move[1][0], pos_move[1][1], pos_move[1][2]].location = pos_move[1]

        value = minimax('W' if turn == 'B' else 'B', overall_turn,
                        depth - 1, start_eval if depth <= 0 else evaluate(overall_turn), not maximising, alpha, beta)[0]
        if maximising:
            if value > bestValue:
                bestValue = value
                best_move = pos_move
            alpha = max(alpha, value)
        else:
            if value < bestValue:
                bestValue = value
                best_move = pos_move
            beta = min(beta, value)
        board[pos_move[0][0], pos_move[0][1], pos_move[0][2]] = board[pos_move[1][0], pos_move[1][1], pos_move[1][2]]
        board[pos_move[1][0], pos_move[1][1], pos_move[1][2]] = to
        board[pos_move[0][0], pos_move[0][1], pos_move[0][2]].location = pos_move[0]
        if beta <= alpha:
            break
    return [bestValue, best_move]


GUI = True

# create board
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

# Setup board
setup = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
colours = ['W', 'B']    
for i in range(2):
    for e in range(len(setup)):
        board[-i * 2 + 2, -i * 7 + 7, e] = setup[e]([-i * 2 + 2, -i * 7 + 7, e], colours[i])
        board[-i * 2 + 2, -i * 5 + 6, e] = Pawn([-i * 2 + 2, -i * 5 + 6, e], colours[i])

if GUI:
    pygame.init()

    screen = pygame.display.set_mode((240, 780))
    surface = pygame.Surface((240, 780), pygame.SRCALPHA)

    font = pygame.font.SysFont(None, 35)

kings = [[2, 7, 4], [0, 0, 4]]
turn = 'W'
back_pieces = {'Q': Queen, 'R': Rook, 'B': Bishop, 'K': Knight}
mode = 'input_from'
while True:
    if GUI:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        output_board()
    else:
        str_board()
        print()

    # if True:
    if turn == 'W':
        if mode == 'input_from':
            if pygame.mouse.get_pressed(3)[0]:
                x, y = pygame.mouse.get_pos()
                if not ((240 < y < 270) or (510 < y < 540)):
                    a = y // 280
                    b = ((y - 30 * a) % 240) // 30
                    c = x // 30
                    if board[a, b, c] != '  ':
                        if board[a, b, c].colour == turn:
                            move_from = [a, b, c]
                            mode = 'input_to'

        if mode == 'input_to':
            output_moves(board[move_from[0], move_from[1], move_from[2]].find_moves())
            if pygame.mouse.get_pressed(3)[0]:
                x, y = pygame.mouse.get_pos()
                if not ((240 < y < 270) or (510 < y < 540)):
                    a = y // 280
                    b = ((y - 30 * a) % 240) // 30
                    c = x // 30
                    if [a, b, c] in board[move_from[0], move_from[1], move_from[2]].find_moves():
                        move_to = [a, b, c]
                        board[move_to[0], move_to[1], move_to[2]] = board[move_from[0], move_from[1], move_from[2]]
                        board[move_from[0], move_from[1], move_from[2]] = '  '
                        board[move_to[0], move_to[1], move_to[2]].location = move_to

                        if (move_to[0] == 0 and move_to[1] == 0 and turn == 'W') or (
                                move_to[0] == 2 and move_to[1] == 2 and turn == 'B'):
                            if board[move_to[0], move_to[1], move_to[2]].name == 'P':
                                board[move_to[0], move_to[1], move_to[2]] = back_pieces['Q'](
                                    board[move_to[0], move_to[1], move_to[2]].location,
                                    board[move_to[0], move_to[1], move_to[2]].colour)
                        if board[move_to[0], move_to[1], move_to[2]].name == 'K':
                            if board[move_to[0], move_to[1], move_to[2]].colour == 'W':
                                kings[0] = [move_to[0], move_to[1], move_to[2]]
                            else:
                                kings[1] = [move_to[0], move_to[1], move_to[2]]

                        if turn == 'W':
                            turn = 'B'
                        else:
                            turn = 'W'

                        mode = 'input_from'
                        output_board()

                    elif board[a, b, c] != '  ':
                        if board[a, b, c].colour == turn:
                            move_from = [a, b, c]

    else:
        # if True:
        start = time.time()
        move = minimax(turn, turn, depth, evaluate(turn))[1]
        print(time.time() - start)
        move_from, move_to = move[0], move[1]

        if not GUI:
            print(f"{turn} moves {board[move_from[0], move_from[1], move_from[2]].name} from {move_from} to {move_to}")
            if board[move_to[0], move_to[1], move_to[2]] != '  ':
                print(f"taking {board[move_to[0], move_to[1], move_to[2]].name}")
            print("White evaluation:", evaluate('W'))
            print()

        board[move_to[0], move_to[1], move_to[2]] = board[move_from[0], move_from[1], move_from[2]]
        board[move_from[0], move_from[1], move_from[2]] = '  '
        board[move_to[0], move_to[1], move_to[2]].location = move_to

        if (move_to[0] == 0 and move_to[1] == 0 and turn == 'W') or (
                                    move_to[0] == 2 and move_to[1] == 2 and turn == 'B'):
            if board[move_to[0], move_to[1], move_to[2]].name == 'P':
                board[move_to[0], move_to[1], move_to[2]] = back_pieces['Q'](board[move_to[0], move_to[1], move_to[
                                    2]].location, board[move_to[0], move_to[1], move_to[2]].colour)
        if board[move_to[0], move_to[1], move_to[2]].name == 'K':
            if board[move_to[0], move_to[1], move_to[2]].colour == 'W':
                kings[0] = [move_to[0], move_to[1], move_to[2]]
            else:
                kings[1] = [move_to[0], move_to[1], move_to[2]]

        if turn == 'W':
            turn = 'B'
        else:
            turn = 'W'
    if GUI:
        pygame.display.flip()



"""
[[
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ], [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 16, 16, 12, 10],
            [0, 0, 0, 0, 16, 16, 12, 10],
            [0, 0, 0, 0, 12, 12, 8, 7],
            [0, 0, 0, 0, 10, 10, 7, 6]
        ], [
            [6, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 16, 16, 13, 10],
            [0, 0, 0, 0, 16, 16, 13, 10],
            [0, 0, 0, 0, 13, 13, 10, 8],
            [6, 8, 0, 0, 10, 10, 8, 6]
        ]]
"""