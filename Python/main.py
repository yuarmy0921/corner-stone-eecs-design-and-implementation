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
    point = score.Scoreboard("data/UID.csv", "Gru", sys.argv[1])    
    #建立溝通介面
    #在這裡會先要求輸入port，如果輸入quit則斷線
    interf = interface.interface()   
    # TODO : Initialize necessary variables
    maze.setNode()
    maze.nd_dict["h"] = "haha"
    interf.send_action(input("Press s to activate: "))
    #清除快取
    interf.ser.ser.flushInput()
    if (sys.argv[1] == '0'):
        print("Mode 0: for treasure-hunting with rule 1")
        # TODO : for treasure-hunting with rule 1, which encourages you to hunt as many scores as possible
        car_dir = 2
        #找到完整路徑(最近)
        interf.tell_you("---------------------------------------------------------------------------")
        solution = maze.strategy(1)
        interf.tell_you("Shortest path: {}".format(solution))
        #傳送指令給車，等到達下一個節點再傳送指令
        complete = False
        
        while not complete:
            #先檢查藍芽
            if not interf.ser.is_open():
                interf.tell_you("Disconncted!")
                interf = interface.interface()
            #一條路徑跑完
            for i in range(len(solution)-1):
                information = maze.getAction(car_dir, solution[i], solution[i+1])
                interf.tell_you("Information: {}".format(information))
                interf.send_action(information[0])
                #等車子回傳一模一樣的指令
                time.sleep(1)
                interf.tell_you("I have already received: {}".format(interf.get_status()))
                #等車子送到達的hint
                while not interf.arrival():
                    pass
                car_dir = information[1]
            interf.tell_you("Arrive!")
            maze.nodes[solution[-1]-1].unvisited_deadend = False
            
            UID = interf.get_UID()
            if UID:
                point.add_UID(UID)
            interf.tell_you("Current score: {}".format(point.getCurrentScore()))
            check = 0
            for i in range(len(maze.nodes)-1):
                if maze.nodes[i].unvisited_deadend == False:
                    check += 1
            if check == len(maze.nodes):
                complete = True
            else:
                complete = False
                interf.tell_you("---------------------------------------------------------------------------")
                solution = maze.strategy(solution[-1])
                interf.tell_you("Shortest path: {}".format(solution))
            
        interf.tell_you("Mission completed!")
        interf.tell_you("Total score: {}".format(point.getCurrentScore()))
        input("Press enter to close.")
        try:
            not interf.ser.is_open()
        except:
            interf.end_process()
        

    elif (sys.argv[1] == '1'):
        print("Mode 1: for treasure-hunting with rule 2")
        # TODO : for treasure-hunting with rule 2, which requires you to hunt as many specified treasures as possible
        route = list(map(int,input("Enter route(separate with space): ").strip().split()))
        car_dir = 2
        #傳送開始指令給車
        interf.send_action(input("Press s to start: "))
        cp = 1 # current point's order
        while cp < len(route):
            #找到路徑
            solution = maze.strategy_2(route[cp-1], route[cp])
            interf.tell_you("Shortest path: {}".format(solution))
            #一條路徑跑完
            for i in range(len(solution)-1):
                information = maze.getAction(car_dir, solution[i], solution[i+1])
                interf.tell_you(information)
                interf.send_action(information[0])
                #等車子送到達的hint
                while not interf.arrival():
                    pass
            car_dir = information[1]
            UID = interf.get_UID()
            if UID:
                point.add_UID(UID)
            interf.tell_you("Current score: {}".format(point.getCurrentScore()))
            cp += 1
        # completed !
        interf.tell_you("Mission completed!")
        interf.tell_you("Total score: {}".format(point.getCurrentScore()))
        input("Press enter to close.")
        

    #自我測試：執行main之後，在interface(terminal)傳送指令，儲存到藍芽
    elif (sys.argv[1] == '2'):
        print("Mode 2: Self-testing mode.")
        # TODO: You can write your code to test specific function.
        action = 1
        while(action):
            action = input("What should I do: ")
            legal = False
            for i in range(6):
                legal = legal or (action == str(i))
            if legal or action == "s":
                interf.send_action(str(action))
                reception = interf.get_status()
                print("I have already received: {}".format(reception))
            elif action == "exit":
                interf.end_process()
                print("Bye bye ~~~")
                break
            else:
                print("You have send a wrong instruction. Please try again.")

if __name__ == '__main__':
    main()
