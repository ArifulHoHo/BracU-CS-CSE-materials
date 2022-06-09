from Task1 import num
from Task1 import graph
from collections import deque

queue = deque()
visited = [0] * num
f2 = open("outputBFS.txt", 'w')

def BFS(visited, graph, node, endPoint):
    visited[int(node) - 1] = 1
    queue.append(node)
    while len(queue) != 0:
        m = queue.popleft()
        f2.write(m + " ")
        if m == endPoint:
            break
        for neighbour in graph[m]:
            if visited[int(neighbour) - 1] == 0:
                visited[int(neighbour) - 1] = 1
                queue.append(neighbour)


BFS(visited, graph, "1", "12")
f2.close()