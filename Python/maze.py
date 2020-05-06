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

class Maze:
    def __init__(self, filepath):
        # TODO : read file and implement a data structure you like
        self.raw_data = pandas.read_csv(filepath).values
        self.nodes = []
        self.nd_dict = dict()  # key: index, value: the correspond node

    def setNode(self):
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
        print(self.nd_dict)


    def getStartPoint(self):
        if (len(self.nd_dict) < 2):
            print("Error: the start point is not included.")
            return 0
        return self.nd_dict[1]

    def getNodeDict(self):
        return self.nd_dict

    def BFS(self, nd):
        # TODO : design your data structure here for your algorithm
        # Tips : return a sequence of nodes from the node to the nearest unexplored deadend
        return None

    def BFS_2(self, nd_from, nd_to):
        # TODO : similar to BFS but fixed start point and end point
        # Tips : return a sequence of nodes of the shortest path
        return None

    def getAction(self, car_dir, nd_from, nd_to):
        # TODO : get the car action
        # Tips : return an action and the next direction of the car
        return None

    def strategy(self, nd):
        return self.BFS(nd)

    def strategy_2(self, nd_from, nd_to):
        return self.BFS_2(nd_from, nd_to)

maze = Maze("data\small_maze.csv")
print(maze.raw_data)
maze.setNode()