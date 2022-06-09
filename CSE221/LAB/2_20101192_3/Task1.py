

f = open("input.txt", "r")
num = int(f.readline())
graph = {}
for i in range(0, num):
    line = f.readline().split()
    graph[line[0]] = line[1:]







