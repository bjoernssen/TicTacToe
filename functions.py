# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

def drawBoard(board):                                               #Passing a string-Array and printing the corresponding board
    print(board[7],'|', board[8],'|',board[9])
    print('----------')
    print(board[4],'|', board[5],'|',board[6])
    print('----------')
    print(board[1],'|', board[2],'|',board[3])
    
def setMark(mark, position, board):
    if not board[position] == ' ':
        print('Position already used!')
        print('Please use another position')
        return board
    board[position] = mark
    return board    

def isWinner(board, mark):
    return((board[1]==mark and board[2]==mark and board[3]==mark) or # first three horizontal
           (board[5]==mark and board[6]==mark and board[7]==mark) or
           (board[7]==mark and board[8]==mark and board[9]==mark) or
           (board[1]==mark and board[4]==mark and board[7]==mark) or # next three vertical
           (board[2]==mark and board[5]==mark and board[8]==mark) or
           (board[3]==mark and board[6]==mark and board[9]==mark) or
           (board[1]==mark and board[5]==mark and board[9]==mark) or # last two diagonal
           (board[3]==mark and board[5]==mark and board[7]==mark))
           
def chooseMark():
    playerMark = ''
    while not (playerMark == 'X' or playerMark == 'O'): 
        print('Which letter do you want to use?')
        playerMark = input().upper()
        if not (playerMark == 'X' or playerMark == 'O'):
            print('Please choose either "X" r "O"!')
    print('You chose', playerMark,'!')
    return playerMark

def startingPlayer():
    r = random.randint(1,2)
    if r == 1:
        print('Player 1 goes first!')
    else:
        print('Player 2 goes first!')
    return r
        