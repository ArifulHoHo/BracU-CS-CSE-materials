from Task1 import num
from Task1 import graph

printed = []
visited = [0] * num
f2 = open("outputDFS.txt", 'w')

def DFS_visit(graph, node):
    visited[int(node)-1] = 1
    printed.append(node)
    for node in graph[node]:
        if visited[int(node)-1] == 0:
            DFS_visit(graph, node)

def DFS(graph, endPoint):
    for node in graph:
        if visited[int(node)-1] == 0:
            DFS_visit(graph, node)
    for node in printed:
        if node == endPoint:
            f2.write(node + " ")
            return
        f2.write(node+ " ")

DFS(graph,"12")
f2.close()
