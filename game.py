#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:16:29 2019

@author: bjoern
"""

import functions as fn


print('Welcome to TicTacToe')
print('Player 1, please choose your letter!')
playerMark1 = fn.chooseMark()

if playerMark1 == 'X':
    playerMark2 ='O'
elif playerMark1 == 'O':
    playerMark2 = 'X'
print('That means Player 2 gets the letter', playerMark2)    

board = [' ']*10 #initialise the board

winner1 = None
winner2 = None
r = fn.startingPlayer()
if r==1: 
    i=1
    while not winner1 or winner2: 
        fn.drawBoard(board)
        if i%2 == 1: 
            print('Player 1, where do you want to put your', playerMark1,'?')
            pos = input()
            pos = int(pos)
            while not board[pos] == ' ':
                print('Position already used!')
                print('Please use another position')
                pos = input()
            board = fn.setMark(playerMark1, pos, board)
            fn.drawBoard(board)
            winner1 = fn.isWinner(board, playerMark1)
            
            
        elif i%2 == 0:
            print('Player 2, where do you want to put your', playerMark2,'?')
            pos = input()
            pos = int(pos)
            while not board[pos] == ' ':
                print('Position already used!')
                print('Please use another position')
                pos = input()
            board = fn.setMark(playerMark2, pos, board)
            fn.drawBoard(board)
            winner2 = fn.isWinner(board, playerMark2)
        if i == 9:
            print('This game ends in a draw.')
            break
        i=i+1
        
elif r==2: 
    i=0
    while not winner1 or winner2: 
        
        if i%2 == 1: 
            print('Player 1, where do you want to put your', playerMark1,'?')
            pos = input()
            pos = int(pos)
            while not board[pos] == ' ':
                print('Position already used!')
                print('Please use another position')
                pos = input()
            board = fn.setMark(playerMark1, pos, board)
            fn.drawBoard(board)
            winner1 = fn.isWinner(board, playerMark1)
            
            
        elif i%2 == 0:
            print('Player 2, where do you want to put your', playerMark2,'?')
            pos = input()
            pos = int(pos)
            while not board[pos] == ' ':
                print('Position already used!')
                print('Please use another position')
                pos = input()
            board = fn.setMark(playerMark2, pos, board)
            fn.drawBoard(board)
            winner2 = fn.isWinner(board, playerMark2)
        if i == 8:
            print('This game ends in a draw.')
            break
        i=i+1
if winner1:
    print('Player 1 won the game! Congratulations!')
elif winner2:
    print('Player 2 won the game! Congratulations!')