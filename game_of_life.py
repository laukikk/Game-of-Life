import numpy as np
import tkinter as tk
import json
from copy import deepcopy

f = open('data.json')
data = json.load(f)
    
root = tk.Tk()
root.title("Conway's Life of Game")

colors = ['white', 'black']


def getNumNeighbours(board, x, y):
    res = 0
    n = len(board)
    m = len(board[0])
    # print("neighbours: ")
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if((i >= 0 and j >= 0) and (i < n and j < m)):
                # print(str(board[i][j]) + " ", end='')
                if(not (i==x and j==y) and board[i][j]):
                    res += 1
    # print(' : ', res)
    # print()
    return res

def getCellValue(board, x, y):
    if board[x][y]:
        if (getNumNeighbours(board, x, y) in [2, 3]):
            return 1
    else:
        if (getNumNeighbours(board, x, y) == 3):
            return 1
    return 0

def runGame(board):
    newBoard = deepcopy(board)

    for i,row in enumerate(board):
        
        for j,column in enumerate(row):
            # print("i = " + str(i) + " j = " + str(j))
            
            newCellValue = getCellValue(board, i, j)
            # print("cell = " + str(board[i][j]) + " newCell = "  + str(newCellValue))
            cell = tk.Button(root, text='', bg=colors[newCellValue], width=5, height=3, state='disabled')
            cell.grid(row=i, column=j)
            newBoard[i][j] = newCellValue

    return newBoard
        
def update():
    global board
    print(board)
    board = runGame(board)
    root.after(1000, update)


if __name__ == '__main__':
    
    while 1:
        life = input("Enter the Life that you want to simulate (glider, oscs, beacon, LWSS, MWSS, HWSS, still): ")
        try:
            board = np.array(data[life])
            
        except:
            print("Incorrect Life, try again...")
            continue
        break

    update()
    root.mainloop()
