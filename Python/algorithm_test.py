graph = [[(2,2)],[(1,2),(3,2),(5,2)],[(2,2),(6,2)],[(5,2),(7,2)],[(2,2),(4,2),(8,2)],[(3,2),(9,2)],[(4,2)],[(5,2),(11,2)],[(6,2)],[(11,2)],[(8,2),(10,2),(12,2)],[(11,2)]]
def Dijkstra(graph ,nd):
    distance = [99]*len(graph)  # set inf = 99
    distance[nd-1] = 0 # distance of nodes from nd
    completed = [] # visited nodes
    pre = [0]*len(graph)
    score = []  # unvisited deadend
    for i in range(len(graph)):
        if len(graph[i]) == 1 and i+1 != nd:
            score.append(i+1)
    # Dijkstra loop
    while len(completed) < len(graph):
        for i in completed:
            distance[i-1] += 100
        nearest = distance.index(min(distance))
        for i in completed:
            distance[i-1] -= 100
        for ad in graph[nearest]:
            d_new = distance[nearest] + ad[1]
            if d_new < distance[ad[0]-1]:
                distance[ad[0]-1] = d_new
                pre[ad[0]-1] = nearest+1
        completed.append(nearest+1) 
    print('dis:',distance)
    print('pre:',pre)

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
    print('Route:', route)


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

