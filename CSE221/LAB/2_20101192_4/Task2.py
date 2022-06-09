from heapq import heappush, heappop


def Dijkstra(graph, N):  # destination node is N
    if len(graph) == 0:
        return "1"

    dist = [float('inf')] * N
    parent = [0] * N
    dist[0] = 0  # source is 1. Hence index in distance is 0
    queue = []
    explored = [False]*N

    heappush(queue, (dist[int("1") - 1], "1"))  # using tuple where (distance from source of the node,the node)
    while len(queue) != 0:
        d_u = heappop(queue)
        u = d_u[1]
        d = d_u[0]

        for v in graph[u]:
            if dist[int(v) - 1] > d + int(graph[u][v]):
                dist[int(v) - 1] = d + int(graph[u][v])
                parent[int(v) - 1] = u
                if v in graph:
                    heappush(queue, (dist[int(v) - 1], v))
                else:
                    explored[int(v) - 1] = True
        explored[int(u) - 1] = True

    path = str(N)
    i = N - 1
    while i != 0:
        j = parent[i]
        path = path + " " + j
        i = int(j) - 1

    return path[::-1]


def graph_list(M):  # graph takes M as input which means M lines will be read from output for u,v,w
    graph = {}
    for i in range(0, int(M)):
        u, v, w = f.readline().split()

        if u not in graph.keys():
            graph[u] = {v: w}
        else:
            graph[u][v] = w
    return graph


f = open("input2.txt", "r")
T = int(f.readline())  # number of test cases
f2 = open("output2.txt", 'w')

for i in range(0, T):
    N, M = f.readline().split()

    graph = graph_list(M)
    path = Dijkstra(graph, int(N))

    f2.write(path + "\n")

f.close()
f2.close()
