from node import *
import numpy as np
import csv
import pandas
from enum import IntEnum
import math

class Action(IntEnum):
    ADVANCE = 1
    U_TURN = 2
    TURN_RIGHT = 3
    TURN_LEFT = 4
    HALT = 5
    END = 0


class Maze:
    def __init__(self, filepath):
        self.raw_data = pandas.read_csv(filepath).values
        self.nodes = []
        self.numbers = len(self.raw_data)
        #每一個value都是一個list
        self.nd_dict = dict()  # key: index, value: the correspond node

    def setNode(self):
        """ Construct node classes of the maze. (index, successors, deadend)
            print every successor while setting, print nd_dict."""
        for i in range(len(self.raw_data)):   #總節點數
            index = int(self.raw_data[i][0])
            self.nodes.append(Node(index))
            ad_list = []
            dis_list = []
            for d in range(1,5): 
                if self.raw_data[i][d] > 0:
                    self.nodes[i].setSuccessor(int(self.raw_data[i][d]), d, int(self.raw_data[i][d+4]))
                    ad_list.append(int(self.raw_data[i][d]))
                    dis_list.append(int(self.raw_data[i][d+4]))
            self.nd_dict[int(self.raw_data[i][0])] = ad_list
            if len(ad_list) == 1:
                self.nodes[i].unvisited_deadend = True
        print(self.nd_dict)

    def getStartPoint(self):
        """ Test if nodes information are settled properly. """
        if (len(self.nd_dict) < 2):
            print("Error: the start point is not included.")
            return 0
        return self.nd_dict[1]

    def getNodeDict(self):
        return self.nd_dict

    def Dijk(self, nd):
        """ for game mode 1.
            input: (int) index of node being starting point.
            output: (list) list of nodes index(int) showing the path to the nearest deadend. """
        # TODO : design your data structure here for your algorithm
        # Tips : return a sequence of nodes from the node to the nearest unexplored deadend
        print('Node', nd)
        distance = [99]*self.numbers  # set inf = 99
        distance[nd-1] = 0 # distance of nodes from nd
        completed = [] # visited nodes
        pre = [0]*self.numbers
        score = []  # unvisited deadend
        for i in self.nodes:
            if i.unvisited_deadend and i.index != nd:
                score.append(i.index)
        # Dijkstra loop
        while len(completed) < self.numbers:
            for i in completed:
                distance[i-1] += 100
            nearest = distance.index(min(distance))
            for i in completed:
                distance[i-1] -= 100
            for ad in self.nodes[nearest].getSuccessors():
                d_new = distance[nearest] + ad[2]
                if d_new < distance[ad[0]-1]:
                    distance[ad[0]-1] = d_new
                    pre[ad[0]-1] = nearest+1
            completed.append(nearest+1) 

        
        if not score:
            return [nd]
        # find nearest score point
        nearest = score[0]
        for node in score:
            if distance[node-1] < distance[nearest-1]:
                nearest = node
        print('Nearest: Node', nearest)
    
        # print route to the nearest score point
        route = [nearest]
        pre_node = pre[nearest-1]
        while pre_node != nd:
            route.insert(0, pre_node)
            pre_node = pre[pre_node-1]
        print('Route:', route, '\n')
        return route

    def Dijk_2(self, nd_from, nd_to):
        """ for game mode 2.
            input: (two int) index of starting point and endpoint.
            output: (list) list of nodes index(int) showing the shotest path. """
        # TODO : similar to Dijk but fixed start point and end point
        # Tips : return a sequence of nodes of the shortest path

        #?????????
        distance = [99]*self.numbers  # set inf = 99
        distance[nd_from-1] = 0 # distance of nodes from nd_from
        completed = [] # visited nodes
        pre = [0]*self.numbers

        # Dijkstra loop
        while nd_to not in completed:
            for i in completed:
                distance[i-1] += 100
            nearest = distance.index(min(distance))
            for i in completed:
                distance[i-1] -= 100
            for ad in self.nodes[nearest].getSuccessors():
                d_new = distance[nearest] + ad[2]
                if d_new < distance[ad[0]-1]:
                    distance[ad[0]-1] = d_new
                    pre[ad[0]-1] = nearest+1
            completed.append(nearest+1) 
        
        # print route to nd_to
        route = [nd_to]
        pre_node = pre[nd_to-1]
        while pre_node != nd_from:
            route.insert(0, pre_node)
            pre_node = pre[pre_node-1]
        print('From %d to %d, Route:'%(nd_from, nd_to), route)
        return route

    def getAction(self, car_dir, nd_from, nd_to):
        # TODO : get the car action
        # Tips : return an action and the next direction of the car
        """ restriction: nd_from and nd_to must be adjacent.
            input: car_dir(class Direction), nd_from(int), nd_to(int)
            output: tuple(Action.Halt, Direction.car_dir)  if invalid
                    tuple(Action.action, Direction.next_dir).  """
        if nd_to not in self.nd_dict[nd_from]:
<<<<<<< HEAD
            return (5, Direction(car_dir))
=======
            return ("5", Direction(car_dir))
>>>>>>> b057f7eddcbd7a5c91da48607cd2944bd0e7bec0
        advance = {(1,1), (2,2), (3,3), (4,4)}
        u_turn = {(1,2), (2,1), (3,4), (4,3)}
        r_turn = {(1,4), (4,2), (2,3), (3,1)}
        l_turn = {(1,3), (3,2), (2,4), (4,1)}
        target = (car_dir, int(self.nodes[nd_from-1].getDirection(nd_to)))
        if target in advance:
            return ("1", self.nodes[nd_from-1].getDirection(nd_to))
        elif target in u_turn:
            return ("2", self.nodes[nd_from-1].getDirection(nd_to))
        elif target in r_turn:
            return ("3", self.nodes[nd_from-1].getDirection(nd_to))
        else:
            return ("4", self.nodes[nd_from-1].getDirection(nd_to))

    def strategy(self, nd):
        return self.Dijk(nd)

    def strategy_2(self, nd_from, nd_to):
        return self.Dijk_2(nd_from, nd_to)

def test():
    maze = Maze("data\medium_maze.csv")
    maze.setNode()
<<<<<<< HEAD
    for i in range(1, maze.numbers+1):
        maze.Dijk(i)
=======
    print(maze.strategy(1))
    #for i in range(1, maze.numbers+1):
        #print(maze.Dijk(i))
    #maze.Dijk_2(6,10)
    #print(maze.getAction(1,3,2)) # (2,2)
    #print(maze.getAction(2,3,2)) # (1,2)
    #print(maze.getAction(3,3,2)) # (4,2)
    #print(maze.getAction(4,3,2)) # (3,2)
    #print(maze.getAction(1,3,9)) # (5,1)

>>>>>>> b057f7eddcbd7a5c91da48607cd2944bd0e7bec0
if __name__ == '__main__':
    test()