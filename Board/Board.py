from .Key import Key
from .Block import Block
from .Player import Player
import numpy as np

import random

# stops=[]

class Board:

    LudoBoard = []
    Players = []
    rows_color=['red','blue','blue','blue','yellow','yellow','yellow','green','green','green','red','red']
    Two=['Red','Yellow']
    inverted= [2, 3, 5, 6, 7, 10]
    CheckPoints=[2, 5, 8, 11]


    def __init__(self):
        self.CreateBoard()


    def mapStringtoInt(self, index):
        indexes = index.split(',')
        return int(indexes[0]), int(indexes[1])



    def MoveTheKey(self, key, dice, player):
        PlayerKeys = player.GetKeys()
        for i in range(len(PlayerKeys)):
            if PlayerKeys[i].GetName() == key:
                key = i
        
        if PlayerKeys[key].GetValue() == 0 and dice == 6:
            index = player.GetStartPoint()
            row, col = self.mapStringtoInt(index)
            PlayerKeys[key].SetValue(1)
            PlayerKeys[key].SetPosition(index) 
            self.LudoBoard[row][col].SetValue(PlayerKeys[key].GetName())
            self.PrintBoard()
            return True   #need to make it false later on
        
        elif PlayerKeys[key].GetValue() == 1:
            print("coming here")
            curr_position = PlayerKeys[key].GetPosition()
            print(curr_position)
            row, col = self.mapStringtoInt(curr_position)
            print(row,col)
            self.LudoBoard[row][col].SetValue("  ")
            if dice > 5-col:
                col = (dice - (5-col))-1
                row += 1
                if(row > 11):
                    row = 0  
            print(row,col) 
            PlayerKeys[key].SetPosition(str(row)+','+str(col))       
            self.LudoBoard[row][col].SetValue(PlayerKeys[key].GetName())
            self.PrintBoard()
            return True

                



    def CreateTwoPlayers(self):
        self.Players=np.empty(2,dtype=Player)
        self.Players[0]=Player(Two[0], '0,1') 
        self.Players[1]=Player(Two[1], '6,1')

    def PlayforTwo(self):
        print(("Two Players Ludo game").center(20,'*'))
        self.CreateTwoPlayers()
        self.PrintBoard()
        i=0
        while(True):
            if i==2:
                i=0
            dice = self.RollDice()
            print("\nRolling dice for "+self.Players[i].color+"'s turn  :  "+ str(dice))
            print("Enter the key's name to move : ")
            keys=self.Players[i].GetKeys()
            names=[]

            for j in range(0,len(keys)):
                names.append(keys[j].GetName())
                print(names[j],end=" ")
                print("||||",end=" ")
            print(" = ", end=" ")  
            key = input()
            if(key in names):
                if self.MoveTheKey(key, dice, self.Players[i])==True:
                    i+=1
            else:
                print("WRONGGG KEY INSERTION")

              
    def CreateBoard(self):
        self.LudoBoard = np.empty((12,6), dtype= Block)
        for i in range(0, 12):
            for j in range(0,6):
                block = Block(rows_color[i],"  ")
                self.LudoBoard[i][j]=block


    def RollDice(self):
        return 6
        # return random.randint(1,6)

    def PrintHalfColumn(self, col, i, j, string):
        print(string, end=" ")
        if col in inverted:
            print(self.LudoBoard[col][j].GetValue(), end=" ")
        else:
            print(self.LudoBoard[col][i].GetValue(), end=" ")

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
            print(self.LudoBoard[row][i].GetValue(), end=" ")
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


        



