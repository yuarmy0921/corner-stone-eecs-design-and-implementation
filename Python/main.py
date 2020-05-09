from node import *
import maze as mz
import score
import interface
import time

import numpy as np
import pandas
import time
import sys
import os

#執行的任務：匯入迷宮、紀錄分數、創建溝通介面、決定遊戲模式
def main():
    #讀取迷宮
    maze = mz.Maze("data/small_maze.csv")
    #建立計分表 在執行檔案時記得把遊戲模式當參數傳入!!!!
    point = score.Scoreboard("data/UID.csv", "team_NTUEE", sys.argv[1])    
    #建立溝通介面
    #在這裡會先要求輸入port，如果輸入quit則斷線
    interf = interface.interface()   
    # TODO : Initialize necessary variables

    #執行BFS，
    if (sys.argv[1] == '0'):
        print("Mode 0: for treasure-hunting with rule 1")
        # TODO : for treasure-hunting with rule 1, which encourages you to hunt as many scores as possible
        maze.strategy()
        #印出執行過程
        interf.tell_you

    elif (sys.argv[1] == '1'):
        print("Mode 1: for treasure-hunting with rule 2")
        # TODO : for treasure-hunting with rule 2, which requires you to hunt as many specified treasures as possible
        maze.strategy_2()

    #自我測試：執行main之後，在interface(terminal)傳送指令，儲存到藍芽
    elif (sys.argv[1] == '2'):
        print("Mode 2: Self-testing mode.")
        # TODO: You can write your code to test specific function.
        action = 1
        while(action):
            action = input("What should I do: ")
            if action == mz.Action:
                reception = interf.send_action(action)
                print("I have already received: {}".format(reception))
            else:
                print("You have send a wrong instruction. Please try again.")

if __name__ == '__main__':
    main()
