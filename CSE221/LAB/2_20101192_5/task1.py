from heapq import  heappop, heapify

def Assignment_selection(arr):
    f2 = open("ouput1.txt","w")
    heapify(arr)
    selected = []
    count = 1

    selected.append(heappop(arr))
    f = selected[0][0]
    while len(arr) != 0:
        pop = heappop(arr)
        if pop[1] >= f:
            count += 1
            f = pop[0]
            selected.append(pop)
    f2.write(str(count))

    for j in range(0,len(selected)):
        f2.write("\n"+str(selected[j][1])+" "+str(selected[j][0]))
    f2.close()



f = open("task1_input.txt", "r")
N = int(f.readline())  # number of assignments
e_s = []  # ending time first, starting time second

for i in range(0, N):
    S, E = f.readline().split()
    e_s.append([int(E),int(S)])


Assignment_selection(e_s)


f.close()
