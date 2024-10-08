# version notes:

# working UI with new game and user options
# Piece images
# No working check
# No checkmate, castling, en passant, but I think castling and en passant lose their purpose in 3 dimensions
# Working multi-move minimax ai
# Position value
# Only first row pawns can move 2

import numpy as np
import pygame
import sys
import random
import time

depth = 2

boards, rows, columns = 3, 8, 8

class Pawn:

    def __init__(self, location, colour):
        self.name = 'P'
        self.location = location
        self.colour = colour
        self.symbol = '♙'
        self.value = 100
        self.table = []
        self.moved = False
        if self.colour == 'W':
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_plt60.png")
        else:
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_pdt60.png")
        self.img = pygame.transform.scale(self.img, (30, 30))
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
        if self.colour == 'W':
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_rlt60.png")
        else:
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_rdt60.png")
        self.img = pygame.transform.scale(self.img, (30, 30))
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
        if self.colour == 'W':
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_blt60.png")
        else:
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_bdt60.png")
        self.img = pygame.transform.scale(self.img, (30, 30))
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
        if self.colour == 'W':
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_nlt60.png")
        else:
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_ndt60.png")
        self.img = pygame.transform.scale(self.img, (30, 30))
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
        if self.colour == 'W':
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_nlt60.png")
        else:
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_ndt60.png")
        self.img = pygame.transform.scale(self.img, (30, 30))
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
        self.value = 10000
        if self.colour == 'W':
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_klt60.png")
        else:
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_kdt60.png")
        self.img = pygame.transform.scale(self.img, (30, 30))
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
        if self.colour == 'W':
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_qlt60.png")
        else:
            self.img = pygame.image.load(r"D:\Dropbox\Alex files\Fun\Programming\Python\Chess\Pieces\Chess_qdt60.png")
        self.img = pygame.transform.scale(self.img, (30, 30))
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

def create_board(new_rows, new_columns, new_boards, knights, pawn_layers, new_depth, new_ai):
    board = []
    for a in range(new_boards):
        board.append([])
        for b in range(new_columns):
            board[-1].append([])
            for x in range(new_rows):
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
    if knights:
        back_pieces = {'Q': Queen, 'R': Rook, 'B': Bishop, 'K': Knight}
    else:
        back_pieces = {'Q': Queen, 'R': Rook, 'B': Bishop, 'U': Unicorn}
    mode = 'input_from'
    history = []
    present = True
    history_pos = 0
    end_game = 0
    taken = {'W': [], 'B': []}
    new_settings = [new_rows, new_columns, new_boards, knights, pawn_layers, new_depth, new_ai]
    global boards, rows, columns, depth
    boards, rows, columns, depth = new_boards, new_rows, new_columns, new_depth
    return board, kings, turn, back_pieces, mode, history, present, history_pos, end_game, taken, new_settings, new_ai


board, kings, turn, back_pieces, mode, history, present, history_pos, end_game, taken, new_settings, ai = create_board(8, 8, 3, True, 1, 2, True)


def output_board(board1=board, winner=0):
    for a in range(boards):
        for b in range(rows):
            for c in range(columns):
                if (a + b + c) % 2 == 0:
                    pygame.draw.rect(screen, (245, 245, 200), (30 * c, 30 * b + 270 * a, 30, 30))
                else:
                    pygame.draw.rect(screen, (225, 198, 153), (30 * c, 30 * b + 270 * a, 30, 30))
                if not board1[a, b, c] == '  ':
                    screen.blit(board1[a,b,c].img, (30 * c - 1, 30 * b + 270 * a))


def output_board_letters(board1=board, winner=0):
    for a in range(boards):
        for b in range(rows):
            for c in range(columns):
                if (a + b + c) % 2 == 0:
                    pygame.draw.rect(screen, (245, 245, 200), (30 * c, 30 * b + 270 * a, 30, 30))
                else:
                    pygame.draw.rect(screen, (225, 198, 153), (30 * c, 30 * b + 270 * a, 30, 30))
                if not board1[a, b, c] == '  ':
                    if board1[a, b, c].colour == 'W':
                        if winner == 2:
                            col = (150, 150, 150)
                        else:
                            col = (255, 0, 0)
                    else:
                        if winner == 1:
                            col = (150, 150, 150)
                        else:
                            col = (0, 0, 0)
                    font = pygame.font.SysFont(None, 35)
                    screen.blit(font.render(board1[a, b, c].name, True, col), (30 * c + 5, 30 * b + 270 * a + 5))


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
                        if colour == 'W':
                            score += board[a, b, c].table[a][b][c]
                        else:
                            score += board[a, b, c].table[boards - a - 1][columns - b - 1][rows - c - 1]
                    else:
                        score -= board[a, b, c].value
                        if colour == 'W':
                            score -= board[a, b, c].table[boards-a-1][columns-b-1][rows-c-1]
                        else:
                            score -= board[a, b, c].table[a][b][c]
    return score


def minimax(turn, overall_turn, depth, maximising=True, alpha=-1000000, beta=1000000):
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

        value = minimax('W' if turn == 'B' else 'B', overall_turn,
                        depth - 1, not maximising, alpha, beta)[0]
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

if GUI:
    pygame.init()

    screen = pygame.display.set_mode((400, 780))
    surface = pygame.Surface((400, 780), pygame.SRCALPHA)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    if not end_game:
        if GUI:
            if present:
                output_board(board)
            else:
                output_board(history[history_pos+1])
            pygame.draw.rect(screen, (200, 200, 200), (250, 10, 65, 40))
            pygame.draw.rect(screen, (200, 200, 200), (325, 10, 65, 40))
            pygame.draw.rect(screen, (0, 100, 0), (250, 730, 140, 40))
            font = pygame.font.SysFont(None, 25)
            text_width, text_height = font.size("New game")
            screen.blit(font.render("New game", True, (255, 255, 255)), (320 - (text_width/2), 750 - (text_height/2)))
            if new_settings[3]:
                pygame.draw.rect(screen, (200, 200, 200), (250, 650, 70, 40))
                pygame.draw.rect(screen, (220, 220, 220), (320, 650, 70, 40))
            else:
                pygame.draw.rect(screen, (220, 220, 220), (250, 650, 70, 40))
                pygame.draw.rect(screen, (200, 200, 200), (320, 650, 70, 40))
            font = pygame.font.SysFont(None, 20)
            screen.blit(font.render("Knights/Unicorns:", True, (0, 0, 0)), (250, 630))
            text_width, text_height = font.size("Knights")
            screen.blit(font.render("Knights", True, (255, 255, 255)),
                        (285 - (text_width / 2), 670 - (text_height / 2)))
            text_width, text_height = font.size("Unicorns")
            screen.blit(font.render("Unicorns", True, (255, 255, 255)),
                        (355 - (text_width / 2), 670 - (text_height / 2)))

            if new_settings[4] == 1:
                pygame.draw.rect(screen, (200, 200, 200), (250, 550, 47, 40))
                pygame.draw.rect(screen, (220, 220, 220), (297, 550, 46, 40))
                pygame.draw.rect(screen, (220, 220, 220), (343, 550, 47, 40))
            elif new_settings[4] == 2:
                pygame.draw.rect(screen, (220, 220, 220), (250, 550, 47, 40))
                pygame.draw.rect(screen, (200, 200, 200), (297, 550, 46, 40))
                pygame.draw.rect(screen, (220, 220, 220), (343, 550, 47, 40))
            elif new_settings[4] == 3:
                pygame.draw.rect(screen, (220, 220, 220), (250, 550, 47, 40))
                pygame.draw.rect(screen, (220, 220, 220), (297, 550, 46, 40))
                pygame.draw.rect(screen, (200, 200, 200), (343, 550, 47, 40))
            font = pygame.font.SysFont(None, 20)
            screen.blit(font.render("Pawn rows:", True, (0, 0, 0)), (250, 530))
            text_width, text_height = font.size("1")
            screen.blit(font.render("1", True, (255, 255, 255)),
                        (273.5 - (text_width / 2), 570 - (text_height / 2)))
            text_width, text_height = font.size("2")
            screen.blit(font.render("2", True, (255, 255, 255)),
                        (320 - (text_width / 2), 570 - (text_height / 2)))
            text_width, text_height = font.size("3")
            screen.blit(font.render("3", True, (255, 255, 255)),
                        (366.5 - (text_width / 2), 570 - (text_height / 2)))

            if new_settings[5] == 1:
                pygame.draw.rect(screen, (200, 200, 200), (250, 450, 47, 40))
                pygame.draw.rect(screen, (220, 220, 220), (297, 450, 46, 40))
                pygame.draw.rect(screen, (220, 220, 220), (343, 450, 47, 40))
            elif new_settings[5] == 2:
                pygame.draw.rect(screen, (220, 220, 220), (250, 450, 47, 40))
                pygame.draw.rect(screen, (200, 200, 200), (297, 450, 46, 40))
                pygame.draw.rect(screen, (220, 220, 220), (343, 450, 47, 40))
            elif new_settings[5] == 3:
                pygame.draw.rect(screen, (220, 220, 220), (250, 450, 47, 40))
                pygame.draw.rect(screen, (220, 220, 220), (297, 450, 46, 40))
                pygame.draw.rect(screen, (200, 200, 200), (343, 450, 47, 40))
            font = pygame.font.SysFont(None, 20)
            screen.blit(font.render("Difficulty:", True, (0, 0, 0)), (250, 430))
            text_width, text_height = font.size("1")
            screen.blit(font.render("1", True, (255, 255, 255)),
                        (273.5 - (text_width / 2), 470 - (text_height / 2)))
            text_width, text_height = font.size("2")
            screen.blit(font.render("2", True, (255, 255, 255)),
                        (320 - (text_width / 2), 470 - (text_height / 2)))
            text_width, text_height = font.size("3")
            screen.blit(font.render("3", True, (255, 255, 255)),
                        (366.5 - (text_width / 2), 470 - (text_height / 2)))

            if new_settings[6]:
                pygame.draw.rect(screen, (200, 200, 200), (250, 350, 70, 40))
                pygame.draw.rect(screen, (220, 220, 220), (320, 350, 70, 40))
            else:
                pygame.draw.rect(screen, (220, 220, 220), (250, 350, 70, 40))
                pygame.draw.rect(screen, (200, 200, 200), (320, 350, 70, 40))
            font = pygame.font.SysFont(None, 20)
            screen.blit(font.render("Black player:", True, (0, 0, 0)), (250, 330))
            text_width, text_height = font.size("AI")
            screen.blit(font.render("AI", True, (255, 255, 255)),
                        (285 - (text_width / 2), 370 - (text_height / 2)))
            text_width, text_height = font.size("Human")
            screen.blit(font.render("Human", True, (255, 255, 255)),
                        (355 - (text_width / 2), 370 - (text_height / 2)))

        else:
            str_board()
            print()
        if present:
            #if True:
            if turn == 'W' or not ai:
                if mode == 'input_from':
                    if pygame.mouse.get_pressed(3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if not ((240 < y < 270) or (510 < y < 540) or (x > 240)):
                            a = y // 270
                            b = ((y - 30 * a) % 240) // 30
                            c = x // 30
                            if board[a, b, c] != '  ':
                                if board[a, b, c].colour == turn:
                                    move_from = [a, b, c]
                                    mode = 'input_to'
                                    output_moves(board[move_from[0], move_from[1], move_from[2]].find_moves())
                if mode == 'input_to':
                    output_moves(board[move_from[0], move_from[1], move_from[2]].find_moves())
                    if pygame.mouse.get_pressed(3)[0]:
                        x, y = pygame.mouse.get_pos()
                        if not ((240 < y < 270) or (510 < y < 540) or (x > 240)):
                            a = y // 270
                            b = ((y - 30 * a) % 240) // 30
                            c = x // 30
                            if [a, b, c] in board[move_from[0], move_from[1], move_from[2]].find_moves():
                                move_to = [a, b, c]
                                history.append(board.copy())
                                history_pos = len(history)-1
                                if board[move_to[0], move_to[1], move_to[2]] != '  ':
                                    taken[turn].append(board[move_to[0], move_to[1], move_to[2]])
                                    if board[move_to[0], move_to[1], move_to[2]].name == 'K':
                                        end_game = 1
                                board[move_to[0], move_to[1], move_to[2]] = board[move_from[0], move_from[1], move_from[2]]
                                board[move_from[0], move_from[1], move_from[2]] = '  '
                                board[move_to[0], move_to[1], move_to[2]].location = move_to
                                if board[move_to[0], move_to[1], move_to[2]].name == 'P':
                                    if (move_to[0] == 0 and move_to[1] == 0 and turn == 'W') or (move_to[0] == 2 and move_to[1] == 7 and turn == 'B'):
                                        board[move_to[0], move_to[1], move_to[2]] = back_pieces['Q'](
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

                                mode = 'input_from'
                                output_board(board)

                            elif board[a, b, c] != '  ':
                                if board[a, b, c].colour == turn:
                                    move_from = [a, b, c]

            else:
                start = time.time()
                move = minimax(turn, turn, depth)[1]
                print(time.time() - start)
                move_from, move_to = move[0], move[1]


                if not GUI:
                    print(f"{turn} moves {board[move_from[0], move_from[1], move_from[2]].name} from {move_from} to {move_to}")
                    if board[move_to[0], move_to[1], move_to[2]] != '  ':
                        print(f"taking {board[move_to[0], move_to[1], move_to[2]].name}")
                    print("White evaluation:", evaluate('W'))
                    print()
                history.append(board.copy())
                history_pos = len(history) - 1
                if board[move_to[0], move_to[1], move_to[2]] != '  ':
                    taken[turn].append(board[move_to[0], move_to[1], move_to[2]])
                    if board[move_to[0], move_to[1], move_to[2]].name == 'K':
                        end_game = 2
                print(move_from, move_to)


                board[move_to[0], move_to[1], move_to[2]] = board[move_from[0], move_from[1], move_from[2]]
                board[move_from[0], move_from[1], move_from[2]] = '  '
                board[move_to[0], move_to[1], move_to[2]].location = move_to
                print(evaluate('W'))
                if board[move_to[0], move_to[1], move_to[2]].name == 'P':
                    if (move_to[0] == 0 and move_to[1] == 0 and turn == 'W') or (
                            move_to[0] == 2 and move_to[1] == 7 and turn == 'B'):
                        board[move_to[0], move_to[1], move_to[2]] = back_pieces['Q'](
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
        if pygame.mouse.get_pressed(3)[0]:
            x, y = pygame.mouse.get_pos()
            if 250 < x < 315 and 10 < y < 50:
                if history_pos >= 0:
                    history_pos -= 1
                    present = False
                    #output_board(history[history_pos])
                    time.sleep(0.1)
            elif 325 < x < 390 and 10 < y < 50:
                if history_pos < len(history) - 1:
                    history_pos += 1
                    #output_board(history[history_pos])
                    if history_pos == len(history) - 1:
                        present = True
                        mode = 'input_from'
                    time.sleep(0.1)
            elif 250 < x < 390 and 730 < y < 770:
                board, kings, turn, back_pieces, mode, history, present, history_pos, end_game, taken, new_settings, ai = create_board(*new_settings)
            elif 250 < x < 320 and 650 < y < 690:
                new_settings[3] = True
            elif 320 < x < 390 and 650 < y < 690:
                new_settings[3] = False
            elif 250 < x < 297 and 550 < y < 590:
                new_settings[4] = 1
            elif 297 < x < 343 and 550 < y < 590:
                new_settings[4] = 2
            elif 343 < x < 390 and 550 < y < 590:
                new_settings[4] = 3
            elif 250 < x < 297 and 450 < y < 490:
                new_settings[5] = 1
            elif 297 < x < 343 and 450 < y < 490:
                new_settings[5] = 2
            elif 343 < x < 390 and 450 < y < 490:
                new_settings[5] = 3
            elif 250 < x < 320 and 350 < y < 390:
                new_settings[6] = True
            elif 320 < x < 390 and 350 < y < 390:
                new_settings[6] = False

        if GUI:
            pygame.display.flip()
    else:
        output_board(board, winner=end_game)
        pygame.display.flip()
