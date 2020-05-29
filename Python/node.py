from enum import IntEnum

class Direction(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST  = 3
    EAST  = 4

# Successor : (Node, direction to node, distance)
class Node:
    def __init__(self, index=0):
        self.index = index
        # store successor as (Node, direction to node, distance)
        self.Successors = []
        self.unvisited_deadend = False
        self.score = 0 ###

    def getIndex(self):
        """ output: index (int). """
        return self.index

    def getSuccessors(self):
        """ output: (tuple) successor:(index (int), direction(Direction), distance(int)) """
        return self.Successors

    def setSuccessor(self, successor, direction, length=1):
        self.Successors.append((successor, Direction(direction), int(length)))
        #print("For Node {}, a successor {} is set.".format(self.index, self.Successors[-1]))
        return self.Successors

    def isSuccessor(self, nd):
            for succ in self.Successors:
                if succ[0] == nd: 
                    return True
            return False

    def getDirection(self, nd):
        # TODO : Return the direction of nd from the present node if nd is adjacent to the present node.
        """ input: index of testing node. (1~n)
            output: None if not adjacent, direction if adjacent(North, South, East, West). """
        for succ in self.Successors:
            if succ[0] == nd: 
                return succ[1]
        return None