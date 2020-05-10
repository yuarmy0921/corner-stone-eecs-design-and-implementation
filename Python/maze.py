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
        # TODO : read file and implement a data structure you like
        self.raw_data = pandas.read_csv(filepath).values
        self.nodes = []
        self.numbers = len(self.raw_data)
        self.nd_dict = dict()  # key: index, value: the correspond node

    def setNode(self):
        """ Construct node classes of the maze. (index, successors, deadend)
            print every successor while setting, print nd_dict."""
        for i in range(len(self.raw_data)):
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
        return None

    def strategy(self, nd):
        return self.Dijk(nd)

    def strategy_2(self, nd_from, nd_to):
        return self.Dijk_2(nd_from, nd_to)

if __name__ == '__main__':
    maze = Maze("data\medium_maze.csv")
    maze.setNode()
    for i in range(1, maze.numbers+1):
        maze.Dijk(i)
    maze.Dijk_2(6,10)