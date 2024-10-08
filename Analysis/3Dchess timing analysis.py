# version notes:

# working UI with new game and user options
# Piece images
# No check
# Working multi-move minimax ai with position value - 3 depth ~1s

#fast
#[0.0007480084896087646, 0.056498974561691284, 0.9633202970027923, 20.416886192560195]
#[0.0006981253623962403, 0.07228095531463623, 8.717268520593644, 1060.2488640129566]

#slow
#[0.004487568140029907, 0.10424690842628478, 5.023096036911011]
#[0.004409965715910259, 0.5469127655029297, 72.4344319343567]

import numpy as np
import random
import matplotlib.pyplot as plt
import time

boards, rows, columns = 3, 8, 8


wtables = False
btables = False
wpawn = 100
games = 1
final_eval_tables = False
str_output = False

class Pawn:

    def __init__(self, location, colour):
        self.name = 'P'
        self.location = location
        self.colour = colour
        self.symbol = '♙'
        if self.colour == 'W':
            self.value = wpawn
        else:
            self.value = 100
        self.fvalue = 100
        self.table = []
        self.moved = False
        self.table = [[
            [0, 0, 0, 0, 0, 0, 0, 0],
            [50, 50, 50, 50, 50, 50, 50, 50],
            [15, 15, 20, 35, 35, 20, 15, 15],
            [10, 10, 13, 30, 30, 13, 10, 10],
            [8, 8, 10, 25, 25, 10, 8, 8],
            [5, 5, 8, 23, 23, 8, 5, 5],
            [0, 0, 0, 20, 20, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ], [
            [50, 50, 50, 50, 50, 50, 50, 50],
            [15, 15, 20, 35, 35, 20, 15, 15],
            [10, 10, 13, 30, 30, 13, 10, 10],
            [8, 8, 10, 25, 25, 10, 8, 8],
            [5, 5, 8, 23, 23, 8, 5, 5],
            [0, 0, 0, 20, 20, 0, 0, 0],
            [5, -5, -5, 0, 0, -5, -5, 5],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ], [
            [15, 15, 20, 35, 35, 20, 15, 15],
            [10, 10, 13, 30, 30, 13, 10, 10],
            [8, 8, 10, 25, 25, 10, 8, 8],
            [5, 5, 8, 23, 23, 8, 5, 5],
            [0, 0, 0, 20, 20, 0, 0, 0],
            [5, -5, -5, 0, 0, -5, -5, 5],
            [5, 10, 10, -25, -25, 10, 10, 5],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]]
    def find_moves(self):
        moves = []
        if self.colour == 'W':
            try:
                if board[self.location[0], self.location[1] - 1, self.location[2]] == '  ':
                    moves.append([self.location[0], self.location[1] - 1, self.location[2]])
                    if not self.moved:
                        if board[self.location[0], self.location[1] - 2, self.location[2]] == '  ':
                            moves.append([self.location[0], self.location[1] - 2, self.location[2]])
            except IndexError:
                pass
            try:
                if board[self.location[0] - 1, self.location[1], self.location[2]] == '  ':
                    moves.append([self.location[0] - 1, self.location[1], self.location[2]])
                    if not self.moved:
                        if board[self.location[0] - 2, self.location[1], self.location[2]] == '  ':
                            if self.location[0] - 2 >= 0:
                                moves.append([self.location[0] - 2, self.location[1], self.location[2]])
            except IndexError:
                pass
            for i in [-1, 1]:
                try:
                    if self.location[1] > 0:
                        if board[self.location[0], self.location[1] - 1, self.location[2] + i] != '  ':
                            if board[self.location[0], self.location[1] - 1, self.location[2] + i].colour != self.colour:
                                moves.append([self.location[0], self.location[1] - 1, self.location[2] + i])
                except IndexError:
                    pass
                try:
                    if self.location[0] > 0:
                        if board[self.location[0] - 1, self.location[1], self.location[2] + i] != '  ':
                            if board[self.location[0] - 1, self.location[1], self.location[2] + i].colour != self.colour:
                                moves.append([self.location[0] - 1, self.location[1], self.location[2] + i])
                except IndexError:
                    pass
        if self.colour == 'B':
            try:
                if board[self.location[0], self.location[1] + 1, self.location[2]] == '  ':
                    moves.append([self.location[0], self.location[1] + 1, self.location[2]])
                    if not self.moved:
                        if board[self.location[0], self.location[1] + 2, self.location[2]] == '  ':
                            moves.append([self.location[0], self.location[1] + 2, self.location[2]])
            except IndexError:
                pass
            try:
                if board[self.location[0] + 1, self.location[1], self.location[2]] == '  ':
                    moves.append([self.location[0] + 1, self.location[1], self.location[2]])
                    if not self.moved:
                        if self.location[0] + 2 < boards:
                            if board[self.location[0] + 2, self.location[1], self.location[2]] == '  ':
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
        self.fvalue = 525
        self.table = [[
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
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ], [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]]

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
        self.fvalue = 350
        self.table = [[
            [-25, -10, -10, -10, -10, -10, -10, -25],
            [-10, 0, 0, 0, 0, 0, 0, -10],
            [-10, 0, 5, 10, 10, 5, 0, -10],
            [-10, 5, 5, 10, 10, 5, 5, -10],
            [-10, 0, 10, 10, 10, 10, 0, -10],
            [-10, 10, 10, 10, 10, 10, 10, -10],
            [-10, 5, 0, 0, 0, 0, 5, -10],
            [-25, -10, -10, -10, -10, -10, -10, -25]
        ], [
            [-20, -5, -5, -5, -5, -5, -5, -20],
            [-5, 5, 5, 5, 5, 5, 5, -5],
            [-5, 5, 10, 15, 15, 10, 5, -5],
            [-5, 10, 10, 15, 15, 10, 10, -5],
            [-5, 5, 15, 15, 15, 15, 5, -5],
            [-10, 10, 10, 10, 10, 10, 10, -5],
            [-5, 10, 5, 5, 5, 5, 10, -5],
            [-20, -5, -5, -5, -5, -5, -5, -20]
        ], [
            [-25, -10, -10, -10, -10, -10, -10, -25],
            [-10, 0, 0, 0, 0, 0, 0, -10],
            [-10, 0, 5, 10, 10, 5, 0, -10],
            [-10, 5, 5, 10, 10, 5, 5, -10],
            [-10, 0, 10, 10, 10, 10, 0, -10],
            [-10, 10, 10, 10, 10, 10, 10, -10],
            [-10, 5, 0, 0, 0, 0, 5, -10],
            [-25, -10, -40, -10, -10, -40, -10, -25]
        ]]

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

class Unicorn:
    def __init__(self, location, colour):
        self.name = 'U'
        self.location = location
        self.colour = colour
        self.symbol = '♗'
        self.value = 300
        self.fvalue = 300
        self.table = [[
            [-35, -20, -10, -10, -10, -10, -20, -35],
            [-20, -6, -3, -3, -3, -3, -6, -20],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-20, -6, -3, -3, -3, -3, -6, -20],
            [-35, -20, -10, -10, -10, -10, -20, -35]
        ], [
            [-35, -20, -10, -10, -10, -10, -20, -35],
            [-20, -6, -3, -3, -3, -3, -6, -20],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-20, -6, -3, -3, -3, -3, -6, -20],
            [-35, -20, -10, -10, -10, -10, -20, -35]
        ], [
            [-35, -20, -10, -10, -10, -10, -20, -35],
            [-20, -6, -3, -3, -3, -3, -6, -20],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-10, -3, 0, 0, 0, 0, -3, -10],
            [-20, -6, -3, -3, -3, -3, -6, -20],
            [-35, -20, -10, -10, -10, -10, -20, -35]
        ]]

    def find_moves(self):
        moves = []
        for i in [-1, 1]:
            for a in [-1, 1]:
                for o in [-1, 1]:
                    flag = False
                    e = 1
                    while not flag:
                        try:
                            if all(x >= 0 for x in [self.location[0] + i * e, self.location[1] + a * e, self.location[2] + o * e]):
                                if board[self.location[0] + i * e, self.location[1] + a * e, self.location[2] + o * e] == '  ':
                                    moves.append([self.location[0] + i * e, self.location[1] + a * e, self.location[2] + o * e])
                                    e += 1
                                elif board[self.location[0] + i * e, self.location[1] + a * e, self.location[
                                        2] + o * e].colour != self.colour:
                                    moves.append([self.location[0] + i * e, self.location[1] + a * e, self.location[2] + o * e])
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
        self.fvalue = 350
        self.table = [[
            [-50, -30, -20, -20, -20, -20, -30, -50],
            [-30, -20, 5, 5, 5, 5, -20, -30],
            [-20, 5, 15, 15, 15, 15, 5, -20],
            [-20, 5, 15, 20, 20, 15, 5, -20],
            [-20, 5, 15, 20, 20, 15, 5, -20],
            [-20, 5, 15, 15, 15, 15, 5, -20],
            [-30, -20, 5, 5, 5, 5, -20, -30],
            [-50, -30, -20, -20, -20, -20, -30, -50]
        ], [
            [-50, -40, -20, -20, -20, -20, -40, -50],
            [-40, -30, 0, 0, 0, 0, -30, -40],
            [-20, 0, 20, 20, 20, 20, 0, -20],
            [-20, 0, 20, 25, 25, 20, 0, -20],
            [-20, 0, 20, 25, 25, 20, 0, -20],
            [-20, 0, 20, 20, 20, 20, 0, -20],
            [-40, -30, 0, 0, 0, 0, -30, -40],
            [-50, -40, -20, -20, -20, -20, -40, -50]
        ], [
            [-50, -30, -20, -20, -20, -20, -30, -50],
            [-30, -20, 5, 5, 5, 5, -20, -30],
            [-20, 5, 15, 15, 15, 15, 5, -20],
            [-20, 5, 15, 20, 20, 15, 5, -20],
            [-20, 5, 15, 20, 20, 15, 5, -20],
            [-20, 5, 15, 15, 15, 15, 5, -20],
            [-30, -20, 5, 5, 5, 5, -20, -30],
            [-50, -30, -20, -20, -20, -20, -30, -50],
        ]]



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
        self.fvalue = 10000
        self.value = 10000
        self.table = [[
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-20, -30, -30, -40, -40, -30, -30, -20],
            [-15, -25, -25, -25, -25, -25, -25, -15]
        ], [
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-20, -30, -30, -40, -40, -30, -30, -20],
            [-15, -25, -25, -25, -25, -25, -25, -15],
            [15, 15, -5, -5, -5, -5, 15, 15]
        ], [
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-30, -40, -40, -50, -50, -40, -40, -30],
            [-20, -30, -30, -40, -40, -30, -30, -20],
            [-10, -20, -20, -20, -20, -20, -20, -10],
            [20, 20, 0, 0, 0, 0, 20, 20],
            [20, 30, 10, 10, 10, 10, 30, 20]
        ]]

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
        self.fvalue = 1000
        self.table = [[
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
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ], [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]]

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


def create_board(knights, pawn_layers):
    board = []
    for a in range(boards):
        board.append([])
        for b in range(columns):
            board[-1].append([])
            for x in range(rows):
                board[-1][-1].append('  ')
    board = np.array(board, dtype=object)
    if knights:
        setup = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    else:
        setup = [Rook, Unicorn, Bishop, Queen, King, Bishop, Unicorn, Rook]
    colours = ['W', 'B']
    for i in range(2):
        for e in range(len(setup)):
            board[-i * 2 + 2, -i * 7 + 7, e] = setup[e]([-i * 2 + 2, -i * 7 + 7, e], colours[i])
            board[-i * 2 + 2, -i * 5 + 6, e] = Pawn([-i * 2 + 2, -i * 5 + 6, e], colours[i])
            if pawn_layers >= 2:
                board[1, -i * 7 + 7, e] = Pawn([1, -i * 7 + 7, e], colours[i])
                if pawn_layers == 3:
                    board[1, -i * 5 + 6, e] = Pawn([1, -i * 5 + 6, e], colours[i])
    kings = [[2, 7, 4], [0, 0, 4]]
    turn = 'W'
    return board, kings, turn


board, kings, turn = create_board(True, 1)


def str_board(board1):
    for x in board1:
        for y in x:
            print([a if a == '  ' else a.colour + a.name for a in y])
        print()


def evaluate(colour, use_table=False, fixed=False):
    score = 0
    for a in range(boards):
        for b in range(columns):
            for c in range(rows):
                if board[a, b, c] != '  ':
                    if board[a, b, c].colour == colour:
                        if fixed:
                            score += board[a, b, c].fvalue
                        else:
                            score += board[a, b, c].value
                        if use_table:
                            if colour == 'W':
                                score += board[a, b, c].table[a][b][c]
                            else:
                                score += board[a, b, c].table[boards - a - 1][columns - b - 1][rows - c - 1]
                    else:
                        if fixed:
                            score -= board[a, b, c].fvalue
                        else:
                            score -= board[a, b, c].value
                        if use_table:
                            if colour == 'W':
                                score -= board[a, b, c].table[boards-a-1][columns-b-1][rows-c-1]
                            else:
                                score -= board[a, b, c].table[a][b][c]
    return score


def minimax(turn, overall_turn, depth, use_table, eval, alpha_beta, maximising=True, alpha=-1000000, beta=1000000):
    if depth <= 0 or sum(isinstance(x, King) for layer in board for row in layer for x in row) < 2:
        return [eval, None]
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
        new_eval = 0
        if board[pos_move[1][0], pos_move[1][1], pos_move[1][2]].name not in ['R', 'Q'] and use_table:
            moving_piece_table = board[pos_move[1][0], pos_move[1][1], pos_move[1][2]].table
            try:
                if turn == 'W':
                    new_eval += moving_piece_table[pos_move[1][0]][pos_move[1][1]][pos_move[1][2]] - moving_piece_table[pos_move[0][0]][pos_move[0][1]][pos_move[0][2]]
                else:
                    new_eval += moving_piece_table[boards - pos_move[1][0] - 1][columns - pos_move[1][1] - 1][rows - pos_move[1][2] - 1] - moving_piece_table[boards - pos_move[0][0] - 1][columns - pos_move[0][1] - 1][rows - pos_move[0][2] - 1]
            except:
                pass
        if to != '  ':
            new_eval += to.value
        if turn != overall_turn:
            new_eval *= -1
        new_eval += eval
        value = minimax('W' if turn == 'B' else 'B', overall_turn,
                        depth - 1, use_table, new_eval, alpha_beta, not maximising, alpha, beta)[0]
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
        if beta <= alpha and alpha_beta:
            break
    return [bestValue, best_move]


def minimax(board, turn, depth, maxmin):
    if depth == 0:
        return [evaluate(board, turn), None]
    bestMove = None
    posmoves = []
    for a in range(boards):
        for b in range(rows):
            for c in range(columns):
                if board[a, b, c] != '  ':
                    if board[a, b, c].colour == turn:
                        try:
                            for move in board[a, b, c].find_moves(board):
                                posmoves.append([[a, b, c], move])
                        except TypeError:
                            pass
    random.shuffle(posmoves)
    if maxmin == 'maxim':
        bestValue = -100000
    else:
        bestValue = 100000
    for posmove in posmoves:
        to = board[posmove[1][0], posmove[1][1], posmove[1][2]]
        board[posmove[1][0], posmove[1][1], posmove[1][2]] = board[posmove[0][0], posmove[0][1], posmove[0][2]]
        board[posmove[0][0], posmove[0][1], posmove[0][2]] = '  '
        board[posmove[1][0], posmove[1][1], posmove[1][2]].location = posmove[1]

        value = minimax(board, 'W' if turn == 'B' else 'B', depth - 1, 'maxim' if maxmin == 'minim' else 'minim')[0]
        if maxmin == 'maxim':
            if value > bestValue:
                bestValue = value
                bestMove = posmove
        else:
            if value < bestValue:
                bestValue = value
                bestMove = posmove
        board[posmove[0][0], posmove[0][1], posmove[0][2]] = board[posmove[1][0], posmove[1][1], posmove[1][2]]
        board[posmove[1][0], posmove[1][1], posmove[1][2]] = to
        board[posmove[0][0], posmove[0][1], posmove[0][2]].location = posmove[0]
    return [bestValue, bestMove]

def slow_minimax(turn, overall_turn, depth, alpha_beta, maximising=True, alpha=-1000000, beta=1000000):
    if depth <= 0 or sum(isinstance(x, King) for layer in board for row in layer for x in row) < 2:
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

        value = slow_minimax('W' if turn == 'B' else 'B', overall_turn,
                        depth - 1, alpha_beta, not maximising, alpha, beta)[0]
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
        if beta <= alpha and alpha_beta:
            break
    return [bestValue, best_move]

for alpha_beta in [False]:
    ave_times = []
    for depth in range(1, 4):
        print(depth)
        wins = []
        board, kings, turn = create_board(knights=True, pawn_layers=1)
        end_game = False
        time_record = []
        move_count = 1
        while not end_game and move_count <= 20:
            if str_output:
                str_board(board)
                print()
            start = time.time()
            if turn == 'W':
                move = slow_minimax('W', 'W', depth, alpha_beta)[1]
            else:
                move = slow_minimax('B', 'B', depth, alpha_beta)[1]
            time_record.append(time.time() - start)
            move_from, move_to = move[0], move[1]

            if board[move_to[0], move_to[1], move_to[2]] != '  ':
                if board[move_to[0], move_to[1], move_to[2]].name == 'K':
                    end_game = True
                    break

            board[move_to[0], move_to[1], move_to[2]] = board[move_from[0], move_from[1], move_from[2]]
            board[move_from[0], move_from[1], move_from[2]] = '  '
            board[move_to[0], move_to[1], move_to[2]].location = move_to

            if board[move_to[0], move_to[1], move_to[2]].name == 'P':
                if (move_to[0] == 0 and move_to[1] == 0 and turn == 'W') or (
                        move_to[0] == 2 and move_to[1] == 7 and turn == 'B'):
                    board[move_to[0], move_to[1], move_to[2]] = Queen(
                        board[move_to[0], move_to[1], move_to[2]].location,
                        board[move_to[0], move_to[1], move_to[2]].colour)
                board[move_to[0], move_to[1], move_to[2]].moved = True
            if board[move_to[0], move_to[1], move_to[2]].name == 'K':
                if board[move_to[0], move_to[1], move_to[2]].colour == 'W':
                    kings[0] = [move_to[0], move_to[1], move_to[2]]
                else:
                    kings[1] = [move_to[0], move_to[1], move_to[2]]
            if turn == 'W':
                turn = 'B'
            else:
                turn = 'W'
                move_count += 1
        ave_times.append(sum(time_record)/len(time_record))
        print(sum(time_record)/len(time_record))
    plotted = False
    print(ave_times)
    plt.plot([x for x in range(1,len(ave_times)+1)], ave_times, label="Alpha-Beta pruning" if alpha_beta else "No Alpha-Beta pruning")

plt.xlabel("Search depth")
plt.ylabel("Average time (seconds)")
plt.yscale('log')
plt.legend()
plt.title("Average time per move")
plt.xticks(range(1,5))
plt.show()