from heapq import heappush, heappop

def Dijkstra(graph, N, source):


    rate = [-1] * N
    rate[int(source)-1] = 0

    parent = [None] * N

    queue = []
    explored = [False]*N

    if source not in graph:

        return rate
    for v in graph[source]:
        rate[int(v) - 1] = int(graph[source][v])
        parent[int(v) - 1] = source
        if v in graph:
            heappush(queue, (-rate[int(v) - 1], v))

    explored[int(source)-1] = True

    while len(queue) != 0:
        d_u = heappop(queue)
        u = d_u[1]
        r = -d_u[0]

        if explored[int(u)-1] is True:
            continue
        for v in graph[u]:

            minimum = min(r,int(graph[u][v]))
            rate[int(v) - 1] = minimum
            parent[int(v) - 1] = u
            explored[int(u) - 1] = True
            if v in graph:
                heappush(queue, (-rate[int(v) - 1], v))
            else:
                explored[int(v) - 1] = True
    return rate



def graph_list(M):  # graph takes M as input which means M lines will be read from output for u,v,w
    graph = {}
    for i in range(0, int(M)):
        u, v, w = f.readline().split()

        if u not in graph.keys():
            graph[u] = {v: w}
        else:
            graph[u][v] = w
    return graph


f = open("input4.txt", "r")
T = int(f.readline())  # number of test cases

f2 = open("output4.txt", 'w')

for i in range(0, T):
    N, M = f.readline().split()

    graph = graph_list(M)

    source = int(f.readline())
    rate = Dijkstra(graph, int(N),str(source))
    for i in rate:
        f2.write(str(i) + " ")
    f2.write("\n")


f.close()
f2.close()

