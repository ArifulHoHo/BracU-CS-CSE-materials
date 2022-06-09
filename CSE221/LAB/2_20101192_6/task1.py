zone_dict = {'Y': 'Yasnaya', 'P': 'Pochinki', 'S': 'School', 'R': 'Rozhok', 'F': 'Farm', 'M': 'Mylta',
             'H': 'Shelter', 'I': 'Prison'}

def LCS(X,Y):
    m = len(X) + 1

    n = len(Y) + 1

    c = [['N']*m for i in range(n)]
    d = [[None]*m for i in range(n)]

    for i in range(0,n):
        c[i][0] = 0


    for j in range(0,m):
        c[0][j] = 0

    for i in range(1,n):
        for j in range(1,m):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                d[i][j] = "diagonal"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                d[i][j] = "up"
            else:
                c[i][j] = c[i][j-1]
                d[i][j] = "left"


    sequence = ""
    tracker = d[n-1][m-1]
    tracker_b = m-2

    while tracker is not None and tracker_b >= 0:

        if tracker == "diagonal":
            sequence = sequence + X[tracker_b]
            n=n-1
            m=m-1
            tracker_b = tracker_b - 1
        elif tracker == "up":
            n=n-1
            tracker_b = tracker_b - 1
        else:
            m=m-1
        tracker = d[n][m]
    return sequence


f = open("input1.txt", "r")
N = int(f.readline())
X = f.readline().rstrip()
Y = f.readline().rstrip()

subsequence = LCS(X, Y)
length = len(subsequence)

correctness = (length * 100) / N
f2 = open("ouput1.txt","w")
for i in range(-1,-length-1,-1):
    f2.write(zone_dict[subsequence[i]] + " ")

f2.write("\n")
f2.write("Correctness of prediction: "+str(int(correctness))+"%")

f2.close()
f.close()