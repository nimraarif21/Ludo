from .Key import Key
from .Block import Block
import numpy as np

import random
rows_color=['red','blue','blue','blue','yellow','yellow','yellow','green','green','green','red','red']
rows_color1=['red','blue','yellow','green']
turn=['red','yellow']
inverted= [2, 3, 5, 6, 7, 10]

class Board:

    LudoBoard = []
    keys = []

    def __init__(self):
        self.CreateBoard()
        self.CreateKeys()

    def MoveTheKey(self):
        
        for cell in self.LudoBoard:
            print(cell)


    # def Play(self):
    #     print(("Two Player game").center(20,'*'))
    #     while(True):
    #         dice = self.RollDice()
    #         print("Rolling dice for "+turn[0]+"'s turn  :  "+ str(dice))
    #         print("Enter the key you want to move : ", end="")
    #         key = input()
    #         self.MoveTheKey(key, dice)
    #         print("Rolling dice for "+turn[1]+"'s turn")

    def CreateKeys(self):
        for i in range(0,4):
            keyRow = []
            for j in range(0,4):
                key = Key(0, rows_color1[i],'-1,-1')
                keyRow.append(key)
            self.keys.append(keyRow)
              
    def CreateBoard(self):
        self.LudoBoard = np.empty((12,6), dtype= Block)
        for i in range(0, 12):
            for j in range(0,6):
                block = Block(rows_color[i],"A1")
                self.LudoBoard[i][j]=block


    def RollDice(self):
        return random.randint(1,6)

    def PrintHalfColumn(self, col, i, j, string):
        print(string, end=" ")
        if col in inverted:
            print(self.LudoBoard[col][j].value, end=" ")
        else:
            print(self.LudoBoard[col][i].value, end=" ")

    def PrintColumns(self, col1, col2, col3, string):
        space = " "
        j = 5
        for i in range(0, 6):
            print(string, end=" ")
            print(space*30, end="") 
            self.PrintHalfColumn(col1, i, j, string)
            self.PrintHalfColumn(col2, i, j, string)
            self.PrintHalfColumn(col3, i, j, string)
            print(string, end="")
            print(space*30, end="") 
            print(string, end="")
            print('\n')
            j -= 1

    def PrintHalfRow(self, row, string):
        if row in inverted:
            i = 5
            j = -1
            dec = -1
        else:
            i = 0
            j = 6
            dec = 1      
        print(string, end=" ")
        for i in range(i, j, dec):
            print(self.LudoBoard[row][i].value, end=" ")
            print(string, end=" ")
        
    def PrintRows(self, row1, row2, string):
        space = " "
        self.PrintHalfRow(row1, string)
        print(space*16, end="")
        self.PrintHalfRow(row2, string)
        print('\n')
          
    def PrintBoard(self):
        string = "#"
        print(string*79)
        self.PrintColumns(10, 11, 0, string)
        self.PrintRows(9, 1, string)
        self.PrintRows(8, 2, string)
        self.PrintRows(7, 3, string)
        self.PrintColumns(6, 5, 4, string)
        print(string*79)


        



