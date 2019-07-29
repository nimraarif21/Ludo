from .Key import Key
from .Block import Block
from .Player import Player
import numpy as np

import random

class Board:

    LudoBoard = []
    Players = []
    rows_color = ['red','blue','blue','blue','yellow','yellow','yellow','green','green','green','red','red']
    Two = ['Red','Yellow']
    inverted = [2, 3, 5, 6, 7, 10]
    CheckPoints = [11, 5, 2, 8] 
    
    def __init__(self):
        self.CreateBoard()

    def mapStringtoInt(self, index):
        indexes = index.split(',')
        return int(indexes[0]), int(indexes[1])

    def WinKey(self, player, key, dice):
        curr_position = key.GetPosition()
        row, col = self.mapStringtoInt(curr_position)
        if dice-(5-col) > 1:
            print("You cannot move this key")
        elif dice-(5-col) == 1:
            print("This key has won")
            key.SetValue(3)
            self.LudoBoard[row][col].SetValue("  ")
            player.IncrementWonKeys()
        else:
            self.LudoBoard[row][col].SetValue("  ")
            col += dice
            self.LudoBoard[row][col].SetValue(key.GetName())
            key.SetPosition(str(row)+','+str(col))

    def MoveorKill(self, row, col, player, key):
        nextPos = self.LudoBoard[row][col].GetValue()
        flag = False
        for i in self.Players:  #OtherPlayer
            if i != player:
                second_player = i

        second_keys = second_player.GetKeys()
        for i in range(len(second_keys)):
            if second_keys[i].GetName() == nextPos:
                second_key_index = i
                flag = True
                break
        
        if flag == True:
            self.LudoBoard[row][col].SetValue(key.GetName())
            second_keys[second_key_index].SetValue(0)
            second_keys[second_key_index].SetPosition('-1,-1')
            key.SetPosition(str(row)+','+str(col))
            print("You killed Other Player's Key")
            return
        else:
            key.SetPosition(str(row)+','+str(col))      
            self.LudoBoard[row][col].SetValue(key.GetName())
            return
            

    def MoveTheKey(self, key, dice, player):
        if key.GetValue() == 0 and dice == 6:
            index = player.GetStartPoint()
            row, col = self.mapStringtoInt(index)
            key.SetValue(1)
            key.SetPosition(index) 
            self.LudoBoard[row][col].SetValue(key.GetName())
            return False        
        elif key.GetValue() == 1:
            curr_position = key.GetPosition()
            old_row, old_col = self.mapStringtoInt(curr_position)
            if dice > 5-old_col:
                col = (dice - (5-old_col))-1
                row = old_row + 1
                if row in self.CheckPoints and col > 0:
                    if row != player.GetCheckPoint():
                        row += 1
                        col -= 1
                if row > 11:
                    row = 0  
            else:
                row = old_row
                col = dice + old_col
            if row == player.GetCheckPoint():
                key.SetValue(2)
                self.WinKey(player, key, dice)
            else:
                self.LudoBoard[old_row][old_col].SetValue("  ")
                self.MoveorKill(row, col, player, key)
            if dice == 6:
                return False
            return True
        elif key.GetValue() == 2:
            if dice == 6:
                return False
            self.WinKey(player, key, dice)
            return True
        elif key.GetValue() == 0 and dice < 6:
            print("Get a 6 to take it out of your house")
            return True
        else:
            print("This key has already won. You cannot move it")
            return False
                            
    def PrintPlayerKeys(self, player): 
        keys = player.GetKeys()
        print(player.GetColor()+' Player In House Keys  =  ', end="")
        for i in keys:
            if i.GetValue() == 0:
                print(i.GetName()+" || ", end ="")

        print("\n" + player.GetColor()+' Player In Game Keys  =  ', end="")
        for i in keys:
            if i.GetValue() == 1 or i.GetValue() == 2:
                print(i.GetName()+" || ", end="")

        print("\n" + player.GetColor()+' Player Keys Won  =  ', end="")
        for i in keys:
            if i.GetValue() == 3:
                print(i.GetName()+" || ", end="")

        

    def CreateTwoPlayers(self):
        self.Players = np.empty(2,dtype=Player)
        self.Players[0] = Player(self.Two[0], '0,1', self.CheckPoints[0], 0) 
        self.Players[1] = Player(self.Two[1], '6,1', self.CheckPoints[1], 0)

    def checkWin(self):
        for i in self.Players:
            if i.GetWonKeys()==4:
                print("Player "+ i.GetColor()+ " has won the game!!!!")
                return True
        return False
            

    def PlayforTwo(self):
        title = "Two Players Ludo game"
        print(title.center(20,'*'))
        self.CreateTwoPlayers()
        self.PrintBoard()
        i = 0
        flag = 0
        while(True):
            if self.checkWin() == True:
                break
            if i == 2:
                i = 0
            dice = self.RollDice(i)
            print("\nRolling dice for "+self.Players[i].color+"'s turn  :  "+ str(dice))
            self.PrintPlayerKeys(self.Players[i])
            print("\nEnter any one of these keys to move = ", end="")
            key = input()
            keys = self.Players[i].GetKeys()
            for j in range(0, len(keys)):
                if keys[j].GetName() == key:
                    flag = 1
                    key = keys[j]
                    break

            if flag == 1:
                if self.MoveTheKey(key, dice, self.Players[i])==True:
                    i += 1
                print(self.PrintBoard())
            else:
                print("WRONGGG KEY INSERTION")

              
    def CreateBoard(self):
        self.LudoBoard = np.empty((12,6), dtype=Block)
        for i in range(0, 12):
            for j in range(0,6):
                block = Block(self.rows_color[i],"  ")
                self.LudoBoard[i][j] = block

    def RollDice(self, value):
        return random.randint(1,6)

    def PrintHalfColumn(self, col, i, j, string):
        print(string, end=" ")
        if col in self.inverted:
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
        if row in self.inverted:
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
        print("\n\n")
        print(string*79)
        self.PrintColumns(10, 11, 0, string)
        self.PrintRows(9, 1, string)
        self.PrintRows(8, 2, string)
        self.PrintRows(7, 3, string)
        self.PrintColumns(6, 5, 4, string)
        print(string*79)


        



