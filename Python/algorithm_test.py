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

for i in range(1,13):
    print('Node:',i)
    Dijkstra(graph, i)
    print('')