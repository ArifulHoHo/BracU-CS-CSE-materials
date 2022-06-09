from heapq import heappop, heapify, heappush


def Assignment_selection(arr, M):
    f2 = open("output2.txt","w")
    count = 0
    for i in range(0, int(M)):
        rejected = []

        heapify(arr)
        count += 1

        first = heappop(arr)
        f = first[0]

        while len(arr) != 0:
            pop = heappop(arr)
            if pop[1] >= f:
                count += 1
                f = pop[0]
            else:
                rejected.append(pop)
        arr = rejected
    f2.write(str(count))
    f2.close()


f = open("task2_input.txt", "r")
N, M = f.readline().split()
e_s = []  # ending time first, starting time second

for i in range(0, int(N)):
    S, E = f.readline().split()
    e_s.append([int(E), int(S)])
f.close()

Assignment_selection(e_s, M)
