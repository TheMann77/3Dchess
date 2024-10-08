from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import numpy as np
import sys
import random
import time

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

class MainApp(App):
    def build(self):
        self.main_layout = FloatLayout()
        self.mode = 'input_from'
        self.turn = 'W'
        self.move_from = []
        self.move_to = []
        for a in range(boards):
            for b in range(rows):
                for c in range(columns):
                    buttons[a,b,c] = Button(text=board[a,b,c].name if board[a,b,c]!= '  ' else '  ', font_size='20sp', pos_hint={'x':0.125*c, 'y':25/26-b/26-a*9/26}, size_hint=(.125, 1/26), background_color=[.96,.96,.78] if (a+b+c)%2 == 0 else [.88,.78,.6])
                    buttons[a,b,c].bind(on_press=self.on_button_press)
                    self.main_layout.add_widget(buttons[a,b,c])

        return self.main_layout

    def on_button_press(self, instance):
        x = int(instance.pos_hint['x']*8)
        y = columns-int((instance.pos_hint['y']%(9/26))*26)-1
        z = boards-int(instance.pos_hint['y']//(9/26))-1
        if self.mode == 'input_from':
            if board[z,y,x] != '  ':
                if board[z,y,x].colour == self.turn:
                    self.move_from = [z,y,x]
                    self.mode = 'input_to'
                    

        elif self.mode == 'input_to':
            if [z,y,x] in board[self.move_from[0], self.move_from[1], self.move_from[2]].find_moves():
                self.move_to = [z,y,x]
                board[self.move_to[0], self.move_to[1], self.move_to[2]] = board[self.move_from[0], self.move_from[1], self.move_from[2]]
                board[self.move_from[0], self.move_from[1], self.move_from[2]] = '  '
                board[self.move_to[0], self.move_to[1], self.move_to[2]].location = self.move_to
                
                if (self.move_to[0] == 0 and self.move_to[1] == 0 and self.turn == 'W') or (
                        self.move_to[0] == 2 and self.move_to[1] == 2 and self.turn == 'B'):
                    if board[self.move_to[0], self.move_to[1], self.move_to[2]].name == 'P':
                        board[self.move_to[0], self.move_to[1], self.move_to[2]] = back_pieces['Q'](
                            board[self.move_to[0], self.move_to[1], self.move_to[2]].location,
                            board[self.move_to[0], self.move_to[1], self.move_to[2]].colour)

                buttons[self.move_to[0], self.move_to[1], self.move_to[2]].text = board[self.move_to[0], self.move_to[1], self.move_to[2]].name
                buttons[self.move_from[0], self.move_from[1], self.move_from[2]].text = '  '
                
                if board[self.move_to[0], self.move_to[1], self.move_to[2]].name == 'K':
                    if board[self.move_to[0], self.move_to[1], self.move_to[2]].colour == 'W':
                        kings[0] = [self.move_to[0], self.move_to[1], self.move_to[2]]
                    else:
                        kings[1] = [self.move_to[0], self.move_to[1], self.move_to[2]]

                self.turn = 'B'
                move = minimax(self.turn, self.turn, 3, evaluate(self.turn))[1]
                [self.move_from, self.move_to] = move
                board[self.move_to[0], self.move_to[1], self.move_to[2]] = board[self.move_from[0], self.move_from[1], self.move_from[2]]
                board[self.move_from[0], self.move_from[1], self.move_from[2]] = '  '
                board[self.move_to[0], self.move_to[1], self.move_to[2]].location = self.move_to

                if (self.move_to[0] == 0 and self.move_to[1] == 0 and self.turn == 'W') or (
                                            self.move_to[0] == 2 and self.move_to[1] == 2 and self.turn == 'B'):
                    if board[self.move_to[0], self.move_to[1], self.move_to[2]].name == 'P':
                        board[self.move_to[0], self.move_to[1], self.move_to[2]] = back_pieces['Q'](board[self.move_to[0], self.move_to[1], self.move_to[
                                            2]].location, board[self.move_to[0], self.move_to[1], self.move_to[2]].colour)

                buttons[self.move_to[0], self.move_to[1], self.move_to[2]].text = board[self.move_to[0], self.move_to[1], self.move_to[2]].name
                buttons[self.move_from[0], self.move_from[1], self.move_from[2]].text = '  '
                if board[self.move_to[0], self.move_to[1], self.move_to[2]].name == 'K':
                    if board[self.move_to[0], self.move_to[1], self.move_to[2]].colour == 'W':
                        kings[0] = [self.move_to[0], self.move_to[1], self.move_to[2]]
                    else:
                        kings[1] = [self.move_to[0], self.move_to[1], self.move_to[2]]
                self.turn = 'W'
                self.mode = 'input_from'
                
            elif board[z,y,x] != '  ':
                if board[z,y,x].colour == self.turn:
                    self.move_from = [z,y,x]
            str_board()
                    




rows = 8
columns = 8
boards = 3
board = []
buttons = []
for a in range(boards):
    board.append([])
    buttons.append([])
    for b in range(columns):
        board[-1].append([])
        buttons[-1].append([])
        for x in range(rows):
            board[-1][-1].append('  ')
            buttons[-1][-1].append(None)
board = np.array(board, dtype=object)
buttons = np.array(board, dtype=object)

# Setup board
setup = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
colours = ['W', 'B']    
for i in range(2):
    for e in range(len(setup)):
        board[-i * 2 + 2, -i * 7 + 7, e] = setup[e]([-i * 2 + 2, -i * 7 + 7, e], colours[i])
        board[-i * 2 + 2, -i * 5 + 6, e] = Pawn([-i * 2 + 2, -i * 5 + 6, e], colours[i])
kings = [[2, 7, 4], [0, 0, 4]]

back_pieces = {'Q': Queen, 'R': Rook, 'B': Bishop, 'K': Knight}



if __name__ == '__main__':
    app = MainApp()
    app.run()
