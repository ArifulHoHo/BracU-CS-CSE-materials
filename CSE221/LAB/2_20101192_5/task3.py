from heapq import heappush, heappop, heapify

f = open("task3_input.txt", "r")
N = int(f.readline())  # number of tasks
task = f.readline().split()
call = f.readline()



heapify(task)
sequence = ""
JakePQ = []
Jake = 0
Jill = 0

for c in call:
    if c == "J":
        choice = heappop(task)
        sequence = sequence + choice
        JakePQ.append(-int(choice))
        Jake = Jake + int(choice)
    elif c == "j":
        heapify(JakePQ)
        choice = -heappop(JakePQ)
        sequence = sequence + str(choice)
        Jill = Jill + choice

f2 = open("ouput3.txt","w")
f2.write(sequence)
f2.write('\n'+str(Jake))
f2.write('\n'+str(Jill))
f2.close()